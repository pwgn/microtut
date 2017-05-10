DEBUG = True

DISCOVERY_SERVICE_URL = 'localhost:6100/discoveryservice'

WTF_CSRF_ENABLED = False

SECRET_KEY = 'super-secret'

SQLALCHEMY_DATABASE_URI = 'sqlite:///microtut-auth.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECURITY_RECOVERABLE = True
SECURITY_REGISTERABLE = True
SECURITY_LOGIN_URL = '/security/login'
SECURITY_LOGOUT_URL = '/security/logout'
SECURITY_REGISTER_URL = '/security/register'
SECURITY_RESET_URL = '/security/reset'
SECURITY_SEND_REGISTER_EMAIL = False
