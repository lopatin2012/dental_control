from django.shortcuts import render

from django.views import View


class MainMenu(View):
    """
    Стартовая страница.
    """
    def get(self, request):
        start_template = 'main_menu/main.html'
        context = {
            'title': "Состояние зубов",
        }
        return render(request=request, template_name=start_template, context=context)

    def post(self, request):
        start_template = 'dental_condition/test.html'
        return render(request=request, template_name=start_template)


