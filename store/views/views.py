# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
class ContactView(View):
    template_name = 'contact.html'
    def get(self, request):
        return render(request, self.template_name)
    @login_required(login_url='login')  # ログインが必要な場合、'login' は実際のログインURLに変更してください
    def post(self, request):
       # POSTデータを取得
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # ログインユーザー情報
        user = request.user
        user_id = user.id if user else None
        # ここでメールの送信やデータベースへの保存などの処理を行う
        return HttpResponse('Your message has been sent successfully!')