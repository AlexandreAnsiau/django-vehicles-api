from django.shortcuts import render
from django.views.generic import View


class TestView(View):
    template = "main/test.html"

    def get(self, request):
        return render(request, self.template)