import sys
sys.path.append('src/collector')
from utility.threads import threaded
import requests
import random
import re
class nginxCollectionAgent:

    def __init__(self):
        self.data={}
        self.collectorFunctions=[ 
            self.getHttpConnectionsMetrics,
            ############### HTTP Methods
            #'''Statistics about observed request methods.'''
            # self.methodGet,
            # self.methodHead,
            # self.methodPost,
            # self.methodPut,
            # self.methodDelete,
            # self.methodOptions, 
            # ############### HTTP Status Codes
            # #'''Number of requests with HTTP status codes per class.'''
            # self.status1xx,
            # self.status2xx,
            # self.status3xx,
            # self.status4xx,
            # self.status5xx,
            # #'''Number of requests with specific HTTP status codes above.'''
            # self.status403,
            # self.status404,
            # self.status500,
            # self.status502,
            # self.status503,
            # self.status504,
            # #'''Number of requests finalized with status code 499 which is logged when the
            #    #client closes the connection.'''
            # self.statusDiscarded,
            # ##################
            # #'''Number of requests using a specific version of the HTTP protocol.'''
            # self.httpV0_9,
            # self.httpV1_0,
            # self.httpV1_1,
            # self.httpV2,
        ]

    @threaded
    def getHttpConnectionsMetrics(self, stubStatusUrl='http://127.0.0.1/nginx_status'):
        
        try:
            stubData=requests.get(stubStatusUrl)
            
            try: 
                stubStatusRegex = re.compile(r'^Active connections: (?P<connections>\d+)\s+[\w ]+\n'
                        r'\s+(?P<accepts>\d+)'
                        r'\s+(?P<handled>\d+)'
                        r'\s+(?P<requests>\d+)'
                        r'\s+Reading:\s+(?P<reading>\d+)'
                        r'\s+Writing:\s+(?P<writing>\d+)'
                        r'\s+Waiting:\s+(?P<waiting>\d+)')
                     
                stubMatchings=stubStatusRegex.match(stubData.text)
                httpMetrics={}

                for metric in ['connections', 'accepts', 'handled', 'requests', 'reading', 'writing', 'waiting']:
                    httpMetrics[metric] = int(stubMatchings.group(metric))
                
                self.data['connectionAccepted'] = httpMetrics['accepts'] #number of connections accepted till this time.
                self.data['connectionsDropped'] = httpMetrics['accepts']-httpMetrics['handled']# number of connections dropped till this time.
                self.data['activeConnections'] = httpMetrics['connections']-httpMetrics['waiting']# number of active connections right now
                self.data['currentConnections'] = httpMetrics['connections']# number of connections right now
                self.data['idleConnections'] = httpMetrics['waiting']# number of idle connections right now 
                self.data['requestCount'] = httpMetrics['requests']# number of requests that have been sent till now. 
                self.data['currentRequest'] = httpMetrics['reading'] + httpMetrics['writing']# number of currently active requests that are  reading and writing.
                self.data['readingRequests'] = httpMetrics['reading']# number of currently active reading headers requests .
                self.data['writingRequests'] = httpMetrics['writing']# number of currently active writing requests to clients. 
                
            except:
                print('Unable to parse stubStatusText')
        except:
            print("Stub Data not received")
            return 
           
    @threaded
    def methodGet(self):
        self.data['methodGet']=random.randint(0,100)
  
    @threaded
    def methodHead(self):
        self.data['methodHead']=random.randint(0,100)

    @threaded
    def methodPost(self):
        self.data['methodPost']=random.randint(0,100)
    
    @threaded
    def methodPut(self):
        self.data['methodPut']=random.randint(0,100)
    
    @threaded
    def methodDelete(self):
        self.data['methodDelete']=random.randint(0,100)
    
    @threaded
    def methodOptions(self):
        self.data['methodOptions']=random.randint(0,100)
    
    @threaded
    def status1xx(self):
        self.data['status1xx']=random.randint(0,100)
    
    @threaded
    def status2xx(self):
        self.data['status2xx']=random.randint(0,100)

    @threaded
    def status3xx(self):
        self.data['status3xx']=random.randint(0,100)

    @threaded
    def status4xx(self):
        self.data['status4xx']=random.randint(0,100)

    @threaded
    def status5xx(self):
        self.data['status5xx']=random.randint(0,100)

    @threaded
    def status403(self):
        self.data['status403']=random.randint(0,100)
    
    @threaded
    def status404(self):
        self.data['status404']=random.randint(0,100)
    
    @threaded
    def status500(self):
        self.data['status500']=random.randint(0,100)
    
    @threaded
    def status502(self):
        self.data['status502']=random.randint(0,100)
    
    @threaded
    def status503(self):
        self.data['status503']=random.randint(0,100)
    
    @threaded
    def status504(self):
        self.data['status504']=random.randint(0,100)

    @threaded
    def statusDiscarded(self):
        self.data['statusDiscarded']=random.randint(0,100)
    
    @threaded
    def httpV0_9(self):
        self.data['httpV0_9']=random.randint(0,100)

    @threaded
    def httpV1_0(self):
        self.data['httpV1_0']=random.randint(0,100)

    @threaded
    def httpV1_1(self):
        self.data['httpV1_1']=random.randint(0,100)
    
    @threaded
    def httpV2(self):
        self.data['httpV2']=random.randint(0,100)
    
    @threaded
    def connectionsAccepted(self):
        self.data['connectionsAccepted']=random.randint(0,100)
         

    @threaded
    def connectionsDropped(self):
        self.data['connectionsDropped']=random.randint(0,100)
        return
     #number of connections dropped till this time.     

    @threaded
    def activeConnections(self):
        self.data['connectionsActive']=random.randint(0,100)
        return
    # number of active connections right now
    
    @threaded
    def currentConnections(self):
        self.data['currentConnections']=random.randint(0, 100)

    # number of connections right now

    @threaded
    def idleConnections(self):
        self.data['idleConnections']=random.randint(0, 100)
        return

    # number of idle connections right now 

    @threaded
    def requestCount(self):
         self.data['requestCount']=random.randint(0, 100)

    # number of requests that have been sent till now. 


    @threaded
    def currentRequests(self):
         self.data['currentRequests']=random.randint(0, 100)

    # number of currently active requests that are  reading and writing.     

    @threaded
    def readingRequests(self):
         self.data['readingRequests']=random.randint(0, 100)

    # number of currently active reading headers requests .     
    @threaded
    def writingRequests(self):
         self.data['writingRequests']=random.randint(0, 100)

    # number of currently active writing requests to clients.    

    @threaded
    def malformedRequets(self):
         self.data['malformedRequets']=random.randint(0, 100)

    #number of malformed requests till now. 
    @threaded
    def bodyBitesSent(self):
         self.data['bodyBitesSent']=random.randint(0, 100)

    # number of bytes sent to the client without counting the response headers. 

    def setData(self):
        handles=[]
        for i in self.collectorFunctions:
            handles.append(i())
        for thread in handles:
            thread.join()
        print('threads completed')
        return self.data

agent=nginxCollectionAgent()

# print(agent.setData())

