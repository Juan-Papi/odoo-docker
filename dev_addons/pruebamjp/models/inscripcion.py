from odoo import models, fields, api


class inscripcion(models.Model):
     _name = 'pruebamjp.inscripcion'
     _description = 'Modelo o tabla inscripcion'

     estado = fields.Char(required=True)
     gestion_id = fields.Many2one('pruebamjp.gestion', string="Gestion", ondelete='cascade', required=True)
     estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)
     curso_id = fields.Many2one('pruebamjp.curso', string="Curso", ondelete='cascade', required=True)
     mensualidad_ids = fields.One2many('pruebamjp.mensualidad', 'inscripcion_id', string="Inscripciones")
