"""Admin configuration for electiononlineapp."""

# pylint: disable=wildcard-import, unused-wildcard-import

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Position)
