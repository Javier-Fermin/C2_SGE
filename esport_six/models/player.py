from odoo import api,models,fields

class Player(models.Model):
    _inherit = "res.users"
    #_name = "esports.player"

    nickname = fields.Char(string="Nickname")
    