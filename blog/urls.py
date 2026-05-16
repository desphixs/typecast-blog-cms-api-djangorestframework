from django.urls import path
from .views import ArticleList, ArticleDetail

# This file is the "Switchboard" for the blog app.
# It maps specific web addresses (URLs) to the views we wrote in views.py.

urlpatterns = [
    # When a user visits '/api/articles/', Django will run the 'ArticleList' view.
    # '.as_view()' is required because ArticleList is a class, not a simple function.
    path('articles/', ArticleList.as_view(), name='article-list'),
    
    # When a user targets a specific article (e.g. '/api/articles/1/'), 
    # we run the 'ArticleDetail' view.
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
]
