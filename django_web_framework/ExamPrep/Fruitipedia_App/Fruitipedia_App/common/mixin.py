class HideLabelsInFormsMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.label = False

        return form


class ShowPlaceholdersInFormsMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field_name, field in form.fields.items():
            verbose_name = self.queryset.model._meta.get_field(field_name).verbose_name
            field.widget.attrs['placeholder'] = verbose_name

        return form


