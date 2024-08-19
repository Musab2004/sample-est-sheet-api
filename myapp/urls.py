from django.urls import path
from .views import InputView

urlpatterns = [
    path("est-sheet-gen/", InputView.as_view(), name="item-create"),
]
