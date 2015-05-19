from django.conf.urls import patterns, include, url
from django.contrib import admin

from holywars import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),

    ## Django-allauth ##
    (r'^accounts/', include('allauth.urls')),

    url(r'^h/$', views.HolywarList.as_view(), name='holywars'),

    url(r'^new_holywar$', views.HolywarCreate.as_view(), name='new_holywar'),
    url(r'^h/(?P<pk>\d+)/$', views.HolywarDetail.as_view(), name='holywar_detail'),

    url(r'^h/(?P<holywar>\d+)/new_thread$', views.ThreadCreate.as_view(), name='new_thread'),
    url(r'^h/(?P<holywar>\d+)/(?P<pk>\d+)/$', views.ThreadDetail.as_view(), name='thread_detail'),

    url(r'^like_comment$', views.like_comment, name='like_comment'),
    url(r'^like_thread$', views.like_thread, name='like_thread'),
    url(r'^like_h$', views.like_holywar, name='like_holywar'),


    url(r'^my_profile$', views.my_profile, name='my_profile'),

    url(r'^$', views.homepage, name='homepage'),


)
