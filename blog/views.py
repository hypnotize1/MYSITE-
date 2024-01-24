from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    now = timezone.now()
    posts = post.objects.filter(status = 1, published_date__lte = now)
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
    
