from django.shortcuts import render

# Create your views here.
from django.utils import http
from django.views import View


class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        注册页面展示
        :param request: 请求对象
        :return: 注册页面
        """
        return render(request, 'register.html')

    def post(self, request):
        """
        用户注册方法实现
        :param request: 请求对象
        :return: 注册结果
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')
        print(username)
        if not all([username, password, password2, mobile, allow]):
            return http.HttpResponseForbidden('缺少必要参数')
