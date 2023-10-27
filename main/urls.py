from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from main.views import test, user, VerifyUser, update_avatar_view, users, CryptosView, CryptoView, RUDCryptosView, \
    AmountView, AmountListView, GetUserAmounts, UpdateUserView, ChangeAmountView, CheckAmount, LowerAmount, DisableUser, \
    ChangeLevelView, ChnageActivityUserView, Oauth, OAuthLogin

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('update_avatar/<pk>', update_avatar_view.as_view()),
    path('ChangeAmountView/', ChangeAmountView),
    path('CheckAmount/', CheckAmount),
    path('LowerAmount/', LowerAmount),
    path('DisableUser/', DisableUser),
    path('DisableUser/', DisableUser),
    path('amount/', AmountView.as_view()),
    path('UpdateUser/<pk>', UpdateUserView.as_view()),
    path('GetUserAmounts/', GetUserAmounts.as_view()),
    path('amounts/', AmountListView.as_view()),
    path('RUDCryptos/<pk>', RUDCryptosView.as_view()),
    path('user/', user.as_view()),
    path('Oauth/', Oauth.as_view()),
    path('OAuthLogin/', OAuthLogin.as_view()),
    path('users/', users.as_view()),
    path('cryptos/', CryptosView.as_view()),
    path('cryptoslist/', CryptoView.as_view()),
    path('VerifyUser/', VerifyUser),
    path('ChangeLevel/', ChangeLevelView),
    path('ChnageActivityUser/', ChnageActivityUserView),
    path('test/', test),
]
