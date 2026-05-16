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


# 'ArticleDetail' is for looking at or modifying one specific blog post.
# Think of this like taking a specific book off the library shelf to read it, 
# fix a typo in it, or throw it away if it's outdated.
class ArticleDetail(APIView):
    
    # Helper method to find an article by its ID (Primary Key).
    # Analogy: A security check at the door—if the book isn't on the shelf, 
    # we tell the user "Sorry, we don't have that here."
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return None

    # The 'get' method is for FETCHING one specific article.
    def get(self, request, pk):
        article = self.get_object(pk)
        if article is None:
            # If the article doesn't exist, we send back a 404 error.
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Translate the single article into JSON.
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # The 'put' method is for UPDATING an article.
    # Analogy: Replacing an old manuscript with a new, corrected version.
    def put(self, request, pk):
        article = self.get_object(pk)
        if article is None:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # We pass the EXISTING article AND the NEW data to the serializer.
        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            # Save the updated information.
            serializer.save()
            return Response(serializer.data)
        
        # If the new data is bad (like a missing title), send back errors.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # The 'delete' method is for REMOVING an article forever.
    # Analogy: Shredding a document. Remember: because of our CASCADE rule, 
    # this will also shred every comment attached to this article!
    def delete(self, request, pk):
        article = self.get_object(pk)
        if article is None:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the article from our database.
        article.delete()
        # Return a "204 No Content" to say "Done! There's nothing left to show."
        return Response(status=status.HTTP_204_NO_CONTENT)
