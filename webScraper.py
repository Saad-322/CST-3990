from bs4 import BeautifulSoup
import requests
page = 0
content = requests.get("https://www.gradcracker.com/search/computing-technology/graduate-jobs-in-london-and-south-east").text
while page <= 1:
    soup = BeautifulSoup(content,"lxml")
    jobs = soup.find_all("div",class_="job-item")
    for job in jobs: 
        try:
            name = job.find("h2").a
            url = name['href']
            subtitle = job.find("h2").div
            info = job.find_all("ul",class_="item fa-ul")
            information_S_L = info[0].find_all("li")
            information_G_D = info[-1].find_all("li")
            salary = information_S_L[0].text.strip()
            location = information_S_L[-1].text.strip()
            grades = information_G_D[0].text.strip()
            deadline = information_G_D[-1].text.strip()

            print("Name: ",name.text.strip())
            print("Location: ",location)
            print("Deadline: ",deadline)
            print("Salary: ",salary)
            print("Grades: ",grades)
            # print("Subtitle: ",subtitle.text.strip().replace('  •  ',''))
            print("URL: ",url.strip())
            print()
        except:
            pass
    page = page + 1 
    content = requests.get("https://www.gradcracker.com/search/computing-technology/graduate-jobs-in-london-and-south-east?page="+str(page)).text       
    
   