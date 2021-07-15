from rest_framework.authentication import SessionAuthentication


class CorsMiddleware(object):
    def process_response(self, req, resp):
        resp["Access-Control-Allow-Origin"] = "*"
        return resp