# -*- coding: utf-8 -*-
# from odoo import http


# class LibarayApp(http.Controller):
#     @http.route('/libaray_app/libaray_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libaray_app/libaray_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libaray_app.listing', {
#             'root': '/libaray_app/libaray_app',
#             'objects': http.request.env['libaray_app.libaray_app'].search([]),
#         })

#     @http.route('/libaray_app/libaray_app/objects/<model("libaray_app.libaray_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libaray_app.object', {
#             'object': obj
#         })
