import sys
BASE_PATH = "/usr/src/app"
#BASE_PATH = "/Users/divyam/Documents/projects/falcon-project-base"
sys.path.append(BASE_PATH)

LOGGER = {
    "test_endpoint" : BASE_PATH + "/logs/test_endpoint.log",
    "authorization" : BASE_PATH + "/logs/authorization.log"
}

REDIS_HOST = "10.10.14.125"
REDIS_PORT = 9091
REDIS_SESSION_MAP = "LICENCE_SESSION_AUTH"

ENCRYPTION_KEY = "Vsa8BD+YQ1obQbfhudCPy2kn/x6O7Io="
ENCRYPT_RESPONSE = False

ROUTE_PREFIX = "/api/v1"

REQUIRED_FIELDS_MAP = {
    'auth-post': ["email", "password"]
}

ERROR_TITLES = {
    "HTTP_400": "Forbidden",
    "HTTP_401": "Unauthorized",
    "HTTP_404": "Not Found",
    "HTTP_500": "Unhandled Exception",
    "HTTP_202": "Accepted",
    "HTTP_200": "Ok"
}

ERROR_CODE = {
    "MISSING_REQUIRE_PARAMETER": "MISSING_REQUIRE_PARAMETER",
}