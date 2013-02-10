from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('accounts.views',
    url(r'^accounts/$', 'account_list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', 'account_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
