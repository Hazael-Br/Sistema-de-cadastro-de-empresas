
from rest_framework import generics
from business.models import Business
from business.serializers import BusinessSerializer
from django.shortcuts import render, redirect

def index (request):
    return render(request, 'index.html')

def index2(request): 
    return render(request, 'index2.html') 

def index3(request): 
    return render(request, 'index3.html')


def Voltar(request): 
    return render(request, 'index.html')

def voltar(request): 
        return redirect('/')

def voltar_para_index(request): 
        return redirect('/')



class BusinessCreateListView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Business.objects.all()
    serializer_class = BusinessSerializer

   