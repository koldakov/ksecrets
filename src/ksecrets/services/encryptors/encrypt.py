from pydantic import SecretStr

from ksecrets.services._base import BaseService, BaseServiceResponse


class EncryptServiceResponse(BaseServiceResponse):
    text: str


class EncryptService(BaseService[EncryptServiceResponse]):
    text: SecretStr
    password: SecretStr

    def _encrypt(self) -> str:
        raise NotImplementedError()

    def __call__(self, *args, **kwargs) -> EncryptServiceResponse:
        return EncryptServiceResponse(text=self._encrypt())
