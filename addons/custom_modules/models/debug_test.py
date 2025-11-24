from odoo import models, fields, api

class DebugTest(models.Model):
    _name = 'debug.test'
    _description = 'Debug Test Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    computed_value = fields.Integer(string='Computed Value', compute='_compute_value')

    @api.depends('name')
    def _compute_value(self):
        for record in self:
            # Đặt breakpoint ở đây để debug
            length = len(record.name or '')  # Ví dụ tính độ dài name
            record.computed_value = length * 2  # Nhân đôi để debug

    def action_debug(self):
        # Method action để trigger từ button
        self.ensure_one()
        # Đặt breakpoint ở đây
        result = self.computed_value + 10
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Debug Result',
                'message': f'Computed value after action: {result}',
                'sticky': False,
            }
        }