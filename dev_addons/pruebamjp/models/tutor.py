
from odoo import models, fields, api


class tutor(models.Model):
    _name = 'pruebamjp.tutor'
    _description = 'Modelo o tabla tutor'

   
    nombre = fields.Char(required=True)
    apellido = fields.Char(required=True)
    telefono = fields.Char(required=True)
    direccion = fields.Char(required=True)
    #estudiante_tutor = fields.One2many('pruebamjp.estudiante_tutor', 'tutor_id', string="Tutores")
    estudiante_tutor=fields.One2many(string="estudiante_tutor", comodel_name="pruebamjp.estudiante_tutor",inverse_name='tutor')
    usuario_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user, required=True)
   
    @api.depends('nombre', 'apellido') 
    def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.nombre} {rec.apellido}"