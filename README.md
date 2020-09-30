To learn about **Redis** from ground up hit this [Medium](https://medium.com/@iamvishalkhare/create-a-redis-cluster-faa89c5a6bb4) Article.

# Installation
- Three folders named node1, node2 and node3 to set up conf files.
- Open up cmd, cd to redis-cluster-python and execute these commands:

  ```
  wget http://download.redis.io/releases/redis-5.0.5.tar.gz
  tar xzf redis-5.0.5.tar.gz
  mv redis-5.0.5 redis
  cd redis
  make
  ```


 - Put this project folder in Desktop.

 - Open a terminal(1) in Desktop and write these commands
 
   ```
   cd redis-cluster-python
   ./redis/src/redis-server ./node1/redis.conf
   ```

 - Open another termianl(2) and write these commands
 
   ```
   cd redis-cluster-python
   ./redis/src/redis-server ./node2/redis.conf
   ```

 - Open another termianl(3) and write these commands
 
   ```
   cd redis-cluster-python
   ./redis/src/redis-server ./node3/redis.conf
   ```
   >So three instances of redis server are up with these ports: 6001,6002,6003 along with their conf files. 
	
 - Now bind these three server in redis-cli so that it knows how to hash and store data according to hash by typing this command
 
   ```
   ./redis/src/redis-cli --cluster create 127.0.0.1:6001 127.0.0.1:6002 127.0.0.1:6003
   ```

 - You can directly start the redis-cli by using this command and do queries
   
   ```
   ./redis/src/redis-cli -c -p 6001
   ```
  **Or**
	
 - Install redis-py-cluster by writing this command:
	
   ```
   pip3 install redis-py-cluster
   ```

 - Execute ***rcp.py*** to access redis-cluster using python.

___
>Explanation on Source code
___

 - In every folder there is a **conf** file which creates a redis server on given port.
 - Upon proper commands given on the top the servers get binded with each other to create a cluster.
 - In python file, when the code gets connected with one server of the cluster, then it automatically finds the rest servers and using hashing algorithm, it inserts data in a round robin fashion.





