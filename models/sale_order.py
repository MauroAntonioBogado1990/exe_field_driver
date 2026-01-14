from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    exe_field_driver = fields.Many2one(
        'res.partner',
        string='Transportista',
        help='Transportista (contacto) asociado a la cotización'
    )
