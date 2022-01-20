from django.urls import path
from .views import HomePageView, MylifePageView, AcademicsPageView, SkillsPageView, InterestsPageView, DreamsPageView,PrimaryPageView, SecondaryPageView, HigherPageView, ProjectsPageView, ProfilePageView, SpeechPageView, DataPageView
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('mylife',MylifePageView.as_view(), name = 'mylife'),
    path('academics',AcademicsPageView.as_view(), name = 'academics'),
    path('skills/',SkillsPageView.as_view(), name = 'skills'),
    path('interests',InterestsPageView.as_view(), name = 'interests'),
    path('dreams',DreamsPageView.as_view(), name = 'dreams'),
    path('primary',PrimaryPageView.as_view(), name = 'primary'),
    path('secondary',SecondaryPageView.as_view(), name = 'secondary'),
    path('higher',HigherPageView.as_view(), name = 'higher'),
    path('projects', ProjectsPageView.as_view(), name='projects'),
    path('profile', ProfilePageView.as_view(), name='profile'),
    path('speech', SpeechPageView.as_view(), name='speech'),
    path('data', DataPageView.as_view(), name='data'),

]

