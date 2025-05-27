from rest_framework import serializers
from .models import Banner, Notice, Collection, Area

from libs.baidu_ai import BaiDuFace
from rest_framework.exceptions import APIException


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


### 采集序列化类
class CollectionSerializer(serializers.ModelSerializer):  # 查询所有序列化类
    class Meta:
        model = Collection
        fields = ['id', 'name', 'avatar', 'area']
        depth = 1  # area 外键关联详情拿到


class CollectionSaveSerializer(serializers.ModelSerializer):  # 信泽序列化类
    class Meta:
        model = Collection
        fields = ['name', 'avatar', 'area']

    def create(self, validated_data):
        # 完成保存
        # 把图片保存到自己本地了---》把图片同时传到百度人脸库--》保存
        # 上传到百度人脸库--》再保存到本地--》返回前端，才算真正的采集完成
        ai = BaiDuFace()
        # 1 取出前端传入的人脸图片
        file_obj = validated_data.get('avatar')
        # 2 取出前端传入的人名
        name = validated_data.get('name')
        # 3 把人名转拼音
        name_pinyin = ai.name_to_pinyin(name)
        # 4 上传到百度人脸库
        res = ai.add_user(file_obj, name_pinyin)
        # 5 上传成功--》取出faceToken--》存到咱们自己表中
        if res.get('error_code') == 0:
            validated_data['face_token'] = res.get('result').get('face_token')
            validated_data['name_pinyin'] = name_pinyin
            # 6 真正保存到数据库：
            instance = super().create(validated_data)
            return instance
        else:
            raise APIException('采集信息失败')


### 网格序列化类
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'desc']


class StatisticsListSerializer(serializers.Serializer):
    date=serializers.DateTimeField(format='%Y年%m月%d日')
    count = serializers.IntegerField()




