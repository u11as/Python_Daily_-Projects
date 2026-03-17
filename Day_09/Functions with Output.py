def format_name(f_name, l_name):
    formated_f_name=(f_name.title())
    formated_l_name=(l_name.title())
    return (f"{formated_f_name} {formated_l_name}")

output = format_name("hello", "HII")
print(output)


def hello(text):
    return text + text

def hii(text):
    return text.title()

output = hii(hello("how are you"))
print(output)

