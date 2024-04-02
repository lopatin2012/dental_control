from django.shortcuts import render

from django.views import View


class BaseReview(View):
    """
    Стартовая страница для отображения состояния полости рта/зубов.
    """
    def get(self, request):
        start_template = 'dental_condition/test.html'
        context = {
            'title': "Состояние зубов"
        }
        return render(request=request, template_name=start_template, context=context)

    def post(self, request):
        start_template = 'dental_condition/test.html'
        return render(request=request, template_name=start_template)


