from django.urls import path
from .views import group_settlements_view

urlpatterns = [
    path("groups/<int:group_id>/settlements/", group_settlements_view),
]
