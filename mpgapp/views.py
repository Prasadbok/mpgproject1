from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,"index.html")
def predict(request):
    dis =request.GET['dis']
    hor =request.GET['hor']
    weight =request.GET['weight']
    acce = request.GET['acce']
    input = [dis,hor,weight,acce]
    return render(request,"result.html",{'output':input,'displacement':dis,'horsepower':hor,'weight':weight,'acceleration':acce})
