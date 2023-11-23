from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns = ["RK","Team","Image Urls","Total Points","+/-","Previous Points","Positions"]

def get_teams_details(row):
    details = row.text.split('\n')
    print(details)
    
    contents = {}
    contents["RK"] =              details[0]
    contents["Team"] =            details[1]
    contents["Total Points"] =    details[2]
    contents["+/-"] =             details[3]
    #contents["Previous Points"] = details[4]
    #contents["Positions"] =       details[5]

    contents["Image Urls"] = row.find_element(By.CLASS_NAME, 'image_img__JuDY4').get_attribute('src')

    return contents



def main():
     
    driver = webdriver.Chrome()

    teams_data = []

    for page_id in range(1,11):
        url =f"https://www.fifa.com/fifa-world-ranking/men?dateId=id14177"
        driver.get(url)
        rankings = driver.find_element(By.CLASS_NAME, 'ranking-table-big_cardsContainer__RwEb7')
        rows = rankings.find_elements(By.CLASS_NAME, 'row_rankingTableFullRow__Y_A4i')

    #row_contents = []

        
    
    
        for idx, row in enumerate(rows):
            if idx % 1 == 0:
                teams_data.append(get_teams_details(row))
        time.sleep(10)

    print(len(teams_data))
    driver.close()
    
    return

    

if __name__== "__main__":
     main()