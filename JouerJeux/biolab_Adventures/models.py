from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    score = models.IntegerField(default=300) 
    
    def _str_(self):
        return f"{self.prenom} {self.nom}"

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    niveau = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], default=1) 
    test_question = models.TextField() 
    choix1 = models.CharField(max_length=255)
    choix2 = models.CharField(max_length=255)
    choix3 = models.CharField(max_length=255)
    reponse_correct = models.CharField(max_length=255) 
    
    def _str_(self):
        return f"Question {self.id} - Niveau {self.niveau}"
    


class UserQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)  
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    choix_correct = models.CharField(max_length=255)  
    reponse_choisie = models.CharField(max_length=255)  #
    def _str_(self):
        return f"Réponse de {self.id_user.prenom} {self.id_user.nom} à la question {self.id_question.id}"
# Create your models here.
