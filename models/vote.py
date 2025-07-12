from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StackVote(models.Model):
    _name = 'stackit.vote'
    _description = 'Answer Vote'

    answer_id = fields.Many2one('stackit.answer', required=True)
    user_id = fields.Many2one('res.users', required=True)
    vote_type = fields.Selection([
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    ], required=True)

    _sql_constraints = [
        (
            'unique_vote_per_user',
            'unique(answer_id, user_id)',
            'You have already voted on this answer.'
        )
    ]
