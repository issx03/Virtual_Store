def generate_input(*data):
    return [input(f" -> {d.capitalize()}: ").strip().lower() for d in data]

def generate_id(prefix:str,list:list):
    if list:
        return f"{prefix.strip()}{(max([int(id[len(prefix)+1:]) for id in list]) + 1):0>3}"
    
    return f"{prefix}001"