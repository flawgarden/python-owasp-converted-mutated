class MagicClass:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"{self.arg}"

    def __repr__(self):
        return f"MagicClass({self.arg!r})"

    def __len__(self):
        return 1

    def __getitem__(self, key):
        return self.arg

    def __eq__(self, other):
        return self.arg == other.arg
