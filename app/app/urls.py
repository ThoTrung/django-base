"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from django_tus.views import TusUpload
# from tus_client_demo.views import DemoClientView

from core import views as core_views
from user import views as user_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('upload/', TusUpload.as_view(), name='tus_upload'),
    # path('upload/<uuid:resource_id>', TusUpload.as_view(), name='tus_upload_chunks'),

    # path('api/health-check/', core_views.health_check, name='health-check'),

    # path('api/', include('rest_framework_tus.urls', namespace='rest_framework_tus')),

    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/login/', user_views.CustomTokenObtainPairView.as_view(), name='user_login'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/user/', include('user.urls')),
    # path('api/recipe/', include('recipe.urls')),
    # path('api/job-managers/', include('job_manager.urls')),
    # path('api/customer-manager/', include('customer_manager.urls')),
    path('api/email-manager/', include('email_manager.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
