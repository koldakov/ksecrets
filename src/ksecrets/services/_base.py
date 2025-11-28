from abc import ABC, abstractmethod

from ksecrets.helpers.pydantic import BaseModel


class BaseServiceResponse(BaseModel):
    pass


class BaseService[T: BaseServiceResponse](BaseModel, ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> T: ...
