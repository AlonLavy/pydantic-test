import json
from typing import Union, Optional, Literal

import typing_extensions

from pydantic import BaseModel, model_serializer
from pydantic.main import IncEx
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
        return self.value if not info.by_alias else self.__dict__


x = DistanceValue(value=10, unit='km')
y = DistanceValue(20)
print(x.model_dump(context={'x': 'y'}))
print(x.model_dump(by_alias=True))
print(y.model_dump())
print(y.model_dump(by_alias=True))
