
from odoo import models, fields, api


class horario(models.Model):
    _name = 'pruebamjp.horario'
    _description = 'Modelo o tabla horario'

    hora_inicio = fields.Datetime(required=True)
    hora_fin = fields.Datetime(required=True)
    dia = fields.Char(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'horario_id', string="Horarios")
