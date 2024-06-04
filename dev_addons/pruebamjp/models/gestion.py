
from odoo import models, fields, api


class gestion(models.Model):
    _name = 'pruebamjp.gestion'
    _description = 'Modelo o tabla gestion'

    year = fields.Char(required=True)
    hora_inicio = fields.Datetime(required=True)
    hora_fin = fields.Datetime(required=True)
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'gestion_id', string="Gestiones")
    modalidad_gestion_id = fields.Many2one('pruebamjp.modalidad_gestion', string="Modalidad de Gestión", ondelete='cascade', required=True)
    inscripcion_ids = fields.One2many('pruebamjp.inscripcion', 'gestion_id', string="Gestiones")
