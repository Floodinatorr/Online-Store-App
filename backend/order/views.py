from django.shortcuts import render

def AnaSayfa(request):
    return render(request,'index.html',{})