
# © 2021 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, _


class Lead(models.Model):
    _inherit = "crm.lead"

    rgpd_acceptance = fields.Boolean(string='RGPD acceptance')
    rgpd_acceptance_date = fields.Date(string='RGPD acceptance date')

    def _create_lead_partner_data(self, partner_name, is_company=False, parent_id=False):
        res = super(Lead, self)._create_lead_partner_data(partner_name, is_company, parent_id)

        if self.rgpd_acceptance:
            res['rgpd_acceptance'] = True
            res['rgpd_acceptance_date'] = self.rgpd_acceptance_date
            
        return res