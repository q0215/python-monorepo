from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from ..application.use_cases.register_user import RegisterUserUseCase
from ..containers import Container


@inject
def get_register_user_use_case(
    use_case: RegisterUserUseCase = Depends(Provide[Container.register_user_use_case]),
) -> RegisterUserUseCase:
    return use_case
