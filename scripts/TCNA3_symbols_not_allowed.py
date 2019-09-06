import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('D:\chromedriver')
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/manager/addAccount.php")


alphabet = string.ascii_lowercase + string.ascii_uppercase
spec_chars = "!\"#$%&'()*+,-./:1;<=>?@[\]^_`{|}~"

customer_id_field = driver.find_element_by_name("cusid")
custid_rmessage = driver.find_element_by_id("message14")
lst = []
for i in spec_chars:
    customer_id_field.send_keys(i)
    if custid_rmessage.text != "Special characters are not allowed":
        lst.append(i)
        customer_id_field.clear()
    else:
        customer_id_field.clear()
        
for i in alphabet:
    customer_id_field.send_keys(i)
    if custid_rmessage.text != "Characters are not allowed":
        lst.append(i)
        customer_id_field.clear()
    else:
        customer_id_field.clear()



print("The following symbols are allowed:\n", lst)
driver.close()