from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views
from ExamPrep.albums.mixins import ReadonlyViewMixin
from ExamPrep.albums.models import Album
from ExamPrep.profiles.mixins import IsProfileMixin


class AlbumCreateView(IsProfileMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.owner_id = self.get_profile().pk
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field_name, field in form.fields.items():
            field.verbose_name = self.queryset.model._meta.get_field(field_name).verbose_name
            field.widget.attrs['placeholder'] = field.verbose_name
        return form


class AlbumDetailsView(IsProfileMixin, views.DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album-details.html"


class AlbumEditView(IsProfileMixin, views.UpdateView):
    queryset = Album.objects.all()
    template_name = "albums/album-edit.html"
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    success_url = reverse_lazy("index")


class AlbumDeleteView(IsProfileMixin, ReadonlyViewMixin, views.DeleteView):
    queryset = Album.objects.all()
    template_name = "albums/album-delete.html"
    success_url = reverse_lazy("index")

    form_class = modelform_factory(
        Album, fields=("name", "artist_name", "genre", "description", "image_url", "price")
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object

        return kwargs
