from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile,Position,Candidate
from django.shortcuts import get_object_or_404
from django.db.models import F
from announcementlib.electionannounce import rotate_announcements
import boto3
from django.views.decorators.csrf import csrf_exempt


# def home(request):
#      positions = Position.objects.all()
#      announcement = rotate_announcements()
#      context = {'positions': positions, 'announcement': announcement}
#      return render (request, 'home.html',context)


from .models import Vote

def home(request):
    positions = Position.objects.all()
    announcement = rotate_announcements()

    voted_positions = []

    if request.user.is_authenticated:
        voted_positions = Vote.objects.filter(user=request.user)\
                        .values_list('position_id', flat=True)

    context = {
        'positions': positions,
        'announcement': announcement,
        'voted_positions': voted_positions
    }

    return render(request, 'home.html', context)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        phonenumber = request.POST['phoneno']
        regtype = request.POST['regtype']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        
        
        profile = UserProfile.objects.create(user=myuser, regtype=regtype)

        messages.success(request, "You have Successfully Signed up")
        return redirect("login")
    
    return render(request, "signup.html")

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "login.html")
@csrf_exempt
def logoutpage(request):       
    logout(request)
    return redirect('home')

@csrf_exempt
def add_position(request):
    if request.method == 'POST':
        position_name = request.POST.get('position_name')
        position = Position.objects.create(name=position_name)
        candidates = request.POST.get('candidate_names').split(',')
        for i, name in enumerate(candidates):
            Candidate.objects.create(position=position, name=name.strip(), votes=0)
    return render (request, 'adminadd.html')

@csrf_exempt
def update_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    
    if request.method == 'POST':
        position_name = request.POST.get('position_name')
        if position_name:
            position.name = position_name
            position.save()
        
        candidate_names = request.POST.get('candidate_names')
        if candidate_names:
            candidate_names_list = candidate_names.split(',')
            
            position.candidates.all().delete()
            for name in candidate_names_list:
                Candidate.objects.create(position=position, name=name.strip(), votes=0)
        return redirect('home')
    
    return render(request, 'updateposition.html', {'position': position})

@csrf_exempt
def delete_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    
    if request.method == 'POST':
        position.delete()
        return redirect('home')
    

    return render(request, 'confirm_delete_position.html', {'position': position})



# @csrf_exempt
# def submit_vote(request):
#     if request.method == 'POST':
#         position_id = request.POST.get('position_id')
#         selected_candidates = request.POST.getlist('candidates')
        
#         # Update votes for selected candidates
#         Candidate.objects.filter(id__in=selected_candidates).update(votes=F('votes') + 1)
        
#         # Fetch the position title based on position_id
#         position = Position.objects.get(id=position_id)
        
#         """ #Send SNS notification
#         topicOfArn = 'arn:aws:sns:eu-west-1:250738637992:vote_App_CPP'
#         subjectToSend = 'Vote Submitted'
#         messageToSend = f'A vote has been submitted for a position'
#         AWS_REGION = 'eu-west-1'
#         sns_client = boto3.client('sns', region_name=AWS_REGION)
#         response = sns_client.publish(
#             TopicArn=topicOfArn,
#             Message=messageToSend,
#             Subject=subjectToSend,
#         )
#         print(response) """  # Print SNS response 

#     return redirect('home')


from .models import Vote

@csrf_exempt
def submit_vote(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must login to vote")
            return redirect('login')

        position_id = request.POST.get('position_id')
        selected_candidate = request.POST.get('candidates')

        position = Position.objects.get(id=position_id)

        # Check if user already voted
        if Vote.objects.filter(user=request.user, position=position).exists():
            messages.error(request, "You have already voted for this position.")
            return redirect('home')

        candidate = Candidate.objects.get(id=selected_candidate)

        # Increase vote
        candidate.votes = F('votes') + 1
        candidate.save()

        # Save vote record
        Vote.objects.create(
            user=request.user,
            position=position,
            candidate=candidate
        )

        messages.success(request, "Vote submitted successfully.")

    return redirect('home')


def vote(request, position_id):
        candidates = Candidate.objects.filter(position_id=position_id)
        return render(request, 'vote.html', {'candidates': candidates})