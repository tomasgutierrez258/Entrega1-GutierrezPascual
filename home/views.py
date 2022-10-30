from datetime import datetime
from re import template
from django.shortcuts import render,redirect
from home.forms  import CreatePostForm, SearchPostForm
from home.models import Posts
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin #limita al usuario a acceder a ciertas paginas
from django.contrib.auth.decorators import login_required
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

@login_required
def create_post(request):
    if request.method == "POST":
        formulario = CreatePostForm(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            date = datetime.now()
            user = request.user
            
            # print("user.id: ",type(user.id))
            # user_avatar = UserExtension.objects.filter(user_id__id__icontains=user.id)
            
            title = data['title']
            subtitle = data['subtitle']
            brief_description = data['brief_description']
            text = data['text']
            image_post = data['image_post']
            
            post = Posts(date = date,user=user,title = title,subtitle = subtitle,brief_description = brief_description,text = text, image_post = image_post)
            post.save()
            return redirect("home")
        else:
            return render(request, "home/create_post.html", {"formulario":formulario})
    formulario = CreatePostForm()
    return render(request, "home/create_post.html", {"formulario":formulario})
    
class EditPost(LoginRequiredMixin,UpdateView):
    model = Posts
    success_url = '/'
    template_name = 'home/edit_post.html'
    fields = ['title','subtitle','brief_description','text']

class RemovePost(LoginRequiredMixin,DeleteView):
    model = Posts
    success_url = '/'
    template_name = 'home/remove_post.html'

class readPost(DetailView):
    model = Posts
    template_name = 'home/read_post.html'

def about(request):
    return render(request, "home/about.html") 