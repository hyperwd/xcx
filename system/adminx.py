import xadmin
from .models import Parameter

# Register your models here.


@xadmin.sites.register(Parameter)
class ParameterAdmin(object):
    readonly_fields = (

    )

    list_display = (
        'key_type',
        'key_key',
        'key_value',
        'key_remark',
    )
