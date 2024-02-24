from django.db.models import Sum
from World_Of_Speed_App.cars.models import Car


class FormFieldDisableViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = True

        form.fields["type"].widget.attrs["disabled"] = True
        form.fields["type"].required = False

        return form


class CarsTotalPriceMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cars_total_price"] = Car.objects.aggregate(total=Sum("price"))["total"]

        return context
