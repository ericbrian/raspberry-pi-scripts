# raspberry-pi-scripts
Things I do often on a Raspberry Pi.

## Updates

```shell
sudo apt update
sudo apt upgrade -y

sudo apt install build-essential git curl

hostname -I # show this pi's hostname.
```

## PIP

```
sudo apt-get install python3-pip -y
```

## UFW (Uncomplicated Firewall)

Uncomplicated Firewall is a program for managing a netfilter firewall designed to be easy to use. It uses a command-line interface consisting of a small number of simple commands, and uses iptables for configuration. 

```shell
sudo apt install ufw -y
sudo ufw enable
sudo ufw status
```

To disable it:
```shell
sudo ufw disable
```

In ufw, allow port 1883 for mqtt. Also allow ssh:

```shell
sudo ufw allow 1883/tcp
sudo ufw allow OpenSSH
```

## MQTT (Message Queue Telemetry Transport)

MQTT is a lightweight, publish-subscribe network protocol that transports messages between devices.

```shell
sudo apt install mosquitto -y
sudo apt install mosquitto-clients
```

Check the status:
```shell
sudo systemctl status mosquitto # looking for 'active (running)'
```

Note: you will probably have to open a hole in the firewall for port 1883. See example of that in UFW section

## Redis

Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability.

```shell
sudo apt install redis-server -y
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

redis-test-script.py
```python
import redis # pip install redis
client = redis.Redis(host='[hostname here]', port=6379, password='[password here]')

# inspect the client object with:
# dir(client)

# set the key and value:
client.set('language', 'python')
print(client.get('language')) # returns: 'python'
```

## Node-RED

Node-RED is a programming tool for wiring together hardware devices, APIs and online services.

```shell
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

Note: The shortcuts were not created. But, you can start and stop the service from command lines using `/usr/bin/node-red start` and `/usr/bin/node-red stop`.

To run as a service:
```shell
sudo systemctl enable nodered.service
```

To disable this service:

```shell
sudo systemctl disable nodered.service
```

## ssh

```shell
ssh-keygen

eval $(ssh-agent)
ssh-add
```

## By-the-Way

Since I am new to all of this, I am making note of things that seem important.... :-)

Logs location: `/var/log`
Running processes: `ps -aux`
