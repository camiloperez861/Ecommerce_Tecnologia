#urls-servicios

from django.urls import path

#Para importa la vista de ejemplo
from Servicios.views import vistaEjemplo

urlpatterns = [
    path('ejemplo', vistaEjemplo  ),
    
]