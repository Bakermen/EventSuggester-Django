from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .utils import *
from .models import Events, EventCountry
from .serializers import EventsSeriailzer


@api_view(["GET"])
def listEvents(request):
    # country = request.GET.get("country")
    country = "US"
    event_country_records = EventCountry.objects.filter(country=country).all()
    if len(event_country_records) == 0:
        get_events(country)
    if timezone.now() - event_country_records[0].created_at > timedelta(seconds=3600):
        get_events(country)
        event_country_records = EventCountry.objects.filter(country=country).all()
    events = []
    for event in event_country_records:
        events.append(Events.objects.filter(id=event.event_id)[0])

    for i in range(len(events)):
        for j in range(len(events) - 1):
            if int(events[j].rank) > int(events[j + 1].rank):
                events[j], events[j + 1] = events[j + 1], events[j]

    serializer = EventsSeriailzer(events, many=True)

    return JsonResponse(data=serializer.data, safe=False)


@api_view(["GET"])
def weather(request):
    pass


@api_view(["GET"])
def flights(request):
    pass
