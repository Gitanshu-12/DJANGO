from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
from .views import home, post,category,contact,about


urlpatterns = [
    path('', home),
    path('contact/',contact),
    path('about/',about),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category)
]