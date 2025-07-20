from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test   
def admin_view(request, user):
    user.UserProfile.role == 'Admin'
    return render(request, 'relationship_app/admin_view.html')
