def new_representation(num):
    try:
        num = float(num)
        hex_repr = float.hex(num)
    except ValueError:
        raise ValueError("Invalid input. Please provide a valid floating-point number.")
    return hex_repr

def hex_to_float(hex_str):
    return float.fromhex(hex_str)

def compare_numbers(num1_hex, operator_hex, num2_hex):
    operators = {
        "3c": "<",
        "3e": ">",
        "3c3d": "<=",
        "3e3d": ">=",
        "3d3d": "==",
        "213d": "!="
    }

    try:
        num1 = hex_to_float(num1_hex)
        num2 = hex_to_float(num2_hex)
        operator = operators.get(operator_hex)
        if not operator:
            raise ValueError("Invalid operator. Supported operators are: '<', '>', '<=', '>=', '==', '!='")
    except ValueError:
        raise ValueError("Invalid input. Please provide valid numbers.")

    return eval(f"{num1} {operator} {num2}")
