# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Safa KB (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import fields, models


class FieldWidget(models.Model):
    """
    Need of this model is because we can't filter a selection field dynamically
    so when we select a field its widgets also need to change according to field
    type, this cannot be achieved using a 'selection' field; we require a
    'Many2one' field.
    """
    _name = 'field.widget'
    _description = 'Field Widget'
    _rec_name = 'description'

    name = fields.Char(string="Name", help="Name of widget")
    description = fields.Char(string="Description",
                              help="Description of widget")
    data_type = fields.Char(string="Data type",
                            widget="Field type of widget",
                            help="Type of field")
