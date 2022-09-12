from django.urls import path

from . import views

urlpatterns = [
    path("wallets/", views.WalletView.as_view()),
    path("wallets/<str:wallet_id>/", views.SubTotalWalletView.as_view()),
]
