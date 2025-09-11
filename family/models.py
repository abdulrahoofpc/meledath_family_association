from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Abstract base model for common family fields
class BaseFamilyMember(MPTTModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    MEMBERSHIP_CATEGORIES = (
        ('LM', 'Life Member'),
        ('PM', 'Paid Member'),
        ('NM', 'Non Member'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)

    baptism_date = models.DateField(null=True, blank=True)
    baptism_place = models.CharField(max_length=255, blank=True, null=True)

    communion_date = models.DateField(null=True, blank=True)
    communion_place = models.CharField(max_length=255, blank=True, null=True)

    marriage_date = models.DateField(null=True, blank=True)
    marriage_place = models.CharField(max_length=255, blank=True, null=True)

    date_of_death = models.DateField(null=True, blank=True)
    place_of_death = models.CharField(max_length=255, blank=True, null=True)
    burial_place = models.CharField(max_length=255, blank=True, null=True)
    cause_of_death = models.CharField(max_length=255, blank=True, null=True)

    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    education = models.CharField(max_length=255, blank=True, null=True)
    employed = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)

    photo = models.ImageField(upload_to='members/', null=True, blank=True)
    family_photo = models.ImageField(upload_to='family-photo/', null=True, blank=True)

    membership_category = models.CharField(
        max_length=2,
        choices=MEMBERSHIP_CATEGORIES,
        default='NM'
    )
    membership_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        help_text="Auto-generated with category prefix"
    )

    date_updated = models.DateTimeField(auto_now=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    spouses = models.ManyToManyField('self', symmetrical=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['first_name']

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Auto-generate membership_number on first save for LM/PM
        if self.membership_category in ('LM', 'PM') and not self.membership_number:
            prefix = self.membership_category
            # Query the concrete subclass, not the abstract base
            count = self.__class__.objects.filter(
                membership_category=self.membership_category
            ).count() + 1
            self.membership_number = f"{prefix}{str(count).zfill(4)}"
        super().save(*args, **kwargs)


# Concrete family models
class AipuFamily(BaseFamilyMember):
    class Meta:
        verbose_name_plural = 'Aipu Family Members'
        ordering = ['first_name', 'last_name']


class LonappanFamily(BaseFamilyMember):
    class Meta:
        verbose_name_plural = 'Lonappan Family Members'
        ordering = ['first_name', 'last_name']


class FrancisFamily(BaseFamilyMember):
    class Meta:
        verbose_name_plural = 'Francis Family Members'
        ordering = ['first_name', 'last_name']


class VarunnyFamily(BaseFamilyMember):
    class Meta:
        verbose_name_plural = 'Varunny Family Members'
        ordering = ['first_name', 'last_name']


class ThomaFamily(BaseFamilyMember):
    class Meta:
        verbose_name_plural = 'Thoma Family Members'
        ordering = ['first_name', 'last_name']


class ChakoruFamily(BaseFamilyMember):
    class Meta:
        verbose_name_plural = 'Chakoru Family Members'
        ordering = ['first_name', 'last_name']


class KochuvareedFamily(BaseFamilyMember):
    class Meta:
        verbose_name_plural = 'Kochuvareed Family Members'
        ordering = ['first_name', 'last_name']