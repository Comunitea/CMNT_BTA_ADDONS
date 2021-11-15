
# © 2021 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, _


class Lead(models.Model):
    _inherit = "crm.lead"

    def _create_lead_partner_data(self, partner_name, is_company=False, parent_id=False):
        res = super(Lead, self)._create_lead_partner_data(partner_name, is_company, parent_id)

        if "checkbox_rgpd_acceptance : on" in self.description:
            res['rgpd_acceptance'] = True
            res['rgpd_acceptance_date'] = self.create_date
            
        return res