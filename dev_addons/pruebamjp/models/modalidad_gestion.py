
from odoo import models, fields, api


class modalidad_gestion(models.Model):
    _name = 'pruebamjp.modalidad_gestion'
    _description = 'Modelo o tabla modalidad gestion'

    nombre = fields.Char(required=True)
    subnota_ids = fields.One2many('pruebamjp.subnota', 'modalidad_gestion_id', string="Modalidad_gestiones")
    
    
    @api.depends('nombre') 
    def _compute_display_name(self): 
         for rec in self: 
             rec.display_name = f"{rec.nombre} "