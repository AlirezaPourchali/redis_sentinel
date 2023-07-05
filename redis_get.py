from redis.sentinel import Sentinel
import redis 
sentinel_instance = Sentinel([('localhost' , 1001),('localhost' , 1002),('localhost' , 1003)])

host , port = sentinel_instance.discover_master('mymaster')

print(host , port)

server = redis.Redis(host , port)

server.set("ali" , "asghar")

ali = server.get("ali")
print(ali.decode())
