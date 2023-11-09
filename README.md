### Install the required libraries
```
pip install -r requirements.txt
```
### Start the django server
```
python manage.py runserver
```

---

### Django settings

```
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # corsheader
    "corsheaders",
    # local django app
    'authentication',
    # rest-framework
    'rest_framework',
    'rest_framework.authtoken',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'django.contrib.sites',
    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # cors header middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# allauth
SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SOCIALACCOUNT_QUERY_EMAIL = True

# rest-framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}

# simple jwt
from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=2),
}

# rest auth
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
    'JWT_AUTH_HTTPONLY': True,
    'SESSION_LOGIN': False,
    'OLD_PASSWORD_FIELD_ENABLED': True,
}

# cors headers
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True
```

```
# urls.py
from django.contrib import admin
from django.urls import path, include
from authentication.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google-login'),
]
```

```
# views.py
from django.shortcuts import render
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/"
    client_class = OAuth2Client
```

---
## Bug
```
IntegrityError at /dj-rest-auth/google/
UNIQUE constraint failed: auth_user.username
Request Method:	POST
Request URL:	http://localhost:8000/dj-rest-auth/google/
Django Version:	4.2.7
Exception Type:	IntegrityError
Exception Value:	
UNIQUE constraint failed: auth_user.username
Exception Location:	/opt/homebrew/lib/python3.11/site-packages/django/db/backends/sqlite3/base.py, line 328, in execute
Raised during:	authentication.views.GoogleLogin
Python Executable:	/opt/homebrew/opt/python@3.11/bin/python3.11
Python Version:	3.11.6
Python Path:	
['/Users/chris/Documents/GitHub/django_oauth',
 '/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python311.zip',
 '/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11',
 '/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload',
 '/opt/homebrew/lib/python3.11/site-packages']
Server time:	
```
### solution:
 - https://github.com/pennersr/django-allauth/issues/1014

## References
[dj-rest-auth documentation](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)

[django-cors-headers document](https://pypi.org/project/django-cors-headers/)

[allauth documentation](https://docs.allauth.org/en/latest/socialaccount/providers/index.html)

[Django React JWT Authentication Applying Google Login In React.js](https://www.youtube.com/watch?v=A22oOjoH5bQ&ab_channel=Rizky%27sWebdev)

[django-react-jwt Github](https://github.com/rizkyrad24/django-react-jwt/tree/main)

[Django auth Logout](https://stackoverflow.com/questions/43069712/how-to-logout-in-django)