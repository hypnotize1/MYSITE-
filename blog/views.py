from unicodedata import category
from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def blog_view(request,**kwargs):
    now = timezone.now()
    posts = post.objects.filter(status = 1, published_date__lte = now)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    print(posts)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        posts = paginator.page(1)        

    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    now = timezone.now()
    all_posts = post.objects.filter(status = 1, published_date__lte = now)
    current_index = 0  
    for index , p in enumerate(all_posts):
        if p.id == pid:
            current_index = index
            break
    previous_post = all_posts[current_index - 1] if (current_index - 1) >= 0 else None
    next_post = all_posts[current_index + 1] if (current_index + 1) < len(all_posts) else None
    current_post = get_object_or_404(all_posts, pk = pid)
    current_post.counted_views += 1
    current_post.save()
    context = {'Post': current_post,
               'pp' : previous_post,
               'np' : next_post,
              }
    return render(request, 'blog/blog-single.html', context)
    

def test(request):
    return render(request, 'test.html')


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
