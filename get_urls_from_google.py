from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from time import sleep

#lists
key_persons = []
links_l = []
links_f = []
links_t = []
links_m = []
profiles = []
i = 0


#reading name
rf = open('persons.csv', 'r')
#rf = open('personsmini.csv', 'r')
dataReader = csv.reader(rf)
for row in dataReader:
    key_persons.append(row[0])
print(key_persons)
rf.close()
print('finished making key_persons')


print("---------------------------")
driver = webdriver.PhantomJS()
for key_person in key_persons:
    print(str(i+1) + "人目")
    driver.get('https://www.google.co.jp/')
    assert 'Google' in driver.title
#linkedin
    print("------------------------")
    print("getting the linkedin url")
    input_element = driver.find_element_by_name('q')
    input_element.send_keys(key_person + " linkedin")
    input_element.send_keys(Keys.RETURN)
    sleep(1)
    assert key_person in driver.title
    #filter and making the list
    for a in driver.find_elements_by_css_selector('h3 > a'):
        print(a.text)
        if 'LinkedIn' in a.text:
            links_l.append(a.text + " " + a.get_attribute('href'))
            break
        else:
            links_l.append("no links")
            break
    print("finished scrayping linkedin")

#facebook
    print("------------------------")
    print("getting the facebook url")
    driver.get('https://www.google.co.jp/')
    assert 'Google' in driver.title
    input_element = driver.find_element_by_name('q')
    input_element.send_keys(key_person + " facebook")
    input_element.send_keys(Keys.RETURN)
    sleep(1)
    assert key_person in driver.title
    #filter and making the list
    for a in driver.find_elements_by_css_selector('h3 > a'):
        print(a.text)
        if 'Facebook' in a.text:
            links_f.append(a.text + " " + a.get_attribute('href'))
            break
        else:
            links_f.append("no links")
            break
    print("finished scrayping facebook")

#Twitter
    print("-----------------------")
    print("getting the twitter url")
    driver.get('https://www.google.co.jp/')
    assert 'Google' in driver.title
    input_element = driver.find_element_by_name('q')
    input_element.send_keys(key_person + " twitter")
    input_element.send_keys(Keys.RETURN)
    sleep(1)
    assert key_person in driver.title
    #filter and making the list
    for a in driver.find_elements_by_css_selector('h3 > a'):
        print(a.text)
        if 'Twitter' in a.text:
            links_t.append(a.text + " " + a.get_attribute('href'))
            break
        else:
            links_t.append("no links")
            break
    print("finished scrayping Twitter")

#medium
    print("-----------------------")
    print("sgetting the medium url")
    driver.get('https://www.google.co.jp/')
    assert 'Google' in driver.title
    input_element = driver.find_element_by_name('q')
    input_element.send_keys(key_person + " medium")
    input_element.send_keys(Keys.RETURN)
    sleep(1)
    assert key_person in driver.title
    #filter and making the list
    for a in driver.find_elements_by_css_selector('h3 > a'):
        print(a.text)
        if 'Medium' in a.text:
            links_m.append(a.text + " " + a.get_attribute('href'))
            break
        else:
            links_m.append("no links")
            break
    print("finished scrayping Medium")

    i += 1

#making profiles list
for name, link, face, twitt, mediu in zip(key_persons, links_l, links_f, links_t, links_m):
    profiles.append([name, link, face, twitt, mediu])
#writing csvfile
print("writing in key_links")
with open('key_links.csv', 'a') as wf:
    writer = csv.writer(wf)
    for profile in profiles:
        writer.writerow(profile)
