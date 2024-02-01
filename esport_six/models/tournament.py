import datetime

from odoo import api,models,fields,exceptions
from datetime import date

class Tournament(models.Model):
    _name = 'esports.tournament'
    _description = 'Tournament entity'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    best_of = fields.Integer(string='Best Of', default=1)
    date = fields.Date(string='Date')
    matches = fields.One2many(comodel_name='esports.match', inverse_name="tournament", string='Matches')

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s' % (rec.name)))
        return result

    @api.onchange('best_of')
    def _check_numeric_values(self):
        for record in self:
            if record.best_of < 1:
                raise exceptions.ValidationError("The tournament best of value must be more than or equal to 1.")

    #constraint de date format
    @api.constrains('date')
    def _constrains_date(self):
        if not self.date:
            raise exceptions.ValidationError("The date field must be informed, the selected date is null.")

    @api.model
    def create(self, vals):
        if 'date' not in vals:
            vals['date'] = date.today()
        return super(Tournament, self).create(vals)

    def write(self, vals):
        return super(Tournament, self).write(vals)