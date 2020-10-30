from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponse
from .messages import NewRequestMessage, NewResponseMessage, DeserializationError
from .db import save_new_code,get_all_active_codes
from .code_gen import generate_short_url, generate_unique_code
# Create your views here.


def new(request: HttpRequest) -> HttpResponse:
    try:
        input_message = NewRequestMessage(request.body)
        all_codes = get_all_active_codes()
        code = generate_unique_code(6, all_codes, 6)
        save_new_code(input_message.url, code)
        output_message = NewResponseMessage(code)
        return JsonResponse(output_message.serialize())
    except DeserializationError as e:
        return HttpResponseBadRequest(str(e))

