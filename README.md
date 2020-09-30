To learn about **Redis** from ground up hit this [Medium](https://medium.com/@iamvishalkhare/create-a-redis-cluster-faa89c5a6bb4) Article.

# Installation
- Three folders named node1, node2 and node3 to set up conf files.
- Open up cmd, cd to redis-cluster-python and execute these commands :
  ```
  	wget http://download.redis.io/releases/redis-5.0.5.tar.gz
	tar xzf redis-5.0.5.tar.gz
	mv redis-5.0.5 redis
	cd redis
	make
  ```


3. Put this project folder in Desktop.

4. Open a terminal in Desktop and write these commands:
		cd redis-cluster-python
		./redis/src/redis-server ./node1/redis.conf
		
	Open another termianl and write these commands: 
		cd redis-cluster-python
		./redis/src/redis-server ./node2/redis.conf
		
	Open another termianl and write these commands: 
		cd redis-cluster-python
		./redis/src/redis-server ./node3/redis.conf
		
	So three instances of redis server are up with these ports: 6001,6002,6003 along with their conf files. 
	
5. Now bind these three server in redis-cli so that it knows how to hash and store data according to hash by typing this command:
	./redis/src/redis-cli --cluster create 127.0.0.1:6001 127.0.0.1:6002 127.0.0.1:6003

6. You can directly start the redis-cli by using this command: 
		./redis/src/redis-cli -c -p 6001
	
	And do your query.
	
	Or
	
	Install redis-py-cluster by writing this command:
	
		pip3 install redis-py-cluster

7. Execute rcp.py to access redis-cluster using python.



