from selenium import webdriver
from tabulate import tabulate




driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")
rows=len(driver.find_elements_by_xpath("//*[@id='example']/tbody/tr"))
columns=len(driver.find_elements_by_xpath("//*[@id='example']/tbody/tr[1]/td"))
print("No of rows:",rows)
print("No of columns:",columns)
print("-----------------------------------------------------------------------------------------------------------------------")
print ("Name"+	"                Position    "+	"        Office     "+	"      Age   "+	"      Start date  "+	"   Salary  ")
print("-----------------------------------------------------------------------------------------------------------------------")
for r in range(1,rows+1):
    for c in range(1,columns+1):
        value=driver.find_element_by_xpath("//*[@id='example']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        tabular=print(value,end='   ')
    print(tabulate(tabular))
driver.quit()
