from odoo import api,models,fields

class Tournament(models.Model):
    _name = 'esport_six.tournament'
    _description = 'Tournament entity'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    best_of = fields.Integer(string='Best Of')
    date = fields.Date(string='Date')
    matches = fields.One2many('esport_six.match', 'tournament_id', string='Matches')

    @api.model
    def find_tournaments_by_name(self, name):
        return self.search([('name', 'ilike', name)])

    @api.model
    def find_tournaments_by_date(self, date):
        return self.search([('date', '=', date)])

    @api.model
    def find_tournaments_by_format(self, best_of):
        return self.search([('best_of', '=', best_of)])

    @api.model
    def find_match_tournament(self, match_id):
        return self.search([('matches.id', '=', match_id)])

    @api.model
    def find_all_tournaments(self):
        return self.search([])

    class Match(models.Model):
        _name = 'esport_six.match'
        _description = 'Match entity'

        # Define match fields
        tournament_id = fields.Many2one('esport_six.tournament', string='Tournament')
        # Add other match fields as needed
