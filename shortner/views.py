from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import uuid
from .models import Url
from django.http import Http404
from .forms import ShortnerForm


def index(request):
    shortner_form = ShortnerForm
    if request.method == 'GET':
        return render(request, 'index.html', context={'form': shortner_form})
    shortner_form = ShortnerForm(request.POST or None)
    if request.method == 'POST' and shortner_form.is_valid():
        link = request.POST['link']
        uid = str(uuid.uuid4())[:8]
        Url.objects.create(url=link, uuid=uid)
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
