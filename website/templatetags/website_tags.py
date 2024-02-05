from django import template 
from blog.models import post


register = template.Library()

@register.inclusion_tag('web/latest-blog.html')
def latest_blog():
    posts = post.objects.filter(status = 1)[:6]
    return {'posts' : posts}
