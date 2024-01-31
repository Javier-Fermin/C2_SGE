import datetime

from odoo import api,models,fields,exceptions
from datetime import date

class Tournament(models.Model):
    _name = 'esports.tournament'
    _description = 'Tournament entity'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    best_of = fields.Integer(string='Best Of')
    date = fields.Date(string='Date')
    matches = fields.One2many('esport_six.match', 'tournament_id', string='Matches')

    @api.onchange('best_of')
    def _check_numeric_values(self):
        for record in self:
            if record.best_of < 1:
                raise exceptions.ValidationError("The tournament best of value must be more than or equal to 1.")

    #constraint de date format
    @api.constrains
    def _onchange_date(self):
        if self.date.null():
            raise exceptions.ValidationError("The date field must be informed, the selected date is null.")

    #api.model create & write
    @api.model
    def create(self, vals):
        if 'date' not in vals:
            vals['date'] = date.today()
        return super(Tournament, self).create(vals)

    @api.model
    def write(self, vals):
        return super(Tournament, self).write(vals)