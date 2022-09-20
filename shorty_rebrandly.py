# url shortening services
#https://bit.ly/38Ccn2n -- google.com
#tinyurl.com/2p8me4xt -- news.google.com
#tinyurl.com/ychk9x25 -- google.com
#tinyurl.com/2p83m28k -- asdsadsaasd.com

import string, random, requests
valid_chars = list(string.ascii_lowercase) + ['0','1','2','3','4','5','6','7','8','9']
f = open(r'C:\users\12246\Desktop\shorty\rebrandly_output.txt','a+',newline="")
while True:
    url_to_try = 'https://rb.gy/'
    for i in range(6):
        url_to_try += random.choice(valid_chars)
    try:
        temp = requests.head(url_to_try).headers['location']
        if temp=='https://free-url-shortener.rb.gy/':
            raise
        if url_to_try in f.read():
            print("ERROR WITH URL "+url_to_try+":\tALREADY IN FILE")
        else:
            print("WRITING:\t"+url_to_try+"\t"+temp+"\n")
            f.write(url_to_try+"\t"+temp+"\n")
            f.flush()
    except Exception as e:
        print("ERROR WITH URL "+url_to_try+":\t"+str(e))
        f.write(url_to_try+"\tNone\n")
        f.flush()