class ClassWrapper:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class ClassWrapperEmpty:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return "fixed_string"