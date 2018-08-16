from django.shortcuts import render
from django.shortcuts import get_object_or_404
from nltk.book import text1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Corpus
from .serializers import ConcordanceSerializer
# from nltk.corpus import *
from nltk.text import Text


# List all Concordances for the given word
class ConcordanceList(APIView):

    # Return all Concordances
    def get(self, request):
        # Read the Corpus
        #emma = Text(gutenberg.words('C:\\Users\\srai\\AppData\\Roaming\\nltk_data\\corpora\\gutenberg\\austen-emma.txt'))
        # tt = emma.concordance("surprize")
        result = (text1.concordance("monstrous"))
        #corpus = Corpus.objects.all()
        # Find the Concordances
        # Serialize data
        #serializer = ConcordanceSerializer(corpus, many=True)
        # return Response('{name: '+ str(ll) +', age: 31, city: "dd"}')

        return Response(result)

    def post(self):
        pass


