from odoo import api,models,fields

class Match(models.Model):
    _name = "esports.match"
    _description = "Rcorded data of the match"

    id = fields.Integer(string='ID', required=True)
    played_date = fields.Date(string='Played Date')
    winner = fields.Selection([('team1', 'Team 1'), ('team2', 'Team 2')], string='Winner')
    #tournament = fields.Many2one('your_module.tournament', string='Tournament')
    #league = fields.Many2one('your_module.league', string='League')
    #plays = fields.One2many('your_module.stats', 'match_id', string='Plays')
    description = fields.Char(string='Description')
