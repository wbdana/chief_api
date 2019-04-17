from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from auth import views

# router = DefaultRouter()
# router.register(r'auth', views.AuthViewSet)

# schema_view = get_schema_view(title='GitHub Auth API')


# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])

get_github_access_code = views.AuthViewSet.as_view({
    'get': 'get_github_access_code',
})


urlpatterns = [
    # path('', include(router.urls)),
    # path('schema/', schema_view),


    # path('login/', views.get_github_access_code, name='get_github_access_code'),
    path('login/', get_github_access_code, name='get_github_access_code')
]
