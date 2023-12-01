from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView,FormView
from django.urls import reverse_lazy
from .forms import NewsPostForm,ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.

class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('contact')

    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)

        message=\
            '送信者名:{0}\n メールアドレス:{1}\n タイトル:{2}\n メッセージ:{3}' \
            .format(name,email,title,message)
        
        from_email='oohara.pretest@gmail.com'
        to_list=['oohara.pretest@gmail.com']
        message=EmailMessage(subject=subject,
                            body=message,
                            from_email=from_email,
                            to=to_list,)
        message.send()
        messages.success(
            self.request,'お問い合わせは正常に送信されました。'
        )
        return super().form_valid(form)
    