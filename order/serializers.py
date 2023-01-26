from rest_framework import serializers
from .models import Order, Comment

class OrderListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    
    member = serializers.HiddenField(default=serializers.CurrentUserDefault(), required=False)  
    created = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')  
    writer = serializers.SerializerMethodField()
    # editable = serializers.SerializerMethodField()
    
    def get_writer(self, obj):
        # print('obj >> ', obj.member.username)
        return obj.member.username
    
    # def get_editable(self, obj):
    #     if (obj.member.username == self.context.get('request').user.username):
    #         return True
    #     else:
    #         return False    
    
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
        