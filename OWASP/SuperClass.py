class SuperClass:
    pass


class SubClass(SuperClass):
    pass


from typing import final


@final
class SubSubClass(SubClass):
    pass


class SiblingClass(SuperClass):
    pass
