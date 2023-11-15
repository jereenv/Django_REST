from rest_framework import serializers

from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    selling_price = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'selling_price'
        ]
    
    def get_selling_price(self, obj):
        return obj.price * 2