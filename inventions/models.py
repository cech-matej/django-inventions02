from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


def flag_path(instance, filename):
    return f"nation/{instance.id}/flag/{filename}"


def inventor_photo_path(instance, filename):
    return f"inventor/{instance.id}/photo/{filename}"


def invention_photo_path(instance, filename):
    return f"invention/{instance.id}/photo/{filename}"


class Nation(models.Model):
    class FormOfState(models.TextChoices):
        MONARCHY = 'MONARCHY', _('Monarchy')
        REPUBLIC = 'REPUBLIC', _('Republic')
        THEOCRACY = 'THEOCRACY', _('Theocracy')

    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="State name")
    abbr = models.CharField(max_length=5, null=False, blank=False, unique=True, verbose_name="State abbreviation")
    flag = models.ImageField(upload_to=flag_path, blank=True, null=True, verbose_name="Flag")
    # flag = models.ImageField(upload_to='nation/flags/%Y/%m/%d/', blank=True, null=True, verbose_name="Flag")
    form_of_state = models.CharField(max_length=15, choices=FormOfState.choices,
                                     default=FormOfState.REPUBLIC)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False,
                            verbose_name="Category name")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Inventor(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="First name")
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Last name")
    birthday = models.DateField(blank=True, null=True,
                                help_text="<em>YYYY-MM-DD</em>",
                                verbose_name="Birthday")
    date_of_death = models.DateField(blank=True, null=True,
                                     help_text="<em>YYYY-MM-DD</em>",
                                     verbose_name="Date of death")
    nation_id = models.ForeignKey(Nation, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True, verbose_name="Biography")
    photo = models.ImageField(upload_to=inventor_photo_path, blank=True, null=True,
                              verbose_name="Photo of the inventor")
    '''photo = models.ImageField(upload_to='inventor/photo/%Y/%m/%d/', blank=True, null=True,
                              verbose_name="Photo of the inventor")'''

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Invention(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name="Invention name")
    inventors = models.ManyToManyField(Inventor, help_text="Select who invented it")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    date_of_invention = models.DateField(blank=True, null=True,
                                         help_text="<em>YYYY-MM-DD</em>",
                                         verbose_name="Date of the invention")
    category = models.ManyToManyField(Category, help_text="Select invention categories")
    photo = models.ImageField(upload_to=invention_photo_path, blank=True, null=True,
                              verbose_name="Photo of the invention")
    '''photo = models.ImageField(upload_to='invention/photo/%Y/%m/%d/', blank=True, null=True,
                              verbose_name="Photo of the invention")'''

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('invention-detail', args=[str(self.id)])
