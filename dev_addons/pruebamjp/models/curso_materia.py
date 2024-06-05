
from odoo import models, fields, api


class curso_materia(models.Model):
    _name = 'pruebamjp.curso_materia'
    _description = 'Modelo o tabla curso materia'

    # Campo Many2one para relacionar con curso
    curso_id = fields.Many2one('pruebamjp.curso', string="Curso", ondelete='cascade', required=True)
    curso_nombre = fields.Char(related='curso_id.nombre', string='Curso') 
    curso_paralelo = fields.Char(related='curso_id.paralelo', string='Curso') 


    materia_id = fields.Many2one('pruebamjp.materia', string="Materia", ondelete='cascade', required=True)
    materia_nombre = fields.Char(related='materia_id.nombre', string='Materia') 
    
    profesor_id = fields.Many2one('pruebamjp.profesor', string="Profesor", ondelete='cascade', required=True)
    profesor_nombre = fields.Char(related='profesor_id.nombre', string='Profesor') 
    


    ciclo_id = fields.Many2one('pruebamjp.ciclo', string="Ciclo", ondelete='cascade', required=True)
    ciclo_nombre = fields.Char(related='ciclo_id.nombre', string='Ciclo') 
    
    
    horario_id = fields.Many2one('pruebamjp.horario', string="Horario", ondelete='cascade', required=True)
    hora_inicio = fields.Integer(related='horario_id.hora_inicio', string='Hora_inicio') 
       
    nota_ids = fields.One2many('pruebamjp.nota', 'curso_materia_id', string="Cursos_Materias_nota")
    
    
    subnota_ids = fields.One2many('pruebamjp.subnota', 'curso_materia_id', string="Cursos_Materias_subnota")
    gestion_id = fields.Many2one('pruebamjp.gestion', string="Gestion", ondelete='cascade', required=True) 
    year = fields.Integer(related='gestion_id.year', string='Año') 
    