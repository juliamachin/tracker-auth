from rest_framework import serializers
from ..models.period import Period

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'mestruation', 'start_date', 'end_date', 'cycle_length')
