from django.views.generic import TemplateView
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('index.html')
        return super().dispatch(request, *args, **kwargs)