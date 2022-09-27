from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

challenges = {
    'january': 'Try a New Workout At Home',
    'february': 'Make One New Connection a Week',
    'march': 'Read a Chapter of a Book a Day',
    'april': 'Meal Prep Your Lunch',
    'may': 'Walk 45 min per day',
    'june': 'Cook a New Recipe a Week',
    'july': 'Take a photo of something that makes you happy every day',
    'august': 'Swap soda for sparkling water',
    'september': 'Create and stick to a budget',
    'octomber': 'Keep your house tidier',
    'november': 'Keep a journal',
    'december': 'Random act of kindness',
}


def index(requst):
    list_items = ''
    months = list(challenges.keys())

    for month in months:
        forward_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{forward_path}">{month.capitalize()}</a></li>'
    return HttpResponse(list_items)


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Month not supported')
    forward_month = months[month - 1]
    forward_path = reverse('month-challenge', args=[forward_month])
    return HttpResponseRedirect(forward_path)


def monthly_challenge(request, month):
    try:
        text = challenges[month]
        response_data = f"<h1>The challenge for {month} is: {text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('Month not supported')
