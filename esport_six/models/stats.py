from odoo import api,models,fields,exceptions

class Stats(models.Model):
    _name = "esports.stats"

    kills = fields.Integer(string="Kills")
    deaths = fields.Integer(string="Deaths")
    assists = fields.Integer(string="Assists")
    team = fields.Selection([("BLUE_TEAM","Blue Team"),("ORANGE_TEAM","Orange Team")],string="Team")
    player = fields.Many2one(comodel_name="res.users",string="Player")
    match = fields.Many2one(comodel_name="esports.match",string="Match")
    image = fields.Binary(string="image",attachment=True)
    @api.onchange('kills', 'deaths', 'assists')
    def _check_positive_values(self):
        for record in self:
            if record.kills < 0 or record.deaths < 0 or record.assists < 0:
                raise exceptions.ValidationError("Kills, Deaths, and Assists must be greater than or equal to 0.")

    @api.constrains('player')
    def _onchange_player(self):
        if not self.player.is_player:
            raise exceptions.ValidationError("You must select a player, the selected user is not a player.")

    @api.model
    def create(self, vals):
        if 'player' not in vals:
            if self.env.uid.is_player:
                vals['player'] = self.env.uid
        return super(Stats, self).create(vals)

    @api.model
    def write(self, vals):
        return super(Stats, self).writeF(vals)