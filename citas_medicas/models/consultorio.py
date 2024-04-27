from odoo import models, fields

DIAS_DISPONIBILIDAD = [
    ('0', 'Lunes'),
    ('1', 'Martes'),
    ('2', 'Miércoles'),
    ('3', 'Jueves'),
    ('4', 'Viernes'),
    ('5', 'Sábado'),
    ('6', 'Domingo'),
]

class Disponibilidad(models.Model):
    _name = "ias.disponibilidad.consultorio"
    _description = "Disponibilidad"

    name = fields.Char(string="Disponibilidad", compute="", store=True)
    dia_semana = fields.Selection(DIAS_DISPONIBILIDAD, string="Disponibilidad")
    hora_inicio = fields.Char(string="Hora inicio", compute="")
    hora_fin = fields.Char(string="Hora Fin", compute="")


class Consultorios(models.Model):

    _name = "ias.consultorio"
    _description = "Modulo de consultorios"

    name = fields.Char(string="Consultorio")
    disponibilidad_ids = fields.Many2many('ias.disponibilidad.consultorio')
    
    