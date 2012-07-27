#http://amon.cx/guide/clients/python/
import amonpy

amonpy.config.address = "http://192.168.101.93:2464"

amonpy.log("Hello")
amonpy.log("Hello w a tag",['tag'])
