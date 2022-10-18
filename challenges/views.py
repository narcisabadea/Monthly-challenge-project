from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december': None
}


def index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


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
        return render(request, "challenges/challenge.html", {"text": text, "month": month})
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
