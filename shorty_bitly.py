# url shortening services
#https://bit.ly/38Ccn2n -- google.com
#tinyurl.com/2p8me4xt -- news.google.com
#tinyurl.com/ychk9x25 -- google.com
#tinyurl.com/2p83m28k -- asdsadsaasd.com
import psycopg2
import string, random, requests
connection3 = psycopg2.connect(user="postgres",
							  password="T1g3rw00dz$$",
							  host="192.168.0.144",
							  port="5432",
							  database="shortened_url_parse")
cursor3 = connection3.cursor()
urls_tried = set()
valid_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + ['0','1','2','3','4','5','6','7','8','9']
while True:
    url_to_try = 'https://bit.ly/3'
    for i in range(6):
        url_to_try += random.choice(valid_chars)
    try:
        #print("TRYING URL\t"+url_to_try)
        temp = requests.head(url_to_try).headers['location']
        x = requests.get(temp)
        if url_to_try not in urls_tried:
            urls_tried.add(url_to_try)
            is_ = "INSERT INTO shortened_urls VALUES ('{0}','{1}','{2}','{3}')".format(url_to_try,temp,int(x.status_code),int(len(x.content)))
            cursor3.execute(is_)
            connection3.commit()
            print("INSERTED STRING: "+is_)
    except Exception as e:
        connection3.commit()
        #print("ERROR WITH URL "+url_to_try+":\t"+str(e))
        urls_tried.add(url_to_try)