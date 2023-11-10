from django.shortcuts import render
from django.http import HttpResponse

# https://docs.allauth.org/en/latest/socialaccount/providers/index.html
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client


def HelloWorld(request):
    return render(request, "google_login.html")
    return HttpResponse('Hello World!')