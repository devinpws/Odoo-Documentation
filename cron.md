---
Title: Cron Untuk Menjalankan Perintah Secara Otomatis Realtime
Author: Devin Purnawansyah
Date: 2021
---

#Cron
Fungsi cron adalah untuk melakukan eksekusi suatu fungsi setiap menit, jam ataupun hari secara otomatis.

##Cron Template Xml
Adapun template cron dalam xml adalah:
```
   <!-- sale.order cron -->
        <record id="sale_order_expired_ir_cron" forcecreate="True" model="ir.cron">
            <field name="name">Sale Order: Expired Quatation</field>
            <field name="doall" eval="False"/>
            <field name="active" eval="True"/>
            <field name="interval_number">1</field>
            <field name="interval_type">days</field>
            <field name="numbercall">-1</field>
            <field name="model_id" ref="model_sale_order"/>
            <field name="state">code</field>
            <field name="code">model.check_expired()</field>
        </record>
```

Penjelasannya adalah sebagai berikut:
| Syntax | Keterangan |
| --- | ----------- |
| `<field name="name">Sale Order: Expired Quatation</field> `| Memberikan nama untuk cron job yang dibuat |
| `<field name="doall" eval="False"/>` | Boolean value untuk menyatakan apakah kesalahan tetap di eksekusi ketika server restart |
| `<field name="active" eval="True"/>` | Boolean value apakah cron job active atau tidak|
| `<field name="interval_number">1</field>` | Integer value untuk menyatakan jumlah waktu untuk pemanggilan cron job |
| `<field name="interval_type">days</field>`| Menyatakan unit interval, nilainya adalah: **minutes, hours, days, weeks, months** |
| `<field name="numbercall">-1</field>`| Integer value untuk menentukan berapa banyak/ berapa kali cron job akan dipanggil, hasil -1 menandakan no limit |
| `<field name="model_id" ref="model_sale_order"/>`| Menyatakan model yang mana untuk dilakukan cron job |
| `<field name="state">code</field>`| Inisialisasi pemanggilan function|
| `<field name="code">model.check_expired()</field>`| Melakukan pemanggilan function|
| `<field name="user_id" ref="base.user_root"/>`| Dalam beberapa kasus melakukan eksekusi berdasarkan spesifik kepada user_id, in most cases this will be base.user_root.|
| `<field name="nextcall" >2016-12-31 23:59:59</field> <!-- notice the date/time format -->`| Untuk mengatur next planned execution date for this job |
| `<field name="args" eval="" />`| The arguments to be passed to the method |
| `<field name="priority" eval="5" />`| The priority of the job, as an integer: 0 means higher priority, 10 means lower priority.|
| `<field name="model" eval="'model.name '" />`|Cara lain pemanggilan model|
| `<field name="function" eval="'method_name '" />`|Cara lain pemanggilan function|

Contoh fungsi untuk eksekusi:
```
def check_expired(self):
        today = fields.Date.today()
        sale_orders = self.env['sale.order'].search([])
        for order in sale_orders:
            if order.state == 'draft' and order.validity_date < today:
                order.state = 'expired'
```


