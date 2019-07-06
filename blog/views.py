from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import Article, Comments, Comment_owner, Author
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . serializers import ArticleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
	articles = Article.objects.all()
	return render(request, 'blog/index.html', {'articles':articles})

def article_detail(request, pk):
	detailed_article = get_object_or_404(Article, pk=pk)
	return render(request, 'blog/article_detail.html', {'detailed_article':detailed_article})


@api_view(['GET', 'POST'])
def article_list_api(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        article_list = Article.objects.all()
        serializer = ArticleSerializer(article_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     return HttpResponse(status=404)
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)