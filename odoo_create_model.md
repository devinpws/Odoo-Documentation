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
Model Fields berfungsi untuk mendefenisikan apa dan dimana model akan disimpan. seluruh isi dari model tergambar dalam model fields tersebut. Model fields terbagi menjadi dua yaitu:
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

