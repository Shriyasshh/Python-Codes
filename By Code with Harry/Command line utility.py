import argparse

import requests

def DownloadFile(url,local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
        #local_filename  is the name of the file by which it will be saved    
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return

parser=argparse.ArgumentParser()


parser.add_argument("url",help="Url of the file to download")

# parser.add_argument("output",help="by whixh name to save the file")
parser.add_argument("-o","--output",help="Name of the file ",default=None)


args=parser.parse_args()

print(args.url)
print(args.output)
DownloadFile(args.url,args.output)
