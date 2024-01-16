from odoo import api,models,fields

class Tournament(models.Model):
    _name = 'esports.tournament'
    _description = 'Tournament entity'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    best_of = fields.Integer(string='Best Of')
    date = fields.Date(string='Date')
    matches = fields.One2many('esport_six.match', 'tournament_id', string='Matches')
