from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import Http404
from .forms import ShortenerForm


# render home page
def index(request):
    shortener_form = ShortenerForm
    # render home page
    if request.method == 'GET':
        return render(request, 'index.html', context={'form': shortener_form})
    # submit Shortener link form in home page
    shortener_form = ShortenerForm(request.POST or None)
    if request.method == 'POST':
        if shortener_form.is_valid():
            link = shortener_form.cleaned_data['link']
            uid = str(uuid.uuid4())[:8]
            ip = get_client_ip(request)
            Url.objects.create(url=link, uuid=uid, ip=ip)
            shortener_form = ShortenerForm
            context = {
                'url': uid,
                'form': shortener_form
            }
            return render(request, 'index.html', context)
    return redirect('home')


# fetch short url in database
def go(request, pk):
    url = Url.objects.filter(uuid=pk).first()
    if url is None:
        raise Http404('not ok')
    return redirect(url.url)


# get user ip address
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
