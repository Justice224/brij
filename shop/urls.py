from django.conf import settings
from django.conf.urls import url
from shop import views
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^search/$', views.search, name='search'),

]
