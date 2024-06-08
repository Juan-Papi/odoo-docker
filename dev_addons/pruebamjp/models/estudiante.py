
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class estudiante(models.Model):
    _name = 'pruebamjp.estudiante'
    _description = 'Modelo o tabla estudiante'

    nombre = fields.Char(readonly=False,required=True)
    apellido = fields.Char(required=True)
    edad = fields.Char(required=True)
    nota_ids = fields.One2many('pruebamjp.nota', 'estudiante_id', string="Estudiantes_nota")
    subnota_ids = fields.One2many('pruebamjp.subnota', 'estudiante_id', string="Estudiantes_subnota")
    inscripcion_ids = fields.One2many('pruebamjp.inscripcion', 'estudiante', string="Estudiantes")
    
    #estudiante_tutor_ids = fields.One2many('pruebamjp.estudiante_tutor', 'estudiante_id', string="Estudiantes")
    estudiante_tutor=fields.One2many(string="estudiante_tutor", comodel_name="pruebamjp.estudiante_tutor",inverse_name='estudiante')
    

    @api.depends('nombre', 'apellido') 
    def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.nombre} {rec.apellido}"




    @api.constrains('nombre','apellido')
    def _check_unique_estudiante(self):
        for rec in self:
            existing_records = self.search([
                ('nombre', '=', rec.nombre),
                ('apellido', '=', rec.apellido),
                
                
                ('id', '!=', rec.id)
            ])
            if existing_records:
                raise ValidationError('ya existe el estudiante')  

    def unlink(self):
        for estudiantes in self:
            if  estudiantes.inscripcion_ids or estudiantes.estudiante_tutor:
                raise ValidationError("No se puede eliminar el estudiante porque tiene  inscripciones  o tutores relacionados.")
        return super(estudiante, self).unlink()          