# Test a website(s) for its availability. Send mail to some people, if the site is down.
# a. Use the python package requests.

import requests
from mailSender import send_mail

url='https://w3schools.com/python/demopage.htm'
url2='https://mynewsite377923690.wordpress.com/'
mailTo='3065037854@qq.com'
#get Request Status Code
def getStatusCode(url):
    x = requests.get(url)
    print(x.headers)
    print(x.status_code)
    print(x.request)
    return x.status_code,x.content


def mailFlow():
    accessUrl=url2
    status_code,content=getStatusCode(accessUrl)
   # mailContent=f'url:{ accessUrl },status_codez:{status_code}\n content:{content}'
    mailContent='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDDGKjHNusHSCxYRMlTZAB93t4xBHvfPN3H4qo8IZxEmc95N9LXr+TcelCZ6vn1V4w/2Om+tGgKFx6pXi42BlM/GI86j1gbjDzP6M0LrbSa/23mIcWGa/mudgOBdxVIjOQWgDSpJN+qFJ6sMaDRdn+Tl4Uwj+BapduVOt3izr/PT8pQ1XMJB4XXP/aldbvbMixVX1nD1orBbOczlniLKE5HT6xpHyrORZgDaXvQE8oboCXG2VvRr9IbGdSP8bsKuSjJJAAdxQ3g4Ma9GFoAH6vY+2rp5I8BoGTARbzkeAwbGlv7mXMxySupj3+B9irB7zBgcocEEZullYdbDFsDW6n0ZMx1Ho4KygxbT1tWME46tETlL2uvTL14uvQmspRO4EmNjtnXrOIw8A+OBpP1fEUI/Pdyq6GRBVh+wY8fhw2Bmxvr7UriQbtmrPUA7pR6FnsR498D1u46rXGbU8PEka1nFAWT4tNyL4qPqkOj0t9Bb1XJGG9vigNPMXLJm6RGqPYcDYZw/70AqdNbs7Qz+CpnrOv0DxSDA9fMHees+sjeOoU5I5reagKPjSLIBKcACuY/KO9pqEeiW22UFwJG7nJNtqDkT2vY00sMhHj5ChtohTUYIex40ZzXM5PKq41ugd8RtBr0R+xGHJheZd/pfjIyoWuzHbw0s1jjChx4v8a0tQ== hugoyang1996@qq.com'
    if status_code!=200:
        send_mail(receiver=mailTo,mail_title=f'Access failed{accessUrl}',mail_content=mailContent)
    else:
        print(f"Access to { accessUrl }Success, status code {status_code}\n content:{content}")

mailFlow()

