from django.urls import path
from .views import *


urlpatterns =[
     
     path('wrk/', TaskView.as_view()),
     path('wrk/<int:id>/', TaskView.as_view()),
     path('wrk/download-csv/', TaskCSVDownload.as_view()),

]