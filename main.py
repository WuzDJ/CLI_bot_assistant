contacts = {"bara":"123",
            "ban":"345"}

def hello():
    return "How can I help you?"

def add(name, phone_num):
    contacts[name] = phone_num

def change(name, phone_num):
    if name in contacts.keys():
        contacts[name] = phone_num

def phone(name):
    return "{:^10} {:^10}".format(name, contacts[name])

def show_all():
    all = []
    for name, phone_num in contacts.items():
        line = "{:^10} {:^10}".format(name, phone_num)
        all.append(line)
    return "\n".join(all)

def good_bye():
    return "Good bye!"

commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all
}

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            print("Key Error")
        except ValueError:
            print("Value Error")
        except IndexError:
            print("Index Error")
        except TypeError:
            print("TypeError")
    return inner

def get_handler(command):
    return commands[command]

@input_error
def handler(func, modifier) -> str:
    result = func(*modifier)
    if result is None:
        func(*modifier)
    return result


def main():    
    while True:
        user_input = input(">>> ")
        user_input = user_input.strip()
        #ok
        if user_input.lower() in ("good bye", "close", "exit"):
            print(good_bye())
            break
        #not ok, calling exception by add(), change(), phone() 
        if user_input.lower() in commands:
            print(get_handler(user_input.lower())())
            continue
        #ok
        user_input = user_input.split(" ")
        command = user_input[0].lower()
        modifier = user_input[1:]
        if command in commands:
            func = get_handler(command)
            result = handler(func, modifier)
            if result is not None:
                print(result)
            continue
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()