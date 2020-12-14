---
Title: Install Odoo 13 di Linux 20.4 
Author: Devin Purnawansyah
Date: 2020
---

## Odoo Installation Cheat Sheet
Langkah Pertama Update dan Upgrade terlebih dahulu ubuntu menggunakan command line di bawah ini:
```
sudo apt-get update
sudo apt-get -y upgrade

//Jika ada error pada upgrade dapat lakukan cara berikut ini:
sudo apt-get upgrade --fix-missing 

```

Selanjutnya secure server agar dapat diakses secara remote.
```
sudo apt-get install openssh-server fail2ban
```

Buat user system untuk menjalankan odoo
```
sudo adduser --system --home=/opt/odoo --group odoo //penamaan user dimulai dari sini
```

Selanjutnya install python beserta packages & libraries.
```
sudo apt-get install -y python3-pip
sudo apt-get install python-dev python3-dev libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev
```

Setelah itu, install node.js dan pengaturannya.
```
sudo apt-get install -y npm
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g less less-plugin-clean-css
sudo apt-get install -y node-less
```

Install wkhtmltopdf untuk print pdf report pada odoo nantinya.
```
sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo apt install -f
```

Configure Postgresql.
```
sudo apt-get install postgresql
sudo su - postgres

//create new postgresql user to managing odoo database
createuser --createdb --username postgres --no-createrole --no-superuser --pwprompt odoo13

//after create password change the user to superuser
psql
ALTER USER odoo13 WITH SUPERUSER;
```

Selanjutnya clone odoo dari git.
```
sudo apt-get install git
sudo su - odoo -s /bin/bash

//after that, clone odoo from github (sampai titik):
git clone https://www.github.com/odoo/odoo --depth 1 --branch 13.0 --single-branch . 

//to continue the installation write exit.
exit
```

Install required odoo.
```
sudo pip3 install -r /opt/odoo/requirements.txt
```

Configuration odoo.
```
 sudo mkdir /var/log/odoo
 sudo chown odoo:root /var/log/odoo

//create odoo.conf
sudo cp /opt/odoo/debian/odoo.conf /etc/odoo.conf

//use nano text editor
sudo nano /etc/odoo.conf

//write:
[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = localhost
db_port = False
db_user = odoo13
db_password = aaaaaa//password postgree
;addon-path =s_path = /usr/lib/python3/dist-packages/odoo/addons
addons_path = /opt/odoo/addons,/opt/odoo_custom
logfile = /var/log/odoo/odoo.log
//to save in nano, click CTRL+o and Click Enter, after that click CTRL+x

//give access to previously create user
sudo chown odoo: /etc/odoo.conf
sudo chmod 640 /etc/odoo.conf

```
Keterangan:
 - **admin_passwd**: admin password for PostgreSQL database
 - **db_host**: the database host
 - **db_port**:  the database port
 - **db_user**: the database user name
 - **db_password**: the database password
 - **addons_path**: addons paths (separated by commas)
 - **logfile**: the log file path

Configuration odoo.service.
```
sudo nano /etc/systemd/system/odoo.service

Unit]
   Description=Odoo
   Documentation=http://www.odoo.com
   [Service]
   # Ubuntu/Debian convention:
   Type=simple
   User=odoo
   ExecStart=/opt/odoo/odoo-bin -c /etc/odoo.conf
   [Install]
   WantedBy=default.target

//give access to system user created odoo installation
sudo chmod 755 /etc/systemd/system/odoo.service
sudo chown root: /etc/systemd/system/odoo.service
```

Test odoo installation.
```
sudo systemctl start odoo.service

//run in web browser:
http://localhost:8069

//to check log
tail sudo tail -f /var/log/odoo/odoo.log

//if you need to start odoo services automatically
sudo systemctl enable odoo.service

//to restart odoo services
sudo systemctl restart odoo.service
```

