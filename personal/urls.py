from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^contact/', views.contact, name='contact'),
    url(r'^read_page1/',views.read_page1, name='read_page1'),
    url(r'^read_page2/',views.read_page2, name='read_page2'),
    url(r'^read_page3/',views.read_page3, name='read_page3'),
    url(r'^read_page4/',views.read_page4, name='read_page4'),
    url(r'^read_page5/',views.read_page5, name='read_page5'),
    url(r'^read_page6/',views.read_page6, name='read_page6'),

]
