from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators
class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')

    #email=serializers.EmailField(write_only=True)
    title=serializers.CharField(validators=[validators.validate_title_no_hello,validators.validate_title])
    class Meta:
        model=Product
        fields=[
            'user',
            'url',
            'edit_url',
            #'email',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    
    # def validate_title(self,value):
    #     qs=Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value
    
    
    # def create(self,validated_data):
    #     #email=validated_data.pop('email')
    #     obj=super().create(validated_data)
    #     #print(email,obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     instance.title=validated_data.get('title')
    #     return instance

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)

    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        return obj.get_discount()