from rest_framework import serializers

from assignment.models import Company


class CompanyInfoList(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyInfoRequestSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    city = serializers.CharField(required=True, allow_null=False, allow_blank=False)

