from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from website.models import Contact
from django.contrib import messages
import sweetify
from website.forms import name_form, contact_form, newsletter_form



def index_view(request):
    return render(request, 'web/index.html')


def about_view(request):
    return render(request, 'web/about.html')


def contact_view(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['name'] = 'unknown'
        form = contact_form(post_data)
        if form.is_valid():
            form.save()
            sweetify.success(request,'submited successfully!')
            return HttpResponseRedirect('/')
        else:
            sweetify.error(request, 'submit failed!')
            return HttpResponseRedirect('/')
    else:
        form = contact_form()
    return render(request, 'web/contact.html', {'form' : form})


def test_f(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid!')

    form = contact_form()
    return render(request, 'test.html', {'form' : form})



def newsletter_view(request):
    if request.method == 'POST':
        form = newsletter_form(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request,'submited successfully!')
            return HttpResponseRedirect('/')
        else:
            sweetify.error(request, 'submit failed!')
            return HttpResponseRedirect('/')


    if request.method == 'GET':
        return HttpResponseRedirect('/')