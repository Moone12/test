from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BannerView,CollectionView,AreaView,StatisticsView,FaceView,VoiceView

router = SimpleRouter()
router.register('banner', BannerView, 'banner')
router.register('collection', CollectionView, 'collection')
router.register('area', AreaView, 'area')
router.register('statistics', StatisticsView, 'statistics')
router.register('face', FaceView, 'face')
router.register('voice', VoiceView, 'voice')

from .views import welcome

urlpatterns = [
    # http://192.168.74.1:8000/smart/welcome/-->>就能获得图片数据
    path('welcome/', welcome),
]
urlpatterns += router.urls
