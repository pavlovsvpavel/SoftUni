from django.views import generic as views

from Fruitipedia_App.fruits.models import Fruit
from Fruitipedia_App.profiles.mixin import CheckForProfileMixin


class IndexView(CheckForProfileMixin, views.TemplateView):
    template_name = "common/index.html"


class DashboardView(CheckForProfileMixin, views.TemplateView):
    template_name = "common/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["fruits"] = Fruit.objects.all()

        return context
