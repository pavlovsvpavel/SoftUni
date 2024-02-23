from django.views import generic as views
from MyPlant_App.plants.models import Plant
from MyPlant_App.common.mixins import CheckForProfileMixin


class IndexView(CheckForProfileMixin, views.TemplateView):
    template_name = 'common/home-page.html'


class CatalogueView(CheckForProfileMixin, views.TemplateView):
    template_name = "common/catalogue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["plants"] = Plant.objects.all()

        return context
