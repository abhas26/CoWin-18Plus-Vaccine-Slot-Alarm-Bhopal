from selenium import webdriver
import time
import winsound

web =webdriver.Chrome()
web.maximize_window()
web.get('https://www.cowin.gov.in/home')

while(True):
    time.sleep(2)
    searchbyCity= web.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[1]/div/label/div')
    searchbyCity.click()
    time.sleep(1)
    selectState= web.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[1]/mat-form-field/div/div[1]')
    selectState.click()
    time.sleep(1)
    selectState= web.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/mat-option[21]/span')
    selectState.click()
    time.sleep(1)
    selectCity= web.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[2]/mat-form-field/div/div[1]')
    selectCity.click()
    time.sleep(1)
    selectCity= web.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/mat-option[9]/span')
    selectCity.click()
    time.sleep(1)
    smt= web.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[3]/button')
    smt.click()
    time.sleep(1)

    #18+slots
    smt= web.find_element_by_xpath('//html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[3]/div/div[1]/label')
    smt.click()
    time.sleep(3)
    slots = web.find_elements_by_css_selector('.vaccine-box.vaccine-box1.vaccine-padding')
    flag=0
    for slot in slots:
        s=slot.text.split('\n')
        for x in s:
            if x.isnumeric():
                flag+=1
                break
    print(flag,"Slots Avaiable")
    if flag>0:
        winsound.Beep(880,10000)
    web.refresh()
input()
web.close()
