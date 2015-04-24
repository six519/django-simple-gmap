from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'simple_gmap_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'simple_gmap_project.view.test_page', name='test_page'),
    url(r'^admin/', include(admin.site.urls)),
]
