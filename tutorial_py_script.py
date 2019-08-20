"""
apple= int(67)
float = 67.86
print(apple)
my_string="i am sparsh"
print(my_string)
my_string=my_string.replace("a","?")
print(my_string)
pretty=bool(2)
print(pretty)
"""
import requests, bs4, webbrowser
username = str(input("Enter Username:\t"))
url = "http://www.spoj.com/users/" + username
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as e:
    print("Username not found")
 
soup = bs4.BeautifulSoup(res.text, 'html.parser')
 
if not soup.select('#user-profile-left'):  # #defines id in html
    print("User Not Found")
else:
    solved = soup.select('#user-profile-tables > div >
                         table.table.table-condensed a')
    sollist = []
    for ques in solved:
        #print(ques.text)
        sollist.append(ques.text)
 
    todo = soup.select('#user-profile-tables a')
    todolist = []
    for q in todo:
        #print(q.text)
        if q.text not in sollist:
            todolist.append(q.text)
 
    #print(todolist)
 
    question = str(input("Enter Question code:\t"))
 
    if question.upper() in sollist:
        print(question + " is solved")
 
    elif question.upper() in todolist:
        print(question + " is in todolist")
 
    else:
        print(question + " not attempted")