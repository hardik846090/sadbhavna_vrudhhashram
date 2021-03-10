from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),

    path('about', views.about, name='about'),
    path('cause', views.cause, name='cause'),
    path('cause_single', views.cause_single, name='cause_single'),
    path('event', views.event, name='event'),
    path('event_single', views.event_single, name='event_single'),
    path('donate', views.donate, name='donate'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('error', views.error, name='error'),

    path('blog', views.blog, name='blog'),
    path('blog_left', views.blog_left, name='blog_left'),
    path('blog_fulwidth/<str:foo>/', views.blog_fulwidth, name='blog_fulwidth'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('blog_single_left', views.blog_single_left, name='blog_single_left'),
    path('blog_single_fluid', views.blog_single_fluid, name='blog_single_fluid'),
    path('contact', views.contact, name='contact'),
]
