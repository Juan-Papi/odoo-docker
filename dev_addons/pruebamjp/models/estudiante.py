
from odoo import models, fields, api


class estudiante(models.Model):
    _name = 'pruebamjp.estudiante'
    _description = 'Modelo o tabla estudiante'

    nombre = fields.Char(required=True)
    apellido = fields.Char(required=True)
    edad = fields.Char(required=True)
    nota_ids = fields.One2many('pruebamjp.nota', 'estudiante_id', string="Estudiantes_nota")
    subnota_ids = fields.One2many('pruebamjp.subnota', 'estudiante_id', string="Estudiantes_subnota")
