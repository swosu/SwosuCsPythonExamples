# ---- Starter Code (modified: numbered menu + numeric input) ----

def build_services_dictionary():
    services = {
        'Air freshener': 1,
        'Rain repellent': 2,
        'Tire shine': 2,
        'Wax': 3,
        'Vacuum': 5
    }
    return services


def build_base_wash_price():
    base_wash = 10
    return base_wash


def build_numbered_menu(services_dict):
    """
    Creates a numbered menu so users can type 1, 2, 3... instead of service names.
    Returns a list of service names in menu order.
    """
    service_names = []
    for name in services_dict:
        service_names.append(name)
    return service_names


def print_numbered_menu(service_names, services_dict):
    print("Available additional services (enter the NUMBER, or 0 for none):")

    index = 0
    while index < len(service_names):
        menu_number = index + 1

        service_name = service_names[index]
        service_cost = services_dict[service_name]

        left = "  " + str(menu_number) + ") " + service_name + " - $"
        right = str(service_cost)
        line = left + right
        print(line)

        index = index + 1

    print("")  # blank line


def get_menu_choice(choice_number, max_number):
    prompt_a = "Enter additional service #"
    prompt_b = str(choice_number)
    prompt_c = " (0 for none, 1-"
    prompt_d = str(max_number)
    prompt_e = "): "
    prompt = prompt_a + prompt_b + prompt_c + prompt_d + prompt_e

    raw = input(prompt)
    return raw


def convert_to_int(raw_text):
    number = int(raw_text)
    return number


def is_choice_none(choice_number):
    none_value = 0
    result = choice_number == none_value
    return result


def is_choice_in_range(choice_number, max_number):
    low_ok = choice_number >= 0
    high_ok = choice_number <= max_number
    ok = low_ok and high_ok
    return ok


def choice_number_to_service_name(service_names, choice_number):
    # choice_number is 1-based; list index is 0-based
    index = choice_number - 1
    name = service_names[index]
    return name


# ---- Output / pricing helpers ----

def print_header():
    print("ZyCar Wash")


def print_base_wash_line(base_price):
    left = "Base car wash - $"
    right = str(base_price)
    line = left + right
    print(line)


def get_service_cost(services_dict, service_name):
    cost = services_dict[service_name]
    return cost


def print_service_line(service_name, service_cost):
    left = service_name + " - $"
    right = str(service_cost)
    line = left + right
    print(line)


def add_cost_to_total(current_total, cost_to_add):
    new_total = current_total + cost_to_add
    return new_total


def print_separator():
    print("-----")


def print_total_line(total_price):
    left = "Total price: $"
    right = str(total_price)
    line = left + right
    print(line)


# ---- Processing one choice (now numeric) ----

def process_one_numeric_choice(services_dict, service_names, choice_number, current_total):
    if is_choice_none(choice_number):
        return current_total

    service_name = choice_number_to_service_name(service_names, choice_number)
    cost = get_service_cost(services_dict, service_name)

    print_service_line(service_name, cost)
    current_total = add_cost_to_total(current_total, cost)

    return current_total


# ---- Main program runner ----

def run_car_wash_program(services_dict, base_price, service_names, choice1_num, choice2_num):
    total = 0

    print_header()
    print_base_wash_line(base_price)
    total = add_cost_to_total(total, base_price)

    total = process_one_numeric_choice(services_dict, service_names, choice1_num, total)
    total = process_one_numeric_choice(services_dict, service_names, choice2_num, total)

    print_separator()
    print_total_line(total)


# ---- Driver flow ----

services = build_services_dictionary()
base_wash = build_base_wash_price()

service_names = build_numbered_menu(services)
print_numbered_menu(service_names, services)

max_number = len(service_names)

raw1 = get_menu_choice(1, max_number)
raw2 = get_menu_choice(2, max_number)

choice1_num = convert_to_int(raw1)
choice2_num = convert_to_int(raw2)

# NOTE: This assumes valid numeric input. If you want, we can add a loop
# to re-prompt when the user types something out of range.
run_car_wash_program(services, base_wash, service_names, choice1_num, choice2_num)
