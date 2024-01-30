from odoo import api,models,fields

class Users(models.Model):
    _inherit = "res.users"

    is_player = fields.Boolean(string="Is player")
    nickname = fields.Char(string="Nickname")
    