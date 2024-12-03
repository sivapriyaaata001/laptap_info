from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def third(request):
    return HttpResponse('''Dell does not exactly make the most affordable laptops out there.
                         but what the brand is known for is reliabilty''')
def third(request):
    return HttpResponse('''<h1>Features</h1>
                          slick frameless keyboard and extra large,
                          feature flipped touchpad,Excellent Performance & battery life
                         ''')    
