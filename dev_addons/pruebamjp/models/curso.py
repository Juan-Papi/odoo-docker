
from odoo import models, fields, api


class curso(models.Model):
    _name = 'pruebamjp.curso'
    _description = 'Modelo o tabla curso'

    nombre = fields.Char(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'curso_id', string="Cursos")
