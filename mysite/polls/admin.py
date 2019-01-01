from django.contrib import admin
from .models import Question, Choice  # import Choice model

admin.site.register(Question)
admin.site.register(Choice)  # register Choice model 