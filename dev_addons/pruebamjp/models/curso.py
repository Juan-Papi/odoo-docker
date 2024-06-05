
from odoo import models, fields, api


class curso(models.Model):
    _name = 'pruebamjp.curso'
    _description = 'Modelo o tabla curso'

    nombre = fields.Char(required=True)
    paralelo=fields.Char()
    curso_materia_ids = fields.One2many('pruebamjp.curso_materia', 'curso_id', string="Cursos")
    inscripcion_ids = fields.One2many('pruebamjp.inscripcion', 'curso', string="Cursos")



    def action_save_and_back_to_tree(self):
        self.ensure_one()
        self.write({'nombre': self.nombre})  
        return {
            'type': 'ir.actions.act_window',
            'name': 'crearCurso',
            'view_mode': 'tree,form',
            'res_model': 'pruebamjp.curso',
            'res_id': self.id,
            'target': 'current',
        }