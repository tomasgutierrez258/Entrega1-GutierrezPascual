from datetime import datetime
from django.shortcuts import render,redirect
from home.forms  import CreatePostForm, SearchPostForm
from home.models import Posts
from django.views.generic.edit import UpdateView,DeleteView

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

def create_post(request):
    if request.method == "POST":
        formulario = CreatePostForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            date = datetime.now()
            author = ""
            
            title = data['title']
            brief_description = data['brief_description']
            category = data['category']
            text = data['text']
            
            post = Posts(date = date,author=author,title = title,brief_description = brief_description,text = text,category=category)
            post.save()
            return redirect("home")
        else:
            return render(request, "home/create_post.html", {"formulario":formulario})
    formulario = CreatePostForm()
    return render(request, "home/create_post.html", {"formulario":formulario})

# class CreatePost(CreateView):
#     model = Posts
#     success_url = '/'
#     template_name = 'home/create_post.html'
#     fields = ['date','title','brief_description','category','featured','text']
    
class EditPost(UpdateView):
    model = Posts
    success_url = '/'
    template_name = 'home/edit_post.html'
    fields = ['title','brief_description','category','text']
    

class RemovePost(DeleteView):
    model = Posts
    success_url = '/'
    template_name = 'home/remove_post.html'

def about(request):
    return render(request, "home/about.html") 