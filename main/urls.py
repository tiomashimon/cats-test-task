from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="CATS",
        default_version='v1',
        description="API for Cats",
        # terms_of_service="https://www.yourapp.com/terms/",
        # contact=openapi.Contact(email="contact@yourapp.com"),
        # license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('api/user/', include('core_apps.user.urls')),
    path('api/cat/', include('core_apps.cat.urls')),
    path('api/profiles/', include('core_apps.profiles.urls')),



    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/auth/', include('djoser.urls')),
    re_path('api/auth/', include('djoser.urls.authtoken')),
    path("admin/", admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
