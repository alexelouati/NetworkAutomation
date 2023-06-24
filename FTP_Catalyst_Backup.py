import netmiko
import datetime
from getpass import getpass
from netmiko import ConnectHandler

username = input("Please provide your SSH username: ")
password = getpass("Please provide your SSH password: ")
enable_secret = getpass("Please provide your enable_secret: ")
Host_Address = input("Please provide the IP of your Cisco device you would like to backup: ")
Server_Address = input("Please provide your FTP server IP Address: ")

cat3560 = {
    "device_type": "cisco_ios",
    "ip": Host_Address,
    "username": username,
    "password": password,
    "secret": enable_secret,
}

start_time = datetime.datetime.now
now = datetime.datetime.now()
net_connect = ConnectHandler(**cat3560)
net_connect.enable()

output = net_connect.send_command("copy running-config ftp://admin:" + password + "@" + Server_Address + "/ftp/", read_timeout=15, expect_string=r'Address or name of remote host')

output = net_connect.send_command(Server_Address, read_timeout=15, expect_string=r'Destination filename')

try:
    output += net_connect.send_command(str(now) + str(), expect_string=r'#')
    
except:
    end_time = datetime.now()
    print("Total time: {}".format(end_time - now))
    raise

print (output)
