
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class horario(models.Model):
    _name = 'pruebamjp.horario'
    _description = 'Modelo o tabla horario'

    hora_inicio = fields.Integer(required=True)
    minuto_inicio=fields.Integer(required=True)
    hora_fin = fields.Integer(required=True)
    minuto_fin=fields.Integer(required=True)
    dia = fields.Char(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'horario_id', string="Horarios")
    

    @api.constrains('hora_inicio', 'hora_fin','minuto_incio','minuto_fin')
    def _check_horas(self):
        for record in self:
            if record.hora_inicio < 7 or record.hora_inicio > 23:
                raise ValidationError("La hora de inicio debe estar entre 7:00 y 23:00.")

            if record.hora_fin < record.hora_inicio:
                raise ValidationError("La hora final no puede ser menor que la hora de inicio.")

            if record.hora_fin > 23:
                raise ValidationError("La hora final no puede ser mayor que las 23:00.")

            if record.minuto_inicio < 0 or record.minuto_inicio > 59 :
                raise ValidationError("La hora final no puede ser mayor que las 23:00.")    
            
            if record.minuto_fin < 0 or record.minuto_fin > 59:
                raise ValidationError("La hora final no puede ser mayor que las 23:00.") 