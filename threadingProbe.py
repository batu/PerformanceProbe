# Batu Aytemiz
# 29.09.2015 13:52
# Performance Monitor

# Steps
# Get the url and make the request
# Log the response to a file
#
#





from threading import Thread
import time, requests, calendar, threading

file = open('probingSamples', 'w')





def probingMonitor(url):
    start_time = time.time()
    print('Request sent to ' + url)
    try:
        request = requests.get(url, timeout=30)
        if (request.status_code == requests.codes.ok):
            print(str( calendar.timegm(time.gmtime()) ) + ',' + str(request.status_code))
            print("--- after %s seconds ---" % (time.time() - start_time))
            file.write(str( calendar.timegm(time.gmtime()) ) + ',' + str(request.status_code) + '\n')
        else:
            print("Bad code received...")
        file.write(str( calendar.timegm(time.gmtime()) ) + ',' + str(-1) + '\n')
    except OSError:
        print("Timed out...")
        file.write(str( calendar.timegm(time.gmtime()) ) + ',' + str(-1) + '\n')
    time.sleep(1)

url = "http://www.facebook.com/"
while(True):
    probeThread = Thread(target=probingMonitor, args=(url,))
    probeThread.start()
    probeThread.join()



