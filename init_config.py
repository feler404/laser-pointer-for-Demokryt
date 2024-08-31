
config = [
    {"name": "X_POINT", "description": "", "init_value": 90, "min_value": 90, "max_value": 130},
    {"name": "Y_POINT", "description": "", "init_value": 70, "min_value": 70, "max_value": 110},
    # {"name": "SOCKET_IP", "description": "", "init_value": "0.0.0.0"},
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

    # def __setattr__(self, key, value):  # Nie działa dla micropython

    def set(self, value):
        value = int(value)
        if value < self.min:
            value = self.min
        elif value > self.max:
            value = self.max
        self.value = value


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


class Logger:

    def __init__(self, time_nf=None, log_nf=None):
        self.time_nf = time_nf
        self.log_nf = log_nf

    def get_time(self):
        if self.time_nf:
            return self.time_nf(':')
        else:
            return "00:00:00"

    def propagate_log(self, log):
        if self.log_nf:
            self.log_nf(log)
        print(log)

    def log(self, message, level="INFO"):
        time = self.get_time()
        log = "%s [%s]: %s" % (time, level, message)
        self.propagate_log(log)

    def info(self, message):
        self.log(message, "INFO")

    def warning(self, message):
        self.log(message, "WARNING")

    def error(self, message):
        self.log(message, "ERROR")


STATE = {param['name']: init_param(**param) for param in config}
STATE['WIFI_SID'] = 'DEMOKRYT3-ROS2-3A2'
STATE['WIFI_PASS'] = '39005816'
logger = Logger()
