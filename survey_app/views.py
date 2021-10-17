from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    if 'result' not in request.session:
        request.session['result']=request.POST
    return redirect('/final')

def final(request):
    return render(request, 'result.html')