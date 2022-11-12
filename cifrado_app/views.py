from django.shortcuts import render
import hashlib

# Create your views here.

def inicio(request):
    palabra=''
    md5=''
    if request.POST.get('cifrado'):
        palabra=request.POST['cifrado']
        print(palabra)
        #sha256 = hashlib.sha256(palabra.encode('utf-8')).hexdigest()
        md5 = hashlib.md5(palabra.encode('utf-8')).hexdigest()





    return render (request,'index.html',{'cifrado':md5,'palabra':palabra})


def sha1(request):
 palabra=''
 sha1=''
 if request.POST.get('cifrado'):
        palabra=request.POST['cifrado']
        print(palabra)
        #sha256 = hashlib.sha256(palabra.encode('utf-8')).hexdigest()
        sha1 = hashlib.sha1(palabra.encode('utf-8')).hexdigest()
 return render(request,'sha1.html',{'cifrado':sha1,'palabra':palabra})




def sha256(request):
 palabra=''
 sha224=''
 if request.POST.get('cifrado'):
        palabra=request.POST['cifrado']
        print(palabra)
        #sha256 = hashlib.sha256(palabra.encode('utf-8')).hexdigest()
        sha224 = hashlib.sha224(palabra.encode('utf-8')).hexdigest()
 return render(request,'sha256.html',{'cifrado':sha224,'palabra':palabra})