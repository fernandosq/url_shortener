import json
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import URL

_validate_url = URLValidator()


class DeserializationError(Exception):
    pass


class NewRequestMessage(object):
    """ Diferents messages we give to user if some with the code failed"""
    def __init__(self, body):
        if body == b"":
            raise DeserializationError(f"Fault request data, empty body")
        data = json.loads(body)
        if "url" not in data:
            raise DeserializationError(f"url data was expected but not found in: {body}")
        try:
            _validate_url(data["url"])
            self.url = data["url"]
        except ValidationError as e:
            raise DeserializationError(f"Invalid url: {str(e)}")


class NewResponseMessage(object):
    """ Messages we give to user to have info about the error"""
    def __init__(self, new_code):
        self.code = new_code

    def serialize(self):
        return {
            "code": self.code
        }


class RankingResponseMessage(object):
    """Different messages we give to user if something with the clicks ranking failed"""

    def __init__(self, clicks: [URL]):
        self.clicks = [click.to_dict() for click in clicks]

    def serialize(self):
        return {
           "ranking": self.clicks
        }
