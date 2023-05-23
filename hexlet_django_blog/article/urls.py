from django.urls import path

from hexlet_django_blog.article import views


app_name = 'article'


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:id>/', views.ArticleView.as_view(), name='detail'),
]
