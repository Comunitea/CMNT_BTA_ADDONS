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

