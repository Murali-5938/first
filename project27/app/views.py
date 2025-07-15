from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
#this is function based view for string response
def String_fbv(request):
    return HttpResponse('this is functionbased view')

#this is class based view for string response
class String_cbv(View):
    def get(self,request):
        return HttpResponse("this is classbased view")

# this is function based view for string response
def fbv(request):
    return render(request,"fbv.html")

class cbv(View):
    def get(self,request):
        return render(request,"cbv.html")
    
def inserting_data(request):
    




