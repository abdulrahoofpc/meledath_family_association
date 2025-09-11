from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Gallery, Event, Profile,Member,Memory,Topic, Comment,TeamMember,PremiumEvent,Advertisement,LifeMember
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from collections import defaultdict

# Get all life members from DB--------------

def History(request):
    members = LifeMember.objects.all().order_by('membership_no')
    return render(request, 'our-history.html', {'members': members})

# Get all life members from DB--------------
def team_list(request):
    # General Members (not women association)
    general_qs = TeamMember.objects.filter(is_women_association=False).order_by("year", "name")

    general_by_year = defaultdict(list)
    for member in general_qs:
        general_by_year[member.year].append(member)

    # Women Association Members
    women_qs = TeamMember.objects.filter(is_women_association=True).order_by("year", "name")

    women_by_year = defaultdict(list)
    for member in women_qs:
        women_by_year[member.year].append(member)

    return render(request, "our-team.html", {
        "general_by_year": dict(general_by_year),
        "women_by_year": dict(women_by_year),
    })


def team_detail(request, slug):
    member = get_object_or_404(TeamMember, slug=slug)
    return render(request, "team-member-detail.html", {"member": member})

#family_tree-----------------------

def family2(request):
    roots = Member.objects.filter(parent=None)
    return render(request, 'family2.html', {'roots': roots})

# def family_tree_view(request):
#     all_people = Person.objects.all()
#     return render(request, 'tree.html', {'people': all_people})

# Home page showing latest events -------------


def Home(request):
    advertisements = Advertisement.objects.all().order_by('-created_at')
    events = Event.objects.all().order_by('-date')[:4]
    memories = Memory.objects.all()
    topic = Topic.objects.first()
    comments = Comment.objects.filter(topic=topic) if topic else []
    premium_events = PremiumEvent.objects.all()

    return render(request, 'index.html', {
        'advertisements': advertisements,
        'events': events,
        'memories': memories,
        'topic': topic,
        'comments': comments,
        'premium_events': premium_events,
    })

def premium_event_view(request): 
    events = PremiumEvent.objects.all()
    return render(request, 'premium_event_list.html', {'events': events})

def premium_event_detail(request, slug):
    event = get_object_or_404(PremiumEvent, slug=slug)
    return render(request, 'premium_event_detail.html', {'event': event})


def memory_detail(request, id):
    memory = get_object_or_404(Memory, id=id)
    return render(request, 'memory_detail.html', {'memory': memory})


# ------------------ User Registration ------------------
def register(request):
    if request.method == "POST":
        email        = request.POST.get("email")
        first_name   = request.POST.get("first_name")
        password1    = request.POST.get("password1")
        password2    = request.POST.get("password2")
        phone_number = request.POST.get("phone")

        # 1️⃣ password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # 2️⃣ user already exists check
        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists.")
            return redirect("register")

        # 3️⃣ create user & profile
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password1,
                first_name=first_name,
            )
            Profile.objects.create(
                user=user,
                full_name=first_name,
                phone_number=phone_number,
            )
            messages.success(request, f"Account created for {email}!")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect("register")

    # GET request → render the shared form
    return render(request, "forms.html")


# ------------------ Login ------------------
def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("family_pillars")
        messages.error(request, "Invalid username or password.")
        return redirect("login")

    # GET request
    return render(request, "forms.html")


# ------------------ Logout ------------------
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")
# -----------------------------------------------------------------------------------------------------#

def discussion_view(request):
    topic = Topic.objects.first()
    comments = Comment.objects.filter(topic=topic) if topic else []
    return render(request, 'discussion/discussion.html', {
        'topic': topic,
        'comments': comments,
    })

@csrf_exempt
@login_required
def post_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        topic = Topic.objects.first()

        if not topic:
            return JsonResponse({'success': False, 'error': 'No topic found.'})

        comment = Comment.objects.create(
            topic=topic,
            user=request.user,
            content=content
        )

        return JsonResponse({
            'success': True,
            'username': request.user.username,
            'timestamp': comment.posted_at.strftime('%Y-%m-%d %H:%M'),
            'content': comment.content
        })

    return JsonResponse({'success': False, 'error': 'Invalid request.'})



# -----------------Static Pages--------------------------
@login_required(login_url='login') 
def FamilyPillars(request):
    return render(request, 'membership.html')

# def History(request):
#     return render(request, 'our-history.html')

def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {'events': events})

def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery.html', {'galleries': galleries})

def Team(request):
    return render(request, 'our-team.html')

def FamilyTree1(request):
    return render(request, 'tree.html')
