import json
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


_validate_url = URLValidator()


class DeserializationError(Exception):
    pass


class NewRequestMessage(object):
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
            raise DeserializationError(str(e))


class NewResponseMessage(object):
    def __init__(self, new_code):
        self.code = new_code

    def serialize(self):
        return {
            "code" : self.code
        }