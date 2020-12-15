---
Title: Data File di Odoo
Author: Devin Purnawansyah
Date: 2020
---

## Data File
Data file dalam odoo dilakukan untuk menjalankan tampilan dari odoo dalam konteks ini model yang telah dibuat sebelumnya akan dihidupkan kedalam interface menggunakan `.xml`.
Ada berbagai hal yang dapat dilakukan dalam tampilan ini, diantaranya adalah dengan membuat menu parent, menu child dan tampilan dalam page. berikut adalah penjelasannya.
Contoh pembuatan menu parent dan child di odoo dalam xml, file **menu.views.xml**:
```
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <!-- Add you code here -->
      <!-- This Menu Item will appear in the Upper bar, that's why It needs NO parent or action -->
        <menuitem id="divisi_menu_root"  web_icon="modul_tes,static/description/icon.png" name="Testing Divisi" sequence="70"/>
      <!-- This Menu Item Must have a parent -->
        <menuitem id="data_divisi_menu_categ" name="Data Divisi" parent="divisi_menu_root" sequence="10"/>
  </data>
</odoo>
```
## Action Views, Tree Views, Search Views dan Form Views
- **Action Views** digunakan untuk melakukan record model dan dapat juga untuk melakukan trigger diantaranya mengaktifkan menu dan button.
- **Tree Views** digunakan untuk menampilkan field yang diinginkan dalam page odoo
- **Search Views** digunakan untuk mengatur fitur pencarian dan juga untuk mengatur filter dan group by di odoo
- **Form Views** digunakan untuk mengatur tampilan form di odoo.

Berikut adalah contoh program lengkapnya dalam file **divisi.views.xml**:
```
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
      <!-- tes.divisi tree view -->
      <record id="divisi_name_view_tree" model="ir.ui.view">
        <field name="name">tes.divisi.view.tree</field>
        <field name="model">tes.divisi</field>
        <field name="arch" type="xml">
          <tree>
            <!-- Add your fields here -->
            <field name="name"/>
            <field name="category_id"/>
            <field name="partner_id"/>
            <field name="description"/>
            <field name="active"/>
          </tree>
        </field>
      </record>

      <!-- tes.divisi form view -->
      <record id="divisi_name_view_form" model="ir.ui.view">
        <field name="name">tes.divisi.view.form</field>
        <field name="model">tes.divisi</field>
        <field name="arch" type="xml">
          <form string="">
            <sheet>
              <group>
                <!-- Add your fields here -->
                <group>
                  <field name="name"/>
                  <field name="category_id"/>
                </group>
                <group>
                  <field name="active"/>
                  <field name="partner_id"/>
                </group>
              </group>
              <notebook>
                <page string="Description">
                  <field name="description"/>
                </page>
              </notebook>
            </sheet>
          </form>
        </field>
      </record>

      <!-- tes.divisi search view -->
      <record id="divisi_name_view_search" model="ir.ui.view">
        <field name="name">tes.divisi.view.search</field>
        <field name="model">tes.divisi</field>
        <field name="arch" type="xml">
          <search string="Search Divisi">
            <!-- Add your fields here -->
            <field name="name"/>
            <field name="description"/>
            <field name="category_id"/>
            <field name="partner_id"/>
          </search>
        </field>
      </record>

    <!-- tes.divisi action view -->
      <record id="divisi_name_action" model="ir.actions.act_window">
      <field name="name">Divisi</field>
      <field name="type">ir.actions.act_window</field>
      <field name="res_model">tes.divisi</field>
      <field name="view_mode">tree,form</field>
      <field name="help" type="html">
        <p class="oe_view_nocontent_create">
          <!-- Add Text Here -->
        </p>
        
        <p>
          <!-- More details about what a user can do with this object will be OK --> 
        </p>
      </field>
    </record>jika a/=b, maka sama dengan a=a/b 
    <menuitem 
      id="divisi_menu_act" 
      name="Divisi" 
      parent="data_divisi_menu_categ" 
      action="divisi_name_action" 
      sequence="10"/>
  </data>
</odoo>
```
