from django.views import generic as views

from World_Of_Speed_App.profiles.mixins import GetProfileMixin


class IndexView(GetProfileMixin, views.TemplateView):
    template_name = "common/index.html"



