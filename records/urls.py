from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view
from records import views

records_router = SimpleRouter()
records_router.register(r'records', views.RecordViewSet)
