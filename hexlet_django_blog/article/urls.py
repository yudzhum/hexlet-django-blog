from django.urls import path

from hexlet_django_blog.article import views


app_name = 'article'


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='article_update'),
    path('<int:id>/delete/', views.ArticleFormDestroyView.as_view(), name='article_destroy'),
    path('<int:id>/', views.ArticleView.as_view(), name='detail'),
    path('create/', views.ArticleFormCreateView.as_view(), name='articles_create'),
]
