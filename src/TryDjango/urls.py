"""TryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
# settings:
from django.conf import settings
# views:
from newsletter.views import home
from newsletter.views import signUpForm
from newsletter.views import contact
from newsletter.views import about
from newsletter.views import thankYouNewsletter
from newsletter.views import recipesVisualisation 
# static files:
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name = "home"),
    url(r'^signUp/', signUpForm, name = "signUp"),
    url(r'^contact/', contact, name = "contact"),
    url(r'^aboutUs/', about, name = "aboutUs"),
    url(r'^thankYou/', thankYouNewsletter, name = "thankYou"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^msiasu/', recipesVisualisation, name = "msiasu"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
