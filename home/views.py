from turtle import pos
from django.http import HttpResponse
from django.template import Context,Template,loader
from datetime import datetime
from django.shortcuts import render,redirect
from home.forms  import CreatePostForm, SearchPostForm
from home.models import Posts

# Create your views here.
def home(request):
    postInfo=""
    title = request.GET.get('title',None)
    if title:
        posts = Posts.objects.filter(title__icontains=title)
        if len(posts) == 0:
            postInfo = "No results found"
    else:
        posts = Posts.objects.all()
        if len(posts) == 0:
            postInfo = "No posts have been created yet"
    formulario = SearchPostForm()
    return render(request, "home/index.html", {"posts" : posts,"formulario":formulario,"postInfo":postInfo})

def about(request):
    return render(request, "home/about.html")

def create_post(request):
    if request.method == "POST":
        
        formulario = CreatePostForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            print("data: ",data)
            date = data.get('date',datetime.now())
            title = data['title']
            brief_description = data['brief_description']
            # category = data['category']
            # featured = data['featured']
            text = data['text']
            
            post = Posts(date = date,title = title,brief_description = brief_description,text = text)
            post.save()
            return redirect("home")
    
    formulario = CreatePostForm()
    return render(request, "home/create-post.html", {"formulario":formulario})