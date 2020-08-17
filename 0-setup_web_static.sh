#!/usr/bin/env bash
#  Prepare your web servers

apt-get -y update
apt-get -y install nginx

file="/etc/nginx/sites-available/default"

header="\\\tadd_header X-Served-By $HOSTNAME;"
sudo sed -i "20 a $header" $file

new_string="\\\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com;\n\t}"
sudo sed -i "22 a $new_string" $file

new_string="\\\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}"
sudo sed -i "26 a $new_string" $file

sudo mkdir -p /data/web_static/releases/test && echo "This is a test..." | sudo tee -a /data/web_static/releases/test/index.html
sudo mkdir -p /data/web_static/shared
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/

new_string="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html index.htm;\n\t}"
sudo sed -i "31 a $new_string" $file

service nginx restart
