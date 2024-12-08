from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("This website is for sale, please contact vulpeanuadrian1994@gmail.com!")