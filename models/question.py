from odoo import models, fields, api

class StackQuestion(models.Model):
    _name = 'stackit.question'
    _description = 'Forum Question'

    title = fields.Char(required=True)
    description = fields.Html(string="Question Details")
    user_id = fields.Many2one('res.users', string="Asked By", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('stackit.tag', string="Tags")
    is_anonymous = fields.Boolean(string="Post Anonymously", default=False)
    created_at = fields.Datetime(string="Created At", default=fields.Datetime.now)
    answer_count = fields.Integer(string="Answer Count", compute='_compute_answer_count')

    def _compute_answer_count(self):
        for rec in self:
            rec.answer_count = self.env['stackit.answer'].search_count([('question_id', '=', rec.id)])
