from django.db import models
from django.utils import timezone
from django.db import connection

def ajout_eleve(self):
        
    cursor = connection.cursor()
    cursor.execute("SELECT ajout_eleve(%s,%s,%s,%s,%s,%s)",[self['nom'],self['prenom'],self['datenaissance'],self['lieunaissance'],self['telephone'],self['email']])
    row = cursor.fetchone()
    cursor.close()
    return row

def ajout_tuteur(self):
        
    cursor = connection.cursor()
    cursor.execute("SELECT ajout_tuteur(%s,%s,%s,%s)",[self['nom'],self['prenom'],self['telephone'],self['email']])
    #cursor.execute("SELECT ajout_tuteur(%s,%s,%s,%s)",nom,prenom,telephone,email)
    row = cursor.fetchone()
    cursor.close()
    return row

def ajout_etablissement(self):
        
    cursor = connection.cursor()
    cursor.execute("SELECT ajout_etablissement(%s,%s)",[self['nom'],self['adresse']])
    row = cursor.fetchone()
    cursor.close()
    return row
