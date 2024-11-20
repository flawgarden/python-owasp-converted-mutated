from typing import TypeVar, Generic, Any


T = TypeVar("T")


class GenericClass(Generic[T]):
    def __init__(self, value: T):
        self.__value = value

    def get_value(self) -> T:
        return self.__value

    def get_object_value(self) -> Any:
        return self.__value


class A:
    pass


class B(A):
    pass


class C(B):
    pass