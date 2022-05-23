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
'''
class LoginForm(forms.Form):
      username=forms.CharField(max_length=100)
      password=forms.CharField(widget=forms.PasswordInput)
'''

'''
class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
      def get_region_perimeters(request):
                    return "%s" % Perimetre.region
         
class add_project_Form(ModelForm):
      def __init__(self, *args, **kwargs):
            self.request = kwargs.pop("request")
            super(add_project_Form, self).__init__(*args, **kwargs)
            self.fields['region'].queryset = Perimetre.objects.filter(user=self.request.user) 

      class Meta:
            model=Project
            fields=('Compte_Analytique','Libelles','Structure_gerante','Perimetre','Famille','Type','Etat','Fiscalite',
                  'Realisation_S1_total','Realisation_S1_devise',
                    'Prevision_S2_total','Prevision_S2_devise','Prevision_2020_total','Prevision_2020_devise',
                    'Prevision_2021_total','Prevision_2021_devise','Prevision_2022_total','Prevision_2022_devise','Prevision_2023_total',
                    'Prevision_2023_devise','Prevision_2024_total','Prevision_2024_devise','Point_situation')

            labels={
                  'Compte_Analytique':'Compte Analytique de projet',
                  'Libelles':'Libellé de projet',
                  'Structure_gerante':'Structure Gerante',
                  'Perimetre':'Périmetre',
                  'Famille':'Famille de projet',
                  'Type':'Type de projet',
                  'Etat':'Etat de projet',
                  'Fiscalite':'Fiscalité',
                   'Realisation_cum_total':'Realisation cum total',
                   'Realisation_cum_devise':'Realisation cum devise',
                   'Realisation_S1_total':'Realisation S1 total',
                   'Realisation_S1_devise':'Realisation S1 devise',
                    'Prevision_S2_total':'Prevision S2 total',
                    'Prevision_S2_devise':'Prevision S2 devise',
                    'Prevision_2020_total':'Prevision 2020 total',
                    'Prevision_2020_devise':'Prevision 2020 devise',
                    'Prevision_2021_total':'Prevision 2021 total',
                    'Prevision_2021_devise':'Prevision 2021 devise',
                    'Prevision_2022_total':'Prevision 2022 total',
                    'Prevision_2022_devise':'Prevision 2022 devise',
                    'Prevision_2023_total':'Prevision 2023 total',
                    'Prevision_2023_devise':'Prevision 2023 devise',
                    'Prevision_2024_total':'Prevision 2024 total',
                    'Prevision_2024_devise':'Prevision 2024 devise',
                    'Point_situation':'Point de situation ou commentaire',
            }
    
            widgets={
                  'Compte_Analytique':forms.TextInput(attrs={'class':'form-control'}),                 
                  'Libelles':forms.TextInput(attrs={'class':'form-control'}),      
                  'Structure_gerante':forms.Select(attrs={'class':'form-control'}),
                  'Perimetre':CustomModelMultipleChoiceField(
                        queryset=None,
                        widget=forms.CheckboxSelectMultiple
                  ),
                  'Famille':forms.Select(attrs={'class':'form-control','placeholder':"Famille de projet"}),                 
                  'Type':forms.Select(attrs={'class':'form-control','placeholder':"Type de projet"}),      
                  'Etat':forms.TextInput(attrs={'class':'form-control'}),
                  'Fiscalite':forms.TextInput(attrs={'class':'form-control'}),    
                  'Realisation_cum_total':forms.TextInput(attrs={'class':'form-control',}),
                  'Realisation_cum_devise':forms.TextInput(attrs={'class':'form-control'}),
                  'Realisation_cum':forms.TextInput(attrs={'class':'form-control'}),      
                  'Realisation_S1_total':forms.TextInput(attrs={'class':'form-control'}),
                  'Realisation_S1_devise':forms.TextInput(attrs={'class':'form-control'}),    
                  'Prevision_S2_total':forms.TextInput(attrs={'class':'form-control',}),
                  'Prevision_S2_devise':forms.TextInput(attrs={'class':'form-control',}),
                  'Prevision_2020_total':forms.TextInput(attrs={'class':'form-control'}),
                  'Prevision_2020_devise':forms.TextInput(attrs={'class':'form-control'}),      
                  'Prevision_2021_total':forms.TextInput(attrs={'class':'form-control'}),
                  'Prevision_2021_devise':forms.TextInput(attrs={'class':'form-control'}),
                  'Prevision_2022_total':forms.TextInput(attrs={'class':'form-control',}),
                  'Prevision_2022_devise':forms.TextInput(attrs={'class':'form-control',}),
                  'Prevision_2023_total':forms.TextInput(attrs={'class':'form-control'}),
                  'Prevision_2023_devise':forms.TextInput(attrs={'class':'form-control'}),      
                  'Prevision_2024_total':forms.TextInput(attrs={'class':'form-control'}),
                  'Prevision_2024_devise':forms.TextInput(attrs={'class':'form-control'}),
                  'Point_situation':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Point de situation ou commentaire"}),       
            }
'''

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
      widget=forms.TextInput(attrs={
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
      max_length=50,
      widget=forms.TextInput(attrs={
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
      max_length=50,
      widget=forms.TextInput(attrs={
            'placeholder':'',
            'class':'form-control form-control-user',

      }))
#############################################################################################################
class add_prevision_form(forms.Form):
      Montant_Prevu_janvier_Total = forms.FloatField(
            widget=forms.NumberInput(attrs={
                  'placeholder':'Jenvier',
                  'class':'form-control form-control-user',
            }))

      Montant_Prevu_janvier_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Jenvier',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_fevrier_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Fevrier',
            'class':'form-control form-control-user',

      }))
      Montant_Prevu_fevrier_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Fevrier',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_mars_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Mars',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_mars_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Mars',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_avril_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Avril',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_avril_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Avril',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_mai_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Mai',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_mai_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Mai',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_juin_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Juin',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_juin_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Juin',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_juiller_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Juillet',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_juiller_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Juillet',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_aout_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Aout',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_aout_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Aout',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_septembre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Septembre',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_septembre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Septembre',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_octobre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Octobre',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_octobre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Octobre',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_novombre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Novombre',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_novombre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Novombre',
            'class':'form-control form-control-user',
      }))

      Montant_Prevu_decembre_Total = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Decembre',
            'class':'form-control form-control-user',
      }))
      Montant_Prevu_decembre_devise = forms.FloatField(
      widget=forms.NumberInput(attrs={
            'placeholder':'Decembre',
            'class':'form-control form-control-user',
      }))

'''
class add_prevision_form(forms.Form):
      Project = forms.ModelChoiceField(queryset=Project.objects.all(),
      widget=forms.Select(attrs={'class':'form-control'}))

      Mois_prév = forms.CharField(###
      max_length=50,
      widget=forms.DateInput(attrs={
            'placeholder':'2022-01-01',
            'class':'form-control form-control-user',
            'type':'username',
            'id':'exampleInputUsername'
      }))
      Montant_Prévu_Total = forms.CharField(
      max_length=50,
      widget=forms.TextInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',
            'type':'username',
            'id':'exampleInputUsername'
      }))
      Montant_Prévu_Devise = forms.CharField(
      max_length=50,
      widget=forms.TextInput(attrs={
            'placeholder':'En Kilo Dinar',
            'class':'form-control form-control-user',
            'type':'username',
            'id':'exampleInputUsername'
      }))

'''



