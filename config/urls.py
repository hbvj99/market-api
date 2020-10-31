from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('market.api.v1.urls')),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]

if settings.DEBUG:
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    from django.views.generic import RedirectView

    schema_view = get_schema_view(
        openapi.Info(
            title="Market API docs",
            default_version='v1',
            description="Market API documentation",
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path('', RedirectView.as_view(url='/api/v1/docs/', permanent=True), name='home'),
        path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
    ]

    # serve media
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
