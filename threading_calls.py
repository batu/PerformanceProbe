# Batu Aytemiz
# 29.09.2015 13:52
# Performance Monitor

# Steps
# Get the url and make the request
# Log the response to a file
#
#


from threading import Thread

import urllib3, time, requests

class ReqThread(Thread):
    def __init__(self, val):
        ''' Constructor. '''

        Thread.__init__(self)
        self.val = val


    def run(self):

        start_time = time.time()
        requests2 = requests.get("http://www.facebook.com/")
        print(requests2.status_code)
        print("--- %s seconds with REQUESTS ---" % (time.time() - start_time))

class UrllibThread(Thread):
    def __init__(self, val):
        ''' Constructor. '''

        Thread.__init__(self)
        self.val = val


    def run(self):
        start_time = time.time()
        http = urllib3.PoolManager()
        request = http.request('GET', 'http://www.facebook.com/')
        print(request.status)
        print("--- %s seconds with URLLIB ---" % (time.time() - start_time))



myThreadOb1 = ReqThread(4)
myThreadOb1.setName('Request Thread')

myThreadOb2 = UrllibThread(4)
myThreadOb2.setName('Urllib Thread')

# Start running the threads!
myThreadOb1.start()
myThreadOb2.start()

# Wait for the threads to finish...
myThreadOb1.join()
myThreadOb2.join()

#while(True):


