from django.urls import path
from . import views
from . import marksheets
from formexample.feedviews import Feedback
urlpatterns=[

path('',views.index,name='index'),
path('addlogic',views.addlogic,name='addlogic'),
path('fact',views.fact,name='fact'),
path('fibo',views.fibo,name='fibo'),
path('marksheet',marksheets.marksheet,name='marksheet'),
path('feedback',Feedback.as_view()),



]