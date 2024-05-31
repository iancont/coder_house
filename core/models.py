from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SalesMember(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre", default="Nombre", unique=True)
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico", default="example@sales.com")
    profile_picture = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default.jpg")

    def __str__(self):
        return self.nombre


class Lead(models.Model):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    CHOICES_PRIORITY = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    )

    NEW = "new"
    CONTACTED = "contacted"
    WON = "won"
    LOST = "lost"

    CHOICES_STATUS = (
        (NEW, "New"),
        (CONTACTED, "Contacted"),
        (WON, "Won"),
        (LOST, "Lost"),
    )

    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    sales_member = models.ForeignKey(SalesMember, on_delete=models.CASCADE, blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    notes = models.TextField(blank=True, null=True)
