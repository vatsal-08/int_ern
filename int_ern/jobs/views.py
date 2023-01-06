from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job
from .forms import CreationForm
class JobListView(LoginRequiredMixin,ListView):
    model = Job
    template_name='jobs/job_list.html'
    login_url = '/accounts/login/'
    context_object_name='jobs'

class JobCreateView(LoginRequiredMixin,CreateView):
    model = Job
    template_name = 'jobs/job_create.html' 
    login_url = '/accounts/login/' 
    form_class=CreationForm
    success_url = reverse_lazy('home')

class JobDetailView(DetailView):
    model = Job
    template_name='jobs/job_detail.html' 
    context_object_name='jobs'

class JobUpdateView(LoginRequiredMixin,UpdateView):
    model = Job
    template_name='jobs/job_update.html' 
    fields=['title','desc','location','contact']

class JobDeleteView(LoginRequiredMixin,DeleteView):
    model = Job 
    template_name='jobs/job_delete.html'
    context_object_name='jobs'
    success_url = reverse_lazy('home')