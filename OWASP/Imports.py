import string

class SimpleImport:
    def func(self, arg):
        arg = str(arg)
        if arg[0] in string.ascii_letters:
            return arg
        return "fixed_string"


import string as string_import

class SimpleImportAlias:
    def func(self, arg):
        arg = str(arg)
        if arg[0] in string_import.ascii_letters:
            return arg
        return "fixed_string"


from string import ascii_letters

class SimpleImportFrom:
    def func(self, arg):
        arg = str(arg)
        if arg[0] in ascii_letters:
            return arg
        return "fixed_string"


from string import ascii_letters as ascii_letters_imported

class SimpleImportFromAs:
    def func(self, arg):
        arg = str(arg)
        if arg[0] in ascii_letters_imported:
            return arg
        return "fixed_string"


try:
    import not_existing_module
except ImportError:
    not_existing_module = None


class ImportNotExistingModule:
    def func(self, arg):
        if not_existing_module:
            return "fixed_string"
        else:
            return arg
