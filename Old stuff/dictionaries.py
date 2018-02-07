import string

def get_personal_data()->dict:
    """

    :return: Returns a dictionary of personal information
    """
    personal_data = {"name":"Charles","a_role":"student"}
    return personal_data

def main() -> int:
    default_dict = dict()
    print(default_dict)
    initialized_dict = dict([('name', 'Charles'), ('a_role', 'Joker')])
    simple_init_dict = dict(name='Charles', a_role='student')
    print(initialized_dict)
    print(simple_init_dict)
    simple_init_dict['a_role'] = 'Joker'
    print(simple_init_dict)
    my_comprehension = {x:x**2 for x in range(5)}
    print(my_comprehension)
    s = "Mary had a little,".translate({ord(i): None for i in string.punctuation})
    print(s)


    return 0




if __name__ == '__main__':
    main()
