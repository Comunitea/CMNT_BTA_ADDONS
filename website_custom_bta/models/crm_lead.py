
# © 2021 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, _


class Lead(models.Model):
    _inherit = "crm.lead"

    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        res = super(Lead, self)._prepare_customer_values(partner_name, is_company, parent_id)

        if "Acepto la política de privacidad%0D%0A                             : Yes" in self.description:
            res['rgpd_acceptance'] = True
            res['rgpd_acceptance_date'] = self.create_date
            
        return res