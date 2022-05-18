from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.


class Home(ListView):
    model = models.Post
    template_name = 'preview_post.html'


class UpdatePostView(UpdateView):
    model = models.Post
    form_class = forms.UpdateForms
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
