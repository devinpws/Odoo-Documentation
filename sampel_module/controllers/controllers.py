# -*- coding: utf-8 -*-
# from odoo import http


# class SampelModule(http.Controller):
#     @http.route('/sampel_module/sampel_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sampel_module/sampel_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sampel_module.listing', {
#             'root': '/sampel_module/sampel_module',
#             'objects': http.request.env['sampel_module.sampel_module'].search([]),
#         })

#     @http.route('/sampel_module/sampel_module/objects/<model("sampel_module.sampel_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sampel_module.object', {
#             'object': obj
#         })
