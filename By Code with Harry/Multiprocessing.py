import multiprocessing
import requests
from concurrent.futures import ThreadPoolExecutor


def download(Url,name):
    print(f"Downloading file{name}")
    r=requests.get(Url)
    open(f"Files/file{name}.jpg","wb").write(r.content)
    print(f"File{name} downloaded")


Url="https://picsum.photos/2000/3000"
pros=[]

if __name__=="__main__":
    for i in range(15):
    # download(Url,i)
        p=multiprocessing.Process(target=download,args=(Url,i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
#or
    with ThreadPoolExecutor() as executor:
        result=executor.map(download,[Url]*15,[i for i in range(15)])
        for r in result:
            print(r)