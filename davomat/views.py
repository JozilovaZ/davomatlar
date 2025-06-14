from datetime import date

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Xodimlar,Davomat
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from .forms import CustomUserCreationForm  # Quyida yaratiladi
from .models import User



def home_page(request):
    return render(request,"home.html")


def davomat_page(request):
    xodimlar=Xodimlar.objects.all()
    davomatlar = Davomat.objects.all()

    context = {
        "davomatlar": davomatlar,
        "xodimlar":xodimlar,

    }

    if request.method=="POST":
        xodim=request.POST.get("xodim")
        kerish_vaqti=request.POST.get("kerish_vaqti")
        chiqish_vaqti=request.POST.get("chiqish_vaqti")
        status_r=request.POST.get("status_r")
        eslatmalar=request.POST.get("eslatmalar")

        xodim=Xodimlar.objects.get(id=xodim)
        if Davomat.objects.filter(xodim=xodim).exists():
            messages.warning(request,"Du davomat allaqachon bajarilgan")
            return redirect("davomat")
        Davomat.objects.create(
            xodim=xodim,
            kerish_vaqti=kerish_vaqti,
            chiqish_vaqti=chiqish_vaqti,
            status_r=status_r,
            eslatmalar=eslatmalar
        )
        messages.success(request,"Davomat muvaffaqiyatli qo`shildi")
        return redirect("davomat")



    return render(request,"davomat.html",context)




def xodimlar_page(request):
    users=User.objects.all()
    xodimlar = Xodimlar.objects.all()
    context={
        "xodimlar":xodimlar,
        "users":users,
    }

    if request.method=="POST":
        user_id=request.POST.get("username")
        lavozim=request.POST.get("lavozim")
        telefon_raqam=request.POST.get("telefon_raqam")
        manzil=request.POST.get("manzil")
        user_role=request.POST.get("user_role")
        is_active=request.POST.get("is_active")

        user=User.objects.get(id=user_id)
        if Xodimlar.objects.filter(user=user).exists():
            messages.warning(request,"Bu faydalanuvchi allaqachon mavjud")
            return redirect("xodimlar")
        Xodimlar.objects.create(
            user=user,
            lavozim=lavozim,
            telefon_raqam=telefon_raqam,
            manzil=manzil,
            user_role=user_role,
            is_active=is_active
        )
        messages.success(request,"Xodim muvaffaqiyatli qo`shildi")
        return redirect("xodimlar")


    return render(request,"xodimlar.html",context)


def delete_employe(request,id):
    xodim=get_object_or_404(Xodimlar,id=id)
    xodim.delete()
    messages.success(request,"Xodim muvaffaqiyatli o`chirildi")
    return redirect('xodimlar')



def update_employe(request, id):
    xodim = get_object_or_404(Xodimlar, id=id)
    users = User.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("username")
        lavozim = request.POST.get("lavozim")
        telefon_raqam = request.POST.get("telefon_raqam")
        manzil = request.POST.get("manzil")
        user_role = request.POST.get("user_role")
        is_active = request.POST.get("is_active")

        # Foydalanuvchi mavjudligini tekshirish
        if not User.objects.filter(id=user_id).exists():
            messages.error(request, "Foydalanuvchi topilmadi.")
            return redirect("xodimlar")

        user = User.objects.get(id=user_id)

        # Yangilash
        xodim.user = user
        xodim.lavozim = lavozim
        xodim.telefon_raqam = telefon_raqam
        xodim.manzil = manzil
        xodim.user_role = user_role
        xodim.is_active = is_active
        xodim.save()

        messages.success(request, "Xodim ma'lumotlari muvaffaqiyatli yangilandi.")
        return redirect("xodimlar")

    context = {
        "xodim": xodim,
        "users": users,
    }
    return render(request, "xodimlar.html", context)




def delete_davomat(request,id):
    davomat=get_object_or_404(Davomat,id=id)
    davomat.delete()
    messages.success(request,"Davomat muvaffaqiyatli o`chirildi")
    return redirect('davomat')




def dashboard_page(request):
    count=Xodimlar.objects.count
    davomat=Davomat.objects.filter(kerish_vaqti__date=date.today()).count()
    kechikkanlar=Davomat.objects.filter(kerish_vaqti__date=date.today(),status_r="kechikkan").count()

    context={
        "count":count,
        "davomat":davomat,
        "kechikkanlar":kechikkanlar,


    }
    return render(request,"dashboard.html",context)


class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro‘yxatdan muvaffaqiyatli o‘tdingiz!")
            return redirect('home')  # Bosh sahifaga yo‘naltirish
        return render(request, 'signup.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Xush kelibsiz, {username}!")
                return redirect('home')  # Bosh sahifaga yo‘naltirish
        messages.error(request, "Noto‘g‘ri foydalanuvchi nomi yoki parol.")
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
        return render(request, 'logout.html')


