from odoo import api,models,fields

class Player(models.Model):
    _inherit = "res.user"
    _name = "esports.stats"

    nickname = fields.Char(string="Nickname")
    