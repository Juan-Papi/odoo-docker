
from odoo import models, fields, api


class subnota(models.Model):
    _name = 'pruebamjp.subnota'
    _description = 'Modelo o tabla subnota'

    nota = fields.Float(required=True)
    modalidad = fields.Char(required=True)
    numero = fields.Integer(required=True)
  
    curso_materia_id = fields.Many2one('pruebamjp.curso_materia', string="Curso_Materia", ondelete='cascade', required=True)
    modalidad_gestion_id = fields.Many2one('pruebamjp.modalidad_gestion', string="Modalidad_Gestion", ondelete='cascade', required=True)
    estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)
