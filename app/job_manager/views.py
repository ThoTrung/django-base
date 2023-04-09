# Create your views here.
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    JobManager, JobStatus, UserSettingJob
)
from . import serializers

class JobManagerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobManagerSerializer
    queryset = JobManager.objects.all()

    def create(self, request, *args, **kwargs):
        return Response({'error': 'Creating objects is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    # permission_classes = [IsAuthenticated]
