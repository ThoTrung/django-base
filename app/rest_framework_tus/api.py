# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import get_upload_model


def get_tus_upload_by_guids(guids):
  return get_upload_model().objects.filter(guid__in=guids)
