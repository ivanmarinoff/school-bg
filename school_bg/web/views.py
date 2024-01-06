from django.urls import reverse_lazy
from django.views import generic as views
from school_bg.web.forms import WEBContentForm, WEBContentReadForm
from school_bg.web.models import WEBContent
from rest_framework import viewsets
from .serializers import WebSerializer


class WEBListView(viewsets.ModelViewSet):
    queryset = WEBContent.objects.all()
    serializer_class = WebSerializer


class IndexView(views.TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        pass


class SchoolLevel_1View(views.TemplateView):
    model = WEBContent
    form_class = WEBContentForm

    template_name = 'home/school_program_level_1.html'

    def get_success_url(self):
        return reverse_lazy('school_program_level_1')


class SchoolLevel_2View(views.TemplateView):
    model = WEBContent
    form_class = WEBContentForm

    template_name = 'home/school_program_level_2.html'

    def get_success_url(self):
        return reverse_lazy('school_program_level_2')


class ReadWEBContentView(views.ListView):
    model = WEBContent
    template_name = 'web/read_web_content.html'
    form_class = WEBContentReadForm

    def get_success_url(self):
        return reverse_lazy('read_web_content')


class BioWEBAutoSView(views.ListView):
    model = WEBContent
    template_name = 'web/auto_s_s.html'
    form_class = WEBContentReadForm


class BioWEBAutoEView(views.ListView):
    model = WEBContent
    template_name = 'web/auto_e_s.html'
    form_class = WEBContentReadForm


class BioWEBAutoRView(views.ListView):
    model = WEBContent
    template_name = 'web/auto_r_s.html'
    form_class = WEBContentReadForm


class BioWEBAutoMView(views.ListView):
    model = WEBContent
    template_name = 'web/auto_m_r.html'
    form_class = WEBContentReadForm
