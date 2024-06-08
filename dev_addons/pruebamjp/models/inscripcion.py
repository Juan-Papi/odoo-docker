from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
     

     @api.depends('estudiante' ,'estudiante_nombre', 'curso_nombre','curso_paralelo','gestion_year') 
     def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.estudiante_nombre} - {rec.estudiante.apellido} {rec.curso_nombre} - {rec.curso_paralelo} - {rec.gestion_year}"


     #def _compute_nombre_estudiante(self):
     # if self.estudiante:
     #   self.estudiante_nombre = self.estudiante.nombre
     # else:
     #   self.estudiante_nombre = ''