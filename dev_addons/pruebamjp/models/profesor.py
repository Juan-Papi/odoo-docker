
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class profesor(models.Model):
    _name = 'pruebamjp.profesor'
    _description = 'Modelo o tabla profesor'

    nombre = fields.Char(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'profesor_id', string="Profesores")
  


        
    @api.depends('nombre') 
    def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.nombre}" 


    @api.constrains('nombre')
    def _check_unique_estudiante(self):
        for rec in self:
            existing_records = self.search([
                ('nombre', '=', rec.nombre),
                
                
                ('id', '!=', rec.id)
            ])
            if existing_records:
                raise ValidationError('ya existe el profesor')
    
    
    def unlink(self):
        for profesores in self:
            if profesores.curso_materia_ids :
                raise ValidationError("No se puede eliminar el profesor porque esta relacionado a un curso.")
        return super(profesor, self).unlink()                            