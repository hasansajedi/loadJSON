from django.urls import path

from app.views import report, analyze, parse

urlpatterns = [
    path(r'', analyze, name='analyze'),
    path(r'report/', report, name='report'),
    path(r'parse/', parse, name='parse'),
]
