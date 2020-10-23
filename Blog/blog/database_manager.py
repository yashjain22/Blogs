from django.db import connection
from .models import Post
from django.contrib.auth.models import User
from .models import Post


def fetch_all_posts(order):
    query = ''' SELECT blog_post.id, title,body,title_tag, created_on, updated_on, username 
                                    FROM blog_post 
                                    INNER JOIN auth_user 
                                    ON auth_user.id = blog_post.author_id
                                    ORDER BY blog_post.created_on {}'''.format(order)
    return Post.objects.raw(query,[order])

def fetch_post_by_id(postid):
    query = ''' SELECT blog_post.id, title, body, title_tag, created_on, updated_on, 
                    blog_post.author_id, username, email
                    FROM blog_post 
                    INNER JOIN auth_user 
                    ON auth_user.id = blog_post.author_id
                    where blog_post.id = {}
                '''.format(postid)
    return Post.objects.raw(query,[postid])