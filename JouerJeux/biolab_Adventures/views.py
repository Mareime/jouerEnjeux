from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import User,UserQuestion,Question
# from django
# Create your views here.

def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request,"login.html")
# @login_required
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        
        user = User.objects.filter(email=username, mot_de_passe=password).first()

        if user:
            request.session['user']=user.id
            questions_non_repondue = Question.objects.exclude(
                id__in=UserQuestion.objects.filter(id_user=user).values('id_question__id')
            )  
            return render(request,"quiz.html",{'user':user,'questions':questions_non_repondue})
        else:
            return render(request,"login.html")
        
    

def GetSunup(request):
    return render(request, 'sunup.html')

def Sunup(request):
    if request.method == 'POST':
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User(username=nom,prenom=prenom ,mot_de_passe=email, password=password)
        user.save()
        return HttpResponse("user created")
        



# @login_required

def quiz(request, question_id, reponce):
    id_user = request.session['user']
    user = User.objects.filter(id=id_user).first()
    return HttpResponse(id_user)
    # Récupérer la question actuelle en fonction de question_id
    # question_v = get_object_or_404(Question, id=question_id)
    # qu_v = question_v.reponse_correct

    # Vérifier si la réponse donnée est correcte
    # if qu_v == reponce:
        # Si la réponse est correcte, ajouter des points au score de l'utilisateur
        # user.score += 5
        # user.save()

    # Enregistrer la réponse de l'utilisateur dans la base de données
    # UserQuestion.objects.create(
    #     id_user=user,
    #     id_question=question_v,
    #     choix_correct=(qu_v == reponce),
    #     reponse_choisie=reponce
    # )
    # request.session['user']=user.id
    # questions_non_repondue = Question.objects.exclude(
    #             id__in=UserQuestion.objects.filter(id_user=user).values('id_question__id')
    #         )
    # return render(request,"quiz.html",{'user':user,'questions':questions_non_repondue})
    