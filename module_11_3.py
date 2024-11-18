import inspect


def introspection_info(obj):
    result = {}
    att_list = []
    result['type'] = type(obj)
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        att_list.append(type(attr))
    result['attributes'] = att_list
    result['methods'] = dir(obj)
    result['module'] = inspect.getmodule(obj)
    return result


class Randclass:
    elem = 15

    def __init__(self):
        randlist = [1, 2, 5]
        self.randlist = randlist
        randstr = 'text'
        self.randstr = randstr
        randfloat = 15.5
        self.randfloat = randfloat

    def randfunc(self):
        x = self.randstr
        print(x)


x = Randclass()
number_info = introspection_info(x)
print(number_info)