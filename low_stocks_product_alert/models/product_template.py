# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, fields, models


class ProductTemplate(models.Model):
    """
    This is an Odoo model for product templates. It inherits from the
    'product.template' model and extends its functionality by adding computed
    fields for product alert state and color field.

    Methods:
         _compute_alert_state: Computes the 'alert_state' and 'color_field'
         fields based on the product's stock quantity and low stock
    alert parameters

    """
    _inherit = 'product.template'

    alert_state = fields.Boolean(string='Product Alert State',
                                 compute='_compute_alert_state',
                                 help='This field represents the alert state'
                                      'of the product')
    color_field = fields.Char(string='Background color',
                              help='This field represents the background '
                                   'color of the product.')

    @api.depends('qty_available')
    def _compute_alert_state(self):
        """ Computes the 'alert_state' and 'color_field' fields based on
        the product's stock quantity and low stock alert parameters."""
        stock_alert = self.env['ir.config_parameter'].sudo().get_param(
            'low_stocks_product_alert.is_low_stock_alert')
        for rec in self:
            if stock_alert:
                rec.alert_state, rec.color_field = (False, 'white') if \
                    rec.type != 'consu' or rec.qty_available > int(
                        rec.env['ir.config_parameter'].sudo().get_param(
                            'low_stocks_product_alert.min_low_stock_alert')) \
                    else (True, '#fdc6c673')
            else:
                rec.alert_state = False
                rec.color_field = 'white'
