import datetime
from django.conf import settings
from datetime import timedelta

...

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': True,

#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': settings.SECRET_KEY,
#     'VERIFYING_KEY': None,

#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         #'rest_framework.authentication.BasicAuthentication',
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication', #Oauth, JWT
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ),
#     # 'DEFAULT_PAGINATION_CLASS': 'cfeapi.restconf.pagination.CFEAPIPagination',
#     'DEFAULT_FILTER_BACKENDS': (
#             'rest_framework.filters.SearchFilter',
#             'rest_framework.filters.OrderingFilter',
#     ),
#     'SEARCH_PARAM': 'q',
#     'ORDERING_PARAM': 'ordering',
# }


JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    #'rest_framework_jwt.utils.jwt_response_payload_handler'
    'authentications.utils.jwt_response_payload_handler',

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=60),

    'JWT_AUTH_HEADER_PREFIX': 'JWT', # Authorization: JWT <token>
    'JWT_AUTH_COOKIE': None,

}