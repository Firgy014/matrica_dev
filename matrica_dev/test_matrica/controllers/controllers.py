# -*- coding: utf-8 -*-
# from odoo import http


# class TestMatrica(http.Controller):
#     @http.route('/test_matrica/test_matrica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_matrica/test_matrica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_matrica.listing', {
#             'root': '/test_matrica/test_matrica',
#             'objects': http.request.env['test_matrica.test_matrica'].search([]),
#         })

#     @http.route('/test_matrica/test_matrica/objects/<model("test_matrica.test_matrica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_matrica.object', {
#             'object': obj
#         })
