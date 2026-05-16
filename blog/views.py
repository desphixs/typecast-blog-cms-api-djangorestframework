from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

# 'ArticleList' is the "Front Door" of our blog API.
# It handles requests that involve the entire collection of articles.
class ArticleList(APIView):
    
    # The 'get' method is for FETCHING data.
    # Analogy: A librarian going into the back room to get all the books on a shelf 
    # and bringing them to the front desk for you.
    def get(self, request):
        # 1. Grab all articles from the database.
        articles = Article.objects.all()
        # 2. Pass those articles to our translator (the serializer).
        # 'many=True' tells it to expect a list of articles.
        serializer = ArticleSerializer(articles, many=True)
        # 3. Send the translated JSON back to the user.
        return Response(serializer.data)

    # The 'post' method is for CREATING new data.
    # Analogy: A writer bringing a new manuscript to the librarian to be added to the collection.
    # The librarian must check if the manuscript is valid (no missing titles, etc.) before saving it.
    def post(self, request):
        # 1. Take the data sent by the user (request.data) and hand it to the translator.
        serializer = ArticleSerializer(data=request.data)
        
        # 2. Check if the data follows our rules (e.g., has a title, body, and author).
        if serializer.is_valid():
            # 3. If valid, save it to the database!
            serializer.save()
            # 4. Return the newly created article and a "201 Created" success code.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 5. If the data is bad, send back the error messages and a "400 Bad Request" code.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
