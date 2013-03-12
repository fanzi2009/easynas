from rest_framework import serializers
from easynas.models import ZPool

class ZPoolSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    id = serializers.Field()
    class Meta:
        model = ZPool
        fields = ('id','volume_name', 'disks')
