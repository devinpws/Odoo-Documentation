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
