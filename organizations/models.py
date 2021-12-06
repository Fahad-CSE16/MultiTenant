from django.db import models

# Create your models here.
from tenant_schemas.models import TenantMixin

class Organization(TenantMixin):
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

# tenant = Organization(domain_url='example.com', # don't add your port or www here! on a local server you'll want to use localhost here
#                 schema_name='public',
#                 name='Schemas Inc.',
#                 paid_until='2016-12-05',
#                 on_trial=False)
# tenant.save()