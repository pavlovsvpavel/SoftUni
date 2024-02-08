from django import forms
from petstagram.photos.models import PetPhoto


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'

        labels = {
            "photo": "Photo file",
            "pets": "Tag Pets"
        }


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta(PhotoBaseForm.Meta):
        exclude = ["photo"]
