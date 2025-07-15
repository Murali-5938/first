from django.shortcuts import render

# Create your views here.
def jinjalooping(request):
    fruits={"a":"apple", "b":"banana", "c":"cherry"}
    return render(request,"jinjalooping.html",context={"fruits":fruits})