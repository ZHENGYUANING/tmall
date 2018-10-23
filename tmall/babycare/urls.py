from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.product_list, name='product_list'), 
	# url(r'^show_list/$', views.showlist),
    url(r'^show_list/(?P<page>\d+)/$',views.showlist,name='show_list'),
	url(r'^get/$',views.get_list),
	url(r'^find/$',views.find_list),
	url(r'^login/$',views.my_login),
]


