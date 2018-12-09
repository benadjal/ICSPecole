from django import forms

class InscriptionEleveForm(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    date_naissance = forms.DateField(required=False)
    lieu_naissance = forms.CharField(max_length=100)
    e_mail = forms.EmailField(label="Votre adresse e-mail")
    telephone = forms.CharField(max_length=100)
    #message = forms.CharField(widget=forms.Textarea)
    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)