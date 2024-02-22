class FormFieldDisableViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["disabled"] = True

        for field_name, field in form.fields.items():
            field.required = False

        return form


class RenameLabelsNamesInFormsMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["name"].label = "Name"
        form.fields["image_url"].label = "Image URL"
        form.fields["description"].label = "Description"
        # form.fields["nutrition"].label = "Nutrition"

        return form
