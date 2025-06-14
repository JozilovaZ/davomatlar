from django.db import models
from shared.models import Base
from django.contrib.auth.models import User



class Xodimlar(Base):
    USER_ROLE = (
        ('admin', 'Admin'),
        ('kadr', 'Kadr'),
        ('boshliq', 'Boshliq'),
        ('xodim', 'Xodim'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    lavozim=models.CharField(max_length=100,null=False,blank=False)
    ishga_qabul_sana=models.DateTimeField(auto_now_add=True)
    telefon_raqam=models.CharField(max_length=17)
    manzil=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    user_role = models.CharField(max_length=20, choices=USER_ROLE, default='xodim')

    def __str__(self):
        return str(self.user)


class Davomat(Base):
    STATUS_R = (
        ("kelgan", "Kelgan"),
        ("kelmagan", "Kelmagan"),
        ("tatil", "Tatil"),
        ("kechikkan", "Kechikkan")
    )
    xodim=models.ForeignKey(Xodimlar,on_delete=models.CASCADE, related_name="davomat")
    kerish_vaqti=models.DateTimeField()
    chiqish_vaqti=models.DateTimeField()
    eslatmalar=models.CharField(max_length=100,null=True,blank=True)
    status_r = models.CharField(max_length=20, choices=STATUS_R, default="kelgan")

    def __str__(self):
        return str(self.xodim)

    class Meta:
        verbose_name = "Davomat"
        verbose_name_plural = "Davomatlar"