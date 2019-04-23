from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.schemas import get_schema_view
from authentication import views

# router = DefaultRouter()
# router.register(r'auth', views.AuthViewSet)

router = SimpleRouter()
router.register(r'owners', views.OwnerViewSet)
router.register(r'collaborators', views.CollaboratorViewSet)
router.register(r'readers', views.ReaderViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'', views.AuthViewSet, base_name='auth')


schema_view = get_schema_view(title='GitHub Auth API')


# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# get_github_access_code = views.AuthViewSet.as_view({
#     'get': 'get_github_access_code',
# })

convert_token = views.AuthViewSet.as_view({
    'post': 'convert_token',
})

get_github_self = views.AuthViewSet.as_view({
    'get': 'get_github_self',
})

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),




    # path('convert_token/', convert_token, name='convert_token'),
    # path('get_github_self/', get_github_self, name='get_github_self')
]
