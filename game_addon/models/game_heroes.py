from odoo import models, fields, api
import json


class GameHeroes(models.Model):
    _name = 'game.heroes'
    _description = 'Game heroes'
    hero_name = fields.Char('Hero name')
    hero_side = fields.Char('Hero side')
    picks_per_day = fields.Integer('Pick frequency')
    picks_per_day_previous_patch = fields.Integer('Previous pick frequency')
    hero_role = fields.Char('Hero role')
    hero_attribute = fields.Char('Hero attribute')
    win_rate = fields.Integer('Win rate')
    pick_rate_coefficient = fields.Float('Coefficient', compute='_get_pick_coeff')

    def _get_pick_coeff(self):
        for coeff in self:
            coeff.pick_rate_coefficient = round(coeff.picks_per_day / coeff.picks_per_day_previous_patch, 2)
