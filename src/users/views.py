# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
# # from django.http import HttpResponseRedirect
# # from django.contrib.auth.forms import UserCreationForm


# def register(request):

#     form = RegistrationForm(request.POST or None)
#     # form = UserCreationForm(request.POST or None)
#     if request.user.is_authenticated:
#         messages.warning(request, "You already have an account")
#         return redirect("blog:list")
#     print(form.is_valid())
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         messages.success(request, f"Account created for {username}!")
#         return redirect('login')
#         # form = RegistrationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/register.html', context)


# @login_required()
# def profile(request):
#     u_form = UserUpdateForm(request.POST or None, instance=request.user)
#     p_form = ProfileUpdateForm(
#         request.POST or None, request.FILES or None, instance=request.user.profile)

#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(
#             request, "Your account has been updated successfully!")
#         print(request.META)
#         print(request.path)
#         print(request.session)
#         return redirect(request.path)
#         # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request, 'users/profile.html', context)


# # Create your views here.
