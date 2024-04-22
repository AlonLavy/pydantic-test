import json
from typing import Union, Optional, Literal

import typing_extensions

from pydantic import BaseModel
from pydantic.main import IncEx


class DistanceValue(BaseModel):
    value: float
    unit: str

    def __init__(self, *args, **kwargs):
        if len(args) != 0:
            super(DistanceValue, self).__init__(value=args[0], unit='M')
        elif 'value' in kwargs.keys() and 'unit' in kwargs.keys():
            super(DistanceValue, self).__init__(value=kwargs['value'], unit=kwargs['unit'])

    def model_dump(
            self,
            *,
            mode: Union[typing_extensions.Literal['json', 'python'], str] = 'python',
            include: IncEx = None,
            exclude: IncEx = None,
            context: Optional[dict] = None,
            by_alias: bool = False,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
            round_trip: bool = False,
            warnings: Union[bool, Literal['none', 'warn', 'error']] = True,
            serialize_as_any: bool = False,
    ):
        if by_alias:
            return json.loads(self.model_dump_json())
        else:
            return self.value
            # In airways we will change it to self.to_object().to_meters() as self.to_object() will be algotils distance


x = DistanceValue(value=10, unit='km')
y = DistanceValue(20)
print(x.model_dump())
print(x.model_dump(by_alias=True))
print(y.model_dump())
print(y.model_dump(by_alias=True))
