---
Title: Membuat Model
Author: Devin Purnawansyah
Date: 2020
---
## Membuat Model di Odoo
Model digunakan untuk mendeklarasikan object yang akan dibentuk dalam program, di dalam model terdapat atribut (`_name` dan `_description`)_ dan model fields. berikut adalah contoh model di odoo:
```
# -*- coding: utf-8 -*-

from odoo import fields, models



class Divisi(models.Model):
    _name = 'tes.divisi'
    _description = 'Divisi Pekerjaan'

    name = fields.Char(
        string= 'Divisi Pekerjaan',
        required=True, 
        help="Isi Divisi Pekerjaan..."
    )

    description = fields.Text(
        string='Description',
    )

    active = fields.Boolean(
        string='Active', 
        default= True
    )

    category_id = fields.Many2one(
        comodel_name='tes.divisi.category',
        string='Kategori Pekerjaan',
    )

    partner_id = fields.Many2one(comodel_name='res.partner', string='ID Customer')
```
Untuk memeriksa apakah model yang dibuat sudah masuk (asumsi telah dalam mode developer), maka kita dapat menuju ke menu Settings -> Technical -> Models. 

### Model Fields
Model Fields berfungsi untuk mendefenisikan apa dan dimana model akan disimpan. seluruh isi dari model tergambar dalam model fields tersebut. Model fields dri sifat pengambilan datanya terbagi menjadi dua yaitu:
#### 1. Simple Fields
Simple fields merupakan field yang di deklarasikan dan disimpan dalam fields tersebut. Contoh beberapa penggunaan fields tersebut:
```
    name = fields.Char(
        string= 'Divisi Pekerjaan',
        required=True, 
        help="Isi Divisi Pekerjaan..."
    )

    description = fields.Text(
        string='Description',
    )

    active = fields.Boolean(
        string='Active', 
        default= True
    )
```
#### 2. Relational Fields
Relational fields merupakan field yang datanya terhubung dengan model yang sama ataupun model yang berbeda.
```
    category_id = fields.Many2one(
            comodel_name='tes.divisi.category',
            string='Kategori Pekerjaan',
    )
    divisi_ids = fields.One2many(
        comodel_name='tes.divisi', 
        inverse_name='category_id', 
        string='Divisi Satu Kategori'
    )
```
Sementara itu jika dilihat pembuatannya terdapat dua sifat fields yaitu:
#### a. fields yang tidak dideklarasikan (otomatis ada dalam model)
Adapun fields yang otomatis ada dalam models disebut juga dengan **Reserved fields**. Berikut adalah semua field tersebut:
**id (Id)**
    The unique identifier for a record in its model.
**create_date (Datetime)**
    Creation date of the record.
**create_uid (Many2one)**
    User who created the record.
**write_date (Datetime)**
    Last modification date of the record.
**write_uid (Many2one)**
    user who last modified the record.
    
#### b. fields yang dideklarasikan
Fields ini harus dideklarasikan dalam model yang akan dibuat agar dapat berjalan. adapun jenis-jenis field ini adalah selain dari Reserved fields sebelumnya.
