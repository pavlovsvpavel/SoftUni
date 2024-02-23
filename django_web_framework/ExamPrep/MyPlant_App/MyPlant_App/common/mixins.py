from MyPlant_App.profiles.models import Profile


class CheckForProfileMixin:

    @staticmethod
    def get_profile():
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.get_profile()

        if profile:
            context["profile"] = True

        else:
            context["profile"] = False

        return context
