# -*- coding: utf-8 -*-
from odoo import http
from odoo.tools.translate import _
from odoo.http import request
from datetime import datetime
from odoo.addons.connecto.controllers.main import WebsiteConatctUsCreate


class WebsiteContactUsCreate(WebsiteConatctUsCreate):

    @http.route('/contact_us_action', type='json', auth='public', website=True)
    def create_subscribe(self, **data):
        data = data and data['datas']
        res = dict()
        for d in eval(data):
            res[d.get('name')] = d.get('value')
        print("res: {}".format(res))
        subscribe = request.env['crm.lead'].sudo().create({
            'name': res.get('name'),
            'email_from': res.get('email'),
            'description': res.get('subject') + ' : ' + res.get('message'),
            'rgpd_acceptance': res.get('checkbox_rgpd_acceptance'),
            'rgpd_acceptance_date': datetime.today() if res.get('checkbox_rgpd_acceptance') else None
        })
        if not subscribe:
            return False
