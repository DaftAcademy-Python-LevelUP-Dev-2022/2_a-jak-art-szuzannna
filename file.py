def greeter(func):
    def say_aloha(*args, **kwargs):
        name = func(*args, **kwargs)
        name = f"Aloha {name.title()}"
        return name
    return say_aloha


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
