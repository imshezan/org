from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('career/', views.career, name='Career'),
    path('contact-us/', views.contact_us, name='Contact-Us'),
    path('donate/', views.donate, name='Donate'),
    path('index/', views.index, name='Index'),
    path('press/', views.post_list, name='Press'),
    path('post/<pk>/', views.view_post, name='post'),
    path('gallery/', views.gallery_view, name='Gallery'),
    path('img/<img_id>/', views.view_pic, name='img'),
    path('Resources/', views.resources, name='Resources'),
    path('thankyou/', views.thankyou, name='Thankyou'),
    path('what-we-do/', views.what_we_do, name='what-we-do'),
    path('where-we-work/', views.where_we_work, name='where-we-work'),
    path('who-we-are/', views.who_we_are, name='who-we-aer'),
    path('slider/', views.slider, name='slider'),



    #

    # log in log out
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
