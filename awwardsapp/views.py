from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from awwardsapp.models import Profile
from .forms import ProfileForm





# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'all-awward/index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path_info)

    else:
        form = ProfileForm()

    return render(request, 'all-awward/profile.html', {"profile": profile,"form":form})