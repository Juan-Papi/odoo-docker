from odoo import models, fields, api


class materia(models.Model):
     _name = 'pruebamjp.materia'
     _description = 'Modelo o tabla materia'

     nombre = fields.Char(required=True)
     curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'materia_id', string="Materias del Curso")