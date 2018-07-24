# -*- coding: utf-8 -*-
from odoo import http

# class Botchat(http.Controller):
#     @http.route('/botchat/botchat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/botchat/botchat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('botchat.listing', {
#             'root': '/botchat/botchat',
#             'objects': http.request.env['botchat.botchat'].search([]),
#         })

#     @http.route('/botchat/botchat/objects/<model("botchat.botchat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('botchat.object', {
#             'object': obj
#         })