# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class CommissionSettlement(models.Model):
    _inherit = "commission.settlement"

    settlement_type = fields.Selection(
        selection_add=[("sale_invoice", "Sales Invoices"), ("sale_order", "Sale Orders")],
        ondelete={"sale_invoice": "set default", "sale_order": "set default"},
    )
    sale_order_id = fields.Many2one(
        string="Sale Order",
        comodel_name="sale.order",
        help="Reference to the sale order related to this settlement.",
    )

    @api.onchange('commission_id')
    def _onchange_commission_id(self):
        self.sale_order_id = self.commission_id.sale_order_id
