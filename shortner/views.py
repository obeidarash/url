from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import Http404
from .forms import ShortnerForm


def index(request):
    shortner_form = ShortnerForm
    if request.method == 'GET':
        return render(request, 'index.html', context={'form': shortner_form})
    shortner_form = ShortnerForm(request.POST or None)
    if request.method == 'POST':
        if shortner_form.is_valid():
            link = shortner_form.cleaned_data['link']
            uid = str(uuid.uuid4())[:8],
            ip = get_client_ip(request)
            Url.objects.create(url=link, uuid=uid, ip=ip)
            shortner_form = ShortnerForm
            context = {
                'url': uid,
                'form': shortner_form
            }
            return render(request, 'index.html', context)
    return redirect('home')


def go(request, pk):
    url = Url.objects.filter(uuid=pk).first()
    if url is None:
        raise Http404('not ok')
    return redirect(url.url)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
