from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, UserProfile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_object_name(self, **kwargs):
        context = super().get_context_object_name(**kwargs)
        context['books'] = self.object.books.all()
        return context
@user_passes_test   
def admin_view(user):
    return user.UserProfile.role == 'Admin'

def librarian_view(user):
    return user.UserProfile.role == 'Librarian'

def member_view(user):
    return user.UserProfile.role == 'Member'
        