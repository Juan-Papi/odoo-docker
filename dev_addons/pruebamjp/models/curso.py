
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class curso(models.Model):
    _name = 'pruebamjp.curso'
    _description = 'Modelo o tabla curso'

    nombre = fields.Char(required=True)
    paralelo=fields.Char()
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'curso_id', string="Cursos")
    inscripcion_ids = fields.One2many('pruebamjp.inscripcion', 'curso', string="Cursos")


    
    @api.model
    def create(self, vals):
        # Convertir a mayúsculas antes de crear el registro
        if 'nombre' in vals:
            vals['nombre'] = vals['nombre'].upper()
        if 'paralelo' in vals:
            vals['paralelo'] = vals['paralelo'].upper()
        return super(curso, self).create(vals)         
    



    
    @api.constrains('nombre', 'paralelo')
    def _check_unique_curso_paralelo(self):
        for record in self:
            # Validar que los campos estén en mayúsculas
            if record.nombre != record.nombre.upper() or record.paralelo != record.paralelo.upper():
                raise ValidationError('Los campos nombre y paralelo deben estar en mayúsculas.')
        for record in self:
            existing = self.search([
                ('nombre', '=', record.nombre),
                ('paralelo', '=', record.paralelo),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError('El curso y paralelo deben ser únicos.')    
   


    @api.depends('nombre','paralelo') 
    def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.nombre} {rec.paralelo} "


    def unlink(self):
        for cursos in self:
            if cursos.curso_materia_ids or cursos.inscripcion_ids:
                raise ValidationError("No se puede eliminar el curso porque tiene materias o inscripciones relacionadas.")
        return super(curso, self).unlink()        