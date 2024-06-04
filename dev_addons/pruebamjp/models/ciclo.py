
from odoo import models, fields, api


class ciclo(models.Model):
    _name = 'pruebamjp.ciclo'
    _description = 'Modelo o tabla ciclo'

    nombre = fields.Char(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'ciclo_id', string="Ciclos")
