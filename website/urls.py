from django.conf.urls import url

from django.conf.urls.static import static

from .import views

urlpatterns = [
    url(r'^$', 'website.views.home', name='home'),
    url(r'^home/$', 'website.views.home', name='home'),
    url(r'^register/$', 'website.views.register', name='register'),
    url(r'^login/$', 'website.views.login', name='login'),
    url(r'^aboutus/$', 'website.views.aboutus', name='aboutus'),
    url(r'^contactus/$', 'website.views.contactus', name='contactus'),
    url(r'^graduation/$', 'website.views.graduation', name='graduation'),
    url(r'^technical/$', 'website.views.technical', name='technical'),
    url(r'^business/$', 'website.views.business', name='business'),
    url(r'^arts/$', 'website.views.arts', name='arts'),
    url(r'^postgraduation/$', 'website.views.postgraduation', name='postgraduation'),
]
