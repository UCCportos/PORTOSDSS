from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('data',views.data,name='data'),
	path('result',views.result,name='result'),

	path('instruct',views.instruct,name='instruct'),
	# path('news',views.news,name='news'),
	path('contact',views.contact,name='contact'),
]