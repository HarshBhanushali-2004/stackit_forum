from odoo import models, fields

class StackNotification(models.Model):
    _name = 'stackit.notification'
    _description = 'User Notification'

    user_id = fields.Many2one('res.users', required=True)
    question_id = fields.Many2one('stackit.question')
    message = fields.Char(required=True)
    is_read = fields.Boolean(default=False)
    created_at = fields.Datetime(default=fields.Datetime.now)
