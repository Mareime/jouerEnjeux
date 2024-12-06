from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.index, name="userlogin"),
    path('login_user/', views.login, name='login'),
    path('sunup/', views.GetSunup, name='GetSunup'),
    # path('quiz/', views.quiz, name='quiz'),  # Vous devrez probablement passer `question_id` à cette URL
    path('quiz/<int:question_id>/', views.quiz, name='quiz_question'),
    path('reponce/<int:question_id>/<repon>/', views.reponc, name='reponce'),

]
