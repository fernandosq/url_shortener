from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponse, HttpResponseServerError, \
     HttpResponseNotAllowed, HttpResponseNotFound, HttpResponsePermanentRedirect
from .messages import NewRequestMessage, NewResponseMessage, DeserializationError, RankingResponseMessage
from .db import save_new_code, get_all_active_codes, get_code_url, CodeNotFound, increment_click_code, \
    top_ranking_clicks
from .code_gen import generate_unique_code, OverLimitError
# Create your views here.


def new(request: HttpRequest) -> HttpResponse:
    """ Endpoint to make a code for url"""
    try:
        if request.method == "POST":
            input_message = NewRequestMessage(request.body)
            all_codes = get_all_active_codes()
            code = generate_unique_code(6, all_codes, 6)
            save_new_code(input_message.url, code)
            output_message = NewResponseMessage(code)
            return JsonResponse(output_message.serialize())
        return HttpResponseNotAllowed(["POST"])
    except DeserializationError as e:
        return HttpResponseBadRequest(str(e))

    except OverLimitError:
        return HttpResponseServerError()


def code_to_url(request: HttpRequest, code: str) -> HttpResponse:
    """Endpoint to do a redirect code to url"""
    try:
        if request.method == "GET":
            url = get_code_url(code)
            increment_click_code(url)
            return HttpResponsePermanentRedirect(f"{url.full_url}")

        return HttpResponseNotAllowed(["GET"])
    except CodeNotFound:
        return HttpResponseNotFound()


def ranking(request: HttpRequest, limit_ranking: int) -> HttpResponse:
    """ Endpoint to get a clicks ranking"""
    if request.method == "GET":
        clicks = top_ranking_clicks(limit_ranking)
        return JsonResponse(
             RankingResponseMessage(clicks).serialize()
        )
    return HttpResponseNotAllowed(["GET"])





