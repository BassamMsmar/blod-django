from django import template
from blog.models import Comment

register  = template.Library()

@register.inclusion_tag('blog/latest_comments.html')
def latest_comment():
    context = {
        'l_comment': Comment.objects.filter(active=True)[0:5] 
    }

    return context