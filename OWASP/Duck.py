class Duck:
    def quack(self, arg):
        return arg


class NotADuck:
    def quack(self, arg):
        return "fixed_string"


class DefinitelyNotADuck:
    def fake_quack(self, arg):
        return "fixed_string"


class DynamicDuck:
    pass


class DuckWithAttribute:
    def __init__(self, arg):
        self.my_arg = arg
        self.constant = 42

    def quack(self, arg):
        return self.my_arg


class FakeDuckWithAttribute:
    def __init__(self, arg):
        self.my_arg = arg

    def quack(self, arg):
        return self.my_arg