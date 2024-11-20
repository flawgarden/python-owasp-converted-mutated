class NestedFieldsBase:
    values: list[str] | None
    value: str | None

    def __init__(self, value: str | None = None, initialValues: list[str] | None = None):
        self.value = value
        self.values = initialValues


class NestedFields1:
    value: str | None
    values: list[str] | None
    nested1: NestedFieldsBase

    def __init__(self, value: str | None = None, initialValues: list[str] | None = None):
        self.value = value
        self.values = initialValues
        self.nested1 = NestedFieldsBase(initialValues=initialValues, value=value)


class NestedFields2:
    value: str | None
    values: list[str] | None
    nested1: NestedFields1

    def __init__(self, value: str | None = None, initialValues: list[str] | None = None):
        self.value = value
        self.values = initialValues
        self.nested1 = NestedFields1(initialValues=initialValues, value=value)


class NestedFields3:
    value: str | None
    values: list[str] | None
    nested1: NestedFields2

    def __init__(self, value: str | None = None, initialValues: list[str] | None = None):
        self.value = value
        self.values = initialValues
        self.nested1 = NestedFields2(initialValues=initialValues, value=value)


class NestedFields4:
    value: str | None
    values: list[str] | None
    nested1: NestedFields3

    def __init__(self, value: str | None = None, initialValues: list[str] | None = None):
        self.value = value
        self.values = initialValues
        self.nested1 = NestedFields3(initialValues=initialValues, value=value)