from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.core.mail import send_mail


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


send_mail(
    'Тема письма',
    'Текст письма.',
    'from@example.com',
    ['zlveresk@gmail.com'],
    fail_silently=False,
)
