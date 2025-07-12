from odoo import models, fields, api

class StackAnswer(models.Model):
    _name = 'stackit.answer'
    _description = 'Forum Answer'

    question_id = fields.Many2one('stackit.question', required=True)
    user_id = fields.Many2one('res.users', string="Answered By", default=lambda self: self.env.user)
    content = fields.Html(string="Answer Content")
    vote_count = fields.Integer(string="Vote Count", compute='_compute_vote_count')

    def _compute_vote_count(self):
        for rec in self:
            upvotes = self.env['stackit.vote'].search_count([
                ('answer_id', '=', rec.id),
                ('vote_type', '=', 'up')
            ])
            downvotes = self.env['stackit.vote'].search_count([
                ('answer_id', '=', rec.id),
                ('vote_type', '=', 'down')
            ])
            rec.vote_count = upvotes - downvotes
