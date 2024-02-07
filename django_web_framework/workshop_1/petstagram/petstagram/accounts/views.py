from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def details_profile(request, pk):
    context = {

    }

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')

