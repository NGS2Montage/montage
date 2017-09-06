from django.shortcuts import redirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class UserDetail(DetailView):
    model = User
    context_object_name='user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'rafter_user_service/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        # Get all the applications for this user
        user = context['user']
        return context

@login_required
def user_profile(request):
    user = request.user
    return redirect('user:user', permanent=True, username=user.username)
