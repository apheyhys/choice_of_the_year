from rest_framework import serializers
from .models import Year
import datetime
import time

# текущая дата
now = datetime.datetime.now()


class YearCreateSerializer(serializers.ModelSerializer):
    def validate(self, data):
        time.sleep(3)  # таймаут для демонтрации работы формы
        if data['year'] == 2018:
            raise serializers.ValidationError("Год не должен быть равен 2018")
        elif data['year'] > now.year and data['checkbox'] is False:
            raise serializers.ValidationError("Введенный год не больше текущего")
        return data

    class Meta:
        model = Year
        fields = [
            "year",
            "checkbox"
        ]
