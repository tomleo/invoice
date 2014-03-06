from django.db import models
from django.core.urlresolvers import reverse

class Span(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def get_hours(self):
        """Return timedelta"""
        pass

class Task(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    notes = models.TextField()
    hours = models.ManyToManyField('Span')

    def get_hours(self):
        """Return aggregate hours"""
        pass

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk':self.id, 'slug': self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    notes = models.TextField()
    job_title = models.CharField(max_length=255)

class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=125)
    contacts = models.ManyToManyField(Contact, related_name='c+')

class Day(models.Model):
    company = models.ForeignKey(Company)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    tasks = models.ManyToManyField('Task')
    date = models.DateField()
    notes = models.TextField()

class Month(models.Model):
    month = models.CharField(max_length=255)
    work_days = models.ManyToManyField(Day)

