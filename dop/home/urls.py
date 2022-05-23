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
      path('admin_home', views.admin_home, name='admin_home'),
      path('delete_project/<str:pk>/', views.delete_project, name='delete_project'),
      path('delete_realisation/<str:pk>/', views.delete_realisation, name='delete_realisation'),
      path('update_project/<str:pk>/', views.update_project, name='update_project'),
      path('search_project', views.search_project, name='search_project'),
      path('search_project_region', views.search_project_region, name='search_project_region'),
      path('PMT', views.PMT, name='PMT'),
      path('export_pmt', views.export_pmt, name='export_pmt'),
      path('recap_fam', views.recap_fam, name='recap_fam'),
      path('recap_reg', views.recap_reg, name='recap_reg'),
      path('recap_act', views.recap_act, name='recap_act'),
      path('recap', views.recap, name='recap'),
      path('project_form', views.project_form, name='project_form'),
      path('search_month', views.search_month, name='search_month'),      
      path('add_project', views.add_project, name='add_project'),

      path('Mensuel', views.Mensuel, name='Mensuel'),
      path('mensuel_form', views.mensuel_form, name='mensuel_form'),
      path('add_mensuel', views.add_mensuel, name='add_mensuel'),

      path('Prevision', views.Prevision, name='Prevision'),
      path('export_prevision', views.export_prevision, name='export_prevision'),
      path('prevision_form', views.prevision_form, name='prevision_form'),
      path('add_prevision', views.add_prevision, name='add_prevision'),

      path('add_monthly', views.add_monthly, name='add_monthly'),
      path('loginuser',views.loginuser,name='loginuser'),
      path('accounts/',include('django.contrib.auth.urls')),
      path('',TemplateView.as_view(template_name='home.html'), name='home')     
      ]
