from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from records import views

router = DefaultRouter()
router.register(r'records', views.RecordViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Records API')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]
