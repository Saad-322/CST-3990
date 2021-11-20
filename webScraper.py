from bs4 import BeautifulSoup
import requests
import time

def find_jobs(p):
    page = p
    if p == 0:
        content = requests.get("https://www.gradcracker.com/search/computing-technology/graduate-jobs-in-london-and-south-east").text
    else:
        content = requests.get("https://www.gradcracker.com/search/computing-technology/graduate-jobs-in-london-and-south-east?page="+str(page)).text       
    soup = BeautifulSoup(content,"lxml")
    jobs = soup.find_all("div",class_="job-item")
    for job in jobs: 
        try:
            h2_tag = job.find("h2").a
            name = h2_tag.text.strip()
            url = h2_tag['href'].strip()
            subtitle = job.find("h2").div
            info = job.find_all("ul",class_="item fa-ul")
            information_S_L = info[0].find_all("li")
            information_G_D = info[-1].find_all("li")
            salary = information_S_L[0].text.strip()
            location = information_S_L[-1].text.strip()
            grades = information_G_D[0].text.strip()
            deadline = information_G_D[-1].text.strip()

            with open(f"jobs.txt","a") as f:
                f.write(f"Name: {name} \n")
                f.write(f"Location: {location} \n")
                f.write(f"Deadline: {deadline} \n")
                f.write(f"Salary: {salary} \n")
                f.write(f"Grades: {grades} \n")
                # f.write("Subtitle: ",subtitle.text.strip().replace('  •  ',''))
                f.write(f"URL: {url} \n")
                f.write(f"\n")
            print("File Saved")
        except:
            pass
if __name__ == '__main__':
    p = 0
    while(p<=6):
        find_jobs(p)
        seconds_wait = 1
        print(f"waiting {seconds_wait} seconds")
        time.sleep(seconds_wait)
        p = p + 1
   