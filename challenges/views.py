from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


monthly_challenges = {
    'January': 'Change your Diet!',
    'February': 'Start Exercising!',
    'March': 'Learn Django!',
    'April': 'learn rest framework!',
    'May': 'build websites apps!',
    'June': 'Do coursera challenges!',
    'July': 'learn python APIs!',
    'August': 'Do opensourse!',
    'September': 'Do data analytics work!',
    'October': 'start freelance earning!',
    'November': 'start saving!',
    'December': None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        'months': months
    })


def month_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid Month!</h1>')

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def month_challenges(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month_name': month
        })
    except:
        raise Http404()
