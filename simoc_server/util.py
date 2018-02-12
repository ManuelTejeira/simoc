

def load_db_attributes_into_dict(attributes, target=None):
    if target is None:
        target = {}

    for attribute in attributes:
        # get type of attribute
        if attribute.value_type == type(None).__name__:
            value = None
        else:
            value_type = eval(attribute.value_type)
            value_str = attribute.value
            value = value_type(value_str)
        attribute_name = attribute.name
        target[attribute_name] = value

    return target


def extend_dict(dict_a, dict_b, in_place=False):
    return dict(dict_a, **dict_b)

def subdict_from_list(d, l):
    """Return a subset of d from a list of keys, l
    
    Parameters
    ----------
    d : dict
        Dictionary to take subset from
    l : list
        list of keys to make the subet
    
    Returns
    -------
    dict
        the subset of d defined by l
    """
    return {key:d[key] for key in l if key in d}