from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    #path("", PostListView.as_view()),
    path("add/", PostAddView.as_view()),
    path("<int:pk>/", PostListView.as_view()),
    path("del/<int:pk>/", PostDelView.as_view()),
    path("<int:pk>/likes/", PostLikeView.as_view()),
    path("scrap/<int:pk>/", PostScrapView.as_view()),
    path("<int:pk>/emotions/", EmotionFunctionsView.as_view()),
    #path("<int:pk>/emotions/add/", EmotionFunctionsView.as_view()),
    path("<int:pk>/emotions/del/", EmotionDelView.as_view()),
]