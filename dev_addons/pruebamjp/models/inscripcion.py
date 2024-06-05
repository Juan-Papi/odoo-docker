from odoo import models, fields, api


class inscripcion(models.Model):
     _name = 'pruebamjp.inscripcion'
     _description = 'Modelo o tabla inscripcion'

     estado = fields.Char(required=True)
     gestion_id = fields.Many2one('pruebamjp.gestion', string="Gestion", ondelete='cascade', required=True)
     gestion_year = fields.Integer(related='gestion_id.year', string='Año')

     estudiante = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)
     estudiante_nombre = fields.Char(related='estudiante.nombre', string='Estudiante')
    
     curso = fields.Many2one('pruebamjp.curso', string="Curso", ondelete='cascade', required=True)
     curso_nombre = fields.Char(related='curso.nombre', string='Curso')
     curso_paralelo = fields.Char(related='curso.paralelo', string='Paralelo')

     mensualidad_ids = fields.One2many('pruebamjp.mensualidad', 'inscripcion_id', string="Inscripciones")
     
     #def _compute_nombre_estudiante(self):
     # if self.estudiante:
     #   self.estudiante_nombre = self.estudiante.nombre
     # else:
     #   self.estudiante_nombre = ''