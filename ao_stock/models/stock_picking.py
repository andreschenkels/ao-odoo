# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class Picking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def copy(self, default=None):
        # When we copy a picking, put it by default in draft to allow
        # the users to change the source or destination locations. By setting
        # in the context 'planned_picking' you allow that.
        return super(Picking, self.with_context(planned_picking=True)).copy(
            default)

    def action_view_account_moves(self):
        self.ensure_one()
        action = self.env.ref('account.action_account_moves_all_a')
        result = action.read()[0]
        result['domain'] = [('stock_move_id', 'in', self.move_lines.ids)]
        return result
