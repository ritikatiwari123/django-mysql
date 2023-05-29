from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from assignment.models import Company
from assignment.serializer import CompanyInfoList, CompanyInfoRequestSerializer


# Create your views here.

class CompanyInfoView(APIView):

    def get(self, request):
        try:
            return Response(CompanyInfoList(Company.objects.all(), many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = CompanyInfoRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer_date = serializer.data
            company_obj = Company.objects.create(name=serializer_date['name'], city=serializer_date['city'])
            return Response(CompanyInfoList(company_obj).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)

