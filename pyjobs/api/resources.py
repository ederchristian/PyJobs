from tastypie.resources import ModelResource
from pyjobs.core.models import Job

class JobResource(ModelResource):
    class Meta:
        queryset = Job.objects.all()
        resource_name = 'jobs'
