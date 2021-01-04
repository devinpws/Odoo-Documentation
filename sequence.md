---
Title: Sequence in Odoo
Author: Devin Purnawansyah
Date: 2021
---

# Sequence
Fungsi sequence adalah untuk memberikan penamaan unik, ataupun memberikan label khusus untuk suatu inputan/data. 
Ada dua metode yang dapat dilakukan untuk membuat sequence di odoo:

## Sequence di Xml
Berikut adalah program sequence di Xml:
```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="0">
        <!-- Sequences -->
        <record id="seq_asset_order" model="ir.sequence">
            <field name="name">Sequence Asset</field>
            <field name="code">account.asset</field>
            <field name="active">TRUE</field>
            <field name="prefix">/%(year)s/ </field>
            <field name="padding">4</field>
            <field name="number_next">1</field>
            <field name="number_increment">1</field>
        </record>
    </data>
</odoo>
```
Penjelasannya adalah:
| Syntax      | Keterangan |
| ----------- | ----------- |
| `<field name="name">Sequence Asset</field>`| Memberikan penamaan sequence yang di buat       |
| `<field name="code">account.asset</field>`| Mendeklarasikan object yang akan dijalankan fungsi sequence        |
| `<field name="active">TRUE</field>`| Boolean value untuk mengidentifikasi apakah sequence active atau tidak      |
| `<field name="prefix">/%(year)s/ </field>`| Karakter yang menjadi prefix atau awalan dari sequence yang akan dibuat, dapat berupa char:SS,ABC dan lainnya, atau tahun dan sebagainya       |
| `<field name="padding">4</field>`| Ukuran sequence, contoh 4 = 0001       |
| `<field name="number_next">1</field>`| Number yang akan digunakan berikutnya        |
| `<field name="number_increment">1</field>`| Increment sequence        |
| `<field name="implementation">no_gap</field>`| Implementation ada 2 standart dan no gap, standar akan mengambil nilai next selalu, sementara untuk no gap apabila salah satu sequence di delete maka akan digunakan kembali untuk number next    |
| `<field name="suffix">A</field>`| Suffix berada di belakang sebagai tambahan , ini disesuaikan dengan kebutuhan  |


function di python untuk pemanggilan ir.sequence adalah:
```
@api.model
    def create(self, vals):
        print('Nilai Vals:', vals)
        vals['name'] = self.env['ir.sequence'].next_by_code('tes.divisi') or 'New'
        result = super(Divisi, self).create(vals)
        print('Hasil dari vals.get---------->',vals)
        return result
```

## sequence langsung di method
Berikut adalah contoh programnya:
```
def make_sequence(self):
        print('fungsinya jalan ya----------------')
        asset_obj = self.env['account.asset'].browse(self._context.get('active_ids'))
        print('asset obj----------------', asset_obj)
        for data in asset_obj:
            if data.asset_seq:
                ir_sequence_obj = self.env['ir.sequence']
                category_asset = self.env['tes.accounting'].search([('id','=',data.asset_seq.id)])
                print('Category Asset--------------------', category_asset.name)
                if not category_asset:
                    raise ValidationError(_("Category not available, please input category first"))
                if category_asset:
                    code = category_asset.name
                    seq = ir_sequence_obj.search([('code','=',code)])
                    year = str(fields.Date.today().year)
                    if not category_asset.code_asset:
                        data.asset_number = '0'
                    elif not seq:
                        add_seq = ir_sequence_obj.create({
                                'name': code + ' Sequence',
                                'code': code ,
                                'implementation': 'no_gap',
                                'prefix': category_asset.code_asset + '/' + year + '/',
                                'padding': 4,
                                'number_next': 1,
                                'number_increment': 1,
                        })
                    new_seq = ir_sequence_obj.next_by_code(code) or '/'
                    data.asset_number = new_seq

```
