# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.utils import *


def index(request):
    """very simple index view"""
    data = {
        "number_of_uploads": 0
    }

    if request.GET:
        data = {
            "number_of_uploads": increment_or_initialize(request.GET["sha"])
        }
        return render(request, u'app/number.html', data)

    return render(request, "app/index.html", data)
