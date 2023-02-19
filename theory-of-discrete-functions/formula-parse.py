VARIABLES = ["x", "y", "z"]

FUNCTIONAL_SYMBOLS = ["→", "~", "·", "&", "|", "↓", "˅"]

SIGMA = {"→": lambda x, y: not x or y,
        "~": lambda x, y: (x and y) or (not x and not y),
        "·": lambda x, y: x and y,
        "&": lambda x, y: x and y,
        "|": lambda x, y: not (x and y),
        "↓": lambda x, y: not (x or y),
        "˅": lambda x, y: x or y}

def is_formula