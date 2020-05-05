from django.shortcuts import render, HttpResponse
from data.models import ApiView
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ApiViewSerializer
from .filters import ApiViewFilters
from rest_framework import filters
from rest_framework import generics


@api_view(['GET', 'POST'])
def index(request):
    """
    Retrieving data from api using GET method and storing it into local DB using POST method:

        parameter:
            url = Retrieving data using get method

        returns:
            Stores all the data from Api,and result HttpResponse as "created".
    """
    response = requests.get("https://jobs.github.com/positions.json")
    data = json.loads(response.text)
    objs = [
        ApiView(
            id=job['id'],
            type=job['type'],
            url=job['url'],
            created_at=job['created_at'],
            company=job['company'],
            company_url=job['company_url'],
            location=job['location'],
            title=job['title'],
            description=job['description'],
        )
        for job in data

    ]

    datas = ApiView.objects.bulk_create(objs=objs)
    db = requests.post('http://127.0.0.1:8000/index', data=datas)
    return HttpResponse("created")


print(index.__doc__)


@api_view(['GET'])
def id_api(request, **args):
    """
    To Filter data by id

    URLParameters:
            id(SlugField): 123xcsc-cxscd-cssdw21

    returns:
            Returns the filtered data.
    """
    ids = request.GET.get('id')
    data = ApiView.objects.filter(id=ids)
    serializer = ApiViewSerializer(data,many=True)
    return Response(serializer.data)


print(id_api.__doc__)


@api_view(['GET'])
def list_out(request):
    """
    To list all the data:

        return:
                Returns all the data as ListApiView
    """
    data = ApiView.objects.all()
    serializer = ApiViewSerializer(data,many=True)
    return Response(serializer.data)


print(list_out.__doc__)


@api_view(['GET'])
def about(request):
    """
    To list out the title field in api view

        Parameter:
            title = a field name in database

        Return:
            Return the title field from database in api view
    """
    title = ApiView.objects.values_list('title')
    return Response(title)


print(about.__doc__)


def search_api(request):
    """
    To filter the data using title, location fields

        Data:
            filters = filter the data using ApiViewFilters search

        Return:
            Returns the serialized filtered data in api view using template file
    """
    data = ApiViewFilters(request.GET, queryset=ApiView.objects.all())
    return render(request, 'template.html', {'filter': data})


print(search_api.__doc__)


class UserListView(generics.ListAPIView):
    """
    To filter the data using title, location fields

        parameter:
            generics = for normal level views
            ListAPIView = to represent the model in api view

        Return:
            Returns the serialized filtered data in api view.
    """
    queryset = ApiView.objects.all()
    serializer_class = ApiViewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location']


print(UserListView.__doc__)


