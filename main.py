contacts = {"bara":"123",
            "ban":"345"}

def hello(): #ok
    return "How can I help you?"

def add(name, phone_num):
    contacts = {name: phone_num}

def change(name, phone_num):
    contacts = {name: phone_num}

def phone(name):
    print("{:^10} {:^10}".format(name, contacts[name]))

def show_all(): #ok
    all = []
    for name, phone_num in contacts.items():
        line = "{:^10} {:^10}".format(name, phone_num)
        all.append(line)
    return "\n".join(all)

def good_bye(): #ok
    return "Good bye!"

commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all#,
    #("good bye", "close", "exit"): good_bye
}

def input_error(func):
    def inner(*args):
        try:
            func(*args)
        except KeyError:
            print("Key Error")
        except ValueError:
            print("Value Error")
        except IndexError:
            print("Index Error")
    return inner

def handler(command):
    return commands[command]

#@input_error
def parser(user_input):
    user_input = user_input.strip()
    if user_input.lower() in commands:
        func = handler(user_input.lower())
    user_input = user_input.split(" ")
    command = user_input[0]
    func = handler(command)
    #func(user_input[1:])


def main():    
    while True:
        user_input = input(">>> ")
        user_input = user_input.strip()
        if user_input.lower() in ("good bye", "close", "exit"):
            print("Good bye!")
            break
        if user_input.lower() in commands:
            print(handler(user_input.lower())())
        
        #parser(user_input)

if __name__ == "__main__":
    main()