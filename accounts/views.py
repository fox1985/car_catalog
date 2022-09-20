from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from  contacts.models import Contact
from  django.contrib.auth.decorators import login_required

# Create your views here.

def login(reguest):
    if reguest.method == 'POST':
        username = reguest.POST['username']
        password = reguest.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(reguest, user)
            messages.success(reguest, 'Вы впервые вошли в систему')
            return redirect('dashboard')
        else:
            messages.error(reguest, 'Не верный логин или пароль')
            return redirect('login')

    return render(reguest, 'accounts/login.html')


def register(reguest):
    if reguest.method == 'POST':
      firstname = reguest.POST['firstname']
      lastname = reguest.POST['lastname']
      username = reguest.POST['username']
      email = reguest.POST['email']
      password = reguest.POST['password']
      confirm_password = reguest.POST['confirm_password']

      if password == confirm_password:
          if User.objects.filter(username=username).exists():
              messages.error(reguest, 'Имя такое уже есть')
              return redirect('register')

          else:
              if User.objects.filter(email=email).exists():
                  messages.error(reguest, 'Проверти правильно ли вы указали email или такой email уже сушествует')
                  return redirect('register')

              else:
                  """Создается  новый пользователь"""
                  user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,  username=username, password=password)
                  auth.login(reguest, user)
                  messages.success(reguest, 'Вы впервые вошли в систему ')
                  return redirect('dashboard')
                  user.save()
                  messages.success(reguest, 'Вы успешно занрегистрировались')
                  return redirect('login')


      else:
          messages.error(reguest, 'Пароль не савпадает видите его воба поля правильно ещё раз')
          return redirect('register')



    else:
        return render(reguest, 'accounts/register.html')

@login_required(login_url='login')
def dashboard(reguest):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=reguest.user.id)
    data = {
        'inquirys': user_inquiry,
    }
    return render(reguest, 'accounts/dashboard.html', data)

def logout(reguest):
    if reguest.method == 'POST':
        auth.logout(reguest)
        messages.success(reguest, "Вы вышли из акаунта")
        return redirect('home')

    return redirect('home')