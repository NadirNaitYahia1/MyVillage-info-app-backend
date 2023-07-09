from django.urls import path
from .  import views
urlpatterns = [
    path('', views.gettest),
    path('getBuses/', views.getBuses),
    path('getPharmacies/', views.getPharmacies),
    path('login/', views.login),
	 
    path('create_bus', views.createBus),
    path('create_pharmacy', views.createPharmacy),
    path('update_bus', views.updateBus),
]