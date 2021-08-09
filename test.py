import requests



def get_req(url):
    r = requests.get(url).text
    print(r)

get_req('https://www.homeworkfox.com')

#git init : create repo
#git add . : add files to watch
#git status : shows all added files
#git branch -M main : create branch named "main"
#git commit -m "your comment" : add commit
#git push -u origin main : add to remote repo

# other changes

