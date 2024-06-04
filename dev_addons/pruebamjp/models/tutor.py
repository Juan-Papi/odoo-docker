
from odoo import models, fields, api


class tutor(models.Model):
    _name = 'pruebamjp.tutor'
    _description = 'Modelo o tabla tutor'

   
    nombre = fields.Char(required=True)
    apellido = fields.Char(required=True)
    telefono = fields.Char(required=True)
    direccion = fields.Char(required=True)
    estudiante_tutor_ids = fields.One2many('pruebamjp.estudiante_tutor', 'tutor_id', string="Tutores")
  
   
