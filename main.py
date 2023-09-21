contacts = {"bara":"123",
            "ban":"345"}

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            
        except KeyError:
            return ("Enter user name")
        except ValueError:
            return ("This command have no modifier")
        except IndexError:
            return ("Give me name and phone please")
        except TypeError:
            return ("Uncorrect name")
        return result
    return inner

def hello():
    return "How can I help you?"


def add(name, phone_num):
    contacts[name] = phone_num


def change(name, phone_num):
    if name in contacts.keys():
        contacts[name] = phone_num
    else:
        raise TypeError

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
    "show": show_all
}

def get_handler(command):
    return commands[command]

@input_error
def handler(command, modifier) -> str:
    if command == "hello" and len(modifier) != 0:
        raise ValueError
    if command == "show" and (len(modifier) != 1 or modifier[0].lower() != "all"):
        raise ValueError
    if command == "phone" and len(modifier) != 1:
        raise KeyError
    if command in ("add", "change") and len(modifier) != 2:
        raise IndexError
    func = get_handler(command)
    if command == "show":
        result = func()
    else:
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
        
        #elif user_input.lower() in commands:
        #    result = get_handler(user_input.lower())()
        #    if result is not None:
        #        print(result)
        #    continue
        
        elif command in commands:
            
            result = handler(command, modifier)
            if result is not None:
                print(result)
            continue
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()