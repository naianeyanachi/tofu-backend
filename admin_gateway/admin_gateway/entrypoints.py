import json

from marshmallow import ValidationError
from nameko.exceptions import BadRequest, safe_for_serialization
from nameko.web.handlers import HttpRequestHandler
from werkzeug import Response

from gateway.exceptions import CartNotFound


class HttpEntrypoint(HttpRequestHandler):
    """ Overrides `response_from_exception` so we can customize error handling.
    """

    mapped_errors = {
        BadRequest: (400, 'BAD_REQUEST'),
        ValidationError: (400, 'VALIDATION_ERROR'),
        CartNotFound: (404, 'CART_NOT_FOUND'),
    }

    def response_from_exception(self, exc):
        status_code, error_code = 500, 'UNEXPECTED_ERROR'

        if isinstance(exc, self.expected_exceptions):
            if type(exc) in self.mapped_errors:
                status_code, error_code = self.mapped_errors[type(exc)]
            else:
                status_code = 400
                error_code = 'BAD_REQUEST'

        return Response(
            json.dumps({
                'error': error_code,
                'message': safe_for_serialization(exc),
            }),
            status=status_code,
            mimetype='application/json',
            headers={
                'Access-Control-Allow-Origin': '*'
            }
        )
    
    def response_from_result(self, *args, **kwargs):
        response = super(HttpEntrypoint, self).response_from_result(*args, **kwargs)
        response.headers.add('Access-Control-Allow-Origin', '*')  # or whatever
        return response


http = HttpEntrypoint.decorator
