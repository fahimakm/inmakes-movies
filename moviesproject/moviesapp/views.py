from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):

    movie=Movie.objects.all()

    return render(request,'index.html',{'movie_list':movie})

def detail(request,movie_id):

    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})

def add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        movie = Movie(name=name,desc=desc,year=year,img=img,img1=img1,img2=img2)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form= MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    movie1=Movie.objects.get(id=id)
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html',{'movie1':movie1})