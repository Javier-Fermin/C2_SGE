import re

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EsportsMatch(models.Model):
    _name = 'esports.match'
    _description = 'Recorded data of the match'

    played_date = fields.Date(string='Played Date')
    winner = fields.Selection([("BLUE_TEAM","Blue Team"),("ORANGE_TEAM","Orange Team")], string='Winner')
    tournament = fields.Many2one(comodel_name='esports.tournament', inverse_name="plays", string='Tournament')
    plays = fields.One2many(comodel_name='esports.stats', inverse_name="match", string='Plays')
    description = fields.Char(string='Description')

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s' % (rec.description)))
        return result

    @api.constrains('played_date')
    def _check_played_date(self):
        for record in self:
            if record.played_date and record.played_date > fields.Date.today():
                raise ValidationError("La fecha de juego no puede ser en el futuro.")

    def write(self, values):
        result = super(EsportsMatch, self).write(values)
        if 'played_date' in values and values['played_date']:
            pass
        return result

    @api.model
    def create(self, values):
        record = super(EsportsMatch, self).create(values)
        if record.played_date and record.played_date > fields.Date.today():
            raise ValidationError("La fecha de juego no puede ser en el futuro.")
        return record

    @api.onchange('description')
    def _check_description(self):
        for record in self:
            if record.description:
                pattern = re.compile(r'^[a-zA-Z0-9\s]*$')
                if not re.match(pattern, record.description):
                    raise ValidationError("La descripción no puede contener caracteres especiales.")