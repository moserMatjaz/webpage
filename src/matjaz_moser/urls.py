from django.conf.urls import include, url
from django.contrib import admin
from recipes.views import home
from django.conf import settings
# static:
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'matjaz_moser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name = "home"),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)