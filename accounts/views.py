from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
# Create your views here.

class SignUpView(CreateView):
    # user_form = CustomUserCreationForm
    # profile_form = ProfileForm()
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['fav_movie']
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile
    
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    def get_object(self):
        return self.request.user


def add_user(request):
    if request.method == "POST":
        uform = UserCreationForm(data = request.POST)
        pform = ProfileForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()