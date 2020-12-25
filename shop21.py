from service import *
import pyodbc
import datetime
import random as r

def generate_dates_birth_employees():
    range_dates_birth_employees = []
    date_start = datetime.date(1990, 9, 13)  
    date_end = datetime.date(1995, 9, 13)
    delta_dates = date_end - date_start
    for date in range(delta_dates.days + 1):
        range_dates_birth_employees.append(date_start + datetime.timedelta(date))
    return range_dates_birth_employees

def genarate_employees_info():
    employees_info=[]
    employees_status = ['женат', 'не женат']
    employees_children = ['да', 'нет']

    for i in range(10):
        employee_status = r.choice(employees_status)
        birth_employee = str (r.choice(generate_dates_birth_employees()))
        employee_children = r.choice(employees_children)
        employees_info.append((employee_status, birth_employee, employee_children))
    
    return employees_info
         



def genarate_products():
    products=['Ноутбук Acer aspire E-576-526GAl','Ноутбук Lenovo ThinkPad x230','Ноутбук Hp qualdragon 5544','Ноутбук Dell insporition 223','Нетбук Acer x257 fly',
    'Сартфон xiaomi redmi 5','Смартфон Ihone 11 pro','Смартфон Ihone 11 pro max','Телевизо xiaomi 55lv21',]
    return products  

def product_storage():
    storage=['Телевизо LG 2122grand 21']
    return storage

def product_cities():
    cities=['Сантехника','Быт_техника','Электро_техника']
    return  cities
    
def generate_full_name(list_fisrtnames, list_lastnames, list_patronymics):
    firstname = r.choice(list_fisrtnames)
    lastname = r.choice(list_lastnames)
    patronymic = r.choice(list_patronymics)
    if list_fisrtnames.index(firstname) >= 32:
        if patronymic[-2:] == "ич":
            patronymic = patronymic[:-2] + "на"
        else:
            patronymic = patronymic[:-2] + "овна"
        if lastname[-1] == "в" or lastname[-1] == "н":
            lastname = lastname + "а"
        elif lastname[-1] == "и" or lastname[-1] == "й":
            lastname = lastname[:-2] + "ая"
    full_name = [lastname, firstname, patronymic]
    return " ".join(full_name)

def generate_address_client(list_cities, list_streets):
    list_cities = open("cities.txt")
    list_streets = open("streets.txt")
    city = r.choice(list_cities)
    street = r.choice(list_streets)
    return " ".join([city, street, str(r.randint(1, 50))])
    


def main ():

    #list_cities = open("cities.txt")
    #list_streets = open("streets.txt")
    #print(generate_address_client(list_cities, list_streets))
    #print(generate_full_name(list_fisrtnames, list_lastnames, list_patronymics))
    #write_database("employees", generate_full_name(list_fisrtnames, list_lastnames, list_patronymics))
    #products = genarate_products()
    #write_database ("Product", products)
    #storage = product_storage()
    #write_database ("Product", storage)
    #print (genarate_employees_info())
    #write_database("Delliver",genarate_employees_info())
    #cities = product_cities()
    #write_database ("shop", cities)
    print (genarate_employees_info())
    write_database("Info",genarate_employees_info())

    







if "__main__" == __name__:
    #logging.config.fileConfig('logging_conf.ini')
    #logger = logging.getLogger()
    try:
        main()
    except Exception as error:
        #logger.error(error)
        print(error)