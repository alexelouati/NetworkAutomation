import netmiko
from netmiko import ConnectHandler

 
cat3560 = {
    "device_type": "cisco_ios",
    "ip": "10.5.3.100",
    "username": "yourusername",
    "password": "yourpassword",
    "secret": "yourenablesecret",
}
net_connect = ConnectHandler(**cat3560)
net_connect.enable()
output = net_connect.send_command("show ip route")
print (output)
