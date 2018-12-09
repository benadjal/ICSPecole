from django.db import models
from django.utils import timezone
from django.db import connection

"""
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    
    class Meta:
        verbose_name = "article"
        ordering = ['date']
    
    def __str__(self):
        
        return self.titre
# Create your models here.
"""

def inscription_eleve(self):
		
	cursor = connection.cursor()
	#cursor.callproc("SELECT * from televe") 
	cursor.execute("SELECT insert_eleve(%s,%s,%s,%s,%s,%s)",[self['nom'],self['prenom'],self['datenaissance'],self['lieunaissance'],self['telephone'],self['email']])
	row = cursor.fetchone()
	cursor.close()
	return row
"""
def modifie_eleve(self):
		
	cursor = connection.cursor()
	#cursor.callproc("SELECT * from televe") 
	cursor.execute("SELECT update_eleve(%s,%s,%s,%s,%s,%s)",[self['nom'],self['prenom'],self['datenaissance'],self['lieunaissance'],self['telephone'],self['email']])
	row = cursor.fetchone()
	cursor.close()
	return row
"""	
"""
def delete_eleve(self):
		
	cursor = connection.cursor()
	#cursor.callproc("SELECT * from televe") 
	cursor.execute("SELECT update_eleve(%s,%s,%s,%s,%s,%s)",[self['nom'],self['prenom'],self['datenaissance'],self['lieunaissance'],self['telephone'],self['email']])
	row = cursor.fetchone()
	cursor.close()
	return row	"""