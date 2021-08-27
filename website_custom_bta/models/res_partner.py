# © 2021 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    rgpd_acceptance = fields.Boolean(string='RGPD acceptance')
    rgpd_acceptance_date = fields.Date(string='RGPD acceptance date')
