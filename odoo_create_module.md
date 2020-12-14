---
Title: Membuat Modul Baru di Odoo 13
Author: Devin Purnawansyah
Date: 2020
---

## Membuat Modul Baru
Untuk membuat modul baru, ada dua cara yang dapat dilakukan. 
### 1. Menggunakan Scaffold
Kita asumsikan odoo sudah terinstall pada perangkat. Selanjutnya adalah kita buat folder untuk meletakkan semua add ons yang kita buat. Penempatan folder bebas namun tetap di konfigurasi nantinya. Setelah itu konfigurasi odoo.conf untuk menempatkan path folder add ons custom yang dibuat sebelumnya. Masuk ke nano odoo.conf:
```
sudo nano /etc/odoo.conf

//masuk nano
[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = localhost
db_port = False
db_user = odoo13
db_password = devgan2212
;addon-path =s_path = /usr/lib/python3/dist-packages/odoo/addons
addons_path = /opt/odoo/addons,/opt/odoo_custom
logfile = /var/log/odoo/odoo.log

```

Langkah selanjutnya adalah menuju terminal dan masuk ke directory odoo di terminal kemudian create default modul dengan scaffold.
```
cd /opt/odoo

// create sudo ./odoo-bin scaffold <module_name> <location_custom_addons>
sudo ./odoo-bin scaffold modul_tes ../odoo_custom/

```
Maka file baru akan terbentuk di dalam folder custom kita.

### 2. Membuat Manual Folder
Pada dasarnya kita dapat membuat modul baru dengan create folder manual asalkan didalamnya terdapat file `__init__.py` dan `__manifest__.py. ` 
Untuk isi file manifest mengikuti pada isi file manifest lainnya dan ubah sesuai dengan kebutuhan.
Apabila terdapat permission access pada folder gunakan CLI berikut, namun terlebih dahulu masuk dulu ke directory dari folder yang akan diganti permission access-nya:
```
sudo chmod -R 777 odoo_custom
```

Adapun cara buat file melalui terminal ubuntu 20.4, terlebih dahulu arahkan terminal ke directory tempat file akan disimpan:
```
touch nama_file

//example
touch __init__.py
```

Sementara cara buat folder di terminal ubuntu 20.4 adalah:
```
mkdir nama_folder

//example
mkdir views
```
