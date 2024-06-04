
from odoo import models, fields, api


class estudiante_tutor(models.Model):
    _name = 'pruebamjp.estudiante_tutor'
    _description = 'Modelo o tabla estudiante tutor'

    estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)
    tutor_id = fields.Many2one('pruebamjp.tutor', string="Tutor", ondelete='cascade', required=True)
  
   
