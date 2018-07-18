import os , requests , colorama , win_unicode_console, sys , time
win_unicode_console.enable()
colorama.init()
#colors
R="\033[91m"         # Red
G="\033[1;32m"       # Green
Y="\033[1;33m"      # Yellow
B="\033[1;34m"        # Blue
P="\033[1;35m"      # Purple
C="\033[1;36m"        # Cyan
W="\033[1;37m"       # White
print B+"Hunter-Gun"+G+" is Simple Tool To Check If sub-domain is WebPage With Html content or Address"+G
print "The Sub-domains links must be start with http or https"
print "[!] Example : python HunterGun.py Sub-domain.list"
time.sleep(10)
print "Coded By : "+B+"Kareem Walid"+W

file = sys.argv[1]

with open (file) as f:



    print "Let's Do It Bro O_O\n"

    for l in f:

        line2 = l.strip()
        for h in l:
            if "http://" or "https://" in h:
                continue
            else:
                print "Notice u must add http or https at first of url okay !"
                exit()

        #line3 = 'http://' + line2
        #print line2
        try:
            response = requests.get(line2, verify=True)
            check = response.status_code
            s = [200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,307]
            #print check
            if check == 200 or 201 or 202 or 204 or 205 or 206 or 207 or 208 or 226 or 300 or 301 or 302 or 303 or 304 or 305 or 306 or 307:
                print G+"[+] "+line2+" Is Running"
                time.sleep(5)

            else:
                print R+"[-]"+line2+" Is Down"+W
                #---------------------------------------------------------------------------------------------------------
        except:
            try:
                line3 = line2.strip("https://")
                line4 = "http://"+line3
                response = requests.get(line4, verify=True)
                check = response.status_code
                s = [200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,307]
                            #print check
                if check == 200 or 201 or 202 or 204 or 205 or 206 or 207 or 208 or 226 or 300 or 301 or 302 or 303 or 304 or 305 or 306 or 307:
                    print G+"[+] "+line4+" Is Running"

                else:

                    print R+"[-]"+line4+" Is Down"+W
            except:

                print R+"[-] There is ERROR with " + response.url +" it may down or redirect u to something else so Please check it manually !"
