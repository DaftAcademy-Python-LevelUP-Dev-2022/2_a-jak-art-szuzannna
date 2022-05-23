def greeter(func):
    def say_aloha(*args, **kwargs):
        name = func(*args, **kwargs)
        name = f"Aloha {name.title()}"
        return name
    return say_aloha


def sums_of_str_elements_are_equal(func):
    def comaprison(*args,**kwargs):
        str_of_numbers = func(*args, **kwargs)
        list_of_numbers =[]
        list_of_strings = str_of_numbers.split()
        for string_ in list_of_strings:
            result = 0
            for char in string_:
                if char == "-":
                    minus = -1
                    continue
                char = int(char)
                try:
                    char = char * minus
                except NameError:
                    pass
                result += char
            list_of_numbers.append(result)
            try:
                del minus
            except UnboundLocalError:
                pass
        if list_of_numbers[0] == list_of_numbers[1]:
            return "" + str(list_of_numbers[0])+" == " + str(list_of_numbers[1])
        else:
            return "" + str(list_of_numbers[0])+" != " + str(list_of_numbers[1])
    return comaprison


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
