from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, \
    MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def directors_detail_view(request, id):
    directors = Director.objects.get(id=id)
    serializer = DirectorDetailSerializer(directors)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_detail_view(request, id):
    movies = Movie.objects.get(id=id)
    serializer = MovieDetailSerializer(movies)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_detail_view(request, id):
    reviews = Review.objects.get(id=id)
    serializer = ReviewDetailSerializer(reviews)
    return Response(data=serializer.data)

