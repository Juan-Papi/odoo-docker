
from odoo import models, fields, api


class profesor(models.Model):
    _name = 'pruebamjp.profesor'
    _description = 'Modelo o tabla profesor'

    nombre = fields.Char(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'profesor_id', string="Profesores")
