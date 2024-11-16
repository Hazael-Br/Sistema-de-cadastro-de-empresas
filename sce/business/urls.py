
from django.urls import path
from . import views





urlpatterns = [
 
    path('', views.index, name='index'),
    path('business/', views.BusinessCreateListView.as_view(), name='business-create-list'),
    path('business/<uuid:pk>/', views.BusinessRetrieveUpdateDestroyView.as_view(), name='business-detail-view'),
    path('index2.html/', views.index2, name='index2'), 
    path('index3.html/', views.index3, name='index3'),
    path('Voltar/', views.Voltar, name='voltar'),
    path('voltar/', views.voltar, name='voltar'),
    path('voltar-para-index/', views.voltar_para_index, name='voltar-para-index'),
]