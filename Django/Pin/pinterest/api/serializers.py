from rest_framework import serializers
from .models import Pin


class TitlePinSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Pin
        fields = ['title', 'img_url']



class PinSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    

    class Meta:
        model = Pin
        fields = '__all__'

   
    def get_img_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        else:
            return None
    




{
    "image": "http://127.0.0.1:8000/media/uploads/image.png",
    "title": "Hello again",
    "author": 2
}

{

    "image": "http://127.0.0.1:8000/media/madia/uploads/banner.jpg",
    "title": "Hello",
    "author": 1
}