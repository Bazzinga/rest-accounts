from django.conf.urls import patterns, url


urlpatterns = patterns('accounts.views',
    url(r'^accounts/$', 'account_list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', 'account_detail'),
)
