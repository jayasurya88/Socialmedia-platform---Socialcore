from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('user_registration',views.user_registration,name="user_registration"),
    path('login_page',views.login_page,name="login_page"),
    path('register/', views.register, name='register'),
    path('verify_otp',views.verify_otp,name="verify_otp"),
    path('login_view',views.login_view,name="login_view"),
    path('admin',views.admin,name="admin"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('verify_reset_otp/', views.verify_reset_otp, name='verify_reset_otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('user/<str:username>/posts/', views.user_posts, name='user_posts'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('my_profile/<str:username>/', views.my_profile_view, name='my_profile_view'),
    path('search/', views.user_search, name='user_search'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('notifications/',views. notifications, name='notifications'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('send-friend-request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept-friend-request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject-friend-request/<int:request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('friend-requests/', views.friend_requests_list, name='friend_requests'),
    path('profile/<str:username>/friends/', views.friends_list, name='friends_list'),
    path('settings/privacy/', views.privacy_settings, name='privacy_settings'),
    path('reply/<int:comment_id>/', views.add_reply, name='add_reply'),
     path('conversations/', views.conversation_list, name='conversation_list'),
    
    path('conversations/start/<int:user_id>/', views.start_conversation, name='start_conversation'),
    path('send-message/<int:recipient_id>/', views.send_message, name='send_message'),
    # pattern for conversation details
    path('conversations/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
]