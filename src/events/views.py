from django.shortcuts import render, redirect, get_object_or_404
from events.models import User, HappeningEvents
from events.forms import SignUpForm, OrganizeEvent
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

def HomePageView(request):
    template_name = 'home.html'
    context = {
        'title': 'HomePage'
    }

    return render(request, template_name, context)

def SignUpView(request):
    template_name = 'signup.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        data = dict(Events = [])
        interest_dict = dict(Interests = [])

        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.email = form.cleaned_data.get('email')
            form_obj.events = data
            form_obj.interests = interest_dict
            main_text = form.cleaned_data.get('interests')
            print(main_text)
            l = main_text.split(",")
            l = [x.strip().lower() for x in l]
            form_obj.interests['Interests'] = l
            form_obj.save()
            
            #auth_login(request, user)
            return redirect('events:events-home')
    
    else:
        form = SignUpForm()
    
    context = {
        'form': form,
    }

    return render(request, template_name, context)

def DevelopmentView(request):
    template_name = 'development.html'
    return render(request, template_name)

def AllEventsView(request):
    template_name = 'allevents.html'
    allevents = HappeningEvents.objects.all()
    context={
        'allevents':allevents,
    }
    return render(request, template_name, context)

def EventInformationView(request, event_id):
    template_name = 'eventinfo.html'
    event_obj = get_object_or_404(HappeningEvents, id=event_id)

    if request.user.username in event_obj.participants['Participants']:
        context = {
            'event': event_obj,
            'present': True,
        }
    else:
        context = {
            'event': event_obj,
        }

    return render(request, template_name, context)

@login_required(login_url='/login/')
def AddEventView(request):
    template_name = 'addevent.html'

    if request.method == 'POST':
        form = OrganizeEvent(request.POST or None, request.FILES)
        data = dict(Participants = [])
        type_dict = dict(Interests = [])
        
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.organizer = request.user
            form_obj.description = form.cleaned_data.get('description')
            form_obj.participants = data
            form_obj.event_type = type_dict
            main_text = form.cleaned_data.get('event_type')
            m = main_text.split(",")
            m = [x.strip().lower() for x in m]
            form_obj.event_type['Type'] = m
            form.save()

            return redirect('events:events-allevents')
    
    else:
        form = OrganizeEvent()

    context = {
        'form' : form,
    }

    return render(request, template_name, context)

@login_required(login_url='/login/')
def EventJoinView(request, event_id):
    template_name = 'eventjoin.html'
    event_obj = get_object_or_404(HappeningEvents, id=event_id)
    user_obj = get_object_or_404(User, id=request.user.id)
    print(event_obj.name)

    if user_obj.username in event_obj.participants['Participants']:
        context = {
            'message': 'Sorry But you are already listed in the Event List.'
        }

        return render(request, template_name, context)
    else:
        event_obj.participants['Participants'].append(user_obj.username)
        event_obj.save()
        context = {
            'message' : 'Yayy. You are going to the Event.'
        }

        return render(request, template_name, context)

@login_required(login_url='/login/')
def ProfileView(request):
    template_name = 'profile.html'
    user_obj = get_object_or_404(User, id=request.user.id)

    l = user_obj.interests['Interests']

    context = {
        'user' : user_obj,
        'ilist' : l
    }

    return render(request, template_name, context)

@login_required(login_url='/login/')
def UserEventsView(request):
    template_name = 'myevents.html'
    eves = HappeningEvents.objects.filter(organizer=request.user)
    print(eves)

    context = {
        'events' : eves,
    }

    return render(request, template_name, context)


@login_required(login_url='/login/')
def EventDeleteView(request, event_id):
    event_obj = get_object_or_404(HappeningEvents, id=event_id)
    
    if request.user == event_obj.organizer:
        event_obj.delete()
        return redirect('events:events-myevents')

@login_required(login_url='/login/')
def ParticipantsListView(request, event_id):
    template_name = 'participants.html'
    event_obj = get_object_or_404(HappeningEvents, id=event_id)

    if request.user == event_obj.organizer:
        context = {
            'participants' : event_obj.participants['Participants'],
            'event' : event_obj,
        }
    else:
        context = {
            'Hello' : 'Hello',
        }

    return render(request, template_name, context)

@login_required(login_url='/login/')
def RecommendationView(request):
    template_name = 'recommendation.html'
    events = HappeningEvents.objects.all()
    event_list = []
    flag = False

    for event in events:
        flag = False
        for i in request.user.interests['Interests']:
            for j in event.event_type['Type']:
                if i == j:
                    if event in event_list:
                        break;
                    event_list.append(event)
                    flag = True
                    break
            
            if(flag):
                break

    context = {
        'event_list' : event_list
    }

    return render(request, template_name, context)