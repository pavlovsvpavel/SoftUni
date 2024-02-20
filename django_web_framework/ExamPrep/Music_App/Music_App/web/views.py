from django.shortcuts import redirect, render
from django.views import generic as views
from Music_App.web.forms import ProfileCreateForm
from Music_App.albums.models import Album
from Music_App.profiles.mixins import IsProfileMixin


class IndexView(IsProfileMixin, views.TemplateView):

    def get_template_names(self):
        if self.get_profile() is None:
            return ["web/home-no-profile.html"]

        return ["web/home-with-profile.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = ProfileCreateForm
        context["albums"] = Album.objects.all()

        return context

    @staticmethod
    def post(request, *args, **kwargs):
        form = ProfileCreateForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect("index")

        return render(request, 'web/home-no-profile.html', {'form': form})
