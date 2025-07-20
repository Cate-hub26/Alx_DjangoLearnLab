from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, UserProfile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required

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

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'
    
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
    
def is_librarian(user):
    return user.is_authenticated and user.userproile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.userproile.role == 'Member'

@login_required
@user_passes_test(is_member)
def librarian_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')
    

        