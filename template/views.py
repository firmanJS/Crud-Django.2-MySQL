#from django.http import HttpResponse
# from django.shortcuts import render
# from models import model
# def index(request):
#     #return HttpResponse("hello")
#     myData = {
#         'title':"| Django Crud"
#     }
#     return render(request, 'utama/utama.html', myData)
#
# def add(request):
#     myData = {
#         'title':"| Django Crud Tambah"
#     }
#     return render(request, 'utama/add.html', myData)
#
# def save(request):
#     username = request.POST['username']
#     email = request.POST['email']
#     password = request.POST['password']
from django.shortcuts import render
from django.template import RequestContext

def handler404(request):
    arr ={
        'pesan': "Oops Page Not Found !",
        'title': "Oops Page Not Found !",
        'code': 404
    }
    return render(request, 'bad.html',arr)

def handler500(request):
    arr ={
        'pesan': "Oops Bad Request !",
        'title': "Oops Bad Request !",
        'code': 500
    }
    return render(request, 'bad.html',arr)
