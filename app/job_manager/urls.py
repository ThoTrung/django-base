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
    path('list-specify-folder-from-disk', views.ListSpecifyFolderFromDiskView.as_view()),
    path('search-folder-setting', views.SearchFolderSettingView.as_view()),
]
