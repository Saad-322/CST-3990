from bs4 import BeautifulSoup
with open("home.html","r") as home_html_file:
    content = home_html_file.read()
    soup = BeautifulSoup(content,"lxml")
    courses = soup.find_all("div",class_="card")
    for course in courses:
        print(course.h5.text.split()[0])
        print(course.p.text)
        print(course.a.text.split()[-1])
