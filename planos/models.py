from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)
    

class Plano(TimeStampedModel):
    nome = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    preco = models.DecimalField(max_digits=10, decimal_places=2) 
    descricao = models.TextField(blank=True)
    objects = models.Manager()
        
    class Meta:
        verbose_name = "plano"
        verbose_name_plural = "planos"
    
    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})