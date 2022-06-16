from django.urls import path
from .views import (
    contato,
    home,
    planos,
    sobre,
    servicos,
)

urlpatterns = [
    path('', home, name='website_home'),
    path('contato/', contato, name='website_contato'),
    path('planos/', planos, name='website_planos'),
    path('sobre/', sobre, name='website_sobre'),
    path('servicos/', servicos, name='website_servicos'),
]
