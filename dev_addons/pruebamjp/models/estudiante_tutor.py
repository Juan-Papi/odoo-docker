
from odoo import models, fields, api


class estudiante_tutor(models.Model):
    _name = 'pruebamjp.estudiante_tutor'
    _description = 'Modelo o tabla estudiante tutor'


    relacion=fields.Char() 
    #estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)
    estudiante = fields.Many2one("pruebamjp.estudiante",ondelete="set null",help="estudiante relacionado")
    tutor = fields.Many2one("pruebamjp.tutor",ondelete="set null",help="tutor relacionado")
    
    #tutor_id = fields.Many2one('pruebamjp.tutor', string="Tutor", ondelete='cascade', required=True)
    estudiante_nombre = fields.Char(related='estudiante.nombre', string='Nombre del Estudiante')
    tutor_nombre = fields.Char(related='tutor.nombre', string='Nombre del tutor')
   
