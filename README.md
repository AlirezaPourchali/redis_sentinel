# redis_sentinel

my r&d about redis-sentinels.      
use the [pdf](https://github.com/AlirezaPourchali/redis_sentinel/blob/main/Redis%20sentinel.pdf).(too lazy to write md)     
up the compose files and test sentinels with killing the master container.       
just create a docker network `sentinel` before the containers:     

```
docker network create sentinel
```
