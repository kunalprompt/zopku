from django.conf.urls import patterns, include, url
# from django.contrib import admin

from views import *

urlpatterns = patterns('',
    url(r'^$', indexView),
    url(r'^read$', crudReadView),
    url(r'^api/search$', searchRecordsAPI),

    # read and delete
    url(r'^read$', crudReadView),
    url(r'^api/record/(?P<id>.*)$', crudReadDeleteAPI),
    # update and delete
    url(r'^create$', crudCreateRecordView),
    url(r'^api/create$', crudCreateUpdateAPI),
    url(r'^update$', crudUpdateRecordView),
)

urlpatterns += patterns('',
	url(
	    regex=r'^static/(?P<path>.*)$', 
	    view='django.views.static.serve', 
	    kwargs={'document_root': settings.STATIC_ROOT,}
	)
)
