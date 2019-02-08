from django.conf.urls import url
from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('query-1', views.ActorListView, 'query-1')
router.register('query-2', views.Query2View, 'query-2')
router.register('query-3', views.Query3View, 'query-3')
router.register('query-4', views.Query4View, 'query-4')
router.register('query-5', views.Query5View, 'query-5')
router.register('query-6', views.Query6View, 'query-6')
router.register('query-8', views.CountLastNameListView, 'query-8')
router.register('query-9', views.Query9View, 'query-9')
router.register('query-10', views.Query10View, 'query-10')
router.register('query-11', views.Query11View, 'query-11')
router.register('query-12', views.Query12View, 'query-12')
router.register('query-13', views.Query13View, 'query-13')
router.register('query-14', views.Query14View, 'query-14')
router.register('query-15', views.Query15View, 'query-15')
router.register('query-16', views.Query16View, 'query-16')
router.register('query-17', views.Query17View, 'query-17')
router.register('query-18', views.Query18View, 'query-18')
router.register('query-19', views.Query19View, 'query-19')

urlpatterns = [
   path('', include(router.urls))
]



