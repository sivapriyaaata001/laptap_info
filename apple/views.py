from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('Apple products have many features,including privacy,user,security&friendly tools')
def first(request):
    return HttpResponse('''<h1>Friendlytools:</h1>
                        1) AirDrop
                        2)Visual Look up
                        3)Smart Reply
                        4)Face ID with Mask&Gurl''')

