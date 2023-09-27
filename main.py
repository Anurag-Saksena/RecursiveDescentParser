variables = [[None, None] for i in range(100)]
variable_count = 0


def file_input_to_nested_list():
    with open("input.txt") as txt:
        lines = txt.readlines()
        nested_array = []
        for line in lines:
            op, arg1, arg2, res = [item.strip() for item in line.split()]
            nested_array.append([op, arg1, arg2, res])
    return nested_array


def goto(statements_list: list[list[str]], statement_label: str):
    for statement_index in range(len(statements_list)):
        if statements_list[statement_index][3] == statement_label and statements_list[statement_index][0] == 'Label':
            return statement_index


def get_variable_value(variable):
    for variable_index in range(len(variables)):
        variable_data = variables[variable_index]
        if variable_data[0] == variable:
            value = variable_data[1]
            if is_numeric(value):
                if '.' in str(value):
                    value = float(value)
                else:
                    value = int(value)
            return value


def bool_to_number(value):
    if value:
        return 1
    else:
        return 0


def set_variable_value(variable, value):
    global variables
    value = str(value)
    variable_present = False
    for variable_index in range(len(variables)):
        if variables[variable_index][0] == variable:
            variable_present = True
            variables[variable_index][1] = parse_value(value)
    if not variable_present:
        global variable_count
        variable_count += 1
        variables[variable_count - 1][0] = variable
        variables[variable_count - 1][1] = parse_value(value)


def is_numeric(value_string: str) -> bool:
    value_string = str(value_string)
    for index in range(len(value_string)):
        character_value = value_string[index]
        if (character_value == '0' or character_value == '1' or character_value == '2' or character_value == '3' or
                character_value == '4' or character_value == '5' or character_value == '6' or character_value == '7' or
                character_value == '8' or character_value == '9' or character_value == '.'):
            pass
        else:
            return False
    return True


def parse_value(value):
    if str(value)[0] == "'":
        return value
    elif is_numeric(str(value)):
        if '.' in str(value):
            value = float(value)
        else:
            value = int(value)
        return value
    else:
        return get_variable_value(value)


def parse_statement_list(statements_list: list[list[str]]):
    statement_index = 0
    while statement_index != len(statements_list):
        statement = statements_list[statement_index]
        operator = statement[0]
        result = statement[3]
        arg1 = statement[1]
        arg2 = statement[2]

        if operator == '=':
            set_variable_value(result, arg1)

        elif operator == 'Label':
            pass

        elif operator == '+':
            set_variable_value(result, parse_value(arg1) + parse_value(arg2))
        elif operator == '-':
            set_variable_value(result, parse_value(arg1) - parse_value(arg2))
        elif operator == '*':
            set_variable_value(result, parse_value(arg1) * parse_value(arg2))
        elif operator == '/':
            set_variable_value(result, parse_value(arg1) / parse_value(arg2))
        elif operator == '%':
            set_variable_value(result, parse_value(arg1) % parse_value(arg2))
        elif operator == '>':
            set_variable_value(result, bool_to_number(parse_value(arg1) > parse_value(arg2)))
        elif operator == '<':
            set_variable_value(result, bool_to_number(parse_value(arg1) < parse_value(arg2)))
        elif operator == '>=':
            set_variable_value(result, bool_to_number(parse_value(arg1) >= parse_value(arg2)))
        elif operator == '<=':
            set_variable_value(result, bool_to_number(parse_value(arg1) <= parse_value(arg2)))
        elif operator == '!=':
            set_variable_value(result, bool_to_number(parse_value(arg1) != parse_value(arg2)))
        elif operator == '==':
            set_variable_value(result, bool_to_number(parse_value(arg1) == parse_value(arg2)))

        elif operator == 'not':
            set_variable_value(result, bool_to_number(not parse_value(arg1)))

        elif operator == 'if':
            if parse_value(arg1):
                statement_index = goto(statements_list, result)
                continue

        elif operator == 'goto':
            statement_index = goto(statements_list, result)
            continue

        elif operator == 'printf':
            print(parse_value(result))

        print(f"Statement parsed: {statement}")
        statement_index += 1


statement_list = file_input_to_nested_list()
parse_statement_list(statement_list)