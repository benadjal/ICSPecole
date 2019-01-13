from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .forms import InscriptionEleveForm
from .models import ajout_eleve
from .models import ajout_tuteur
from .models import ajout_etablissement
def acceuil(request):
    return render(request,'acceuil.html',locals())

def inscription_get(request):
    #form = InscriptionEleveForm()
    return render(request,'eleve/inscription.html',locals())



def inscription_post(request):
    
    #form = InscriptionEleveForm(request.POST or None)
    #if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
    #print(request)
    eleve = {}
    
    eleve['nom'] = request.POST['nom']
    eleve['prenom'] = request.POST['prenom']
    eleve['datenaissance'] = request.POST['date_naissance']
    eleve['lieunaissance'] = request.POST['lieu_naissance']
    eleve['email'] = request.POST['email']
    eleve['telephone'] = request.POST['telephone']
    print(eleve)
    print(type(eleve))
    eleveAdd = ajout_eleve(eleve)
    envoi = True
    
    return render(request,'eleve/inscription.html',locals())            
    
def ajout_tuteur(request):
    #print(request)
    #tuteur = request.POST['data']
     
    tuteur = {}
    """
    tuteur['nom'] = request.POST['nom_tuteur']
    tuteur['prenom'] = request.POST['prenom_tuteur']
    tuteur['email'] = request.POST['email_tuteur']
    tuteur['telephone'] = request.POST['telephone_tuteur']
    """
    nom = request.POST['nom_tuteur']
    prenom = request.POST['prenom_tuteur']
    email = request.POST['email_tuteur']
    telephone = request.POST['telephone_tuteur']
    print(tuteur)   
    print(type(tuteur))
    tuteurADD = ajout_tuteur(nom,prenom,email,telephone)
    
    print(tuteur['nom'])
    print(tuteur['prenom'])
    print(tuteur['email'])
    print(tuteur['telephone'])
    
    return render(request,'eleve/inscription.html',locals())    

def ajout_etablissement(request):
    #print(request)
    #tuteur = request.POST['data']
     
    #etablissement = {}
    #etablissement['nom'] = request.POST['nom_etablissement']
    #etablissement['adresse'] = request.POST['adresse_etablissement']
    #print(etablissement)   
    #print(type(etablissement))
    
    etablissement1 = {}
    etablissement1['nom'] = 'nom_etablissement'
    etablissement1['adresse'] = 'adresse_etablissement'
    
    etablissementADD = ajout_etablissement(etablissement1)
    """
    print(etablissement['nom'])
    print(etablissement['adresse'])
    """
    return render(request,'eleve/inscription.html',locals())     