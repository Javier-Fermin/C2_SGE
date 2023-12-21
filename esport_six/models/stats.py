from odoo import api,models,fields

class Stats(models.Model):
    _name = "esports.stats"

    kills = fields.Integer(string="Kills")
    deaths = fields.Integer(string="Deaths")
    assists = fields.Integer(string="Assists")
    team = fields.Selection([("BLUE_TEAM","Blue Team"),("ORANGE_TEAM","Orange Team")],string="Team")
    #player = fields.Many2one(comodel_name="esports.player",string="Player")
    match = fields.Many2one(comodel_name="esports.match",string="Match")