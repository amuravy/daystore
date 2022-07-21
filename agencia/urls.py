from agencia.views import AutoView
from django.urls import include, path

urlpatterns = [
    path('auto', AutoView.as_view()),
]