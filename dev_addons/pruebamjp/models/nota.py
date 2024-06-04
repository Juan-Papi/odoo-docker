
from odoo import models, fields, api


class nota(models.Model):
    _name = 'pruebamjp.nota'
    _description = 'Modelo o tabla nota'

    nota = fields.Float(required=True)
    curso_materia_id = fields.Many2one('pruebamjp.curso_materia', string="Curso_Materia", ondelete='cascade', required=True)
    estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)