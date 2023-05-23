from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


# For example
def index(request):
    return redirect(reverse('article', kwargs={
        'tags': 'python',
        'article_id': 42
        }))


class IndexView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return self.render_to_response(context)


def about(request):
    return render(request, 'about.html')
