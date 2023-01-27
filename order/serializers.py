from rest_framework import serializers
from .models import Order, Comment, Like

class OrderListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Order
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    
    member = serializers.HiddenField(default=serializers.CurrentUserDefault(), required=False)  
    created = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')  
    writer = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        # print('obj >> ', obj.member.username)
        return obj.member.username
    
    def validate_member(self, value):
        print('value >> ', value)
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required.')
        return value
    
    def validate(self, data):
        for key, value in data.items():
            print(f'key: {key}, value: {value}')
        return data    
    class Meta:
        model = Comment
        fields = '__all__'
        
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'
        extra_kwargs = {
            'created': {
                'required': False,
                'read_only': True,
                'format': '%Y-%m-%d %H:%M:%S',
            }
        }
        