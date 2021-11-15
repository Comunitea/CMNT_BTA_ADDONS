# © 2021 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Website RGPD Custom",
    "summary": "Customization to move RGPD acceptance fields from crm lead to partner.",
    "version": "12.0.1.0.0",
    "author": "Comunitea Servicios Tecnológicos S.L.",
    "website": "www.comunitea.com",
    "category": "Custom",
    "depends": [
        "website_crm",
        "website_sale",
        "payment"
    ],
    "license": "LGPL-3",
    "data": [
        "views/payment.xml",
        "views/assets.xml",
        "views/partner.xml",
        "views/contact_form.xml",
    ],
}
