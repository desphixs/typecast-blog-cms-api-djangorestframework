"""
URL configuration for typecast_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# This is the "Master Switchboard" for the entire project.
# It delegates specific sections of the website to different apps.

urlpatterns = [
    # The 'admin/' path gives us access to our data dashboard.
    path('admin/', admin.site.urls),
    
    # We include all the URLs from our 'blog' app and prefix them with 'api/'.
    # This means our blog endpoints will start with http://127.0.0.1:8000/api/
    path('api/', include('blog.urls')),
]
