from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from awwardsapp.models import Profile,Project
from .forms import ProfileForm,NewProjectForm





# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    project = Project.objects.all().order_by('-id')

    return render(request, 'all-awward/index.html',{'projects':project})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'all-awward/profile.html', {"form":form,'projects':project,'profile':profile})
@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Project.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'all-awward/search.html', {'message': message, 'images': images})
    else:
        message = 'Not found'
    return render(request, 'all-awward/search.html', {'message': message})