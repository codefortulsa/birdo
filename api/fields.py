from rest_framework.serializers import PrimaryKeyRelatedField


class MPTTRelationField(PrimaryKeyRelatedField):
    """Field is a property returning an MPTT related queryset
    Used against a property, such as:
    class MyModel(MPTTModel):
        parent = TreeForeignKey(
            'self', null=True, blank=True, related_name='children')
        @property
        def ancestors(self):
            return self.get_ancestors(include_self=True)
    ancestors = MPTTRelationField(many=True, source="ancestors")

    pulled from: https://github.com/jwhitlock/web-platform-compat/blob/master/webplatformcompat%2Fdrf_fields.py
    """

    def __init__(self, **kwargs):
        self.relation = kwargs.pop('source', None)
        read_only = kwargs.pop('read_only', True)
        assert read_only, 'read_only must be True'
        super(MPTTRelationField, self).__init__(
            read_only=read_only, **kwargs)
