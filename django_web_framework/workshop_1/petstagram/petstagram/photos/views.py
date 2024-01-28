from django.shortcuts import render


# Create your views here.
def add_photos(request):
    return render(request, 'photos/photo-add-page.html')


def details_photos(request, pk):
    return render(request, 'photos/photo-details-page.html')


def edit_photos(request, pk):
    return render(request, 'photos/photo-edit-page.html')
