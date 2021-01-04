---
Title: Report Tips
Author: Devin Purnawansyah
Date: 2021
---

# Tips in Report File
Dokumentasi ini ditujukan untuk pembuatan report di odoo.

## Tips Membuka File Report Tanpa Download
Untuk melakukan pengeditan di file report kita harus memeriksa apakah pengeditan tersebut berjalan 
pada hasil report tersebut. oleh karena itu kita butuh untuk menjalankan hasilnya di browser tanpa harus download filenya.
Berikut adalah cara yang dapat dilakukan:
```
Template: 
http://localhost:8013/report/pdf/(Template Name)/(id)

Example: 
http://localhost:8013/report/pdf/account.report_invoice_with_payments/2

```
untuk menemukan template name: **Settings => technical => report => search report yang mana (invoices)=> Template Name**

## Tips Mengedit Table
Table di odoo secara default bentuknya seperti table biasa berlatar putih. kita dapat memodifikasi tabel dengan membuat style kita sendiri.

Langkah pertama kita buat dulu file **static =>  src => css => nama_file.css** pada module yang kita buat. Setelah itu buat style kita sendiri di file css tersebut.
contoh style css yang dibuat:
```
.table-alto > tbody > tr:nth-child(2n+1) > td, 
.table-alto > tbody > tr:nth-child(2n+1) > th {
   background-color: #E0FFFF;
}
.table-alto > tbody > tr:nth-child(2n+2) > td{
   background-color: #DFE8E8;
}
.bg-navy{
	background-color: navy;
}
```
Setelah itu masuk ke file xml untuk report dari module, lalu kita hubungkan style yang kita buat agar bisa dipanggil dalam file xml. caranya adalah:
```
<template id="report_assets_common" name="alto_invoices_report assets" inherit_id="web.report_assets_common">
      <xpath expr="." position="inside">
          <link rel="stylesheet" href="/alto_invoices_report/static/src/css/alto_invoices_report.css"/>
      </xpath>
</template>
```

Jika semua step telah dilakukan maka kita dapat memanggil style tersebut di template report yang kita buat.
