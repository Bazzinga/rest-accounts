from django.conf.urls import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns

from accounts import views


urlpatterns = patterns('',
    url(r'^accounts/$', views.AccountList.as_view()),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view()),
    url(r'^hotels/$', views.HotelList.as_view()),
    url(r'^hotels/(?P<pk>[0-9]+)/$', views.HotelInstance.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

urlpatterns = format_suffix_patterns(urlpatterns)
