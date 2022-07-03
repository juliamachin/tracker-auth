from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.period import Period
from ..serializers.period import PeriodSerializer
from django.shortcuts import get_object_or_404

from api.models import period

class PeriodsView(APIView):
    def get(self, request):
        periods = Period.objects.all()
        data = PeriodSerializer(periods, many=True).data
        return Response(data)

    def post(self, request):
        period = PeriodSerializer(data=request.data)
        if period.is_valid():
            period.save()
            return Response(period.data, status=status.HTTP_201_CREATED)
        else:
            return Response(period.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PeriodView(APIView):
    def get(self, request, pk):
        period = get_object_or_404(Period, pk=pk)
        data = PeriodSerializer(period).data
        return Response(data)

    def delete(self, request, pk):
        period = get_object_or_404(Period, pk=pk)
        period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        period = get_object_or_404(Period, pk=pk)
        updated_period = PeriodSerializer(period, data=request.data)
        if updated_period.is_valid():
            updated_period.save()
            return Response(updated_period.data)
        else:
            return Response(updated_period.errors, status=status.HTTP_400_BAD_REQUEST) 