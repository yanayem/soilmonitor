from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import UserProfile
from .forms import ProfilePicForm

# -------------------------
# LOGIN / SIGNUP
# -------------------------
def loginsignuppage(request):
    mode = request.GET.get('mode', 'login')

    if request.method == "POST" and "login_submit" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            
            next_url = request.GET.get("next", None)
            if not next_url:
                next_url = "soildata:dashboard"
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
            mode = "login"

    elif request.method == "POST" and "signup_submit" in request.POST:
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        location = request.POST.get("location")
        agree_terms = request.POST.get("agreeTerms")

        if not agree_terms:
            messages.error(request, "You must agree to Terms & Privacy Policy!")
            mode = "signup"
        elif password1 != password2:
            messages.error(request, "Passwords do not match!")
            mode = "signup"
        elif User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username already taken!")
            mode = "signup"
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=full_name
            )
            UserProfile.objects.create(
                user=user,
                phone_number=phone_number,
                location=location
            )
            messages.success(request, "Account created! Please log in.")
            return redirect("account:login")

    elif request.method == "POST" and "forgot_submit" in request.POST:
        email = request.POST.get("forgot_email")
        try:
            user = User.objects.get(email=email)
            messages.success(request, "Password reset link sent to your email!")
        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")
        mode = "login"

    return render(request, "login_signup.html", {"mode": mode})




# -------------------------
# Profile page
# -------------------------
@login_required
def profilepage(request):
    user = request.user

    profile, _ = UserProfile.objects.get_or_create(user=user)


    if request.method == "POST":
        if request.FILES.get("profile_pic"):  
            form = ProfilePicForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile picture updated!")
                return redirect('account:profilepage')
        else:
            messages.error(request, "No picture selected.")
            return redirect("account:profilepage")


    form = ProfilePicForm(instance=profile)

    try:
        profile_pic_url = profile.profile_pic.url
    except:
        profile_pic_url = "/static/images/default_profile.png"

    return render(request, 'profile.html', {
        'user': user,
        'profile': profile,
        'form': form,
        'profile_pic_url': profile_pic_url,
    })




@login_required
def remove_profile_pic(request):
    if request.method == "POST":
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.profile_pic.delete(save=True)  # delete file from storage
        user_profile.profile_pic = None
        user_profile.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "failed"}, status=400)


# -------------------------
# LOGOUT
# -------------------------
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("account:login")

def terms_privacy_views(request):
    return render(request, "terms_privacy.html")