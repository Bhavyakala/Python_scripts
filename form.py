import requests
parameters = {"answers":"[{\"questionId\":\"r33cf4062eb384a798e1fd94b053cb8e3\",\"answer1\":\"Student\"},{\"questionId\":\"rf0c089621969422b9c0c080138f53641\",\"answer1\":\"UG\"},{\"questionId\":\"reb528d6cd15a4917b8eeb152740d47e5\",\"answer1\":\"Option 1, Option 2, Option 3\"}]","startDate":"2020-05-28T10:33:52.359Z","submitDate":"2020-05-28T10:34:19.158Z"}
import json
url1 = "https://forms.office.com/formapi/api/12b4fbf9-dea8-4490-bede-9cc40309ad61/users/d1a87db6-0921-4c49-9c02-ef92352bb637/forms('-fu0EqjekES-3pzEAwmtYbZ9qNEhCUlMnALvkjUrtjdUOVo2NU5BUDNNNjZJWVpNWk1WNTA3OUE1US4u')/responses"
# url ='https://forms.office.com/Pages/ResponsePage.aspx?id=-fu0EqjekES-3pzEAwmtYbZ9qNEhCUlMnALvkjUrtjdUOVo2NU5BUDNNNjZJWVpNWk1WNTA3OUE1US4u&amp;embed=true'
r = requests.post(url1,data=parameters)
print(r.status_code)
print(r.text.encode('utf8'))
json_string = json.loads(r.text)
# print(json_string)
print(json.dumps(json_string, sort_keys=True, indent=4))
# print(r.content)
# print(r.reason)
# print(r.headers)
# import io
# with io.open("requests_results.html", "w", encoding="utf-8") as f:
#     f.write(r.text)
# with open("requests_results.html", "w") as f:
    # f.write(r.text)
# print(r.text)
import re
re.split('[a-c]', '0a3B6', re.I)
type(re.sub('morning', 'evening', 'good morning'))

a=10
b=10
print(id(a)==id(b))

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
st = "Hello World"
print("st[0:5] is ", st[0:5]) 
m = re.search('a', 'The blue umbrella') 
m.re.pattern 
l = ['h','e','l','l','o']