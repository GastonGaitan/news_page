from django.shortcuts import render
from .models import News
import html
from .forms import NewForm
from django.http import HttpResponseRedirect
from .my_functions import new_day_call_api
from .api import import_data_from_api

# Create your views here.
def index(request):
    """
    The index function is the main function of this app. It takes a request from
    the user and returns an HTML page with all the news articles that are in our
    database. If there is no news article in our database, it will call the API to
    get new data and then return an HTML page with all those new articles.
    
    :param request: Get the request from the user
    :return: The index
    :doc-author: Trelent
    """
    # Video that I used to create this part:
    # https://www.youtube.com/watch?v=AGtae4L5BbI&t=861s&ab_channel=Codemy.com
    if request.method == "POST":
        searched = request.POST['searched']
        news = News.objects.filter(title__contains = searched)
    else:
        if new_day_call_api():
            import_data_from_api()
        news = News.objects.all()
    for new in news:
        new.description = html.unescape(new.description)
    context = {'news': news}
    return render(request, 'index.html', context)

def add_news(request):
    """
    The add_news function is used to add a new news item to the database.
    The function first checks if the request method is POST, and if it is, 
    it validates the form data and saves it in the database. If not, then 
    the function creates an empty form object for use in rendering on a page.
    
    :param request: Get the request object sent by the user
    :return: The rendered add_new
    :doc-author: Trelent
    """
    submitted = False
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_new?submitted=True')
    else:
        form = NewForm() 
        if 'submitted' in request.GET:
            submitted = True
    context = {'form':form, 'submitted':submitted} 
    return render(request, 'add_new.html', context)
