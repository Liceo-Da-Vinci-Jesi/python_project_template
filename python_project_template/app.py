from python_project_template import easy_module
from python_project_template import easy_class


def run():
    num = easy_module.easy_number()
    print("easy module num:", num)
    
    c = easy_class.EasyClass(num)
    string = c.write_sentence()
    print("easy class, write sentence method:", string)
    
    return
