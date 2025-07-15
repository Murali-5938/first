from django.shortcuts import render

def jinjaprint(request):
    d={"name":'krishna',"age":22,"gender":'M'}
    return render(request,"jinjaprint.html",context=d)
