
# from odoo import models, fields, api
# from odoo.exceptions import ValidationError
# from datetime import date
from odoo import models, fields, api
from datetime import date
class asistencia(models.Model):
     _name = 'pruebamjp.asistencia'
     _description = 'Modelo o tabla asistencia'
     curso_materia_id = fields.Many2one('pruebamjp.curso_materia', string="Curso Materia", required=True)
     estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", required=True)
     gestion_id = fields.Many2one('pruebamjp.gestion', string="Gestion", required=True, compute='_compute_gestion_id', store=True)
     fecha = fields.Date(string="Fecha", default=fields.Date.context_today, required=True)
     asistio = fields.Boolean(string="Asistió", default=False, required=True)

#     @api.depends('curso_materia_id')
#     def _compute_gestion_id(self):
#         for record in self:
#             record.gestion_id = record.curso_materia_id.gestion_id if record.curso_materia_id else False

#     @api.constrains('curso_materia_id', 'gestion_id')
#     def _check_gestion(self):
#         for record in self:
#             if record.curso_materia_id.gestion_id != record.gestion_id:
#                 raise ValidationError("La gestión del Curso Materia y la gestión seleccionada deben coincidir.")

#     @api.model
#     def create(self, vals):
#         # Verificar si ya existe una asistencia para el estudiante, curso materia y fecha
#         existing_asistencia = self.search([
#             ('curso_materia_id', '=', vals.get('curso_materia_id')),
#             ('estudiante_id', '=', vals.get('estudiante_id')),
#             ('fecha', '=', vals.get('fecha'))
#         ])
#         if existing_asistencia:
#             raise ValidationError("Ya existe un registro de asistencia para este estudiante en este curso materia y fecha.")
#         return super(asistencia, self).create(vals)

class asistenciawizard(models.Model):
    _name = 'pruebamjp.asistenciawizard'
    _description = 'Wizard para registrar asistencia'

    curso_materia_id = fields.Many2one('pruebamjp.curso_materia', string="Curso Materia", required=True)
    asistencia_line_ids = fields.One2many('pruebamjp.asistencia_wizard_line', 'wizard_id', string="Asistencia")

    # @api.onchange('curso_materia_id')
    # def _onchange_curso_materia_id(self):
    #     if self.curso_materia_id:
    #         inscripciones = self.env['pruebamjp.inscripcion'].search([
    #             ('curso', '=', self.curso_materia_id.curso_id.id),
    #             ('gestion_id', '=', self.curso_materia_id.gestion_id.id)
    #         ])
    #         estudiantes = inscripciones.mapped('estudiante')
    #         lines = []
    #         for estudiante in estudiantes:
    #             lines.append((0, 0, {
    #                 'estudiante': estudiante.id,
    #                 'curso_materia_id': self.curso_materia_id.id,
    #                 'fecha': fields.Date.today(),
    #             }))
    #         self.asistencia_line_ids = lines

    # def action_confirm(self):
    #     for line in self.asistencia_line_ids:
    #         self.env['pruebamjp.asistencia'].create({
    #             'curso_materia_id': line.curso_materia_id.id,
    #             'estudiante': line.estudiante.id,
    #             'gestion_id': self.curso_materia_id.gestion_id.id,
    #             'fecha': line.fecha,
    #             'asistio': line.asistio,
    #         })

class asistenciawizardline(models.TransientModel):
    _name = 'pruebamjp.asistencia_wizard_line'
    _description = 'Línea del Wizard de Asistencia'

    wizard_id = fields.Many2one('pruebamjp.asistencia_wizard', string="Wizard")
    estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", required=True)
    curso_materia_id = fields.Many2one('pruebamjp.curso_materia', string="Curso Materia", required=True)
    fecha = fields.Date(string="Fecha", default=fields.Date.context_today, required=True)
    asistio = fields.Boolean(string="Asistió", default=False, required=True)


   
    

    #@api.model
    #def create(self, vals):
        # Convertir a mayúsculas antes de crear el registro
    #    if 'nombre' in vals:
    #        vals['nombre'] = vals['nombre'].upper()
    #    if 'apellido' in vals:
    #        vals['apellido'] = vals['apellido'].upper()
    #    return super(tutor, self).create(vals) 

    
    #@api.constrains('nombre', 'apellido')
    #def _check_mayusculas(self):
    #    for record in self:
    #        # Validar que los campos estén en mayúsculas
    #        if record.nombre != record.nombre.upper() or record.apellido != record.apellido.upper():
    #            raise ValidationError('Los campos nombre y apelliido deben estar en mayúsculas.')
   
   
   
    #@api.depends('nombre', 'apellido') 
    #def _compute_display_name(self): 
    #     for rec in self: 
    #         rec.display_name = f"{rec.nombre} {rec.apellido}"

   




    #@api.constrains('nombre','apellido')
    #def _check_unique_tutor(self):
    #    for rec in self:
    #        existing_records = self.search([
    #            ('nombre', '=', rec.nombre),
    #            ('apellido', '=', rec.apellido),
                
                
    #            ('id', '!=', rec.id)
    #        ])
    #        if existing_records:
    #            raise ValidationError('ya existe el tutor')           