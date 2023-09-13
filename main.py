contacts = {"bara":"123",
            "ban":"345"}

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            
        except KeyError:
            return ("Key Error")
        except ValueError:
            return ("Value Error")
        except IndexError:
            return ("Index Error")
        except TypeError:
            return ("TypeError")
        return result
    return inner

def hello():
    return "How can I help you?"

@input_error
def add(name, phone_num):
    contacts[name] = phone_num

@input_error
def change(name, phone_num):
    if name in contacts.keys():
        contacts[name] = phone_num

@input_error
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
        user_command = user_input.split(" ")
        command = user_command[0].lower()
        modifier = user_command[1:]
        
        if user_input.lower() in ("good bye", "close", "exit"):
            print(good_bye())
            break
        
        elif user_input.lower() in commands:
            result = get_handler(user_input.lower())()
            if result is not None:
                print(result)
            continue
        
        elif command in commands:
            func = get_handler(command)
            result = handler(func, modifier)
            if result is not None:
                print(result)
            continue
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()