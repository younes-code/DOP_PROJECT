from django.db import models

# Create your models here.
from asyncio.windows_events import NULL
from email.policy import default
from msilib import type_valid
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
import computed_property 
from computedfields.models import ComputedFieldsModel, computed, compute
from django.contrib.auth.models import User
from django.forms import CharField


# Create your models here.


class Famille(models.Model):
    famille_id=models.BigAutoField(primary_key=True)
    famille=models.CharField(max_length=100)
    def __str__(self):
        return self.famille

class Activité(models.Model):
    activité_id=models.BigAutoField(primary_key=True)
    activité=models.CharField(max_length=100)
    def __str__(self):
        return self.activité


class Region(models.Model):
    region_id=models.BigAutoField(primary_key=True)
    region=models.CharField(max_length=100)
    def __str__(self):
        return self.region

class Perimetre(models.Model):
    perimetre_id=models.BigAutoField(primary_key=True)
    Code_perimetre = models.CharField(max_length=30)
    perimetre=models.CharField(max_length=100)
    activite=models.ForeignKey(Activité,on_delete=models.CASCADE,null=True)
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.perimetre

class Champ(models.Model):
    champ_id=models.BigAutoField(primary_key=True)
    champ=models.CharField(max_length=100)
    activite=models.ForeignKey(Activité,on_delete=models.CASCADE,null=True)
    perimetre=models.ForeignKey(Perimetre,on_delete=models.CASCADE)
    def __str__(self):
        return self.champ

class Type(models.Model):
    type_id=models.BigAutoField(primary_key=True)
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type

class Etat(models.Model):
    etat_id=models.BigAutoField(primary_key=True)
    etat=models.CharField(max_length=100)
    def __str__(self):
        return self.etat

class Structure(models.Model):
    structure_id=models.BigAutoField(primary_key=True)
    structure=models.CharField(max_length=50)
    def __str__(self):
        return self.structure

class Fiscalite(models.Model):
    fiscalite_id=models.BigAutoField(primary_key=True)
    fiscalite=models.CharField(max_length=100)
    def __str__(self):
        return self.fiscalite


class Project(models.Model):
    PMT=models.IntegerField(null=True)
    Compte_Analytique = models.CharField(max_length=30)#
    Libelles = models.CharField(max_length=255)
    Structure_gerante = models.ForeignKey(Structure,on_delete=models.CASCADE)
    Perimetre = models.ForeignKey(Perimetre,on_delete=models.CASCADE)
    champ = models.ForeignKey(Champ,on_delete=models.CASCADE,null=True)
    Famille = models.ForeignKey(Famille,on_delete=models.CASCADE)
    Type = models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    Fiscalite = models.ForeignKey(Fiscalite,on_delete=models.CASCADE)
    Cout_Globale_initial_total=models.FloatField(default=0)##
    Cout_Globale_initial_devise=models.FloatField(default=0)##
    Realisation_cum_total = models.FloatField(max_length=50,blank=True)
    Realisation_cum_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_devise = models.FloatField(max_length=50,)
    Realisation_S1_total = models.FloatField(max_length=50,)
    Prevision_S2_total = models.FloatField(max_length=30)
    Previson_de_cloture_total=models.FloatField(default=0)##
    Prevision_S2_devise= models.FloatField(max_length=30,)
    Previson_de_cloture_devise=models.FloatField(default=0)##
    Reste_a_realiser_total=models.FloatField(default=0)#
    Reste_a_realiser_devise=models.FloatField(default=0)##
    Prevision_n_total = models.FloatField(max_length=30,)
    Prevision_n_devise = models.FloatField(max_length=30,)
    Prevision_n1_total = models.FloatField(max_length=30,)
    Prevision_n1_devise = models.FloatField(max_length=30,)
    Prevision_n2_total = models.FloatField(max_length=30,)
    Prevision_n2_devise = models.FloatField(max_length=30,)
    Prevision_n3_total = models.FloatField(max_length=30,)
    Prevision_n3_devise = models.FloatField(max_length=30,)
    Prevision_n4_total = models.FloatField(max_length=30,)
    Prevision_n4_devise = models.FloatField(max_length=30,)
    Point_situation = models.CharField(max_length=1000)
    Project_puit=models.CharField(max_length=50,null=True)



    def __str__(self):
        return self.Libelles


class Prévision_mensuelle(models.Model):
    prevision_mensuelle_id=models.BigAutoField(primary_key=True)
    Mois_prev=models.CharField(max_length=50,null=True)
    Montant_Prevu_Total = models.FloatField(max_length=30)
    Montant_Prevu_Devise = models.FloatField(max_length=30)
    Prev_cum_total = models.FloatField(max_length=30,default=0)
    Prev_cum_devise = models.FloatField(max_length=30,default=0)       
    Project=models.ForeignKey(Project, on_delete=models.CASCADE)




class Realisation_mensuelle(models.Model):
    PMT=models.IntegerField(null=True)
    Realisation_mensuelle_id=models.BigAutoField(primary_key=True)
    Mois_real=models.CharField(max_length=50,null=True)
    prevision_mensuelle_id=models.ForeignKey(Prévision_mensuelle,on_delete=models.CASCADE,null=True)
    Montant_real_Total = models.FloatField(max_length=30)
    Montant_real_Devise = models.FloatField(max_length=30)
    Point_situation = models.CharField(max_length=1000,)
    Project=models.ForeignKey(Project, on_delete=models.CASCADE)
    real_cum_total=models.FloatField(default=0)#
    real_cum_devise=models.FloatField(default=0)#
    taux_real_mois=models.FloatField(default=0)#
    taux_real_cum=models.FloatField(default=0)#
    taux_real_ann=models.FloatField(default=0)#


    def __str__(self):
        return str(self.Project.Libelles) +'-'+str(self.Mois_real)


class Stimulation(models.Model):
    PMT=models.IntegerField(null=True)
    stimulation_id=models.BigAutoField(primary_key=True)
    stimulation=models.CharField(max_length=255)  
    Compte_Analytique = models.CharField(max_length=30,null=True)#
    Structure_gerante = models.ForeignKey(Structure,on_delete=models.CASCADE,null=True)
    Perimetre = models.ForeignKey(Perimetre,on_delete=models.CASCADE,null=True)
    champ = models.ForeignKey(Champ,on_delete=models.CASCADE,null=True)
    Famille = models.ForeignKey(Famille,on_delete=models.CASCADE,null=True)
    Type = models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    Fiscalite = models.ForeignKey(Fiscalite,on_delete=models.CASCADE,null=True)  
    Cout_Globale_initial_total=models.FloatField(default=0)##
    Cout_Globale_initial_devise=models.FloatField(default=0)##
    Realisation_cum_total = models.FloatField(max_length=50,blank=True)
    Realisation_cum_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_devise = models.FloatField(max_length=50,)
    Realisation_S1_total = models.FloatField(max_length=50,)
    Prevision_S2_total = models.FloatField(max_length=30)
    Previson_de_cloture_total=models.FloatField(default=0)##
    Prevision_S2_devise= models.FloatField(max_length=30,)
    Previson_de_cloture_devise=models.FloatField(default=0)##
    Reste_a_realiser_total=models.FloatField(default=0)#
    Reste_a_realiser_devise=models.FloatField(default=0)##
    Prevision_n_total = models.FloatField(max_length=30,)
    Prevision_n_devise = models.FloatField(max_length=30,)
    Prevision_n1_total = models.FloatField(max_length=30,)
    Prevision_n1_devise = models.FloatField(max_length=30,)
    Prevision_n2_total = models.FloatField(max_length=30,)
    Prevision_n2_devise = models.FloatField(max_length=30,)
    Prevision_n3_total = models.FloatField(max_length=30,)
    Prevision_n3_devise = models.FloatField(max_length=30,)
    Prevision_n4_total = models.FloatField(max_length=30,)
    Prevision_n4_devise = models.FloatField(max_length=30,)
    Point_situation = models.CharField(max_length=1000)
    Project_puit=models.BooleanField(max_length=50,null=True)

    def __str__(self):
        return self.stimulation

class Prévision_mensuelle_stimulation(models.Model):
    prevision_mensuelle_id=models.BigAutoField(primary_key=True)
    Mois_prev=models.CharField(max_length=50,null=True)
    Montant_Prevu_Total = models.FloatField(max_length=30)
    Montant_Prevu_Devise = models.FloatField(max_length=30)
    Prev_cum_total = models.FloatField(max_length=30,default=0)
    Prev_cum_devise = models.FloatField(max_length=30,default=0)       
    Stimulation=models.ForeignKey(Stimulation, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.Stimulation.stimulation) +'-'+ str(self.Mois_prev)



class  Acces(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    region=models.OneToOneField(Region,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) +'-'+str(self.region)

class Recap_region(models.Model):
    PMT=models.IntegerField(null=True)
    region=models.CharField(max_length=1000,)
    CGI_total=models.FloatField(null=True)
    CGI_devise=models.FloatField(null=True)
    Realisation_cum_total = models.FloatField(max_length=50,blank=True)
    Realisation_cum_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_total = models.FloatField(max_length=50,blank=True)
    Prevision_S2_total = models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_total=models.FloatField(default=0,blank=True)##
    Prevision_S2_devise= models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_devise=models.FloatField(default=0)##
    Reste_a_realiser_total=models.FloatField(default=0)#
    Reste_a_realiser_devise=models.FloatField(default=0)##
    Prevision_n_total = models.FloatField(max_length=30,blank=True)
    Prevision_n_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n1_total = models.FloatField(max_length=30,blank=True)
    Prevision_n1_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n2_total = models.FloatField(max_length=30,blank=True)
    Prevision_n2_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n3_total = models.FloatField(max_length=30,blank=True)
    Prevision_n3_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n4_total = models.FloatField(max_length=30,blank=True)
    Prevision_n4_devise = models.FloatField(max_length=30,blank=True)

    def __str__(self):
        return self.region
    
class Recap_famille(models.Model):
    PMT=models.IntegerField(null=True)
    famille= models.CharField(max_length=1000,)
    CGI_total=models.FloatField(null=True)
    CGI_devise=models.FloatField(null=True)
    Realisation_cum_total = models.FloatField(max_length=50,blank=True)
    Realisation_cum_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_total = models.FloatField(max_length=50,blank=True)
    Prevision_S2_total = models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_total=models.FloatField(default=0)##
    Prevision_S2_devise= models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_devise=models.FloatField(default=0)##
    Reste_a_realiser_total=models.FloatField(default=0)#
    Reste_a_realiser_devise=models.FloatField(default=0)##
    Prevision_n_total = models.FloatField(max_length=30,blank=True)
    Prevision_n_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n1_total = models.FloatField(max_length=30,blank=True)
    Prevision_n1_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n2_total = models.FloatField(max_length=30,blank=True)
    Prevision_n2_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n3_total = models.FloatField(max_length=30,blank=True)
    Prevision_n3_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n4_total = models.FloatField(max_length=30,blank=True)
    Prevision_n4_devise = models.FloatField(max_length=30,blank=True)

    def __str__(self):
        return self.famille

class Recap_activite(models.Model):
    PMT=models.IntegerField(null=True)
    activite= models.CharField(max_length=1000,)
    CGI_total=models.FloatField(null=True)
    CGI_devise=models.FloatField(null=True)
    Realisation_cum_total = models.FloatField(max_length=50,blank=True)
    Realisation_cum_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_total = models.FloatField(max_length=50,blank=True)
    Prevision_S2_total = models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_total=models.FloatField(default=0)##
    Prevision_S2_devise= models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_devise=models.FloatField(default=0)##
    Reste_a_realiser_total=models.FloatField(default=0)#
    Reste_a_realiser_devise=models.FloatField(default=0)##
    Prevision_n_total = models.FloatField(max_length=30,blank=True)
    Prevision_n_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n1_total = models.FloatField(max_length=30,blank=True)
    Prevision_n1_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n2_total = models.FloatField(max_length=30,blank=True)
    Prevision_n2_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n3_total = models.FloatField(max_length=30,blank=True)
    Prevision_n3_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n4_total = models.FloatField(max_length=30,blank=True)
    Prevision_n4_devise = models.FloatField(max_length=30,blank=True)

    def __str__(self):
        return self.activite

class Recap(models.Model):
    PMT=models.IntegerField(null=True)
    region=models.CharField(max_length=1000,)
    famille= models.CharField(max_length=1000,)
    activite= models.CharField(max_length=1000,)
    CGI_total=models.FloatField(null=True)
    CGI_devise=models.FloatField(null=True)
    Realisation_cum_total = models.FloatField(max_length=50,blank=True)
    Realisation_cum_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_devise = models.FloatField(max_length=50,blank=True)
    Realisation_S1_total = models.FloatField(max_length=50,blank=True)
    Prevision_S2_total = models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_total=models.FloatField(default=0)##
    Prevision_S2_devise= models.FloatField(max_length=30,blank=True)
    Previson_de_cloture_devise=models.FloatField(default=0)##
    Reste_a_realiser_total=models.FloatField(default=0)#
    Reste_a_realiser_devise=models.FloatField(default=0)##
    Prevision_n_total = models.FloatField(max_length=30,blank=True)
    Prevision_n_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n1_total = models.FloatField(max_length=30,blank=True)
    Prevision_n1_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n2_total = models.FloatField(max_length=30,blank=True)
    Prevision_n2_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n3_total = models.FloatField(max_length=30,blank=True)
    Prevision_n3_devise = models.FloatField(max_length=30,blank=True)
    Prevision_n4_total = models.FloatField(max_length=30,blank=True)
    Prevision_n4_devise = models.FloatField(max_length=30,blank=True)

    def __str__(self):
        return self.region+'-'+self.famille+'-'+ self.activite