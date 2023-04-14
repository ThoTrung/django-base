from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.JobManagerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-folder-from-disk', views.ListFolderFromDiskView.as_view()),
    path('user-setting-job', views.UserSettingJobViewGet.as_view()),
    path('user-setting-job/<key>', views.UserSettingJobViewPut.as_view()),
]
