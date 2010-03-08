from datetime import datetime

def transform_datetime(dt):
    """ converts datetime parameter"""                               

    if dt is None:
        dt = ''
    else:
        assert isinstance(dt, datetime)
        dt = dt.strftime('%Y-%m-%d %H:%M:%S')
 
    return dt


def flatten(params, key=None):
    """ flatten nested dictionaries and lists """
    flat = {}
    for name, val in params.items():
        if key is not None and not isinstance(key, int):
            name = "%s[%s]" % (key, name)
        if isinstance(val, dict):
            flat.update(flatten(val, name))
        elif isinstance(val, list):
            flat.update(flatten(dict(enumerate(val)), name))
        elif val is not None:
            flat[name] = val
    return flat

