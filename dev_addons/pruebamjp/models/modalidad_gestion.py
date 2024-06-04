
from odoo import models, fields, api


class modalidad_gestion(models.Model):
    _name = 'pruebamjp.modalidad_gestion'
    _description = 'Modelo o tabla modalidad'

    nombre = fields.Char(required=True)
    subnota_ids = fields.One2many('pruebamjp.subnota', 'modalidad_gestion_id', string="Modalidad_gestiones")
    
   
