from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True
    auto_drop_schema = True 

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class Domain(DomainMixin):
    pass
