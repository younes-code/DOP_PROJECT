from pipes import Template
from django.contrib import admin
from django.urls import path,include
from home import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

#django costumize

admin.site.site_header="Tableau de bord DP"
admin.site.site_title="DOP Dashboard"
admin.site.index_title=""


urlpatterns = [
      path('', views.home, name='home'),
      path('delete_project/<str:pk>/', views.delete_project, name='delete_project'),
      path('delete_realisation/<str:pk>/', views.delete_realisation, name='delete_realisation'),

      path('search_project', views.search_project, name='search_project'),
      path('search_project_region', views.search_project_region, name='search_project_region'),
      path('PMT', views.PMT, name='PMT'),
      path('export_pmt', views.export_pmt, name='export_pmt'),
      path('recap_fam', views.recap_fam, name='recap_fam'),
      path('export_famille', views.export_famille, name='export_famille'),
      path('recap_reg', views.recap_reg, name='recap_reg'),
      path('export_region', views.export_region, name='export_region'),

      path('recap_act', views.recap_act, name='recap_act'),
      path('export_activite', views.export_activite, name='export_activite'),

      path('recap', views.recap, name='recap'),
      path('export_recap', views.export_recap, name='export_recap'),

      path('project_form', views.project_form, name='project_form'),
      path('search_month', views.search_month, name='search_month'),      
      path('add_project', views.add_project, name='add_project'),

      path('Mensuel', views.Mensuel, name='Mensuel'),
      path('export_mensuel', views.export_mensuel, name='export_mensuel'),
      path('mensuel_form', views.mensuel_form, name='mensuel_form'),
      path('add_mensuel', views.add_mensuel, name='add_mensuel'),

      path('Prevision', views.Prevision, name='Prevision'),
      path('export_prevision', views.export_prevision, name='export_prevision'),
      path('prevision_form', views.prevision_form, name='prevision_form'),
      path('add_prevision', views.add_prevision, name='add_prevision'),
      path('update_previsions_form', views.update_previsions_form, name='update_previsions_form'),

      path('login',views.loginPage,name='login'),
      path('logout',views.logoutUser,name='logoutUser'),
      #path('accounts/',include('django.contrib.auth.urls')),
      path('',TemplateView.as_view(template_name='home.html'), name='home')     
      ]
