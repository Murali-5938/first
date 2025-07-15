from django.shortcuts import render

def jinjaconditinal(request):
    d={"a":500,"b":400}
    return render(request,"jinjaconditinal.html",context=d)
