from django.urls import path
from . import views

urlpatterns = [
    path('', views.listLots, name='Lotes'),
    path('lot/<int:id>', views.viewLot, name='Lote'),
    path('deleteLot/<int:id>', views.deleteLot, name='Delete Lote'),
    path('editLot/<int:id>', views.editLot, name='Edit Lote'),
    path('editCut/<int:id>', views.editCut, name='Edit Corte'),
    path('deleteCut/<int:id>', views.deleteCut, name='Delete Corte'),
]
