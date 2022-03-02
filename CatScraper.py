from selenium import webdriver
from EmailHandler import EmailHandler
from db_manager import DBManager
import time

EMAIL_HANDLER = EmailHandler()
DB_MANAGER = DBManager()

while True:
    time.sleep(3600)
    try:
        message = f'Subject: New cats up for adoption!\n\n Hey McFamily, new cats were posted for adoption:'
        URL = 'https://petharbor.com/search.asp?searchtype=ADOPT&bgcolor=639ace&text=ffffff&link=FEFF81&alink=FF814A&vlink=FEFF81&col_hdr_bg=004d84&col_hdr_fg=efeff7&col_bg=004d84&col_fg=ffffff&SBG=004d84&rows=10&imght=120&imgres=thumb&view=sysadm.v_animal_short&fontface=tahoma&zip=80443&miles=10&shelterlist=%27TRNT1%27,%27TRNT%27,%27TRNT2%27,%27TRNT3%27,%27TRNT4%27,%27TRNT5%27'
        PATH = 'chromedriver/chromedriver' 
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        BROWSER = webdriver.Chrome(PATH, options=option)
        BROWSER.get(URL)
        
        cat_radio_button = BROWSER.find_element_by_xpath('/html/body/form/div/center/table/tbody/tr[2]/td[1]/p[3]/font/input')
        cat_radio_button.click()
        
        time.sleep(1)

        BROWSER.find_element_by_name("cmdSearchNow").click()


        try:
            cat_table = BROWSER.find_element_by_class_name('ResultsTable')
            
        except:
            no_cats = True

        else:
            counter = 0
            available_cats = cat_table.find_elements_by_css_selector('tr')
            #iterate through each cats row
            for i in range(0, len(available_cats)):
                #first row returns table definitions, so skip
                if i != 0:
                    #Get info from cats row
                    cat_info = available_cats[i].find_elements_by_css_selector('td')
                    name_info = cat_info[2].text.split(" ")
                    name = name_info[0]
                    code = name_info[1]
                    gender = cat_info[3].text
                    color = cat_info[4].text
                    breed = cat_info[5].text
                    age = cat_info[6].text
                    location = cat_info[7].text

                    if DB_MANAGER.is_seen(name) == False:
                        counter += 1
                        message += "\n\n#{}: {} is a {} coloured {}. {} is a {} {} who is located at {}. {}'s code: {}".format(counter, name, breed, color, name, age, gender, location, name, code)
                        DB_MANAGER.add_to_seen(name)

            if counter != 0:
                email_list = ['ethan_mcfarland@outlook.com']#,'scottmcf@bell.net','highland_las@hotmail.com']
                for email in email_list:
                    EMAIL_HANDLER.send_email(message,email)

            else:
                print("no cats")

    finally:
        time.sleep(1)
        BROWSER.quit()



