from odoo import models, fields, api


ESTADOS_RESERVA = [
    ('borrador', 'Borrador'),
    ('confirmado', 'Confirmado'),
    ('reservado', 'Reservado')
]


class Reserva(models.Model):
    _name = "ias.reserva"
    _description = "Reserva por consultorio"


    name = fields.Char(string="Numero de reserva", store=True, default=lambda self: self.next_seque_name())
    doctor = fields.Many2one('res.partner', domain=[('es_doctor', '=', True)], required=True)
    responsable = fields.Many2one('res.users', default=lambda self: self.env.user)
    fecha_inicio = fields.Datetime(string="Fecha Inicio de la reserva")
    fecha_fin =  fields.Datetime(string="Fecha Fin de la reserva")
    dia_semana = fields.Char(string="Dia de la semana", compute="")
    hora_inicio = fields.Char(string="Hora inicio", compute="")
    hora_fin = fields.Char(string="Hora Fin", compute="")
    costo_reserva = fields.Integer(string="Costo de la reserva")
    consultorio_id = fields.Many2one('ias.consultorio', string="Consultorio")
    especialidad_del_doctor = fields.Char(related='doctor.especialidad', store=True)
    estado = fields.Selection(ESTADOS_RESERVA, string="Estado de reserva", default="borrador")


    def next_seque_name(self):
        rv_ins = self.env['ias.reserva']
        next_val = len(rv_ins.search([])) + 1
        return f"RES000{next_val}"
    
    def create(self, vals):
        res = super(Reserva, self).create(vals.update({'name': self.next_seque_name()}))
        return res
    