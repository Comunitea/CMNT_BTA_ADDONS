# © 2021 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import http
from odoo.http import request
from datetime import datetime
from werkzeug.exceptions import BadRequest

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.mass_mailing.controllers.main import MassMailController


class WebsiteSaleBta(WebsiteSale):

    @http.route()
    def payment_transaction(self, *args, **kwargs):
        res = super(WebsiteSaleBta, self).payment_transaction(*args, **kwargs)

        order = request.website.sale_get_order()
        if order and order.partner_id and not order.partner_id.rgpd_acceptance:
            order.partner_id.write({
                'rgpd_acceptance': True,
                'rgpd_acceptance_date': datetime.today(),
            })

        return res

class MassMailController(MassMailController):

    @http.route('/website_custom_bta/subscribe', type="http", auth="public", methods=["GET"],)
    def subscribe(self, list_id, email, **post):

        if not email or not list_id:
            return BadRequest()
        
        ContactSubscription = request.env['mailing.contact.subscription'].sudo()
        Contacts = request.env['mailing.contact'].sudo()
        name, email = Contacts.get_name_email(email)

        subscription = ContactSubscription.search([('list_id', '=', int(list_id)), ('contact_id.email', '=', email)], limit=1)
        if not subscription:
            contact_id = Contacts.search([('email', '=', email)], limit=1)
            if not contact_id:
                contact_id = Contacts.create({'name': name, 'email': email})
            ContactSubscription.create({'contact_id': contact_id.id, 'list_id': int(list_id)})
        elif subscription.opt_out:
            subscription.opt_out = False

        return request.render("website_custom_bta.subscription_successful")
        