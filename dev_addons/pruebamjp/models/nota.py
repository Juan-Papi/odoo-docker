
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class nota(models.Model):
    _name = 'pruebamjp.nota'
    _description = 'Modelo o tabla nota'

    nota = fields.Float(required=True)
    
    
    curso_materia_id = fields.Many2one('pruebamjp.curso_materia', string="Curso_Materia", ondelete='cascade', required=True)
    curso_nombre = fields.Char(related='curso_materia_id.curso_nombre', string='Curso') 
    curso_paralelo = fields.Char(related='curso_materia_id.curso_paralelo', string='Paralelo')
    materia_nombre=fields.Char(related='curso_materia_id.materia_nombre', string='Materia')
    year=fields.Integer(related='curso_materia_id.year', string='Año')
 
    estudiante_id = fields.Many2one('pruebamjp.estudiante', string="Estudiante", ondelete='cascade', required=True)
    estudiante_nombre=fields.Char(related='estudiante_id.nombre', string='Estudiante')