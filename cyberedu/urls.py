from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('topic/<int:id>/preview/',views.topic_preview,name = 'topic_preview'),
    path('topic/<int:id>',views.topic_detail,name = 'topic_detail'),
    path('quiz/<int:topic_id>/',views.quiz_view, name = 'quiz'),
    path('search/',views.search, name = 'search'),
    path('phishing/',views.phishing,name = 'phishing'),
]
