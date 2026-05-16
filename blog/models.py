from django.db import models

# 'Article' is the main model for our blog posts.
# Think of it like a physical newspaper article—it has a headline, the story itself, 
# and the name of the person who wrote it.
class Article(models.Model):
    # 'title' stores the headline of the article.
    # CharField is for shorter text (like a single line).
    title = models.CharField(max_length=255)

    # 'body' stores the actual content of the blog post.
    # TextField is for long-form content (like several paragraphs).
    body = models.TextField()

    # 'author' stores the name of the person who wrote the post.
    # We use a simple CharField here to keep it easy for beginners.
    author = models.CharField(max_length=100)

    # 'created_at' automatically records the date and time when the article is first saved.
    # 'auto_now_add=True' is like a timestamp on a receipt—it's set once and never changes.
    created_at = models.DateTimeField(auto_now_add=True)

    # The __str__ method tells Django what to show in the Admin panel.
    # Instead of seeing "Article object (1)", we will see the actual title.
    def __str__(self):
        return self.title


# 'Comment' allows readers to leave feedback on specific articles.
# This model uses a 'ForeignKey' to create a relationship between the comment and an article.
# Analogy: If an Article is a "Parent", the Comment is the "Child" that belongs to it.
class Comment(models.Model):
    # 'article' connects this comment to one specific Article.
    # 'on_delete=models.CASCADE' means if the article is deleted, the comments vanish too.
    # 'related_name="comments"' allows us to ask an article: "Hey Article, show me all your comments!"
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    # 'author' is the name of the person leaving the comment.
    author = models.CharField(max_length=100)

    # 'body' is the text content of the comment.
    body = models.TextField()

    # 'created_at' is the timestamp for when the comment was posted.
    created_at = models.DateTimeField(auto_now_add=True)

    # This helps identify the comment in the Admin panel.
    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
