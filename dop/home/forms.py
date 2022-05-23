from cgitb import text
from dataclasses import field
from tkinter import Label, Widget
from turtle import textinput
from django import forms
from django.forms import ModelForm, PasswordInput
from numpy import blackman
from .models import *
import datetime


#Cearting project form
####################### admin forms ######################################

PROJECT_CHOICES= [
    ('stimulation', 'Stimulation'),
    ('acidification', 'Acidification'),
    ('fracturation', 'Fracturation'),
    ('Autre', 'Autre'),
   ]

class add_project_Form(forms.Form):
      Compte_Analytique = forms.CharField(
      required=False,
      label='Compte Analytique',
      max_length=50,
      widget=forms.TextInput(attrs={
            'placeholder':'',
            'class':'form-control form-control-user',


      }))
      Libelles = forms.CharField(
      label='Libellé ',
      max_length=1000000,
      widget=forms.TextInput(attrs={
            'placeholder':'',
            'class':'form-control form-control-user',

      }))
      Structure_gerante = forms.ModelChoiceField(queryset=Structure.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
            label='Structure gérante',
      )
      
      Perimetre =  forms.ModelChoiceField(queryset=Perimetre.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
            label='Perimetre',)
      
      Champ =  forms.ModelChoiceField(queryset=Champ.objects.all(),
      required=False,
      widget=forms.Select(attrs={'class':'form-control'}),
            label='Champ',)
        
      Famille = forms.ModelChoiceField(queryset=Famille.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
      label='Famille',
      )

      Type = forms.ModelChoiceField(queryset=Type.objects.all(),
      required=False,
      widget=forms.Select(attrs={'class':'form-control'}),
      label='Type',
      )
      
      Fiscalite = forms.ModelChoiceField(queryset=Fiscalite.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
      label='Fiscalite',
      )

      Realisation_cum_total = forms.FloatField(
      label='Realisation cumuée réelle total',
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Realisation_cum_devise = forms.FloatField(
      label='Realisation cumuée réelle devise',
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Realisation_S1_total = forms.FloatField(
      label='Realisation s1 total',
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Realisation_S1_devise = forms.FloatField(
      label='Realisation s1 devise',
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Prevision_S2_total = forms.FloatField(
      label='Prévision s2 total',
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Prevision_S2_devise = forms.FloatField(
      label='Prévision s2 devise',
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Prevision_n_total = forms.FloatField(
      label="Prévision d'année n total",
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Prevision_n_devise = forms.FloatField(
      label="Prévision d'année n devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Prevision_n1_total = forms.FloatField(
      label="Prévision d'année n+1 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Prevision_n1_devise = forms.FloatField(
      label="Prévision d'année n+1 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Prevision_n2_total = forms.FloatField(
      label="Prévision d'année n+2 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Prevision_n2_devise = forms.FloatField(
      label="Prévision d'année n+2 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Prevision_n3_total = forms.FloatField(
      label="Prévision d'année n+3 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Prevision_n3_devise = forms.FloatField(
      label="Prévision d'année n+3 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Prevision_n4_total = forms.FloatField(
      label="Prévision d'année n+4 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Prevision_n4_devise = forms.FloatField(
      label="Prévision d'année n+4 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'Don Devise',
            'class':'form-control form-control-user',

      }))
      Point_situation = forms.CharField(
      max_length=1000000,
      widget=forms.Textarea(attrs={
            'rows':5,
            'placeholder':'',
            'class':'form-control form-control-user',

      }))
      Project_puit=forms.BooleanField(
      required=False,
      label='Veuillez préciser si le projet est une stimulaton :',      
      )



############################################################################
class add_stimulation(forms.Form):
      Compte_Analytique = forms.CharField(
      required=False,
      label='Compte Analytique',
      max_length=1000000,
      widget=forms.TextInput(attrs={
            'placeholder':'',
            'class':'form-control form-control-user',


      }))
      Libelles = forms.CharField(
      label='Libellé ',
      max_length=1000000,
      widget=forms.TextInput(attrs={
            'placeholder':'',
            'class':'form-control form-control-user',

      }))
      Structure_gerante = forms.ModelChoiceField(queryset=Structure.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
            label='Structure gérante',
      )
      
      Perimetre =  forms.ModelChoiceField(queryset=Perimetre.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
            label='Perimetre',)
      
      Champ =  forms.ModelChoiceField(queryset=Champ.objects.all(),
      required=False,
      widget=forms.Select(attrs={'class':'form-control'}),
            label='Champ',)
        
      Famille = forms.ModelChoiceField(queryset=Famille.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
      label='Famille',
      )

      Type = forms.ModelChoiceField(queryset=Type.objects.all(),
      required=False,
      widget=forms.Select(attrs={'class':'form-control'}),
      label='Type',
      )
      
      Fiscalite = forms.ModelChoiceField(queryset=Fiscalite.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}),
      label='Fiscalite',
      )

      Realisation_cum_total = forms.FloatField(
      label='Realisation cumuée réelle total',
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Realisation_cum_devise = forms.FloatField(
      label='Realisation cumuée réelle devise',
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Realisation_S1_total = forms.FloatField(
      label='Realisation s1 total',
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Realisation_S1_devise = forms.FloatField(
      label='Realisation s1 devise',
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_S2_total = forms.FloatField(
      label='Prévision s2 total',
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_S2_devise = forms.FloatField(
      label='Prévision s2 devise',
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n_total = forms.FloatField(
      label="Prévision d'année n total",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n_devise = forms.FloatField(
      label="Prévision d'année n devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n1_total = forms.FloatField(
      label="Prévision d'année n+1 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n1_devise = forms.FloatField(
      label="Prévision d'année n+1 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n2_total = forms.FloatField(
      label="Prévision d'année n+2 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n2_devise = forms.FloatField(
      label="Prévision d'année n+2 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n3_total = forms.FloatField(
      label="Prévision d'année n+3 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n3_devise = forms.FloatField(
      label="Prévision d'année n+3 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n4_total = forms.FloatField(
      label="Prévision d'année n+4 total",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Prevision_n4_devise = forms.FloatField(
      label="Prévision d'année n+4 devise",
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Point_situation = forms.CharField(
      max_length=1000000,
      widget=forms.Textarea(attrs={
            'rows':5,
            'placeholder':'',
            'class':'form-control form-control-user',

      }))
######################################################################################################
class search_form_region(forms.Form):
      region = forms.CharField(max_length=100,
      label='',
      widget=forms.TextInput(attrs={
            'placeholder':'',
            'class':'form-control form-control-user',

      }))
      

class search_month_form(forms.Form):
      Month = forms.CharField(
      label='',
      widget=forms.TextInput(attrs={
            'placeholder':'Mois',
            'class':'form-control form-control-user',

      }))

class search_form(forms.Form):
      annee = forms.IntegerField(
      label='',
      widget=forms.NumberInput(attrs={
            'placeholder':datetime.date.today().year+0,
            'class':'form-control form-control-user',

      }))
#######################################################################################################
class add_realisation_form(forms.Form):
    
      Project = forms.ModelChoiceField(queryset=Project.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}))



      tab=( 
            ("janvier","javnier"),
            ("fevrier","fevrier"),
            ("mars","mars"),
            ("avril","avril"),
            ("mai","mai"),
            ("juin","juin"),
            ("juillet","juillet"),
            ("aout","aout"),
            ("sptembre","sptembre"),
            ("octobre","octobre"),
            ("novombre","novombre"),
            ("decembre","decembre"),
      )
      Mois_real = forms.ChoiceField(choices=tab,
      widget=forms.Select(attrs={'class':'form-control'}))

      
      Montant_real_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',
      }))
      Montant_real_Devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',

      }))
      Point_situation = forms.CharField(
      max_length=1000000,
      widget=forms.Textarea(attrs={
            'rows':5,
            'placeholder':'',
            'class':'form-control form-control-user',

      }))
#############################################################################################################
class add_prevision_form(forms.Form):
      Montant_Prevu_janvier_Total = forms.FloatField(
            widget=forms.NumberInput(attrs={
                  'placeholder':'Total',
                  'class':'form-control form-control-user',
            }))

      Montant_Prevu_janvier_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_fevrier_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',

      }))
      Montant_Prevu_fevrier_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_mars_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_mars_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_avril_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_avril_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_mai_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_mai_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_juin_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_juin_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_juiller_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_juiller_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_aout_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_aout_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_septembre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_septembre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_octobre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_octobre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_novombre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_novombre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_decembre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Total',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_decembre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Don devise',
            'class':'form-control form-control-user',
      }))




