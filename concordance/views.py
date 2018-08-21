# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from nltk.book import text1
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
# from .models import Corpus
# from .serializers import ConcordanceSerializer
# from nltk.corpus import *
from nltk.text import Text
from django.views import generic
# from django.http import JsonResponse


class IndexView(generic.ListView):
    template_name = 'corpusapp/index.html'
    def get_queryset(self):
        return ""

# List all Concordances for the given word
class ConcordanceList(APIView):

    # Return all Concordances
    def get(self, request):
        # Open and Read the txt files
        corpusFile = open('D:\\data\Downloads\\ENGLE200F-Assignments-Sample\\test.txt', 'rU')
        corpusFileRead = corpusFile.read()
        # ftext1 = corpusFileRead.split()
        abst = Text(corpusFileRead.split())
        result = (abst.concordance(str(request.GET.get('param'))))
        return Response(result)

    def post(self):
        pass


