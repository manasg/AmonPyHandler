import logging
import socket
import amonpy

class AmonPlusHandler(logging.Handler):
    amonClient = amonpy
    
    def __init__(self, key, destinationIp, destinationPort, appName, hostname=None, level=logging.WARN):
        logging.Handler.__init__(self)
        self.level = level
        self.appName = appName
        
        if hostname == None:
            self.hostname = socket.gethostname()
        else:
            self.hostname = hostname
        # configure amonpy
        self.amonClient.config.address = "http://%s:%s" % (destinationIp,destinationPort)
        self.amonClient.config.application_key = key

    
    def emit(self, record):
        if self.formatter==None:
            formatter = logging.Formatter("[%(asctime)s][%(filename)s:%(lineno)d] %(levelname)s: %(message)s")
            self.formatter = formatter
        #
        message = self.format(record)
        tags = [self.appName, self.hostname, record.levelname ]
        
        self.amonClient.log(message, tags)
        
    
        