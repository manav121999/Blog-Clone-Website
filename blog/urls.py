from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/',views.PostCreateView.as_view(),name='post_new'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<str:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/<str:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<str:pk>/remove/',views.PostDeleteView.as_view(),name='post_remove'),
    path('draft/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<str:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<str:pk>/approve/',views.comment_approved,name='comment_approve'),
    path('comment/<str:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<str:pk>/publish/',views.post_publish,name='post_publish'),
]


