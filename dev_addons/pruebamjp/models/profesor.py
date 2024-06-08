
from odoo import models, fields, api


class profesor(models.Model):
    _name = 'pruebamjp.profesor'
    _description = 'Modelo o tabla profesor'

    nombre = fields.Char(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'profesor_id', string="Profesores")
  


        
    @api.depends('nombre') 
    def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.nombre}" 