from django.shortcuts import render

# Create your views here.
def val(request):
  return render(request, 'val.html')
