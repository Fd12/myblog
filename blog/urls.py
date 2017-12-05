from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^more/', include('posts.urls', namespace="more")),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^googly/', include('googly.urls', namespace="googly")),
    url(r'^api/', include('api.urls', namespace="api")),
    

]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)