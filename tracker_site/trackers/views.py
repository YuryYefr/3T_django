from django.shortcuts import render
from .models import Tracker
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    context = {
        'trackers': Tracker.objects.all()
    }
    return render(request, 'trackers/home.html', context)


class TrackerList(ListView):
    model = Tracker
    template_name = 'trackers/home.html'
    context_object_name = 'trackers'
    ordering = ['-date_created']


class TrackerDetail(DetailView):
    model = Tracker


class TrackerCreate(CreateView):
    model = Tracker
    fields = ['tracker_name', 'content']

    def create_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TrackerUpdate(UpdateView, LoginRequiredMixin):
    model = Tracker
    fields = ['tracker_name', 'content']

    def create_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'trackers/about.html', {'title': 'About'})
