from pydantic import SecretStr

from ksecrets.services._base import BaseService, BaseServiceResponse


class DecryptServiceResponse(BaseServiceResponse):
    text: SecretStr


class DecryptService(BaseService[DecryptServiceResponse]):
    text: str
    password: SecretStr

    def _decrypt(self) -> SecretStr:
        raise NotImplementedError()

    def __call__(self, *args, **kwargs) -> DecryptServiceResponse:
        return DecryptServiceResponse(text=self._decrypt())
