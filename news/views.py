from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def news_of_day(request):
    date = dt.date.today()
    news = Article.today_news()
    return render(request, 'all-news/today-news.html', {'date':date,'news':news})


# view function to present news from past days
def past_days_news(request, past_date):

    try:
        # converts data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
      return redirect(news_of_day)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {'date':date,'news':news})
