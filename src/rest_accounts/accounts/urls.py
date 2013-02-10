from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from accounts import views


urlpatterns = patterns('',
    url(r'^accounts/$', views.AccountList.as_view()),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
