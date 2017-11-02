from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from shop import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^shop/', include('shop.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register.html/$', views.RangoRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)