from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'WebJecApp/Base.html')

def home(request):

    return render(request, 'WebJecApp/Home.html')
