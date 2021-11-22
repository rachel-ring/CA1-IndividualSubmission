# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser, Profile
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
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

class ProfileCreationView(CreateView):
    form_class = ProfileForm
    template_name = 'registration/add_profile.html'
    success_url = reverse_lazy('home')



# def add_user(request):
#     if request.method == "POST":
#         pform = ProfileForm(data = request.POST)
#         if pform.is_valid():
#             profile = pform.save(commit = False)
#             profile.user = CustomUser
#             profile.save()