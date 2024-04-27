from odoo import models, fields


class ResPartner(models.Model):

    _inherit = "res.partner"
    

    es_doctor = fields.Boolean(string="Es doctor?", default=False)
    especialidad = fields.Char(string="Especialidad")