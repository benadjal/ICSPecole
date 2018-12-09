from django.shortcuts import render
from django.http import HttpResponse
from .forms import InscriptionEleveForm
from .models import inscription_eleve
def hello(request):
	return HttpResponse("""<p>hello word!</p>""")

def inscription_get(request):
	form = InscriptionEleveForm()
	return render(request,'eleve/inscription.html',locals())



def inscription_post(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = InscriptionEleveForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        eleve = {}
        eleve['nom'] = form.cleaned_data['nom']
        eleve['prenom'] = form.cleaned_data['prenom']
        eleve['datenaissance'] = form.cleaned_data['date_naissance']
        eleve['lieunaissance'] = form.cleaned_data['lieu_naissance']
        eleve['email'] = form.cleaned_data['e_mail']
        eleve['telephone'] = form.cleaned_data['telephone']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        eleve22 = inscription_eleve(eleve)
        envoi = True
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request,'eleve/inscription.html',locals())			

# Create your views here.
