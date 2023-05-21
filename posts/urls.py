from django.urls import path
from posts.views import *

urlpatterns = [
    #path('', hello_world, name = 'hello_world'),
    # path('<int:id>/', post_detail),
    # path('new/', create_post, name = 'create_post'),
    # path('', get_post_all, name="get_post_all"),
    # path('comment/<int:post_id>/', get_comment, name = "get_comment"),
    path('',PostList.as_view()),
    path('<int:id>/',PostDetail.as_view()),
]