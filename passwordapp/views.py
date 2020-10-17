from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password, check_password
from .forms import PasswordForm
from .models import PasswordModel
from .password_hash import encrypt_password, decrypt_password

# Create your views here.

@login_required
def password_index(request):
    try:    
        password_objs = PasswordModel.objects.filter(user=request.user)
        for obj in password_objs:
            obj.site_password = decrypt_password(obj.site_password, obj.key)
        

    except KeyError as e:
        print(e)

    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():

            
            new_site = password_form.save(commit=False)

            user = request.user
            new_site.user = user

            # encrpt password

            get_password = str(password_form.cleaned_data['site_password'])

            encoded_password, key = encrypt_password(get_password)

            new_site.site_password = encoded_password
            new_site.key = key
            new_site.save()

            # cd = password_form.cleaned_data
            messages.success(request, "Your data has been saved.")
            return redirect('passwordsapp:home')
    
    else:
        password_form = PasswordForm()
    return render(request, 'passwordapp/index.html', {'password_form':password_form, 'password_objs':password_objs})


