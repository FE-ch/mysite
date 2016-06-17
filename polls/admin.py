# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2016-06-18 01:18:04
# @Last Modified by:   root
# @Last Modified time: 2016-06-18 01:33:43
from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

