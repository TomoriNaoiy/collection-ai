from selenium import webdriver
import os
from json import dump, load
import time
import re
import os
import csv
from selenium.webdriver.common.by import By
from lxml import etree
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



f=open(r'C:\Users\宋志坤\Desktop\新建文件夹\学习\新建文件夹\zhihu.csv','w',encoding='utf-8')
writer=csv.writer(f)
t=0

driver = webdriver.Chrome()
actions=ActionChains(driver)
# if os.path.exists("cookies"):
#     cookies=load(open("cookies"))
#     for cookie in cookies:
#         driver.add_cookies(cookie)
# else:
#     while driver.current_url != "https://www.zhihu.com/":
#             time.sleep(1)
#     dump(
#             [

#                 {"name":cookie["name"],"value":cookie["value"]}
#                 for cookie in driver.get_cookies()
#             ],
#             open("cookies","w"),

#     )

# 加载指定的页面
driver.get('https://www.zhihu.com/')

time.sleep(20)
# 这里手动登录

driver.get('https://www.zhihu.com/topic/19554298/top-answers')
driver.maximize_window()
time.sleep(5)
#print(page)
# question1=page.xpath('//div/a')
# print(question1)
#driver.find_element(By.XPATH,'//button')
for _ in range(1):
    #js=f"window.scrollTo(0, {x*500});"
    js="window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(2)
time.sleep(5)

question1=driver.find_elements(By.XPATH, "//h2/div/a")
url_list=[]
title_list=[]
Answer=[]
question_content=[]
for question in question1:
    url_list.append(question.get_attribute("href"))
    title_list.append(question.text)
# 爬取答案
writer.writerow(title_list)
for url in url_list:
    t+=1
    if(t==10):  
        break
    driver.get(f"{url}")
    time.sleep(5)
    
    
    try:
         stretch=driver.find_element(By.XPATH,'//div[@class="QuestionRichText QuestionRichText--expandable QuestionRichText--collapsed"]/div/button').click()
         question_content.append(driver.find_element(By.XPATH,'//div[@class="QuestionRichText QuestionRichText--expandable"]').text)
      
    except:
        try:
            question_content.append(driver.find_element(By.XPATH,'//div/span[@class="RichText ztext css-ob6uua"]').text)
        except:
            question_content.append("没有内容")
  
    time.sleep(5)
    try:
        driver.find_element(By.XPATH,'//div[@class="Card ViewAll"]/a').click()
    except:
        pass

    for i in range(10):
    
        js_real=f"window.scrollTo(0, {i*5000});"
        driver.execute_script(js_real)
        actions.send_keys(Keys.PAGE_UP).perform()
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        
    answers=driver.find_elements(By.XPATH,'//div[@class="ContentItem AnswerItem"]')
    answer_text=[element.text for element in answers]
    Answer.append(answer_text)
    

        

    



print('*'*100)





#写入csv

driver.quit()
writer.writerow(question_content)
for answer in Answer:
    writer.writerow(answer)
# for question in title_list:
#     print(question)
#     f.write(question+',')
# f.write('\n')
# f.write("问题内容"+',')
# for q_c in question_content:
#      if q_c==1:
#          f.write("None")
#      else:
#         f.write(q_c,+ ",")
# f.write("\n")
# f.write("回答"+",")
# for answers in Answer:
#     for answer in answers:
#         print(answer)
#         f.write(answer)
#     f.write(',')

f.close()

