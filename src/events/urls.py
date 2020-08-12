from django.urls import path
from events.views import (
    HomePageView,
    SignUpView,
    DevelopmentView,
    AllEventsView,
    AddEventView,
    EventInformationView,
    EventJoinView,
    ProfileView,
    UserEventsView,
    EventDeleteView,
    ParticipantsListView,
    RecommendationView,
)

from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

app_name = 'events'

urlpatterns = [
    path('', HomePageView, name='events-home'),
    path('signup/', SignUpView, name='events-signup'),
    path('inprogress', DevelopmentView, name='events-inprogress'),
    path('login/', LoginView.as_view(template_name='login.html'), name='events-login'),
    path('logout/', LogoutView.as_view(), name='events-logout'),
    path('allevents/', AllEventsView, name='events-allevents'),
    path('addevent/', AddEventView, name='events-addevent'),
    path('allevents/<int:event_id>/', EventInformationView, name='events-eventinfo'),
    path('allevents/<int:event_id>/delete/', EventDeleteView, name='events-eventdelete'),
    path('allevents/<int:event_id>/join/', EventJoinView, name='events-eventjoin'),
    path('profile/', ProfileView, name='events-profile'),
    path('myevents/', UserEventsView, name='events-myevents'),
    path('myevents/<int:event_id>/participants/', ParticipantsListView, name='events-participants'),
    path('reccomended/', RecommendationView, name='events-recommended'),
]
