from django.db import models


class Register(models.Model):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('caretaker', 'Caretaker'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    def set_password(self, raw_password):
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)


# -------------------------
# Role Specific Profiles with ForeignKey
# -------------------------

class CustomerProfile(models.Model):
    id = models.AutoField(primary_key=True)  # default in Django, explicit here
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="customer_profiles")
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"CustomerProfile {self.id} -> {self.user.username}"


class AdminProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="admin_profiles")
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"AdminProfile {self.id} -> {self.user.username}"


class DoctorProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="doctor_profiles")
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField(default=0)
    license_number = models.CharField(max_length=50)

    def __str__(self):
        return f"DoctorProfile {self.id} -> {self.user.username}"


class CaretakerProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="caretaker_profiles")
    shift_timings = models.CharField(max_length=100, blank=True, null=True)
    assigned_patients = models.TextField(blank=True, null=True)  # could be JSON later
    skills = models.TextField(blank=True, null=True)
    id_proof = models.FileField(upload_to="caretaker_id_proofs/", blank=True, null=True)  


    def __str__(self):
        return f"CaretakerProfile {self.id} -> {self.user.username}"
