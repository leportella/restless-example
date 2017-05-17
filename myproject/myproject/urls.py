from django.conf.urls import include, url
from django.contrib import admin

from livraria.views import LivrosView
from livraria.api import LivrosResource

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^livraria-views/', LivrosView),
    url(r'^livraria-api/', include(LivrosResource.urls())),
]
