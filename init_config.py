
config = [
    {"name": "X_POINT", "description": "", "init_value": 1, "min_value": 90, "max_value": 130},
    {"name": "Y_POINT", "description": "", "init_value": 1, "min_value": 70, "max_value": 110},
    {"name": "IP_SOCKET", "description": "", "init_value": "0.0.0.0"},
    {"name": "SOCKET_PORT", "description": "", "init_value": 5000, "min_value": 1024, "max_value": 65535},
    {"name": "SOCKET_PARALEL", "description": "", "init_value": 1, "min_value": 1, "max_value": 10},
]


class IntParam:
    __slots__ = ('name', 'description', 'value', 'min', 'max')

    def __init__(self, name, description, init_value, min_value, max_value):
        self.name = name
        self.description = description
        self.min = min_value
        self.max = max_value
        self.value = init_value

    def __str__(self):
        return "%s=%d" % (self.name, self.value)

    def __repr__(self):
        return "%s=%d" % (self.name, self.value)

    def __setattr__(self, key, value):
        if key == 'value':
            value = int(value)
            if value < self.min:
                value = self.min
            elif value > self.max:
                value = self.max
        super().__setattr__(key, value)


class StrParam:
    __slots__ = ('name', 'description', 'value')

    def __init__(self, name, description, init_value):
        self.name = name
        self.description = description
        self.value = init_value

    def __str__(self):
        return "%s=%s" % (self.name, self.value)

    def __repr__(self):
        return "%s=%s" % (self.name, self.value)

    def __setattr__(self, key, value):
        if key == 'value':
            value = str(value)
        super().__setattr__(key, value)


def init_param(**param_config):
    value = param_config.get('init_value')
    if isinstance(value, int):
        return IntParam(**param_config)
    elif isinstance(value, str):
        return StrParam(**param_config)
    else:
        raise ValueError("Nieobsługiwany typ wartości początkowej parametru: %s" % type(value))


STATE = {param['name']: init_param(**param) for param in config}
