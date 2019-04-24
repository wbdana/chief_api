from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view
from authentication import views


router = SimpleRouter()
router.register(r'owners', views.OwnerViewSet)
router.register(r'collaborators', views.CollaboratorViewSet)
router.register(r'readers', views.ReaderViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'', views.AuthViewSet, base_name='auth')

schema_view = get_schema_view(title='GitHub Auth API')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]
