from ExamPrep.profiles.models import Profile


class IsProfileMixin:

    @staticmethod
    def get_profile():
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        is_profile = self.get_profile()

        if is_profile is None:
            context['profile'] = False
        else:
            context['profile'] = True

        return context
