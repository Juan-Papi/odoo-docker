from odoo import models, fields, api


class materia(models.Model):
     _name = 'pruebamjp.materia'
     _description = 'Modelo o tabla materia'

     nombre = fields.Char(required=True)
     curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'materia_id', string="Materias del Curso")



     
     @api.depends('nombre') 
     def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.nombre}" 