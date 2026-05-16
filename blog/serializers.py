from rest_framework import serializers
from .models import Article, Comment

# 'CommentSerializer' is like a specialized translator for our comments.
# It takes a single comment from the database and turns it into JSON.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        # We tell DRF which model it should be translating.
        model = Comment
        # We include all fields from the model in the JSON.
        fields = '__all__'


# 'ArticleSerializer' is a more complex translator. 
# It handles the Article data AND it knows how to include the Article's comments.
class ArticleSerializer(serializers.ModelSerializer):
    # This is where the magic happens! 
    # We tell DRF: "When you translate an article, reach out and grab all 
    # its comments and translate them using the CommentSerializer too."
    # 'many=True' means there could be multiple comments.
    # 'read_only=True' means we only want to SEE comments in the API; 
    # we don't send comment data through this specific door when creating an article.
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        # By including '__all__', DRF will include our special 'comments' field we defined above
        # along with the standard title, body, author, etc.
        fields = '__all__'
