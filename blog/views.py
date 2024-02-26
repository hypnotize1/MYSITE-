from django.http import HttpResponse, HttpResponseRedirect
from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.urls import reverse
import sweetify

# Create your views here.
def blog_view(request,**kwargs):
    now = timezone.now()
    posts = post.objects.filter(status = 1, published_date__lte = now)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        posts = paginator.page(1)        

    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)






def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Submitted successfully!')
        else:
            sweetify.error(request, 'Submission failed!')
    else:
        form = CommentForm()

    now = timezone.now()
    all_posts = post.objects.filter(status=1, published_date__lte=now)
    current_index = 0

    for index, p in enumerate(all_posts):
        if p.id == pid:
            current_index = index
            break

    previous_post = all_posts[current_index - 1] if (current_index - 1) >= 0 else None
    next_post = all_posts[current_index + 1] if (current_index + 1) < len(all_posts) else None

    current_post = get_object_or_404(all_posts, pk = pid)
    current_post.counted_views += 1
    current_post.save()

    if not current_post.login_require:
        comments = Comment.objects.filter(Post = current_post.id, approved = True)
        context = {'Post': current_post, 'pp': previous_post, 'np': next_post, 'comments': comments, 'form': form}
        return render(request, 'blog/blog-single.html', context)
    
    else:
        if request.user.is_authenticated:
            comments = Comment.objects.filter(Post = current_post.id, approved = True)
            context = {'Post': current_post, 'pp': previous_post, 'np': next_post, 'comments': comments, 'form': form}
            return render(request, 'blog/blog-single.html', context)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))




def blog_category(request, cat_name):
    posts = post.objects.filter(status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)



def blog_search(request):
    now = timezone.now() 
    posts = post.objects.filter(status = 1, published_date__lte = now)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)
