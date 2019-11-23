from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class BlockedIPSMiddleware(MiddlewareMixin):
    """中间类"""

    exclude_ips = ['127.0.0.2']

    @staticmethod
    def process_view(request, view_func, *view_args, **view_kwargs):
        # 获取浏览器端ip
        user_ip = request.META["REMOTE_ADDR"]

        # 判断ip是否合法
        if user_ip in BlockedIPSMiddleware.exclude_ips:
            return HttpResponse("<h1>Forbidden</h1>")