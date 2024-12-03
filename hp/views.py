from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def second(request):
    return HttpResponse('hp laptops uses everywhere from schools to offices')
def second(request):
    return HttpResponse('''<h1>Features</h1>
                          AI assisted with features<br>
                          1.future-proof technology
                          2.Improved productivity
                          3.seamless connectivity<br>
                          These laptops provides an exceptional compputing experience
                         ''')    
