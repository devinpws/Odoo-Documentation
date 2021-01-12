---
Title: Github Documentation
Author: Devin Purnawansyah
Date: 2021
---

#Github Documentation
Berikut adalah dokumentasi untuk github:

## Git Clone
Clone repository digunakan untuk menyimpan/ mendownload file repository ke dalam penyimpanan local di device yang kita gunakan. 
```
#git clone 
git clone [link github untuk clone]

#git clone in Ubuntu
sudo git clone [link github untuk clone]

#example
sudo git clone https://github.com/devpws/Odoo-Documentation.git
```

## Git Log 
Git log digunakan untuk melihat history commit.
```
git log

#keluar dari git log klik q
```

## Git Status
Git status digunakan untuk memeriksa file yang telah dimodifikasi atau di add, dan untuk memeriksa file yang belum di commit untuk selanjutnya di commit.
```
git status
```

## Git Pull
Untuk mengupdate file yang sudah di push sebelumnya oleh orang lain dapat digunakan git pull.
```
#git pull
git pull origin master

#git pull in ubuntu
sudo git pull origin master
```

## Git Add
Sebelum akan melakukan commit terlebih dahulu add file atau directory menggunakan git add.
```
#git add
git add [name_file]

#example
git add alto_invoices_report
```

## Git Commit
Setelah file di add selanjutnya lakukan commit terhadap file tersebut menggunakan git commit.
```
#git commit
git commit -m "Your comment about file"

#example
git commit -m "Add New Module"
```

## Git Push
Setelah melakukan commit agar file dapat masuk ke dalam repository github lakukan push.

```
git push -u origin master
```



