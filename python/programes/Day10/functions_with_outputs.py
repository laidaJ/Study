#Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't type right string"

    return f_name.title() + " " + l_name.title()

print(format_name(input("Type your first name:"), input("Type your last name:")))
