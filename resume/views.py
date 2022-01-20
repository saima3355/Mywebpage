from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class MylifePageView(TemplateView):
    template_name = 'mylife.html'

class AcademicsPageView(TemplateView):
    template_name = 'academics.html'

class SkillsPageView(TemplateView):
    template_name = 'skills.html'

class InterestsPageView(TemplateView):
    template_name = 'interests.html'

class DreamsPageView(TemplateView):
    template_name = 'dreams.html'

class PrimaryPageView(TemplateView):
    template_name = 'primary.html'

class SecondaryPageView(TemplateView):
    template_name = 'secondary.html'

class HigherPageView(TemplateView):
    template_name = 'higher.html'

class ProjectsPageView(TemplateView):
    template_name = 'projects.html'

class ProfilePageView(TemplateView):
    template_name = 'profile.html'

class SpeechPageView(TemplateView):
    template_name = 'speech.html'

class DataPageView(TemplateView):
    template_name = 'data.html'


