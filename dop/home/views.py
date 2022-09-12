from cmath import log
from email import message
from genericpath import exists
from multiprocessing import context
from pickle import NONE
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponsePermanentRedirect,HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
#from django.contrib.auth.forms import UserCreationForm

from .forms import *
from .models import *

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)# check if they exist

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, "Mot de passe ou nom d'utilisateur incorrect")

		context = {}
		return render(request, 'authenticate/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def delete_realisation (request,pk):
      realisation=Realisation_mensuelle.objects.filter(Realisation_mensuelle_id=pk)
      if realisation.exists():
            realisation=Realisation_mensuelle.objects.get(Realisation_mensuelle_id=pk)
            if request.method=="POST":
                  realisation.delete()
                  messages.success(request,"La réalisation a été supprimé avec succès")     
                  return redirect('Mensuel')
            return render(request,'delete.html')

#function to delete projects (delete button)
@login_required(login_url='login')
def delete_project (request,pk):
      project=Project.objects.filter(id=pk)
      if project.exists():
            project=Project.objects.get(id=pk)
            if request.method=="POST":

                  r_reg = Recap_region.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region)
                  r_reg.CGI_total= r_reg.CGI_total- project.Cout_Globale_initial_total
                  r_reg.CGI_devise= r_reg.CGI_devise- project.Cout_Globale_initial_devise
                  r_reg.Previson_de_cloture_total= r_reg.Previson_de_cloture_total- project.Previson_de_cloture_total
                  r_reg.Previson_de_cloture_devise= r_reg.Previson_de_cloture_devise- project.Previson_de_cloture_devise                 
                  r_reg.Reste_a_realiser_total= r_reg.Reste_a_realiser_total- project.Reste_a_realiser_total
                  r_reg.Reste_a_realiser_devise= r_reg.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                  r_reg.Realisation_cum_total=r_reg.Realisation_cum_total-project.Realisation_cum_total
                  r_reg.Realisation_cum_devise=r_reg.Realisation_cum_devise- project.Realisation_cum_devise
                  r_reg.Realisation_S1_total=r_reg.Realisation_S1_total-project.Realisation_S1_total
                  r_reg.Realisation_S1_devise=r_reg.Realisation_S1_devise-project.Realisation_S1_devise
                  r_reg.Prevision_S2_total=r_reg.Prevision_S2_total-project.Prevision_S2_total
                  r_reg.Prevision_S2_devise=r_reg.Prevision_S2_devise-project.Prevision_S2_devise
                  r_reg.Prevision_n_total=r_reg.Prevision_n_total-project.Prevision_n_total
                  r_reg.Prevision_n_devise=r_reg.Prevision_n_devise-project.Prevision_n_devise
                  r_reg.Prevision_n1_total=r_reg.Prevision_n1_total-project.Prevision_n1_total
                  r_reg.Prevision_n1_devise=r_reg.Prevision_n1_devise-project.Prevision_n1_devise
                  r_reg.Prevision_n2_total=r_reg.Prevision_n2_total-project.Prevision_n2_total
                  r_reg.Prevision_n2_devise=r_reg.Prevision_n2_devise-project.Prevision_n2_devise
                  r_reg.Prevision_n3_total=r_reg.Prevision_n3_total-project.Prevision_n3_total
                  r_reg.Prevision_n3_devise=r_reg.Prevision_n3_devise-project.Prevision_n3_devise
                  r_reg.Prevision_n4_total=r_reg.Prevision_n4_total-project.Prevision_n4_total
                  r_reg.Prevision_n4_devise=r_reg.Prevision_n4_devise-project.Prevision_n4_devise
                  r_reg.save()

                  r_fam = Recap_famille.objects.get(PMT=datetime.date.today().year+0,famille=project.Famille)
                  r_fam.CGI_total= r_fam.CGI_total- project.Cout_Globale_initial_total
                  r_fam.CGI_devise= r_fam.CGI_devise- project.Cout_Globale_initial_devise
                  r_fam.Previson_de_cloture_total= r_fam.Previson_de_cloture_total- project.Previson_de_cloture_total
                  r_fam.Previson_de_cloture_devise= r_fam.Previson_de_cloture_devise- project.Previson_de_cloture_devise        
                  r_fam.Reste_a_realiser_total= r_fam.Reste_a_realiser_total- project.Reste_a_realiser_total
                  r_fam.Reste_a_realiser_devise= r_fam.Reste_a_realiser_devise- project.Reste_a_realiser_devise             
                  r_fam.Realisation_cum_total=r_fam.Realisation_cum_total-project.Realisation_cum_total
                  r_fam.Realisation_cum_devise=r_fam.Realisation_cum_devise- project.Realisation_cum_devise
                  r_fam.Realisation_S1_total=r_fam.Realisation_S1_total-project.Realisation_S1_total
                  r_fam.Realisation_S1_devise=r_fam.Realisation_S1_devise-project.Realisation_S1_devise
                  r_fam.Prevision_S2_total=r_fam.Prevision_S2_total-project.Prevision_S2_total
                  r_fam.Prevision_S2_devise=r_fam.Prevision_S2_devise-project.Prevision_S2_devise
                  r_fam.Prevision_n_total=r_fam.Prevision_n_total-project.Prevision_n_total
                  r_fam.Prevision_n_devise=r_fam.Prevision_n_devise-project.Prevision_n_devise
                  r_fam.Prevision_n1_total=r_fam.Prevision_n1_total-project.Prevision_n1_total
                  r_fam.Prevision_n1_devise=r_fam.Prevision_n1_devise-project.Prevision_n1_devise
                  r_fam.Prevision_n2_total=r_fam.Prevision_n2_total-project.Prevision_n2_total
                  r_fam.Prevision_n2_devise=r_fam.Prevision_n2_devise-project.Prevision_n2_devise
                  r_fam.Prevision_n3_total=r_fam.Prevision_n3_total-project.Prevision_n3_total
                  r_fam.Prevision_n3_devise=r_fam.Prevision_n3_devise-project.Prevision_n3_devise
                  r_fam.Prevision_n4_total=r_fam.Prevision_n4_total-project.Prevision_n4_total
                  r_fam.Prevision_n4_devise=r_fam.Prevision_n4_devise-project.Prevision_n4_devise
                  r_fam.save()
                  if str(project.Perimetre.activite)=="Pétrole" or str(project.Perimetre.activite)=="Gaz":
                        r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=project.Perimetre.activite)
                        r_act.CGI_total= r_act.CGI_total- project.Cout_Globale_initial_total
                        r_act.CGI_devise= r_act.CGI_devise- project.Cout_Globale_initial_devise
                        r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total- project.Previson_de_cloture_total
                        r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise- project.Previson_de_cloture_devise                       
                        r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total- project.Reste_a_realiser_total
                        r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise- project.Reste_a_realiser_devise                        
                        r_act.Realisation_cum_total=r_act.Realisation_cum_total-project.Realisation_cum_total
                        r_act.Realisation_cum_devise=r_act.Realisation_cum_devise- project.Realisation_cum_devise
                        r_act.Realisation_S1_total=r_act.Realisation_S1_total-project.Realisation_S1_total
                        r_act.Realisation_S1_devise=r_act.Realisation_S1_devise-project.Realisation_S1_devise
                        r_act.Prevision_S2_total=r_act.Prevision_S2_total-project.Prevision_S2_total
                        r_act.Prevision_S2_devise=r_act.Prevision_S2_devise-project.Prevision_S2_devise
                        r_act.Prevision_n_total=r_act.Prevision_n_total-project.Prevision_n_total
                        r_act.Prevision_n_devise=r_act.Prevision_n_devise-project.Prevision_n_devise
                        r_act.Prevision_n1_total=r_act.Prevision_n1_total-project.Prevision_n1_total
                        r_act.Prevision_n1_devise=r_act.Prevision_n1_devise-project.Prevision_n1_devise
                        r_act.Prevision_n2_total=r_act.Prevision_n2_total-project.Prevision_n2_total
                        r_act.Prevision_n2_devise=r_act.Prevision_n2_devise-project.Prevision_n2_devise
                        r_act.Prevision_n3_total=r_act.Prevision_n3_total-project.Prevision_n3_total
                        r_act.Prevision_n3_devise=r_act.Prevision_n3_devise-project.Prevision_n3_devise
                        r_act.Prevision_n4_total=r_act.Prevision_n4_total-project.Prevision_n4_total
                        r_act.Prevision_n4_devise=r_act.Prevision_n4_devise-project.Prevision_n4_devise
                        r_act.save()

                        rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region,famille=project.Famille,activite=project.Perimetre.activite)
                        rog.CGI_total= rog.CGI_total- project.Cout_Globale_initial_total
                        rog.CGI_devise= rog.CGI_devise- project.Cout_Globale_initial_devise
                        rog.Previson_de_cloture_total= rog.Previson_de_cloture_total- project.Previson_de_cloture_total
                        rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise- project.Previson_de_cloture_devise
                        rog.Reste_a_realiser_total= rog.Reste_a_realiser_total- project.Reste_a_realiser_total
                        rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                        rog.Realisation_cum_total=rog.Realisation_cum_total-project.Realisation_cum_total
                        rog.Realisation_cum_devise=rog.Realisation_cum_devise- project.Realisation_cum_devise
                        rog.Realisation_S1_total=rog.Realisation_S1_total-project.Realisation_S1_total
                        rog.Realisation_S1_devise=rog.Realisation_S1_devise-project.Realisation_S1_devise
                        rog.Prevision_S2_total=rog.Prevision_S2_total-project.Prevision_S2_total
                        rog.Prevision_S2_devise=rog.Prevision_S2_devise-project.Prevision_S2_devise
                        rog.Prevision_n_total=rog.Prevision_n_total-project.Prevision_n_total
                        rog.Prevision_n_devise=rog.Prevision_n_devise-project.Prevision_n_devise
                        rog.Prevision_n1_total=rog.Prevision_n1_total-project.Prevision_n1_total
                        rog.Prevision_n1_devise=rog.Prevision_n1_devise-project.Prevision_n1_devise
                        rog.Prevision_n2_total=rog.Prevision_n2_total-project.Prevision_n2_total
                        rog.Prevision_n2_devise=rog.Prevision_n2_devise-project.Prevision_n2_devise
                        rog.Prevision_n3_total=rog.Prevision_n3_total-project.Prevision_n3_total
                        rog.Prevision_n3_devise=rog.Prevision_n3_devise-project.Prevision_n3_devise
                        rog.Prevision_n4_total=rog.Prevision_n4_total-project.Prevision_n4_total
                        rog.Prevision_n4_devise=rog.Prevision_n4_devise-project.Prevision_n4_devise
                        rog.save()
                  else:
            
                        #if str(project.champ.activite)=="Pétrole" or str(project.champ.activite)=="Gaz" :
                        r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=project.champ.activite)
                        r_act.CGI_total= r_act.CGI_total- project.Cout_Globale_initial_total
                        r_act.CGI_devise= r_act.CGI_devise- project.Cout_Globale_initial_devise
                        r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total- project.Previson_de_cloture_total
                        r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise- project.Previson_de_cloture_devise                       
                        r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total- project.Reste_a_realiser_total
                        r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise- project.Reste_a_realiser_devise                        
                        r_act.Realisation_cum_total=r_act.Realisation_cum_total-project.Realisation_cum_total
                        r_act.Realisation_cum_devise=r_act.Realisation_cum_devise- project.Realisation_cum_devise
                        r_act.Realisation_S1_total=r_act.Realisation_S1_total-project.Realisation_S1_total
                        r_act.Realisation_S1_devise=r_act.Realisation_S1_devise-project.Realisation_S1_devise
                        r_act.Prevision_S2_total=r_act.Prevision_S2_total-project.Prevision_S2_total
                        r_act.Prevision_S2_devise=r_act.Prevision_S2_devise-project.Prevision_S2_devise
                        r_act.Prevision_n_total=r_act.Prevision_n_total-project.Prevision_n_total
                        r_act.Prevision_n_devise=r_act.Prevision_n_devise-project.Prevision_n_devise
                        r_act.Prevision_n1_total=r_act.Prevision_n1_total-project.Prevision_n1_total
                        r_act.Prevision_n1_devise=r_act.Prevision_n1_devise-project.Prevision_n1_devise
                        r_act.Prevision_n2_total=r_act.Prevision_n2_total-project.Prevision_n2_total
                        r_act.Prevision_n2_devise=r_act.Prevision_n2_devise-project.Prevision_n2_devise
                        r_act.Prevision_n3_total=r_act.Prevision_n3_total-project.Prevision_n3_total
                        r_act.Prevision_n3_devise=r_act.Prevision_n3_devise-project.Prevision_n3_devise
                        r_act.Prevision_n4_total=r_act.Prevision_n4_total-project.Prevision_n4_total
                        r_act.Prevision_n4_devise=r_act.Prevision_n4_devise-project.Prevision_n4_devise
                        r_act.save()

                        rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region,famille=project.Famille,activite=project.champ.activite)
                        rog.CGI_total= rog.CGI_total- project.Cout_Globale_initial_total
                        rog.CGI_devise= rog.CGI_devise- project.Cout_Globale_initial_devise
                        rog.Previson_de_cloture_total= rog.Previson_de_cloture_total- project.Previson_de_cloture_total
                        rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise- project.Previson_de_cloture_devise
                        rog.Reste_a_realiser_total= rog.Reste_a_realiser_total- project.Reste_a_realiser_total
                        rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                        rog.Realisation_cum_total=rog.Realisation_cum_total-project.Realisation_cum_total
                        rog.Realisation_cum_devise=rog.Realisation_cum_devise- project.Realisation_cum_devise
                        rog.Realisation_S1_total=rog.Realisation_S1_total-project.Realisation_S1_total
                        rog.Realisation_S1_devise=rog.Realisation_S1_devise-project.Realisation_S1_devise
                        rog.Prevision_S2_total=rog.Prevision_S2_total-project.Prevision_S2_total
                        rog.Prevision_S2_devise=rog.Prevision_S2_devise-project.Prevision_S2_devise
                        rog.Prevision_n_total=rog.Prevision_n_total-project.Prevision_n_total
                        rog.Prevision_n_devise=rog.Prevision_n_devise-project.Prevision_n_devise
                        rog.Prevision_n1_total=rog.Prevision_n1_total-project.Prevision_n1_total
                        rog.Prevision_n1_devise=rog.Prevision_n1_devise-project.Prevision_n1_devise
                        rog.Prevision_n2_total=rog.Prevision_n2_total-project.Prevision_n2_total
                        rog.Prevision_n2_devise=rog.Prevision_n2_devise-project.Prevision_n2_devise
                        rog.Prevision_n3_total=rog.Prevision_n3_total-project.Prevision_n3_total
                        rog.Prevision_n3_devise=rog.Prevision_n3_devise-project.Prevision_n3_devise
                        rog.Prevision_n4_total=rog.Prevision_n4_total-project.Prevision_n4_total
                        rog.Prevision_n4_devise=rog.Prevision_n4_devise-project.Prevision_n4_devise
                        rog.save()
            
                              
                  
                  pev=Prévision_mensuelle.objects.filter(Project=project)#to delete also the previsions of the project
                  pev.delete()
                  project.delete()
                  messages.success(request,"le projet a été supprimé avec succès")     
                  return redirect('PMT')
            return render(request,'delete.html')

      
      else:       #to delete stimulations
            if request.method=="POST":
                  stimulation=Stimulation.objects.get(stimulation_id=pk)
                  stimulation.delete()
                  messages.success(request,"la stimulation a été supprimé avec succès")     
                  return redirect('PMT')
            return render(request,'delete.html')


#this delete functon is for update projets it deletes the project without deleting it previsions 
@login_required(login_url='login')
def delete_project_modif (request,pk):
      project=Project.objects.filter(id=pk)
      if project.exists():
            project=Project.objects.get(id=pk)
            if request.method=="POST":
                  
                  r_reg = Recap_region.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region)
                  r_reg.CGI_total= r_reg.CGI_total- project.Cout_Globale_initial_total
                  r_reg.CGI_devise= r_reg.CGI_devise- project.Cout_Globale_initial_devise
                  r_reg.Previson_de_cloture_total= r_reg.Previson_de_cloture_total- project.Previson_de_cloture_total
                  r_reg.Previson_de_cloture_devise= r_reg.Previson_de_cloture_devise- project.Previson_de_cloture_devise                 
                  r_reg.Reste_a_realiser_total= r_reg.Reste_a_realiser_total- project.Reste_a_realiser_total
                  r_reg.Reste_a_realiser_devise= r_reg.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                  r_reg.Realisation_cum_total=r_reg.Realisation_cum_total-project.Realisation_cum_total
                  r_reg.Realisation_cum_devise=r_reg.Realisation_cum_devise- project.Realisation_cum_devise
                  r_reg.Realisation_S1_total=r_reg.Realisation_S1_total-project.Realisation_S1_total
                  r_reg.Realisation_S1_devise=r_reg.Realisation_S1_devise-project.Realisation_S1_devise
                  r_reg.Prevision_S2_total=r_reg.Prevision_S2_total-project.Prevision_S2_total
                  r_reg.Prevision_S2_devise=r_reg.Prevision_S2_devise-project.Prevision_S2_devise
                  r_reg.Prevision_n_total=r_reg.Prevision_n_total-project.Prevision_n_total
                  r_reg.Prevision_n_devise=r_reg.Prevision_n_devise-project.Prevision_n_devise
                  r_reg.Prevision_n1_total=r_reg.Prevision_n1_total-project.Prevision_n1_total
                  r_reg.Prevision_n1_devise=r_reg.Prevision_n1_devise-project.Prevision_n1_devise
                  r_reg.Prevision_n2_total=r_reg.Prevision_n2_total-project.Prevision_n2_total
                  r_reg.Prevision_n2_devise=r_reg.Prevision_n2_devise-project.Prevision_n2_devise
                  r_reg.Prevision_n3_total=r_reg.Prevision_n3_total-project.Prevision_n3_total
                  r_reg.Prevision_n3_devise=r_reg.Prevision_n3_devise-project.Prevision_n3_devise
                  r_reg.Prevision_n4_total=r_reg.Prevision_n4_total-project.Prevision_n4_total
                  r_reg.Prevision_n4_devise=r_reg.Prevision_n4_devise-project.Prevision_n4_devise
                  r_reg.save()

                  r_fam = Recap_famille.objects.get(PMT=datetime.date.today().year+0,famille=project.Famille)
                  r_fam.CGI_total= r_fam.CGI_total- project.Cout_Globale_initial_total
                  r_fam.CGI_devise= r_fam.CGI_devise- project.Cout_Globale_initial_devise
                  r_fam.Previson_de_cloture_total= r_fam.Previson_de_cloture_total- project.Previson_de_cloture_total
                  r_fam.Previson_de_cloture_devise= r_fam.Previson_de_cloture_devise- project.Previson_de_cloture_devise        
                  r_fam.Reste_a_realiser_total= r_fam.Reste_a_realiser_total- project.Reste_a_realiser_total
                  r_fam.Reste_a_realiser_devise= r_fam.Reste_a_realiser_devise- project.Reste_a_realiser_devise             
                  r_fam.Realisation_cum_total=r_fam.Realisation_cum_total-project.Realisation_cum_total
                  r_fam.Realisation_cum_devise=r_fam.Realisation_cum_devise- project.Realisation_cum_devise
                  r_fam.Realisation_S1_total=r_fam.Realisation_S1_total-project.Realisation_S1_total
                  r_fam.Realisation_S1_devise=r_fam.Realisation_S1_devise-project.Realisation_S1_devise
                  r_fam.Prevision_S2_total=r_fam.Prevision_S2_total-project.Prevision_S2_total
                  r_fam.Prevision_S2_devise=r_fam.Prevision_S2_devise-project.Prevision_S2_devise
                  r_fam.Prevision_n_total=r_fam.Prevision_n_total-project.Prevision_n_total
                  r_fam.Prevision_n_devise=r_fam.Prevision_n_devise-project.Prevision_n_devise
                  r_fam.Prevision_n1_total=r_fam.Prevision_n1_total-project.Prevision_n1_total
                  r_fam.Prevision_n1_devise=r_fam.Prevision_n1_devise-project.Prevision_n1_devise
                  r_fam.Prevision_n2_total=r_fam.Prevision_n2_total-project.Prevision_n2_total
                  r_fam.Prevision_n2_devise=r_fam.Prevision_n2_devise-project.Prevision_n2_devise
                  r_fam.Prevision_n3_total=r_fam.Prevision_n3_total-project.Prevision_n3_total
                  r_fam.Prevision_n3_devise=r_fam.Prevision_n3_devise-project.Prevision_n3_devise
                  r_fam.Prevision_n4_total=r_fam.Prevision_n4_total-project.Prevision_n4_total
                  r_fam.Prevision_n4_devise=r_fam.Prevision_n4_devise-project.Prevision_n4_devise
                  r_fam.save()
                  if str(project.Perimetre.activite)=="Pétrole" or str(project.Perimetre.activite)=="Gaz":
                        r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=project.Perimetre.activite)
                        r_act.CGI_total= r_act.CGI_total- project.Cout_Globale_initial_total
                        r_act.CGI_devise= r_act.CGI_devise- project.Cout_Globale_initial_devise
                        r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total- project.Previson_de_cloture_total
                        r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise- project.Previson_de_cloture_devise                       
                        r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total- project.Reste_a_realiser_total
                        r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise- project.Reste_a_realiser_devise                        
                        r_act.Realisation_cum_total=r_act.Realisation_cum_total-project.Realisation_cum_total
                        r_act.Realisation_cum_devise=r_act.Realisation_cum_devise- project.Realisation_cum_devise
                        r_act.Realisation_S1_total=r_act.Realisation_S1_total-project.Realisation_S1_total
                        r_act.Realisation_S1_devise=r_act.Realisation_S1_devise-project.Realisation_S1_devise
                        r_act.Prevision_S2_total=r_act.Prevision_S2_total-project.Prevision_S2_total
                        r_act.Prevision_S2_devise=r_act.Prevision_S2_devise-project.Prevision_S2_devise
                        r_act.Prevision_n_total=r_act.Prevision_n_total-project.Prevision_n_total
                        r_act.Prevision_n_devise=r_act.Prevision_n_devise-project.Prevision_n_devise
                        r_act.Prevision_n1_total=r_act.Prevision_n1_total-project.Prevision_n1_total
                        r_act.Prevision_n1_devise=r_act.Prevision_n1_devise-project.Prevision_n1_devise
                        r_act.Prevision_n2_total=r_act.Prevision_n2_total-project.Prevision_n2_total
                        r_act.Prevision_n2_devise=r_act.Prevision_n2_devise-project.Prevision_n2_devise
                        r_act.Prevision_n3_total=r_act.Prevision_n3_total-project.Prevision_n3_total
                        r_act.Prevision_n3_devise=r_act.Prevision_n3_devise-project.Prevision_n3_devise
                        r_act.Prevision_n4_total=r_act.Prevision_n4_total-project.Prevision_n4_total
                        r_act.Prevision_n4_devise=r_act.Prevision_n4_devise-project.Prevision_n4_devise
                        r_act.save()

                        rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region,famille=project.Famille,activite=project.Perimetre.activite)
                        rog.CGI_total= rog.CGI_total- project.Cout_Globale_initial_total
                        rog.CGI_devise= rog.CGI_devise- project.Cout_Globale_initial_devise
                        rog.Previson_de_cloture_total= rog.Previson_de_cloture_total- project.Previson_de_cloture_total
                        rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise- project.Previson_de_cloture_devise
                        rog.Reste_a_realiser_total= rog.Reste_a_realiser_total- project.Reste_a_realiser_total
                        rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                        rog.Realisation_cum_total=rog.Realisation_cum_total-project.Realisation_cum_total
                        rog.Realisation_cum_devise=rog.Realisation_cum_devise- project.Realisation_cum_devise
                        rog.Realisation_S1_total=rog.Realisation_S1_total-project.Realisation_S1_total
                        rog.Realisation_S1_devise=rog.Realisation_S1_devise-project.Realisation_S1_devise
                        rog.Prevision_S2_total=rog.Prevision_S2_total-project.Prevision_S2_total
                        rog.Prevision_S2_devise=rog.Prevision_S2_devise-project.Prevision_S2_devise
                        rog.Prevision_n_total=rog.Prevision_n_total-project.Prevision_n_total
                        rog.Prevision_n_devise=rog.Prevision_n_devise-project.Prevision_n_devise
                        rog.Prevision_n1_total=rog.Prevision_n1_total-project.Prevision_n1_total
                        rog.Prevision_n1_devise=rog.Prevision_n1_devise-project.Prevision_n1_devise
                        rog.Prevision_n2_total=rog.Prevision_n2_total-project.Prevision_n2_total
                        rog.Prevision_n2_devise=rog.Prevision_n2_devise-project.Prevision_n2_devise
                        rog.Prevision_n3_total=rog.Prevision_n3_total-project.Prevision_n3_total
                        rog.Prevision_n3_devise=rog.Prevision_n3_devise-project.Prevision_n3_devise
                        rog.Prevision_n4_total=rog.Prevision_n4_total-project.Prevision_n4_total
                        rog.Prevision_n4_devise=rog.Prevision_n4_devise-project.Prevision_n4_devise
                        rog.save()
                  else:
            
                        #if str(project.champ.activite)=="Pétrole" or str(project.champ.activite)=="Gaz" :
                        r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=project.champ.activite)
                        r_act.CGI_total= r_act.CGI_total- project.Cout_Globale_initial_total
                        r_act.CGI_devise= r_act.CGI_devise- project.Cout_Globale_initial_devise
                        r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total- project.Previson_de_cloture_total
                        r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise- project.Previson_de_cloture_devise                       
                        r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total- project.Reste_a_realiser_total
                        r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise- project.Reste_a_realiser_devise                        
                        r_act.Realisation_cum_total=r_act.Realisation_cum_total-project.Realisation_cum_total
                        r_act.Realisation_cum_devise=r_act.Realisation_cum_devise- project.Realisation_cum_devise
                        r_act.Realisation_S1_total=r_act.Realisation_S1_total-project.Realisation_S1_total
                        r_act.Realisation_S1_devise=r_act.Realisation_S1_devise-project.Realisation_S1_devise
                        r_act.Prevision_S2_total=r_act.Prevision_S2_total-project.Prevision_S2_total
                        r_act.Prevision_S2_devise=r_act.Prevision_S2_devise-project.Prevision_S2_devise
                        r_act.Prevision_n_total=r_act.Prevision_n_total-project.Prevision_n_total
                        r_act.Prevision_n_devise=r_act.Prevision_n_devise-project.Prevision_n_devise
                        r_act.Prevision_n1_total=r_act.Prevision_n1_total-project.Prevision_n1_total
                        r_act.Prevision_n1_devise=r_act.Prevision_n1_devise-project.Prevision_n1_devise
                        r_act.Prevision_n2_total=r_act.Prevision_n2_total-project.Prevision_n2_total
                        r_act.Prevision_n2_devise=r_act.Prevision_n2_devise-project.Prevision_n2_devise
                        r_act.Prevision_n3_total=r_act.Prevision_n3_total-project.Prevision_n3_total
                        r_act.Prevision_n3_devise=r_act.Prevision_n3_devise-project.Prevision_n3_devise
                        r_act.Prevision_n4_total=r_act.Prevision_n4_total-project.Prevision_n4_total
                        r_act.Prevision_n4_devise=r_act.Prevision_n4_devise-project.Prevision_n4_devise
                        r_act.save()

                        rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region,famille=project.Famille,activite=project.champ.activite)
                        rog.CGI_total= rog.CGI_total- project.Cout_Globale_initial_total
                        rog.CGI_devise= rog.CGI_devise- project.Cout_Globale_initial_devise
                        rog.Previson_de_cloture_total= rog.Previson_de_cloture_total- project.Previson_de_cloture_total
                        rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise- project.Previson_de_cloture_devise
                        rog.Reste_a_realiser_total= rog.Reste_a_realiser_total- project.Reste_a_realiser_total
                        rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                        rog.Realisation_cum_total=rog.Realisation_cum_total-project.Realisation_cum_total
                        rog.Realisation_cum_devise=rog.Realisation_cum_devise- project.Realisation_cum_devise
                        rog.Realisation_S1_total=rog.Realisation_S1_total-project.Realisation_S1_total
                        rog.Realisation_S1_devise=rog.Realisation_S1_devise-project.Realisation_S1_devise
                        rog.Prevision_S2_total=rog.Prevision_S2_total-project.Prevision_S2_total
                        rog.Prevision_S2_devise=rog.Prevision_S2_devise-project.Prevision_S2_devise
                        rog.Prevision_n_total=rog.Prevision_n_total-project.Prevision_n_total
                        rog.Prevision_n_devise=rog.Prevision_n_devise-project.Prevision_n_devise
                        rog.Prevision_n1_total=rog.Prevision_n1_total-project.Prevision_n1_total
                        rog.Prevision_n1_devise=rog.Prevision_n1_devise-project.Prevision_n1_devise
                        rog.Prevision_n2_total=rog.Prevision_n2_total-project.Prevision_n2_total
                        rog.Prevision_n2_devise=rog.Prevision_n2_devise-project.Prevision_n2_devise
                        rog.Prevision_n3_total=rog.Prevision_n3_total-project.Prevision_n3_total
                        rog.Prevision_n3_devise=rog.Prevision_n3_devise-project.Prevision_n3_devise
                        rog.Prevision_n4_total=rog.Prevision_n4_total-project.Prevision_n4_total
                        rog.Prevision_n4_devise=rog.Prevision_n4_devise-project.Prevision_n4_devise
                        rog.save()
            
                              
                  
                  project.delete()
                  messages.success(request,"le projet a été modifié avec succès")     
                  return redirect('PMT')
            return render(request,'delete.html')

      
      else:       #to delete stimulations
            if request.method=="POST":
                  stimulation=Stimulation.objects.get(stimulation_id=pk)
                  stimulation.delete()
                  messages.success(request,"la stimulation a été supprimé avec succès")     
                  return redirect('PMT')
            return render(request,'delete.html')


#function to delete any project that do not have monthly prévisions
def delete_project_without_previsions(request):
      p=Project.objects.all()
      prev = Prévision_mensuelle.objects.all()
      for project in p:
            have_prevision=False
            for prevision in prev:
                  if project == prevision.Project:
                        have_prevision=True
            if have_prevision==False:
                  pk=str(project.id)
                  
                  project=Project.objects.filter(id=pk)
                  if project.exists():
                        project=Project.objects.get(id=pk)

                        r_reg = Recap_region.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region)
                        r_reg.CGI_total= r_reg.CGI_total- project.Cout_Globale_initial_total
                        r_reg.CGI_devise= r_reg.CGI_devise- project.Cout_Globale_initial_devise
                        r_reg.Previson_de_cloture_total= r_reg.Previson_de_cloture_total- project.Previson_de_cloture_total
                        r_reg.Previson_de_cloture_devise= r_reg.Previson_de_cloture_devise- project.Previson_de_cloture_devise                 
                        r_reg.Reste_a_realiser_total= r_reg.Reste_a_realiser_total- project.Reste_a_realiser_total
                        r_reg.Reste_a_realiser_devise= r_reg.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                        r_reg.Realisation_cum_total=r_reg.Realisation_cum_total-project.Realisation_cum_total
                        r_reg.Realisation_cum_devise=r_reg.Realisation_cum_devise- project.Realisation_cum_devise
                        r_reg.Realisation_S1_total=r_reg.Realisation_S1_total-project.Realisation_S1_total
                        r_reg.Realisation_S1_devise=r_reg.Realisation_S1_devise-project.Realisation_S1_devise
                        r_reg.Prevision_S2_total=r_reg.Prevision_S2_total-project.Prevision_S2_total
                        r_reg.Prevision_S2_devise=r_reg.Prevision_S2_devise-project.Prevision_S2_devise
                        r_reg.Prevision_n_total=r_reg.Prevision_n_total-project.Prevision_n_total
                        r_reg.Prevision_n_devise=r_reg.Prevision_n_devise-project.Prevision_n_devise
                        r_reg.Prevision_n1_total=r_reg.Prevision_n1_total-project.Prevision_n1_total
                        r_reg.Prevision_n1_devise=r_reg.Prevision_n1_devise-project.Prevision_n1_devise
                        r_reg.Prevision_n2_total=r_reg.Prevision_n2_total-project.Prevision_n2_total
                        r_reg.Prevision_n2_devise=r_reg.Prevision_n2_devise-project.Prevision_n2_devise
                        r_reg.Prevision_n3_total=r_reg.Prevision_n3_total-project.Prevision_n3_total
                        r_reg.Prevision_n3_devise=r_reg.Prevision_n3_devise-project.Prevision_n3_devise
                        r_reg.Prevision_n4_total=r_reg.Prevision_n4_total-project.Prevision_n4_total
                        r_reg.Prevision_n4_devise=r_reg.Prevision_n4_devise-project.Prevision_n4_devise
                        r_reg.save()

                        r_fam = Recap_famille.objects.get(PMT=datetime.date.today().year+0,famille=project.Famille)
                        r_fam.CGI_total= r_fam.CGI_total- project.Cout_Globale_initial_total
                        r_fam.CGI_devise= r_fam.CGI_devise- project.Cout_Globale_initial_devise
                        r_fam.Previson_de_cloture_total= r_fam.Previson_de_cloture_total- project.Previson_de_cloture_total
                        r_fam.Previson_de_cloture_devise= r_fam.Previson_de_cloture_devise- project.Previson_de_cloture_devise        
                        r_fam.Reste_a_realiser_total= r_fam.Reste_a_realiser_total- project.Reste_a_realiser_total
                        r_fam.Reste_a_realiser_devise= r_fam.Reste_a_realiser_devise- project.Reste_a_realiser_devise             
                        r_fam.Realisation_cum_total=r_fam.Realisation_cum_total-project.Realisation_cum_total
                        r_fam.Realisation_cum_devise=r_fam.Realisation_cum_devise- project.Realisation_cum_devise
                        r_fam.Realisation_S1_total=r_fam.Realisation_S1_total-project.Realisation_S1_total
                        r_fam.Realisation_S1_devise=r_fam.Realisation_S1_devise-project.Realisation_S1_devise
                        r_fam.Prevision_S2_total=r_fam.Prevision_S2_total-project.Prevision_S2_total
                        r_fam.Prevision_S2_devise=r_fam.Prevision_S2_devise-project.Prevision_S2_devise
                        r_fam.Prevision_n_total=r_fam.Prevision_n_total-project.Prevision_n_total
                        r_fam.Prevision_n_devise=r_fam.Prevision_n_devise-project.Prevision_n_devise
                        r_fam.Prevision_n1_total=r_fam.Prevision_n1_total-project.Prevision_n1_total
                        r_fam.Prevision_n1_devise=r_fam.Prevision_n1_devise-project.Prevision_n1_devise
                        r_fam.Prevision_n2_total=r_fam.Prevision_n2_total-project.Prevision_n2_total
                        r_fam.Prevision_n2_devise=r_fam.Prevision_n2_devise-project.Prevision_n2_devise
                        r_fam.Prevision_n3_total=r_fam.Prevision_n3_total-project.Prevision_n3_total
                        r_fam.Prevision_n3_devise=r_fam.Prevision_n3_devise-project.Prevision_n3_devise
                        r_fam.Prevision_n4_total=r_fam.Prevision_n4_total-project.Prevision_n4_total
                        r_fam.Prevision_n4_devise=r_fam.Prevision_n4_devise-project.Prevision_n4_devise
                        r_fam.save()
                        if str(project.Perimetre.activite)=="Pétrole" or str(project.Perimetre.activite)=="Gaz":
                              r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=project.Perimetre.activite)
                              r_act.CGI_total= r_act.CGI_total- project.Cout_Globale_initial_total
                              r_act.CGI_devise= r_act.CGI_devise- project.Cout_Globale_initial_devise
                              r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total- project.Previson_de_cloture_total
                              r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise- project.Previson_de_cloture_devise                       
                              r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total- project.Reste_a_realiser_total
                              r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise- project.Reste_a_realiser_devise                        
                              r_act.Realisation_cum_total=r_act.Realisation_cum_total-project.Realisation_cum_total
                              r_act.Realisation_cum_devise=r_act.Realisation_cum_devise- project.Realisation_cum_devise
                              r_act.Realisation_S1_total=r_act.Realisation_S1_total-project.Realisation_S1_total
                              r_act.Realisation_S1_devise=r_act.Realisation_S1_devise-project.Realisation_S1_devise
                              r_act.Prevision_S2_total=r_act.Prevision_S2_total-project.Prevision_S2_total
                              r_act.Prevision_S2_devise=r_act.Prevision_S2_devise-project.Prevision_S2_devise
                              r_act.Prevision_n_total=r_act.Prevision_n_total-project.Prevision_n_total
                              r_act.Prevision_n_devise=r_act.Prevision_n_devise-project.Prevision_n_devise
                              r_act.Prevision_n1_total=r_act.Prevision_n1_total-project.Prevision_n1_total
                              r_act.Prevision_n1_devise=r_act.Prevision_n1_devise-project.Prevision_n1_devise
                              r_act.Prevision_n2_total=r_act.Prevision_n2_total-project.Prevision_n2_total
                              r_act.Prevision_n2_devise=r_act.Prevision_n2_devise-project.Prevision_n2_devise
                              r_act.Prevision_n3_total=r_act.Prevision_n3_total-project.Prevision_n3_total
                              r_act.Prevision_n3_devise=r_act.Prevision_n3_devise-project.Prevision_n3_devise
                              r_act.Prevision_n4_total=r_act.Prevision_n4_total-project.Prevision_n4_total
                              r_act.Prevision_n4_devise=r_act.Prevision_n4_devise-project.Prevision_n4_devise
                              r_act.save()

                              rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region,famille=project.Famille,activite=project.Perimetre.activite)
                              rog.CGI_total= rog.CGI_total- project.Cout_Globale_initial_total
                              rog.CGI_devise= rog.CGI_devise- project.Cout_Globale_initial_devise
                              rog.Previson_de_cloture_total= rog.Previson_de_cloture_total- project.Previson_de_cloture_total
                              rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise- project.Previson_de_cloture_devise
                              rog.Reste_a_realiser_total= rog.Reste_a_realiser_total- project.Reste_a_realiser_total
                              rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                              rog.Realisation_cum_total=rog.Realisation_cum_total-project.Realisation_cum_total
                              rog.Realisation_cum_devise=rog.Realisation_cum_devise- project.Realisation_cum_devise
                              rog.Realisation_S1_total=rog.Realisation_S1_total-project.Realisation_S1_total
                              rog.Realisation_S1_devise=rog.Realisation_S1_devise-project.Realisation_S1_devise
                              rog.Prevision_S2_total=rog.Prevision_S2_total-project.Prevision_S2_total
                              rog.Prevision_S2_devise=rog.Prevision_S2_devise-project.Prevision_S2_devise
                              rog.Prevision_n_total=rog.Prevision_n_total-project.Prevision_n_total
                              rog.Prevision_n_devise=rog.Prevision_n_devise-project.Prevision_n_devise
                              rog.Prevision_n1_total=rog.Prevision_n1_total-project.Prevision_n1_total
                              rog.Prevision_n1_devise=rog.Prevision_n1_devise-project.Prevision_n1_devise
                              rog.Prevision_n2_total=rog.Prevision_n2_total-project.Prevision_n2_total
                              rog.Prevision_n2_devise=rog.Prevision_n2_devise-project.Prevision_n2_devise
                              rog.Prevision_n3_total=rog.Prevision_n3_total-project.Prevision_n3_total
                              rog.Prevision_n3_devise=rog.Prevision_n3_devise-project.Prevision_n3_devise
                              rog.Prevision_n4_total=rog.Prevision_n4_total-project.Prevision_n4_total
                              rog.Prevision_n4_devise=rog.Prevision_n4_devise-project.Prevision_n4_devise
                              rog.save()
                        else:
                  
                              #if str(project.champ.activite)=="Pétrole" or str(project.champ.activite)=="Gaz" :
                              r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=project.champ.activite)
                              r_act.CGI_total= r_act.CGI_total- project.Cout_Globale_initial_total
                              r_act.CGI_devise= r_act.CGI_devise- project.Cout_Globale_initial_devise
                              r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total- project.Previson_de_cloture_total
                              r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise- project.Previson_de_cloture_devise                       
                              r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total- project.Reste_a_realiser_total
                              r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise- project.Reste_a_realiser_devise                        
                              r_act.Realisation_cum_total=r_act.Realisation_cum_total-project.Realisation_cum_total
                              r_act.Realisation_cum_devise=r_act.Realisation_cum_devise- project.Realisation_cum_devise
                              r_act.Realisation_S1_total=r_act.Realisation_S1_total-project.Realisation_S1_total
                              r_act.Realisation_S1_devise=r_act.Realisation_S1_devise-project.Realisation_S1_devise
                              r_act.Prevision_S2_total=r_act.Prevision_S2_total-project.Prevision_S2_total
                              r_act.Prevision_S2_devise=r_act.Prevision_S2_devise-project.Prevision_S2_devise
                              r_act.Prevision_n_total=r_act.Prevision_n_total-project.Prevision_n_total
                              r_act.Prevision_n_devise=r_act.Prevision_n_devise-project.Prevision_n_devise
                              r_act.Prevision_n1_total=r_act.Prevision_n1_total-project.Prevision_n1_total
                              r_act.Prevision_n1_devise=r_act.Prevision_n1_devise-project.Prevision_n1_devise
                              r_act.Prevision_n2_total=r_act.Prevision_n2_total-project.Prevision_n2_total
                              r_act.Prevision_n2_devise=r_act.Prevision_n2_devise-project.Prevision_n2_devise
                              r_act.Prevision_n3_total=r_act.Prevision_n3_total-project.Prevision_n3_total
                              r_act.Prevision_n3_devise=r_act.Prevision_n3_devise-project.Prevision_n3_devise
                              r_act.Prevision_n4_total=r_act.Prevision_n4_total-project.Prevision_n4_total
                              r_act.Prevision_n4_devise=r_act.Prevision_n4_devise-project.Prevision_n4_devise
                              r_act.save()

                              rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=project.Perimetre.region,famille=project.Famille,activite=project.champ.activite)
                              rog.CGI_total= rog.CGI_total- project.Cout_Globale_initial_total
                              rog.CGI_devise= rog.CGI_devise- project.Cout_Globale_initial_devise
                              rog.Previson_de_cloture_total= rog.Previson_de_cloture_total- project.Previson_de_cloture_total
                              rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise- project.Previson_de_cloture_devise
                              rog.Reste_a_realiser_total= rog.Reste_a_realiser_total- project.Reste_a_realiser_total
                              rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise- project.Reste_a_realiser_devise
                              rog.Realisation_cum_total=rog.Realisation_cum_total-project.Realisation_cum_total
                              rog.Realisation_cum_devise=rog.Realisation_cum_devise- project.Realisation_cum_devise
                              rog.Realisation_S1_total=rog.Realisation_S1_total-project.Realisation_S1_total
                              rog.Realisation_S1_devise=rog.Realisation_S1_devise-project.Realisation_S1_devise
                              rog.Prevision_S2_total=rog.Prevision_S2_total-project.Prevision_S2_total
                              rog.Prevision_S2_devise=rog.Prevision_S2_devise-project.Prevision_S2_devise
                              rog.Prevision_n_total=rog.Prevision_n_total-project.Prevision_n_total
                              rog.Prevision_n_devise=rog.Prevision_n_devise-project.Prevision_n_devise
                              rog.Prevision_n1_total=rog.Prevision_n1_total-project.Prevision_n1_total
                              rog.Prevision_n1_devise=rog.Prevision_n1_devise-project.Prevision_n1_devise
                              rog.Prevision_n2_total=rog.Prevision_n2_total-project.Prevision_n2_total
                              rog.Prevision_n2_devise=rog.Prevision_n2_devise-project.Prevision_n2_devise
                              rog.Prevision_n3_total=rog.Prevision_n3_total-project.Prevision_n3_total
                              rog.Prevision_n3_devise=rog.Prevision_n3_devise-project.Prevision_n3_devise
                              rog.Prevision_n4_total=rog.Prevision_n4_total-project.Prevision_n4_total
                              rog.Prevision_n4_devise=rog.Prevision_n4_devise-project.Prevision_n4_devise
                              rog.save()
                  
                                    
                        
                        pev=Prévision_mensuelle.objects.filter(Project=project)#to delete also the previsions of the project
                        pev.delete()
                        project.delete()
                        messages.error(request,"vous ne pouvez pas ajouter de projets sans y ajouter des preévisions mensuelles")  
                        return redirect('PMT')

            
                  else:       #to delete stimulations
                        stimulation=Stimulation.objects.get(stimulation_id=pk)
                        stimulation.delete()
                        messages.error(request,"vous ne pouvez pas ajouter de projets sans y ajouter des preévisions mensuelles")  
                        return redirect('PMT')


      
####################################### functions Caluclations #######################################

def Taux_real(p,r):
      if p==0: #to prevent the zero division error
           return 0
      else: 
            return (r*100)/p



      
def CGI(Realisation_cum,Realisation_S1,Prevision_S2,Prevision_n,Prevision_n1,Prevision_n2,Prevision_n3,Prevision_n4):
      return Realisation_cum+Realisation_S1+Prevision_S2+Prevision_n+Prevision_n1+Prevision_n2+Prevision_n3+Prevision_n4



def Cloture(Realisation_S1,Prevision_S2):
      return Realisation_S1+Prevision_S2

def Reste_a_realiser (Prevision_n1,Prevision_n2,Prevision_n3,Prevision_n4):
      return Prevision_n1+Prevision_n2+Prevision_n3+Prevision_n4



# Create your views here.
########################################## Models views ##############################################
@login_required(login_url='login')
def export_recap(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap.objects.filter(PMT=year)
            return render(request,'export_recap.html',{'recaps':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})

      i = Acces.objects.get(user=request.user) 
      p = Perimetre.objects.filter(region=i.region)
      year=datetime.date.today().year+0
      obj=Recap.objects.filter(Perimetre=p[0],PMT=year)
      return render(request,'export_recap.html',{'recaps':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})

@login_required(login_url='login')
def recap(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap.objects.filter(PMT=year)
            return render(request,'recap.html',{'recaps':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})

      i = Acces.objects.filter(user=request.user)
      if i.exists():
            i = Acces.objects.get(user=request.user)
            p = Perimetre.objects.filter(region=i.region)
            year=datetime.date.today().year+0
            obj=Recap.objects.filter(Perimetre=p[0],PMT=year)
            return render(request,'PMT.html',{'recaps':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})
      else:
            return render(request,'404.html')

@login_required(login_url='login')
def export_region(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap_region.objects.filter(PMT=year)
            return render(request,'export_region.html',{'Recap_regs':obj,'form1':search_form,'my_year':my_year})

      i = Acces.objects.get(user=request.user) 
      p = Perimetre.objects.filter(region=i.region)
      year=datetime.date.today().year+0
      obj=Recap_region.objects.filter(Perimetre=p[0],PMT=year)
      return render(request,'export_region.html',{'Recap_regs':obj,'form1':search_form,'my_year':my_year})

@login_required(login_url='login')
def recap_reg(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap_region.objects.filter(PMT=year)
            return render(request,'Recap_reg.html',{'Recap_regs':obj,'form1':search_form,'my_year':my_year})

      i = Acces.objects.filter(user=request.user)
      if i.exists():
            i = Acces.objects.get(user=request.user) 
            p = Perimetre.objects.filter(region=i.region)
            year=datetime.date.today().year+0
            obj=Recap_region.objects.filter(Perimetre=p[0],PMT=year)
            return render(request,'Recap_reg.html',{'Recap_regs':obj,'form1':search_form,'my_year':my_year})
      else:
            return render(request,'404.html')

@login_required(login_url='login')
def export_famille(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap_famille.objects.filter(PMT=year)
            return render(request,'export_famille.html',{'recap_fams':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})

      i = Acces.objects.get(user=request.user) 
      p = Perimetre.objects.filter(region=i.region)
      year=datetime.date.today().year+0
      obj=Recap_famille.objects.filter(Perimetre=p[0],PMT=year)
      return render(request,'export_famille.html',{'recap_fams':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})

@login_required(login_url='login')
def recap_fam(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap_famille.objects.filter(PMT=year)
            return render(request,'recap_fam.html',{'recap_fams':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})

      i = Acces.objects.filter(user=request.user)
      if i.exists():
            i = Acces.objects.get(user=request.user) 
            p = Perimetre.objects.filter(region=i.region)
            year=datetime.date.today().year+0
            obj=Recap_famille.objects.filter(Perimetre=p[0],PMT=year)
            return render(request,'recap_fam.html',{'recap_fams':obj,'form1':search_form,'form2':search_form_region,'my_year':my_year})
      else:
            return render(request,'404.html')
def export_activite(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap_activite.objects.filter(PMT=year)
            return render(request,'export_activite.html',{'recap_acts':obj,'form1':search_form,'my_year':my_year})

      i = Acces.objects.get(user=request.user) 
      p = Perimetre.objects.filter(region=i.region)
      year=datetime.date.today().year+0
      obj=Recap_activite.objects.filter(Perimetre=p[0],PMT=year)
      return render(request,'export_activite.html',{'recap_acts':obj,'form1':search_form,'my_year':my_year})

@login_required(login_url='login')
def recap_act(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Recap_activite.objects.filter(PMT=year)
            return render(request,'recap_act.html',{'recap_acts':obj,'form1':search_form,'my_year':my_year})

      i = Acces.objects.filter(user=request.user)
      if i.exists():
            i = Acces.objects.get(user=request.user)
            p = Perimetre.objects.filter(region=i.region)
            year=datetime.date.today().year+0
            obj=Recap_activite.objects.filter(Perimetre=p[0],PMT=year)
            return render(request,'PMT.html',{'recap_acts':obj,'form1':search_form,'my_year':my_year})
      else:
            return render(request,'404.html')
      
def search_project(request): #search projects by year for PMT
      form = search_form(request.POST)
      if form.is_valid():
            user=request.user
            if user.is_staff:
                  obj=Project.objects.filter(PMT=form.cleaned_data["annee"])
                  return render(request,'PMT.html',{'projects':obj,'form1':search_form})
            i = Acces.objects.get(user=request.user) 
            p = Perimetre.objects.filter(region=i.region)
            obj=Project.objects.filter(Perimetre=p[0],PMT=form.cleaned_data["annee"])
            return render(request,'PMT.html',{'projects':obj,'form1':search_form})


def search_month(request): #search monthly reports by month
      form = search_month_form(request.POST)
      if form.is_valid():
            user=request.user
            if user.is_staff:
                  obj=Realisation_mensuelle.objects.filter(Mois_real=form.cleaned_data["Month"])
                  return render(request,'Mensuel.html',{'Mensuel':obj,'form3':search_month_form})   
            i = Acces.objects.get(user=request.user) 
            p = Perimetre.objects.filter(region=i.region)
            obj=Realisation_mensuelle.objects.filter(Perimetre=p[0],Mois_real=form.cleaned_data["Month"])
            return render(request,'Mensuel.html',{'Mensuel':obj,'form3':search_month_form}) 
      
      return render(request,'Mensuel.html')    

@login_required(login_url='login')          
def search_project_region(request): #search project by region for recap
      form = search_form_region(request.POST)
      if form.is_valid():
            user=request.user
            if user.is_staff:
                  obj=Recap.objects.filter(region=form.cleaned_data["region"])
                  return render(request,'recap.html',{'recaps':obj,'form2':search_form_region})   
            i = Acces.objects.get(user=request.user) 
            p = Perimetre.objects.filter(region=i.region)
            obj=Recap.objects.filter(Perimetre=p[0],PMT=form.cleaned_data["annee"],region=form.cleaned_data["region"])
            return render(request,'recap.html',{'recaps':obj,'form2':search_form_region})




                             
@login_required(login_url='login')
def project_form(request):
      my_year=int(datetime.date.today().year)
      context= {
            "form":add_project_Form,
            "my_year":my_year
      }
      return render(request,'project_form.html',context)

@login_required(login_url='login')
def export_pmt(request):
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Project.objects.filter(PMT=year).order_by()
            stm=Stimulation.objects.filter(PMT=year).order_by()
            return render(request,'export_pmt.html',{'projects':obj,'stimulations':stm,'form1':search_form,'my_year':my_year})
      i = Acces.objects.get(user=request.user) 
      p = Perimetre.objects.filter(region=i.region)
      year=datetime.date.today().year+0
      obj=Project.objects.filter(Perimetre=p[0],PMT=year)
      stm=Stimulation.objects.filter(Perimetre=p[0],PMT=year).order_by()
      return render(request,'export_pmt.html',{'projects':obj,'stimulations':stm,'form1':search_form,'my_year':my_year})

@login_required(login_url='login')
def PMT(request):
      delete_project_without_previsions(request)
      my_year=int(datetime.date.today().year)
      user=request.user
      if user.is_staff:
            year=datetime.date.today().year+0
            obj=Project.objects.filter(PMT=year).order_by()
            stm=Stimulation.objects.filter(PMT=year).order_by()            
            return render(request,'PMT.html',{'projects':obj,'stimulations':stm,'form1':search_form,'my_year':my_year})
      i = Acces.objects.filter(user=request.user)
      if i.exists(): # to check if the user have access to anything
            i = Acces.objects.get(user=request.user) 
            p = Perimetre.objects.filter(region=i.region)
            year=datetime.date.today().year+0
            if not p:
                  messages.info(request,"La région auquel vous avez accès n'a pas encore de périmètre")
                  return redirect('/')  
            else:      
                  obj=Project.objects.filter(Perimetre=p[0],PMT=year)
                  stm=Stimulation.objects.filter(Perimetre=p[0],PMT=year).order_by()
                  return render(request,'PMT.html',{'projects':obj,'stimulations':stm,'form1':search_form,'my_year':my_year})
      else:
            return render(request,'404.html')
 
@login_required(login_url='login')
def add_project(request):
      submitted=False
      if request.method=="POST":
            form=add_project_Form(request.POST)
            if form.is_valid():
                  p = Project(PMT=datetime.date.today().year+0,
                              Compte_Analytique=form.cleaned_data["Compte_Analytique"],
                              Libelles=form.cleaned_data["Libelles"],
                              Structure_gerante=form.cleaned_data["Structure_gerante"],
                              Perimetre=form.cleaned_data["Perimetre"],
                              champ=form.cleaned_data["Champ"],
                              Famille=form.cleaned_data["Famille"],
                              Type=form.cleaned_data["Type"],
                              Fiscalite=form.cleaned_data["Fiscalite"],
                              Realisation_cum_total=form.cleaned_data["Realisation_cum_total"],
                              Realisation_cum_devise=form.cleaned_data["Realisation_cum_devise"],                          
                              Realisation_S1_total=form.cleaned_data["Realisation_S1_total"],
                              Realisation_S1_devise=form.cleaned_data["Realisation_S1_devise"],
                              Prevision_S2_total=form.cleaned_data["Prevision_S2_total"],
                              Prevision_S2_devise=form.cleaned_data["Prevision_S2_devise"],
                              Prevision_n_total=form.cleaned_data["Prevision_n_total"],#2020
                              Prevision_n_devise=form.cleaned_data["Prevision_n_devise"],
                              Prevision_n1_total=form.cleaned_data["Prevision_n1_total"],
                              Prevision_n1_devise=form.cleaned_data["Prevision_n1_devise"],
                              Prevision_n2_total=form.cleaned_data["Prevision_n2_total"],
                              Prevision_n2_devise=form.cleaned_data["Prevision_n2_devise"],
                              Prevision_n3_total=form.cleaned_data["Prevision_n3_total"],
                              Prevision_n3_devise=form.cleaned_data["Prevision_n3_devise"],
                              Prevision_n4_total=form.cleaned_data["Prevision_n4_total"],
                              Prevision_n4_devise=form.cleaned_data["Prevision_n4_devise"],
                              Point_situation=form.cleaned_data["Point_situation"],
                              Project_puit=form.cleaned_data['Project_puit'],
                              #Is_stimulation=form.data.get("Is_stimulation") == "on",#assgin true if the checkbox is on
                              #Is_acidification=form.data.get("Is_acidification") == "on",
                              #Is_fracturation=form.data.get("Is_fracturation") == "on",
                              Previson_de_cloture_total=Cloture(form.cleaned_data["Realisation_S1_total"],form.cleaned_data["Prevision_S2_total"]),
                              Previson_de_cloture_devise=Cloture(form.cleaned_data["Realisation_S1_devise"],form.cleaned_data["Prevision_S2_devise"]),
                             
                              Reste_a_realiser_total=Reste_a_realiser(form.cleaned_data["Prevision_n1_total"],form.cleaned_data["Prevision_n2_total"], 
                                                                    form.cleaned_data["Prevision_n3_total"],form.cleaned_data["Prevision_n4_total"]),
                                                        
                              Reste_a_realiser_devise=Reste_a_realiser(form.cleaned_data["Prevision_n1_devise"],form.cleaned_data["Prevision_n2_devise"],
                                                                     form.cleaned_data["Prevision_n3_devise"],form.cleaned_data["Prevision_n4_devise"]),
                                                        
                              Cout_Globale_initial_total=CGI(form.cleaned_data["Realisation_cum_total"],form.cleaned_data["Realisation_S1_total"],
                                                            form.cleaned_data["Prevision_S2_total"],form.cleaned_data["Prevision_n_total"],
                                                            form.cleaned_data["Prevision_n1_total"],form.cleaned_data["Prevision_n2_total"], 
                                                            form.cleaned_data["Prevision_n3_total"],form.cleaned_data["Prevision_n4_total"]),

                              Cout_Globale_initial_devise=CGI(form.cleaned_data["Realisation_cum_devise"],form.cleaned_data["Realisation_S1_devise"],
                                                          form.cleaned_data["Prevision_S2_devise"],form.cleaned_data["Prevision_n_devise"],
                                                          form.cleaned_data["Prevision_n1_devise"],form.cleaned_data["Prevision_n2_devise"], 
                                                          form.cleaned_data["Prevision_n3_devise"],form.cleaned_data["Prevision_n4_devise"]))
                                                          
                        #region recap
                  if p.Project_puit==True : #it's a stimulation
                        s=Stimulation(PMT=p.PMT,
                                          Compte_Analytique = p.Compte_Analytique,
                                          Structure_gerante=p.Structure_gerante,
                                          Perimetre=p.Perimetre,
                                          champ=p.champ,
                                          Famille=p.Famille,
                                          Type=p.Type,
                                          Fiscalite=p.Fiscalite,
                                          stimulation=p.Libelles,
                                          Cout_Globale_initial_total=p.Cout_Globale_initial_total,
                                          Cout_Globale_initial_devise=p.Cout_Globale_initial_devise,
                                          Realisation_cum_total =p.Realisation_cum_total,
                                          Realisation_cum_devise =p.Realisation_cum_devise,
                                          Realisation_S1_devise = p.Realisation_S1_devise,
                                          Realisation_S1_total = p.Realisation_S1_total,
                                          Prevision_S2_total =p.Prevision_S2_total,
                                          Previson_de_cloture_total=p.Previson_de_cloture_total,
                                          Prevision_S2_devise= p.Prevision_S2_devise,
                                          Previson_de_cloture_devise=p.Previson_de_cloture_devise,
                                          Reste_a_realiser_total=p.Reste_a_realiser_total,
                                          Reste_a_realiser_devise=p.Reste_a_realiser_devise,
                                          Prevision_n_total = p.Prevision_n_total,
                                          Prevision_n_devise = p.Prevision_n_devise,
                                          Prevision_n1_total = p.Prevision_n1_total,
                                          Prevision_n1_devise = p.Prevision_n1_devise,
                                          Prevision_n2_total = p.Prevision_n2_total,
                                          Prevision_n2_devise = p.Prevision_n2_devise,
                                          Prevision_n3_total = p.Prevision_n3_total,
                                          Prevision_n3_devise = p.Prevision_n3_devise,
                                          Prevision_n4_total = p.Prevision_n4_total,
                                          Prevision_n4_devise = p.Prevision_n4_devise,
                                          Point_situation = p.Point_situation,
                                          Project_puit=p.Project_puit
                                          )
                        s.save()
                        print(s.Project_puit)
                        request.session["id"]=s.stimulation_id
                        return redirect('/prevision_form')  

                  else: 

                        prj=Project.objects.filter(PMT=datetime.date.today().year+0,Compte_Analytique=p.Compte_Analytique)
                        if prj.exists():
                              messages.error(request,"Le compte analytique est déjà utilisé par un autre projet")
                              return redirect('project_form')
                        else:
                              p.save()   
                              r_reg = Recap_region.objects.filter(PMT=datetime.date.today().year+0,region=p.Perimetre.region)
                              if r_reg.exists():
                                    r_reg = Recap_region.objects.get(PMT=datetime.date.today().year+0,region=p.Perimetre.region)
                                    r_reg.CGI_total= r_reg.CGI_total+ p.Cout_Globale_initial_total
                                    r_reg.CGI_devise= r_reg.CGI_devise+ p.Cout_Globale_initial_devise
                                    r_reg.Previson_de_cloture_total= r_reg.Previson_de_cloture_total+ p.Previson_de_cloture_total
                                    r_reg.Previson_de_cloture_devise= r_reg.Previson_de_cloture_devise+ p.Previson_de_cloture_devise                 
                                    r_reg.Reste_a_realiser_total= r_reg.Reste_a_realiser_total+ p.Reste_a_realiser_total
                                    r_reg.Reste_a_realiser_devise= r_reg.Reste_a_realiser_devise+ p.Reste_a_realiser_devise
                                    r_reg.Realisation_cum_total=r_reg.Realisation_cum_total+p.Realisation_cum_total
                                    r_reg.Realisation_cum_devise=r_reg.Realisation_cum_devise+ p.Realisation_cum_devise
                                    r_reg.Realisation_S1_total=r_reg.Realisation_S1_total+p.Realisation_S1_total
                                    r_reg.Realisation_S1_devise=r_reg.Realisation_S1_devise+p.Realisation_S1_devise
                                    r_reg.Prevision_S2_total=r_reg.Prevision_S2_total+p.Prevision_S2_total
                                    r_reg.Prevision_S2_devise=r_reg.Prevision_S2_devise+p.Prevision_S2_devise
                                    r_reg.Prevision_n_total=r_reg.Prevision_n_total+p.Prevision_n_total
                                    r_reg.Prevision_n_devise=r_reg.Prevision_n_devise+p.Prevision_n_devise
                                    r_reg.Prevision_n1_total=r_reg.Prevision_n1_total+p.Prevision_n1_total
                                    r_reg.Prevision_n1_devise=r_reg.Prevision_n1_devise+p.Prevision_n1_devise
                                    r_reg.Prevision_n2_total=r_reg.Prevision_n2_total+p.Prevision_n2_total
                                    r_reg.Prevision_n2_devise=r_reg.Prevision_n2_devise+p.Prevision_n2_devise
                                    r_reg.Prevision_n3_total=r_reg.Prevision_n3_total+p.Prevision_n3_total
                                    r_reg.Prevision_n3_devise=r_reg.Prevision_n3_devise+p.Prevision_n3_devise
                                    r_reg.Prevision_n4_total=r_reg.Prevision_n4_total+p.Prevision_n4_total
                                    r_reg.Prevision_n4_devise=r_reg.Prevision_n4_devise+p.Prevision_n4_devise
                                    r_reg.save()
                              else:
                                    r_reg= Recap_region(PMT=datetime.date.today().year+0,region=p.Perimetre.region,CGI_total=p.Cout_Globale_initial_total,
                                                                                                                  CGI_devise=p.Cout_Globale_initial_devise,
                                                                                                                  Previson_de_cloture_total= p.Previson_de_cloture_total,
                                                                                                                  Previson_de_cloture_devise= p.Previson_de_cloture_devise,                 
                                                                                                                  Reste_a_realiser_total= p.Reste_a_realiser_total,
                                                                                                                  Reste_a_realiser_devise= p.Reste_a_realiser_devise,
                                                                                                                  Realisation_cum_total=p.Realisation_cum_total,
                                                                                                                  Realisation_cum_devise=p.Realisation_cum_devise,
                                                                                                                  Realisation_S1_total=p.Realisation_S1_total,
                                                                                                                  Realisation_S1_devise=p.Realisation_S1_devise,
                                                                                                                  Prevision_S2_total=p.Prevision_S2_total,
                                                                                                                  Prevision_S2_devise=p.Prevision_S2_devise,
                                                                                                                  Prevision_n_total=p.Prevision_n_total,
                                                                                                                  Prevision_n_devise=p.Prevision_n_devise,
                                                                                                                  Prevision_n1_total=p.Prevision_n1_total,
                                                                                                                  Prevision_n1_devise=p.Prevision_n1_devise,
                                                                                                                  Prevision_n2_total=p.Prevision_n2_total,
                                                                                                                  Prevision_n2_devise=p.Prevision_n2_devise,
                                                                                                                  Prevision_n3_total=p.Prevision_n3_total,
                                                                                                                  Prevision_n3_devise=p.Prevision_n3_devise,
                                                                                                                  Prevision_n4_total=p.Prevision_n4_total,
                                                                                                                  Prevision_n4_devise=p.Prevision_n4_devise,
                                                                                                                  )
                                    r_reg.save() 


                              #famille recap
                              r_fam = Recap_famille.objects.filter(PMT=datetime.date.today().year+0,famille=p.Famille)
                              if r_fam.exists():
                                    r_fam = Recap_famille.objects.get(PMT=datetime.date.today().year+0,famille=p.Famille)
                                    r_fam.CGI_total= r_fam.CGI_total+ p.Cout_Globale_initial_total
                                    r_fam.CGI_devise= r_fam.CGI_devise+ p.Cout_Globale_initial_devise
                                    r_fam.Previson_de_cloture_total= r_fam.Previson_de_cloture_total+ p.Previson_de_cloture_total
                                    r_fam.Previson_de_cloture_devise= r_fam.Previson_de_cloture_devise+ p.Previson_de_cloture_devise        
                                    r_fam.Reste_a_realiser_total= r_fam.Reste_a_realiser_total+ p.Reste_a_realiser_total
                                    r_fam.Reste_a_realiser_devise= r_fam.Reste_a_realiser_devise+ p.Reste_a_realiser_devise             
                                    r_fam.Realisation_cum_total=r_fam.Realisation_cum_total+p.Realisation_cum_total
                                    r_fam.Realisation_cum_devise=r_fam.Realisation_cum_devise+ p.Realisation_cum_devise
                                    r_fam.Realisation_S1_total=r_fam.Realisation_S1_total+p.Realisation_S1_total
                                    r_fam.Realisation_S1_devise=r_fam.Realisation_S1_devise+p.Realisation_S1_devise
                                    r_fam.Prevision_S2_total=r_fam.Prevision_S2_total+p.Prevision_S2_total
                                    r_fam.Prevision_S2_devise=r_fam.Prevision_S2_devise+p.Prevision_S2_devise
                                    r_fam.Prevision_n_total=r_fam.Prevision_n_total+p.Prevision_n_total
                                    r_fam.Prevision_n_devise=r_fam.Prevision_n_devise+p.Prevision_n_devise
                                    r_fam.Prevision_n1_total=r_fam.Prevision_n1_total+p.Prevision_n1_total
                                    r_fam.Prevision_n1_devise=r_fam.Prevision_n1_devise+p.Prevision_n1_devise
                                    r_fam.Prevision_n2_total=r_fam.Prevision_n2_total+p.Prevision_n2_total
                                    r_fam.Prevision_n2_devise=r_fam.Prevision_n2_devise+p.Prevision_n2_devise
                                    r_fam.Prevision_n3_total=r_fam.Prevision_n3_total+p.Prevision_n3_total
                                    r_fam.Prevision_n3_devise=r_fam.Prevision_n3_devise+p.Prevision_n3_devise
                                    r_fam.Prevision_n4_total=r_fam.Prevision_n4_total+p.Prevision_n4_total
                                    r_fam.Prevision_n4_devise=r_fam.Prevision_n4_devise+p.Prevision_n4_devise
                                    r_fam.save()
                              else:
                                    r_fam= Recap_famille(PMT=datetime.date.today().year+0,famille=p.Famille,CGI_total=p.Cout_Globale_initial_total,
                                                                                                            CGI_devise=p.Cout_Globale_initial_devise,
                                                                                                            
                                                                                                            Previson_de_cloture_total= p.Previson_de_cloture_total,
                                                                                                            Previson_de_cloture_devise= p.Previson_de_cloture_devise,
                                                                                                            
                                                                                                            Reste_a_realiser_total= p.Reste_a_realiser_total,
                                                                                                            Reste_a_realiser_devise= p.Reste_a_realiser_devise,
                                                                                                                                                                                                                        Realisation_cum_total=p.Realisation_cum_total,
                                                                                                            Realisation_cum_devise=p.Realisation_cum_devise,
                                                                                                            Realisation_S1_total=p.Realisation_S1_total,
                                                                                                            Realisation_S1_devise=p.Realisation_S1_devise,
                                                                                                            Prevision_S2_total=p.Prevision_S2_total,
                                                                                                            Prevision_S2_devise=p.Prevision_S2_devise,
                                                                                                            Prevision_n_total=p.Prevision_n_total,
                                                                                                            Prevision_n_devise=p.Prevision_n_devise,
                                                                                                            Prevision_n1_total=p.Prevision_n1_total,
                                                                                                            Prevision_n1_devise=p.Prevision_n1_devise,
                                                                                                            Prevision_n2_total=p.Prevision_n2_total,
                                                                                                            Prevision_n2_devise=p.Prevision_n2_devise,
                                                                                                            Prevision_n3_total=p.Prevision_n3_total,
                                                                                                            Prevision_n3_devise=p.Prevision_n3_devise,
                                                                                                            Prevision_n4_total=p.Prevision_n4_total,
                                                                                                            Prevision_n4_devise=p.Prevision_n4_devise)
                                    r_fam.save()
                              #activite recap
                              if str(p.Perimetre.activite)=="Pétrole" or str(p.Perimetre.activite)=="Gaz":
                                    r_act = Recap_activite.objects.filter(PMT=datetime.date.today().year+0,activite=p.Perimetre.activite)
                                    if r_act.exists():
                                          r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=p.Perimetre.activite)
                                          r_act.CGI_total= r_act.CGI_total+ p.Cout_Globale_initial_total
                                          r_act.CGI_devise= r_act.CGI_devise+ p.Cout_Globale_initial_devise
                                          r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total+ p.Previson_de_cloture_total
                                          r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise+ p.Previson_de_cloture_devise                       
                                          r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total+ p.Reste_a_realiser_total
                                          r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise+ p.Reste_a_realiser_devise                        
                                          r_act.Realisation_cum_total=r_act.Realisation_cum_total+p.Realisation_cum_total
                                          r_act.Realisation_cum_devise=r_act.Realisation_cum_devise+ p.Realisation_cum_devise
                                          r_act.Realisation_S1_total=r_act.Realisation_S1_total+p.Realisation_S1_total
                                          r_act.Realisation_S1_devise=r_act.Realisation_S1_devise+p.Realisation_S1_devise
                                          r_act.Prevision_S2_total=r_act.Prevision_S2_total+p.Prevision_S2_total
                                          r_act.Prevision_S2_devise=r_act.Prevision_S2_devise+p.Prevision_S2_devise
                                          r_act.Prevision_n_total=r_act.Prevision_n_total+p.Prevision_n_total
                                          r_act.Prevision_n_devise=r_act.Prevision_n_devise+p.Prevision_n_devise
                                          r_act.Prevision_n1_total=r_act.Prevision_n1_total+p.Prevision_n1_total
                                          r_act.Prevision_n1_devise=r_act.Prevision_n1_devise+p.Prevision_n1_devise
                                          r_act.Prevision_n2_total=r_act.Prevision_n2_total+p.Prevision_n2_total
                                          r_act.Prevision_n2_devise=r_act.Prevision_n2_devise+p.Prevision_n2_devise
                                          r_act.Prevision_n3_total=r_act.Prevision_n3_total+p.Prevision_n3_total
                                          r_act.Prevision_n3_devise=r_act.Prevision_n3_devise+p.Prevision_n3_devise
                                          r_act.Prevision_n4_total=r_act.Prevision_n4_total+p.Prevision_n4_total
                                          r_act.Prevision_n4_devise=r_act.Prevision_n4_devise+p.Prevision_n4_devise
                                          r_act.save()
                                    else:
                                          r_act= Recap_activite(PMT=datetime.date.today().year+0,activite=p.Perimetre.activite,CGI_total=p.Cout_Globale_initial_total,
                                                                                                                  CGI_devise=p.Cout_Globale_initial_devise,
                                                                                                                  
                                                                                                                  Previson_de_cloture_total= p.Previson_de_cloture_total,
                                                                                                                  Previson_de_cloture_devise= p.Previson_de_cloture_devise,
                                                                                                                  
                                                                                                                  Reste_a_realiser_total= p.Reste_a_realiser_total,
                                                                                                                  Reste_a_realiser_devise= p.Reste_a_realiser_devise,
                                                                                                                  Realisation_cum_total=p.Realisation_cum_total,
                                                                                                                  Realisation_cum_devise=p.Realisation_cum_devise,
                                                                                                                  Realisation_S1_total=p.Realisation_S1_total,
                                                                                                                  Realisation_S1_devise=p.Realisation_S1_devise,
                                                                                                                  Prevision_S2_total=p.Prevision_S2_total,
                                                                                                                  Prevision_S2_devise=p.Prevision_S2_devise,
                                                                                                                  Prevision_n_total=p.Prevision_n_total,
                                                                                                                  Prevision_n_devise=p.Prevision_n_devise,
                                                                                                                  Prevision_n1_total=p.Prevision_n1_total,
                                                                                                                  Prevision_n1_devise=p.Prevision_n1_devise,
                                                                                                                  Prevision_n2_total=p.Prevision_n2_total,
                                                                                                                  Prevision_n2_devise=p.Prevision_n2_devise,
                                                                                                                  Prevision_n3_total=p.Prevision_n3_total,
                                                                                                                  Prevision_n3_devise=p.Prevision_n3_devise,
                                                                                                                  Prevision_n4_total=p.Prevision_n4_total,
                                                                                                                  Prevision_n4_devise=p.Prevision_n4_devise)
                                          r_act.save()      
                              else:                        
                                    #if str(p.champ.activite)=="Pétrole" or str(p.champ.activite)=="Gaz" :
                                    
                                    r_act = Recap_activite.objects.filter(PMT=datetime.date.today().year+0,activite=p.champ.activite)
                                    if r_act.exists():
                                          r_act = Recap_activite.objects.get(PMT=datetime.date.today().year+0,activite=p.champ.activite)
                                          r_act.CGI_total= r_act.CGI_total+ p.Cout_Globale_initial_total
                                          r_act.CGI_devise= r_act.CGI_devise+ p.Cout_Globale_initial_devise
                                          r_act.Previson_de_cloture_total= r_act.Previson_de_cloture_total+ p.Previson_de_cloture_total
                                          r_act.Previson_de_cloture_devise= r_act.Previson_de_cloture_devise+ p.Previson_de_cloture_devise                       
                                          r_act.Reste_a_realiser_total= r_act.Reste_a_realiser_total+ p.Reste_a_realiser_total
                                          r_act.Reste_a_realiser_devise= r_act.Reste_a_realiser_devise+ p.Reste_a_realiser_devise                        
                                          r_act.Realisation_cum_total=r_act.Realisation_cum_total+p.Realisation_cum_total
                                          r_act.Realisation_cum_devise=r_act.Realisation_cum_devise+ p.Realisation_cum_devise
                                          r_act.Realisation_S1_total=r_act.Realisation_S1_total+p.Realisation_S1_total
                                          r_act.Realisation_S1_devise=r_act.Realisation_S1_devise+p.Realisation_S1_devise
                                          r_act.Prevision_S2_total=r_act.Prevision_S2_total+p.Prevision_S2_total
                                          r_act.Prevision_S2_devise=r_act.Prevision_S2_devise+p.Prevision_S2_devise
                                          r_act.Prevision_n_total=r_act.Prevision_n_total+p.Prevision_n_total
                                          r_act.Prevision_n_devise=r_act.Prevision_n_devise+p.Prevision_n_devise
                                          r_act.Prevision_n1_total=r_act.Prevision_n1_total+p.Prevision_n1_total
                                          r_act.Prevision_n1_devise=r_act.Prevision_n1_devise+p.Prevision_n1_devise
                                          r_act.Prevision_n2_total=r_act.Prevision_n2_total+p.Prevision_n2_total
                                          r_act.Prevision_n2_devise=r_act.Prevision_n2_devise+p.Prevision_n2_devise
                                          r_act.Prevision_n3_total=r_act.Prevision_n3_total+p.Prevision_n3_total
                                          r_act.Prevision_n3_devise=r_act.Prevision_n3_devise+p.Prevision_n3_devise
                                          r_act.Prevision_n4_total=r_act.Prevision_n4_total+p.Prevision_n4_total
                                          r_act.Prevision_n4_devise=r_act.Prevision_n4_devise+p.Prevision_n4_devise
                                          r_act.save()
                                    else:
                                          r_act= Recap_activite(PMT=datetime.date.today().year+0,activite=p.champ.activite,CGI_total=p.Cout_Globale_initial_total,
                                                                                                            CGI_devise=p.Cout_Globale_initial_devise,
                                                                                                            
                                                                                                            Previson_de_cloture_total= p.Previson_de_cloture_total,
                                                                                                            Previson_de_cloture_devise= p.Previson_de_cloture_devise,
                                                                                                            
                                                                                                            Reste_a_realiser_total= p.Reste_a_realiser_total,
                                                                                                            Reste_a_realiser_devise= p.Reste_a_realiser_devise,
                                                                                                            Realisation_cum_total=p.Realisation_cum_total,
                                                                                                            Realisation_cum_devise=p.Realisation_cum_devise,
                                                                                                            Realisation_S1_total=p.Realisation_S1_total,
                                                                                                            Realisation_S1_devise=p.Realisation_S1_devise,
                                                                                                            Prevision_S2_total=p.Prevision_S2_total,
                                                                                                            Prevision_S2_devise=p.Prevision_S2_devise,
                                                                                                            Prevision_n_total=p.Prevision_n_total,
                                                                                                            Prevision_n_devise=p.Prevision_n_devise,
                                                                                                            Prevision_n1_total=p.Prevision_n1_total,
                                                                                                            Prevision_n1_devise=p.Prevision_n1_devise,
                                                                                                            Prevision_n2_total=p.Prevision_n2_total,
                                                                                                            Prevision_n2_devise=p.Prevision_n2_devise,
                                                                                                            Prevision_n3_total=p.Prevision_n3_total,
                                                                                                            Prevision_n3_devise=p.Prevision_n3_devise,
                                                                                                            Prevision_n4_total=p.Prevision_n4_total,
                                                                                                            Prevision_n4_devise=p.Prevision_n4_devise)
                                    r_act.save()     
                              
                              #detailed recap
                              if str(p.Perimetre.activite)=="Pétrole" or str(p.Perimetre.activite)=="Gaz":
                                    rog = Recap.objects.filter(PMT=datetime.date.today().year+0,region=p.Perimetre.region,famille=p.Famille,activite=p.Perimetre.activite)
                                    if rog.exists():
                                          rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=p.Perimetre.region,famille=p.Famille,activite=p.Perimetre.activite)
                                          rog.CGI_total= rog.CGI_total+ p.Cout_Globale_initial_total
                                          rog.CGI_devise= rog.CGI_devise+ p.Cout_Globale_initial_devise
                                          rog.Previson_de_cloture_total= rog.Previson_de_cloture_total+ p.Previson_de_cloture_total
                                          rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise+ p.Previson_de_cloture_devise
                                          rog.Reste_a_realiser_total= rog.Reste_a_realiser_total+ p.Reste_a_realiser_total
                                          rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise+ p.Reste_a_realiser_devise
                                          rog.Realisation_cum_total=rog.Realisation_cum_total+p.Realisation_cum_total
                                          rog.Realisation_cum_devise=rog.Realisation_cum_devise+ p.Realisation_cum_devise
                                          rog.Realisation_S1_total=rog.Realisation_S1_total+p.Realisation_S1_total
                                          rog.Realisation_S1_devise=rog.Realisation_S1_devise+p.Realisation_S1_devise
                                          rog.Prevision_S2_total=rog.Prevision_S2_total+p.Prevision_S2_total
                                          rog.Prevision_S2_devise=rog.Prevision_S2_devise+p.Prevision_S2_devise
                                          rog.Prevision_n_total=rog.Prevision_n_total+p.Prevision_n_total
                                          rog.Prevision_n_devise=rog.Prevision_n_devise+p.Prevision_n_devise
                                          rog.Prevision_n1_total=rog.Prevision_n1_total+p.Prevision_n1_total
                                          rog.Prevision_n1_devise=rog.Prevision_n1_devise+p.Prevision_n1_devise
                                          rog.Prevision_n2_total=rog.Prevision_n2_total+p.Prevision_n2_total
                                          rog.Prevision_n2_devise=rog.Prevision_n2_devise+p.Prevision_n2_devise
                                          rog.Prevision_n3_total=rog.Prevision_n3_total+p.Prevision_n3_total
                                          rog.Prevision_n3_devise=rog.Prevision_n3_devise+p.Prevision_n3_devise
                                          rog.Prevision_n4_total=rog.Prevision_n4_total+p.Prevision_n4_total
                                          rog.Prevision_n4_devise=rog.Prevision_n4_devise+p.Prevision_n4_devise
                                          rog.save()
                                    
                                    else:
                                          rog= Recap(activite=p.Perimetre.activite,PMT=datetime.date.today().year+0,region=p.Perimetre.region,famille=p.Famille,
                                                                                                            CGI_total=p.Cout_Globale_initial_total,
                                                                                                            CGI_devise=p.Cout_Globale_initial_devise,                                                                                    
                                                                                                            Previson_de_cloture_total= p.Previson_de_cloture_total,
                                                                                                            Previson_de_cloture_devise= p.Previson_de_cloture_devise,                      
                                                                                                            Reste_a_realiser_total= p.Reste_a_realiser_total,
                                                                                                            Reste_a_realiser_devise= p.Reste_a_realiser_devise,
                                                                                                            Realisation_cum_total=p.Realisation_cum_total,
                                                                                                            Realisation_cum_devise=p.Realisation_cum_devise,
                                                                                                            Realisation_S1_total=p.Realisation_S1_total,
                                                                                                            Realisation_S1_devise=p.Realisation_S1_devise,
                                                                                                            Prevision_S2_total=p.Prevision_S2_total,
                                                                                                            Prevision_S2_devise=p.Prevision_S2_devise,
                                                                                                            Prevision_n_total=p.Prevision_n_total,
                                                                                                            Prevision_n_devise=p.Prevision_n_devise,
                                                                                                            Prevision_n1_total=p.Prevision_n1_total,
                                                                                                            Prevision_n1_devise=p.Prevision_n1_devise,
                                                                                                            Prevision_n2_total=p.Prevision_n2_total,
                                                                                                            Prevision_n2_devise=p.Prevision_n2_devise,
                                                                                                            Prevision_n3_total=p.Prevision_n3_total,
                                                                                                            Prevision_n3_devise=p.Prevision_n3_devise,
                                                                                                            Prevision_n4_total=p.Prevision_n4_total,
                                                                                                            Prevision_n4_devise=p.Prevision_n4_devise)
                                    rog.save()   
                              else:
                                    #if str(p.champ.activite)=="Pétrole" or str(p.champ.activite)=="Gaz" :
                                    rog = Recap.objects.filter(PMT=datetime.date.today().year+0,region=p.Perimetre.region,famille=p.Famille,activite=p.champ.activite)
                                    if rog.exists():
                                          rog = Recap.objects.get(PMT=datetime.date.today().year+0,region=p.Perimetre.region,famille=p.Famille,activite=p.champ.activite)
                                          rog.CGI_total= rog.CGI_total+ p.Cout_Globale_initial_total
                                          rog.CGI_devise= rog.CGI_devise+ p.Cout_Globale_initial_devise
                                          rog.Previson_de_cloture_total= rog.Previson_de_cloture_total+ p.Previson_de_cloture_total
                                          rog.Previson_de_cloture_devise= rog.Previson_de_cloture_devise+ p.Previson_de_cloture_devise
                                          rog.Reste_a_realiser_total= rog.Reste_a_realiser_total+ p.Reste_a_realiser_total
                                          rog.Reste_a_realiser_devise= rog.Reste_a_realiser_devise+ p.Reste_a_realiser_devise
                                          rog.Realisation_cum_total=rog.Realisation_cum_total+p.Realisation_cum_total
                                          rog.Realisation_cum_devise=rog.Realisation_cum_devise+ p.Realisation_cum_devise
                                          rog.Realisation_S1_total=rog.Realisation_S1_total+p.Realisation_S1_total
                                          rog.Realisation_S1_devise=rog.Realisation_S1_devise+p.Realisation_S1_devise
                                          rog.Prevision_S2_total=rog.Prevision_S2_total+p.Prevision_S2_total
                                          rog.Prevision_S2_devise=rog.Prevision_S2_devise+p.Prevision_S2_devise
                                          rog.Prevision_n_total=rog.Prevision_n_total+p.Prevision_n_total
                                          rog.Prevision_n_devise=rog.Prevision_n_devise+p.Prevision_n_devise
                                          rog.Prevision_n1_total=rog.Prevision_n1_total+p.Prevision_n1_total
                                          rog.Prevision_n1_devise=rog.Prevision_n1_devise+p.Prevision_n1_devise
                                          rog.Prevision_n2_total=rog.Prevision_n2_total+p.Prevision_n2_total
                                          rog.Prevision_n2_devise=rog.Prevision_n2_devise+p.Prevision_n2_devise
                                          rog.Prevision_n3_total=rog.Prevision_n3_total+p.Prevision_n3_total
                                          rog.Prevision_n3_devise=rog.Prevision_n3_devise+p.Prevision_n3_devise
                                          rog.Prevision_n4_total=rog.Prevision_n4_total+p.Prevision_n4_total
                                          rog.Prevision_n4_devise=rog.Prevision_n4_devise+p.Prevision_n4_devise
                                          rog.save()
                                    
                                    else:
                                          rog= Recap(activite=p.champ.activite,PMT=datetime.date.today().year+0,region=p.Perimetre.region,famille=p.Famille,
                                                                                                            CGI_total=p.Cout_Globale_initial_total,
                                                                                                            CGI_devise=p.Cout_Globale_initial_devise,                                                                                    
                                                                                                            Previson_de_cloture_total= p.Previson_de_cloture_total,
                                                                                                            Previson_de_cloture_devise= p.Previson_de_cloture_devise,                      
                                                                                                            Reste_a_realiser_total= p.Reste_a_realiser_total,
                                                                                                            Reste_a_realiser_devise= p.Reste_a_realiser_devise,
                                                                                                            Realisation_cum_total=p.Realisation_cum_total,
                                                                                                            Realisation_cum_devise=p.Realisation_cum_devise,
                                                                                                            Realisation_S1_total=p.Realisation_S1_total,
                                                                                                            Realisation_S1_devise=p.Realisation_S1_devise,
                                                                                                            Prevision_S2_total=p.Prevision_S2_total,
                                                                                                            Prevision_S2_devise=p.Prevision_S2_devise,
                                                                                                            Prevision_n_total=p.Prevision_n_total,
                                                                                                            Prevision_n_devise=p.Prevision_n_devise,
                                                                                                            Prevision_n1_total=p.Prevision_n1_total,
                                                                                                            Prevision_n1_devise=p.Prevision_n1_devise,
                                                                                                            Prevision_n2_total=p.Prevision_n2_total,
                                                                                                            Prevision_n2_devise=p.Prevision_n2_devise,
                                                                                                            Prevision_n3_total=p.Prevision_n3_total,
                                                                                                            Prevision_n3_devise=p.Prevision_n3_devise,
                                                                                                            Prevision_n4_total=p.Prevision_n4_total,
                                                                                                            Prevision_n4_devise=p.Prevision_n4_devise)
                                          rog.save()   
                  
                  
         
                        request.session["id"]=p.id
                        return redirect('/prevision_form')  

      else:
            form=add_project_Form
            if 'submitted' in request.GET:
                  submitted=True
      return render(request,'PMT.html',{'form':form,'submitted':submitted})      

@login_required(login_url='login')
def export_mensuel(request):
      user=request.user
      if user.is_staff:
            year=int(datetime.date.today().year)
            obj=Realisation_mensuelle.objects.filter(PMT=year)
            return render(request,'export_mensuel.html',{'Mensuel':obj,'form1':search_form,'form2':search_form_region,
            'form3':search_month_form})

      i = Acces.objects.get(user=request.user) 
      p = Perimetre.objects.filter(region=i.region)
      year=datetime.date.today().year+0
      obj1=Project.objects.filter(Perimetre=p[0],PMT=year)
      obj=Realisation_mensuelle.objects.filter(Project__in=obj1)
      return render(request,'export_mensuel.html',{'Mensuel':obj,'form1':search_form,'form2':search_form_region,
      'form3':search_month_form}) 

@login_required(login_url='login')
def Mensuel(request):
      user=request.user
      if user.is_staff:
            year=int(datetime.date.today().year)
            obj=Realisation_mensuelle.objects.filter(PMT=year)
            return render(request,'Mensuel.html',{'Mensuel':obj,'form1':search_form,'form2':search_form_region,
            'form3':search_month_form})

      i = Acces.objects.filter(user=request.user)
      if i.exists():
            i = Acces.objects.get(user=request.user)
            p = Perimetre.objects.filter(region=i.region)
            year=datetime.date.today().year+0
            if not p:
                  messages.info(request,"La région auquel vous avez accès n'a pas encore de périmètre")
                  return redirect('/')  
            else:      
                  obj1=Project.objects.filter(Perimetre=p[0],PMT=year)
                  obj=Realisation_mensuelle.objects.filter(Project__in=obj1)
                  return render(request,'Mensuel.html',{'Mensuel':obj,'form1':search_form,'form2':search_form_region,
                  'form3':search_month_form}) 
      else:
            return render(request,"404.html")

@login_required(login_url='login')
def mensuel_form(request):
      context= {
            "form":add_realisation_form
      }
      return render(request,'mensuel_form.html',context)

  
@login_required(login_url='login')
def add_mensuel(request):
      form=add_realisation_form(request.POST)
      if form.is_valid():
            new_mensuel=Realisation_mensuelle(PMT=datetime.date.today().year,
                              Mois_real=form.cleaned_data['Mois_real'],
                              Montant_real_Total=form.cleaned_data['Montant_real_Total'],
                              Montant_real_Devise=form.cleaned_data['Montant_real_Devise'],
                              Point_situation=form.cleaned_data['Point_situation'],
                              Project=form.cleaned_data['Project'],

                              
            )
            #to set the cummulation values 
            p = Prévision_mensuelle.objects.get(Mois_prev=form.cleaned_data['Mois_real'],Project=form.cleaned_data['Project'])
            new_mensuel.prevision_mensuelle_id=p
            cum = Realisation_mensuelle.objects.filter(PMT=datetime.date.today().year,Project=form.cleaned_data['Project'])
            if cum.exists():
                  m=max(c.real_cum_total for c in cum)
                  cum = Realisation_mensuelle.objects.get(PMT=datetime.date.today().year,Project=form.cleaned_data['Project'],real_cum_total=m)
                  new_mensuel.real_cum_total=int(new_mensuel.Montant_real_Total)+int(cum.real_cum_total)
                  new_mensuel.real_cum_devise=int(new_mensuel.Montant_real_Total)+int(cum.real_cum_devise)

            else:
                  new_mensuel.real_cum_total=new_mensuel.Montant_real_Total
                  new_mensuel.real_cum_devise=new_mensuel.Montant_real_Devise

            new_mensuel.save()
            p = Project.objects.get(Libelles=form.cleaned_data['Project'],PMT=datetime.date.today().year)
            pre = Prévision_mensuelle.objects.get(Project=p,Mois_prev=form.cleaned_data['Mois_real'])
            new_mensuel.taux_real_mois=Taux_real(int(pre.Montant_Prevu_Total),int(new_mensuel.Montant_real_Total))
            new_mensuel.taux_real_cum=Taux_real(int(pre.Prev_cum_total),int(new_mensuel.real_cum_total))
            new_mensuel.taux_real_ann=Taux_real(int(new_mensuel.Project.Prevision_n_total),int(new_mensuel.real_cum_total))
            
            new_mensuel.save()
            return HttpResponseRedirect('Mensuel?submitted=True')  
      else:
            form=add_realisation_form
            if 'submitted' in request.GET:
                  submitted=True
      return render(request,'Mensuel.html',{'form':form,'submitted':submitted})   

@login_required(login_url='login')
def export_prevision(request):
      obj=Prévision_mensuelle.objects.values('Project').distinct()
      obj1 = Prévision_mensuelle.objects.all()

      stm=Prévision_mensuelle_stimulation.objects.values('Stimulation').distinct()
      stm1 = Prévision_mensuelle_stimulation.objects.all()

      context={ "Prevision":obj,
            "Prevision1":obj1,
            "Prevision_stm":stm,
            "Prevision_stm1":stm1,
             }
      return render(request,'export_prevision.html',context)

@login_required(login_url='login')
def Prevision(request):
      user=request.user
      if user.is_staff:
            obj=Prévision_mensuelle.objects.values('Project').distinct()
            obj1 = Prévision_mensuelle.objects.all()            
            stm=Prévision_mensuelle_stimulation.objects.values('Stimulation').distinct()
            stm1 = Prévision_mensuelle_stimulation.objects.all()
            context={ "Prevision":obj,
            "Prevision1":obj1,
            "Prevision_stm":stm,
            "Prevision_stm1":stm1,
             }
            return render(request,'Prevision.html',context)

      i = Acces.objects.filter(user=request.user)
      if i.exists():
            i = Acces.objects.get(user=request.user)

    
            p = Perimetre.objects.filter(region=i.region)
            year=datetime.date.today().year+0            
            if not p:
                  messages.info(request,"La région auquel vous avez accès n'a pas encore de périmètre")
                  return redirect('/')   
            else:  
                  prj=Project.objects.filter(Perimetre=p[0],PMT=year)#getting the projets that the user can access
                  per=Prévision_mensuelle.objects.filter(Project__in=prj)#getting the prevision of those project

                  obj=per.values('Project').distinct()#getting distinct projects for the first loop 
                  obj1 = Prévision_mensuelle.objects.all()#all previsions (12) for the seconde loop
                  
                  ############ the same work for the stimulations #############
                  simulation=Stimulation.objects.filter(Perimetre=p[0],PMT=year)
                  stms=Prévision_mensuelle_stimulation.objects.filter(Stimulation__in=simulation)
                  stm=stms.values('Stimulation').distinct()
                  stm1 = Prévision_mensuelle_stimulation.objects.all()
                  
                  context={ "Prevision":obj,
                        "Prevision1":obj1,
                        "Prevision_stm":stm,
                        "Prevision_stm1":stm1,
                        }
                  return render(request,'Prevision.html',context)
      else:
            return render(request,'404.html')

@login_required(login_url='login')
def prevision_form(request):
      context= {
            "form":add_prevision_form
      }
      return render(request,'prevision_form.html',context)

@login_required(login_url='login')
def add_prevision(request):
      submitted=False
      form=add_prevision_form(request.POST)
      if form.is_valid():
            #validation 
            somme_globale=form.cleaned_data['Montant_Prevu_janvier_Total']+form.cleaned_data['Montant_Prevu_fevrier_Total']+form.cleaned_data['Montant_Prevu_mars_Total']+form.cleaned_data['Montant_Prevu_avril_Total']+form.cleaned_data['Montant_Prevu_mai_Total']+form.cleaned_data['Montant_Prevu_juin_Total']+form.cleaned_data['Montant_Prevu_juiller_Total']+form.cleaned_data['Montant_Prevu_aout_Total']+form.cleaned_data['Montant_Prevu_septembre_Total']+form.cleaned_data['Montant_Prevu_octobre_Total']+form.cleaned_data['Montant_Prevu_novombre_Total']+form.cleaned_data['Montant_Prevu_decembre_Total']
            somme_globale_int=int(somme_globale)
            somme_globale_rouned=round(somme_globale)

            p = Project.objects.filter(id=request.session["id"]) 
            if p.exists():
                  n=Project.objects.get(id=request.session["id"])
                  print(n.Prevision_n_total,somme_globale,somme_globale_int,somme_globale_rouned)
                  #needed to allow all cases because the users asked for that (somtimes they used true values and other times int or rounded values)
                  if  somme_globale_int==n.Prevision_n_total or somme_globale_rouned==n.Prevision_n_total or somme_globale==int(n.Prevision_n_total) or somme_globale_int==int(n.Prevision_n_total) or somme_globale_rouned==int(n.Prevision_n_total) or somme_globale==round(n.Prevision_n_total) or somme_globale_int==round(n.Prevision_n_total) or somme_globale_rouned==round(n.Prevision_n_total) :             
                        new_prevision1=Prévision_mensuelle(Mois_prev="janvier",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_janvier_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_janvier_devise'],
                                          Project=n,
                                          Prev_cum_total = form.cleaned_data['Montant_Prevu_janvier_Total'],
                                          Prev_cum_devise = form.cleaned_data['Montant_Prevu_janvier_devise'],

                              
                        )

                        new_prevision1.save()
                        new_prevision2=Prévision_mensuelle(Mois_prev="fevrier",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_fevrier_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_fevrier_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise']),
                        )

                        new_prevision2.save()
                        new_prevision3=Prévision_mensuelle(Mois_prev="mars",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_mars_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_mars_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise']),
                        )

                        new_prevision3.save()
                        new_prevision4=Prévision_mensuelle(Mois_prev="avril",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_avril_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_avril_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise']),
                        )

                        new_prevision4.save()
                        new_prevision5=Prévision_mensuelle(Mois_prev="mai",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_mai_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_mai_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise']),
                        )

                        new_prevision5.save()
                        new_prevision6=Prévision_mensuelle(Mois_prev="juin",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_juin_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_juin_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise']),
                        )

                        new_prevision6.save()
                        new_prevision7=Prévision_mensuelle(Mois_prev="juillet",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_juiller_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_juiller_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise']),
                        )

                        new_prevision7.save()
                        new_prevision8=Prévision_mensuelle(Mois_prev="aout",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_aout_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_aout_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise']),
                        )

                        new_prevision8.save()
                        new_prevision9=Prévision_mensuelle(Mois_prev="septembre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_septembre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_septembre_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise']),
                        )

                        new_prevision9.save()
                        new_prevision10=Prévision_mensuelle(Mois_prev="octobre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_octobre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_octobre_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total'])+int(form.cleaned_data['Montant_Prevu_octobre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise'])+int(form.cleaned_data['Montant_Prevu_octobre_devise']),
                        )

                        new_prevision10.save()
                        new_prevision11=Prévision_mensuelle(Mois_prev="novombre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_novombre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_novombre_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total'])+int(form.cleaned_data['Montant_Prevu_octobre_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_novombre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise'])+int(form.cleaned_data['Montant_Prevu_octobre_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_novombre_devise']),
                        )

                        new_prevision11.save()
                        new_prevision12=Prévision_mensuelle(Mois_prev="decembre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_decembre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_decembre_devise'],
                                          Project=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total'])+int(form.cleaned_data['Montant_Prevu_octobre_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_novombre_Total'])+int(form.cleaned_data['Montant_Prevu_decembre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise'])+int(form.cleaned_data['Montant_Prevu_octobre_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_novombre_devise'])+int(form.cleaned_data['Montant_Prevu_decembre_devise']),
                        )

                        new_prevision12.save()
                        messages.success(request,"projet ajouté avec succès")
                        return redirect('PMT')
                  else:

                        messages.error(request,"Veuillez réinsérer les prévisions, la prévision annuelle globale et les prévisions mensuelles du projet ne correspondent pas")
                        delete_project (request,n.id)
                        return redirect('prevision_form')
            else: 
#####################################  to add previsions to the stimulation ################################################

                  s=Stimulation.objects.filter(stimulation_id=request.session["id"])
                  n=Stimulation.objects.get(stimulation_id=request.session["id"]) 
                  if somme_globale==n.Prevision_n_total:
                        new_prevision1=Prévision_mensuelle_stimulation(Mois_prev="janvier",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_janvier_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_janvier_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = form.cleaned_data['Montant_Prevu_janvier_Total'],
                                          Prev_cum_devise = form.cleaned_data['Montant_Prevu_janvier_devise'],
                                          
                        )

                        new_prevision1.save()
                        new_prevision2=Prévision_mensuelle_stimulation(Mois_prev="fevrier",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_fevrier_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_fevrier_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise']),
                        )

                        new_prevision2.save()
                        new_prevision3=Prévision_mensuelle_stimulation(Mois_prev="mars",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_mars_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_mars_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise']),
                        )

                        new_prevision3.save()
                        new_prevision4=Prévision_mensuelle_stimulation(Mois_prev="avril",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_avril_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_avril_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise']),
                        )

                        new_prevision4.save()
                        new_prevision5=Prévision_mensuelle_stimulation(Mois_prev="mai",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_mai_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_mai_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise']),
                        )

                        new_prevision5.save()
                        new_prevision6=Prévision_mensuelle_stimulation(Mois_prev="juin",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_juin_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_juin_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise']),
                        )

                        new_prevision6.save()
                        new_prevision7=Prévision_mensuelle_stimulation(Mois_prev="juillet",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_juiller_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_juiller_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise']),
                        )

                        new_prevision7.save()
                        new_prevision8=Prévision_mensuelle_stimulation(Mois_prev="aout",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_aout_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_aout_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise']),
                        )

                        new_prevision8.save()
                        new_prevision9=Prévision_mensuelle_stimulation(Mois_prev="septembre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_septembre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_septembre_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise']),
                        )

                        new_prevision9.save()
                        new_prevision10=Prévision_mensuelle_stimulation(Mois_prev="octobre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_octobre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_octobre_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total'])+int(form.cleaned_data['Montant_Prevu_octobre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise'])+int(form.cleaned_data['Montant_Prevu_octobre_devise']),
                        )

                        new_prevision10.save()
                        new_prevision11=Prévision_mensuelle_stimulation(Mois_prev="novombre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_novombre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_novombre_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total'])+int(form.cleaned_data['Montant_Prevu_octobre_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_novombre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise'])+int(form.cleaned_data['Montant_Prevu_octobre_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_novombre_devise']),
                        )

                        new_prevision11.save()
                        new_prevision12=Prévision_mensuelle_stimulation(Mois_prev="decembre",
                                          Montant_Prevu_Total=form.cleaned_data['Montant_Prevu_decembre_Total'],
                                          Montant_Prevu_Devise=form.cleaned_data['Montant_Prevu_decembre_devise'],
                                          Stimulation=n,
                                          Prev_cum_total = int(form.cleaned_data['Montant_Prevu_janvier_Total'])+int(form.cleaned_data['Montant_Prevu_fevrier_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mars_Total'])+int(form.cleaned_data['Montant_Prevu_avril_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_mai_Total'])+int(form.cleaned_data['Montant_Prevu_juin_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_juiller_Total'])+int(form.cleaned_data['Montant_Prevu_aout_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_septembre_Total'])+int(form.cleaned_data['Montant_Prevu_octobre_Total'])+
                                                      int(form.cleaned_data['Montant_Prevu_novombre_Total'])+int(form.cleaned_data['Montant_Prevu_decembre_Total']),
                                          Prev_cum_devise = int(form.cleaned_data['Montant_Prevu_janvier_devise'])+int(form.cleaned_data['Montant_Prevu_fevrier_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mars_devise'])+int(form.cleaned_data['Montant_Prevu_avril_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_mai_devise'])+int(form.cleaned_data['Montant_Prevu_juin_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_juiller_devise'])+int(form.cleaned_data['Montant_Prevu_aout_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_septembre_devise'])+int(form.cleaned_data['Montant_Prevu_octobre_devise'])+
                                                            int(form.cleaned_data['Montant_Prevu_novombre_devise'])+int(form.cleaned_data['Montant_Prevu_decembre_devise']),
                        )

                        new_prevision12.save()
                        messages.success(request,"projet ajouté avec succès")
                        return redirect('PMT') 
                  else:
                        messages.error(request,"Veuillez réinsérer les prévisions, la prévision annuelle globale et les prévisions mensuelles de la stimulation ne correspondent pas")
                        delete_project (request,n.id)
                        return redirect('prevision_form')

 
      else:
            form=add_prevision_form
            if 'submitted' in request.GET:
                  submitted=True
      return render(request,'PMT.html',{'form':form,'submitted':submitted}) 

      
        
########################################## templates forms ##########################################


@login_required(login_url='login')
def home(request):
      return render(request,'home.html')





                        
                  

            #pev=Prévision_mensuelle.objects.filter(Project.id=pk)



      project=Project.objects.filter(id=pk)
      if project.exists():
            project=Project.objects.get(id=pk)
            form = update_project_Form(initial={'Compte_Analytique': project.Compte_Analytique,
            'Libelles':project.Libelles,
            'Structure_gerante':project.Structure_gerante,
            'Perimetre':project.Perimetre,
            #'Champ':project.Champ,
            'Famille':project.Famille,
            'Type':project.Type,
            'Fiscalite':project.Fiscalite,
            'Realisation_cum_total':project.Realisation_cum_total,
            'Realisation_cum_devise':project.Realisation_cum_devise,
            'Realisation_S1_total':project.Realisation_S1_total,
            'Realisation_S1_devise':project.Realisation_S1_devise,
            'Prevision_S2_total':project.Prevision_S2_total,
            'Prevision_S2_devise':project.Prevision_S2_devise,
            'Prevision_n_total':project.Prevision_n_total,
            'Prevision_n_devise':project.Prevision_n_devise,
            'Prevision_n1_total':project.Prevision_n1_total,
            'Prevision_n1_devise':project.Prevision_n1_devise,
            'Prevision_n2_total':project.Prevision_n2_total,
            'Prevision_n2_devise':project.Prevision_n2_devise,    
            'Prevision_n3_total':project.Prevision_n3_total,
            'Prevision_n3_devise':project.Prevision_n3_devise,
            'Prevision_n4_total':project.Prevision_n4_total,
            'Prevision_n4_devise':project.Prevision_n4_devise,
            'Point_situation':project.Point_situation,
            }) 
            #form=update_project_Form(request.POST or None, obj=project)
            project.Compte_Analytique="Compte_Analytique"+"crypt"
            context={'form':form}
            #print(project.Champ)
            return render(request,'project_form_update.html',context)
            
            
      else:       #to update stimulations
 
            stimulation=Stimulation.objects.get(stimulation_id=pk)
            form = add_project_Form(initial={'Compte_Analytique': stimulation.Compte_Analytique,
            'Libelles':stimulation.stimulation,
            'Structure_gerante':stimulation.Structure_gerante,
            'Perimetre':stimulation.Perimetre,
            #'Champ':project.Champ,
            'Famille':stimulation.Famille,
            'Type':stimulation.Type,
            'Fiscalite':stimulation.Fiscalite,
            'Realisation_cum_total':stimulation.Realisation_cum_total,
            'Realisation_cum_devise':stimulation.Realisation_cum_devise,
            'Realisation_S1_total':stimulation.Realisation_S1_total,
            'Realisation_S1_devise':stimulation.Realisation_S1_devise,
            'Prevision_S2_total':stimulation.Prevision_S2_total,
            'Prevision_S2_devise':stimulation.Prevision_S2_devise,
            'Prevision_n_total':stimulation.Prevision_n_total,
            'Prevision_n_devise':stimulation.Prevision_n_devise,
            'Prevision_n1_total':stimulation.Prevision_n1_total,
            'Prevision_n1_devise':stimulation.Prevision_n1_devise,
            'Prevision_n2_total':stimulation.Prevision_n2_total,
            'Prevision_n2_devise':stimulation.Prevision_n2_devise,
            'Prevision_n3_total':stimulation.Prevision_n3_total,
            'Prevision_n3_devise':stimulation.Prevision_n3_devise,
            'Prevision_n4_total':stimulation.Prevision_n4_total,
            'Prevision_n4_devise':stimulation.Prevision_n4_devise,
            'Point_situation':stimulation.Point_situation,
            }) 
            #form=update_project_Form(request.POST or None, obj=project)

            #print(project.Champ)
            context={'form':form}
            return render(request,'project_form_update.html',context)


