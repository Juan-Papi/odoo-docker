
from odoo import models, fields, api


class comunicado_usuario(models.Model):
    _name = 'pruebamjp.comunicado_usuario'
    _description = 'Modelo o tabla comunicado_usuario'

    visto = fields.Char(required=True)
    comunicado_id = fields.Many2one('pruebamjp.comunicado', string="Comunicado", ondelete='cascade', required=True)
    usuario_recibe_id = fields.Many2one('res.users', string='UsuarioRecibe', default=lambda self: self.env.user, required=True)
    usuario_envia_id = fields.Many2one('res.users', string='UsuarioEnvia', default=lambda self: self.env.user)

    @api.model
    def default_get(self, fields_list):
        res = super(comunicado_usuario, self).default_get(fields_list)
        user = self.env.user
        if 'usuario_envia_id' in fields_list:
            res['usuario_envia_id'] = user.id
        return res