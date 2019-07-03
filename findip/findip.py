import re


def searchIp(txt):
    pattern = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    match = pattern.search(txt) 
    if match: 
        print (match.group())
        with open('ips.txt','a+')as f:
            f.writelines(match.group()+'\n')
			
if __name__ == '__main__':
    f = open("sources.txt", "r")
    while True:
        line = f.readline()
        if not line:  # no data
            break;
        else:
#             print l
            searchIp(line)
            
    f.close()