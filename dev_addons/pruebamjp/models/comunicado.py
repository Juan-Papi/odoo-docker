
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class comunicado(models.Model):
    _name = 'pruebamjp.comunicado'
    _description = 'Modelo o tabla comunicado'

    nombre = fields.Char(required=True)
    description = fields.Text(required=True)
    fecha = fields.Datetime(required=True)
    comunicado_usuario_ids = fields.One2many('pruebamjp.comunicado_usuario', 'comunicado_id', string="Comunicados")
   
    @api.model
    def create_comunicado_for_all_users(self, nombre, description):
        comunicado = self.create({
            'nombre': nombre,
            'description': description,
            'fecha': datetime.now(),
        })
        users = self.env['res.users'].search([])
        comunicado._create_comunicado_usuarios(users)
        return comunicado
