from requests import get
from os import getenv
from dotenv import load_dotenv
from .models import Events, EventCountry
from django.utils import timezone

load_dotenv()


# prettier-ignore
def get_events(country):
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer" + getenv("event_key"),
    }
    response = get(
        "https://api.predicthq.com/v1/events/",
        headers={
            "Authorization": "Bearer " + getenv("event_key"),
            "Accept": "application/json",
        },
        params={"country": country},
    ).json()
    if len(response["results"]) >= 10:
        results = response["results"][:10]
    results = response["results"]
    for result in response["results"]:
        Events(
            event_id=result["id"],
            title=result["title"],
            category=result["category"],
            rank=result["rank"],
            lon=result["location"][1],
            lat=result["location"][0],
        ).save()
        event = Events.objects.filter(event_id=result["id"])[0]
        EventCountry(
            event_id=event, country=result["country"], created_at=timezone.now()
        ).save()
