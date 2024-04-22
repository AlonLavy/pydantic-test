from pydantic import BaseModel, model_serializer, Field
from pydantic_core.core_schema import SerializationInfo


class DistanceValue(BaseModel):
    value: float
    unit: str

    def __init__(self, *args, **kwargs):
        if len(args) != 0:
            super(DistanceValue, self).__init__(value=args[0], unit='M')
        elif 'value' in kwargs.keys() and 'unit' in kwargs.keys():
            super(DistanceValue, self).__init__(value=kwargs['value'], unit=kwargs['unit'])

    @model_serializer
    def serialize(self, info: SerializationInfo):
        if info.context is None or 'system' not in info.context.keys():
            raise AttributeError('DistanceValue class expected system in serialization context but could not find it')
        if info.context['system'] == 'client':
            return {'hello': self.value, 'world': self.unit}
        if info.context['system'] == 'engine':
            return self.value

        else:
            raise AttributeError('DistanceValue is not aware of system '+info.context['system'])


x = DistanceValue(value=10, unit='km')
y = DistanceValue(20)
print(x.model_dump(context={'system': 'client'}))
print(x.model_dump(context={'system': 'engine'}))
