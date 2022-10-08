# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import models


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg','.jpeg', '.png','.doc' ,'.docx','.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Seleccione un tipo de Archivo Fotográfico, Correcto: "JPG, JPEG o PNG."')
