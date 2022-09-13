from django.urls import path

from . import views

urlpatterns = [
    path("transactions/", views.ListCreateTransactionView.as_view()),
    path("transactions/<str:wallet_id>/", views.ListTransactionView.as_view()),
]
