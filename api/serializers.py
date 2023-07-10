from rest_framework.serializers import ModelSerializer
from .models import Events, Weather, Flights


class EventsSeriailzer(ModelSerializer):
    class Meta:
        model = Events
        fields = ["title", "rank", "category"]
