def defangIPaddr(address : str) -> str:
    return "[.]".join(str(i) for i in address.split("."))