from django.conf.urls import url, include
from . import views
app_name = 'notes'

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /search/
    url(r'^search/$', views.search, name='search'),
    # /notes/<pk>/
    url(r'^notes/(?P<pk>[0-9]+)/$', views.detail, name='note-detail'),
     # /notes/<pk>/favorite/
    url(r'^notes/(?P<pk>[0-9]+)/favorite/$', views.favorite, name='note-favorite'),
    # /notes/add/
    url(r'^notes/add/$', views.NoteCreate.as_view(), name='note-add'),
     # /notes/<pk>/update/
    url(r'^notes/(?P<pk>[0-9]+)/update/$', views.NoteUpdate.as_view(), name='note-update'),
     # /notes/<pk>/delete/
    url(r'^notes/(?P<pk>[0-9]+)/delete/$', views.NoteDelete.as_view(), name='note-delete'),

]
