# raspberry-pi-scripts
Things I do often on a Raspberry Pi.

## Updates

```shell
sudo apt update
sudo apt upgrade -y

sudo apt install git
```

## PIP

```
sudo apt-get install python3-pip
```

## UFW (Uncomplicated Firewall)

```shell
sudo apt install ufw -y
sudo ufw enable
sudo ufw status
```

To disable it:
```shell
sudo ufw disable
```

In ufw, allow port 1883 for mqtt:

```shell
sudo ufw allow 1883/tcp
```

## MQTT (Message Queue Telemetry Transport)

```shell
sudo apt install mosquitto mosquitto-clients
sudo systemctl status mosquitto # looking for 'active (running)'
```

Note: you will probably have to open a hole in the firewall for port 1883. See example of that in UFW section

## Redis

```shell
sudo apt install redis-server
```

Configuration file at

```shell
sudo nano /etc/redis/redis.conf
```

In the config file change the following:

- From: # bind 127.0.0.1
- To: bind 0.0.0.0

--

- From: protected-mode yes
- To: protected-mode no
 
 --

- From: # requirepass foobared
- To: requirepass [your password here]

Finally, restart the instance:

```shell
sudo /etc/init.d/redis-server restart
```

To test you can use this simple python script:

```python
import redis # pip install redis
client = redis.Redis(host='[hostname here]', port=6379, password='[password here]')

# inspect the client object with:
# dir(client)

# set the key and value:
client.set('language', 'python')
print(client.get('language')) # returns: 'python'
```
