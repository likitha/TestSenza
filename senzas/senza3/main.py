import jsonpickle
from senza3_dep.utils import stringutil

def kensci_senza(var1):
    output = jsonpickle.encode({'foo': True}, max_depth=0)
    return output + str(var1) + stringutil.remove_vowels(var1)
