# -*- coding: utf-8 -*-
# from odoo import http


# class Opencademy(http.Controller):
#     @http.route('/opencademy/opencademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/opencademy/opencademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('opencademy.listing', {
#             'root': '/opencademy/opencademy',
#             'objects': http.request.env['opencademy.opencademy'].search([]),
#         })

#     @http.route('/opencademy/opencademy/objects/<model("opencademy.opencademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('opencademy.object', {
#             'object': obj
#         })
