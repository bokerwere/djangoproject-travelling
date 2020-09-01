from django.shortcuts import render, get_object_or_404
from blog.models import Post

#userpassestestmixin allow particular user to update post
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
#class base view// import list view
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from  django.contrib.auth.models import User
# Create your views here. user


def home(reguest):
    content={'posts':Post.objects.all()}

    return render(reguest,'home.html',content)
class PostListView(ListView):
    #indicate model went to query to view list
    model = Post
    #< app > / < model > < viewtype.
    template_name ='home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class UserPostListView(ListView):
        # indicate model went to query to view list
        model = Post
        # < app > / < model > < viewtype.
        template_name = 'user_post.html'
        context_object_name = 'posts'
        ordering = ['-date_posted']
        paginate_by = 2
        def get_queryset(self):
            user=get_object_or_404(User, username=self.kwargs.get('username'))
            return  Post.objects.filter(author=user ).order_by('-date_posted')

#post individual
class  PostDetailView(DetailView):
    #indicate model went to query to view list
    model = Post
    template_name = 'post_detail.html'

#creating views import CreatView
#share template
class PostCreatView(LoginRequiredMixin,  CreateView):
    # indicate model went to query to view list
    model = Post
    fields = ["title","content"]
    template_name = 'post_form.html'

    def form_valid (self,  form):
        form.instance.author=self.request.user

        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # indicate model went to query to view list
    model = Post
    fields = ["title","content"]
    template_name = 'post_form.html'

    def form_valid (self,  form):
        form.instance.author=self.request.user

        return super().form_valid(form)
#prevent other user updating other people post
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False



class  PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    #indicate model went to query to view list
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'

    # prevent other user updating other people post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    #return HttpResponse('<h1>About Blog</h1>')
    return render(request,'about.html',{'title':'blog-about'})