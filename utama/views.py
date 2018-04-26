from django.shortcuts import render,redirect,get_object_or_404
from utama.models import Tbl_user as SQL
from django.contrib import messages
from django.utils.html import escape

headerData = {
    'title':"| Django Crud"
}

def index(request):
    userData = SQL.objects.all()
    headerData['userData'] = userData
    return render(request, 'utama/utama.html', headerData)

def add(request,id=0):
    myData = {
        'title':"| Django Crud Tambah"
    }
    return render(request, 'utama/add.html', myData)

def edit(request,id=0):
    myData = {
        'title':"| Django Crud Tambah"
    }
    cek = get_object_or_404(SQL,id_user=id)
    param = SQL.objects.get(id_user=id)
    myData['res'] = param
    return render(request, 'utama/edit.html', myData)

def save(request):
    if request.method == 'POST':
        username = escape(request.POST['username'])
        email = request.POST['email']
        password = request.POST['password']

        save_data = SQL(username=username,email=email,password=password)
        save_data.save()
        messages.success(request,'data tersimpan !')
        return redirect('/', headerData)
    else:
        messages.warning(request, 'Method Not Allowed !')
        return redirect('/', headerData)

def update(request,id=None):
    if request.method == 'POST':
        cek = get_object_or_404(SQL,id_user=id)
        param = SQL.objects.get(id_user=id)
        param.username = escape(request.POST['username'])
        param.email = request.POST['email']
        param.password = request.POST['password']

        param.save()
        messages.success(request,'data berhasil di perbarui !')
        return redirect('/', headerData)
    else:
        messages.warning(request, 'Method Not Allowed !')
        return redirect('/', headerData)

def delete(request,id=None):
    if request.method == 'GET':
        param = get_object_or_404(SQL,id_user=id)
        param.delete()
        messages.success(request,'data terhapus !')
        return redirect('/', headerData)
    else:
        messages.warning(request, 'Method Not Allowed !')
        return redirect('/', headerData)
