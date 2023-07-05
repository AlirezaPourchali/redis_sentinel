from redis.sentinel import Sentinel

sentinel_instance = Sentinel([('localhost' , 1001),('localhost' , 1002),('localhost' , 1003)])

current_master = sentinel_instance.master_for('master-name' , socket_timeout=0.1)

print(current_master)