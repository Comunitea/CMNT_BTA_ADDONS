
# © 2021 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, _


class MailMail(models.AbstractModel):
    _inherit = "mail.mail"

    def _send_prepare_values(self, partner=None):
        res = super()._send_prepare_values(partner)

        get_param = self.env['ir.config_parameter'].sudo().get_param
        base_url = get_param('web.base.url')
        list_id = get_param('website_custom_bta.list_id')

        newsletter_string = '<tr><td align="center" style="min-width: 590px; padding: 8px; font-size:11px;"><a target="_blank" href="{}/website_custom_bta/subscribe?list_id={}&email={}" style="color: #875A7B;">{}</a></td></tr>'.format(
            base_url,
            list_id,
            partner.email if partner else self.email_to,
            _('Subscribe to our newsletter'),
        )        

        position = res['body'].rfind('</table>')
        res['body'] = res['body'][:position] + newsletter_string + res['body'][position:]

        return res