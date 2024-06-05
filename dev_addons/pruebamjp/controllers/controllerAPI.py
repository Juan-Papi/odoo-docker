from odoo import http
from odoo.http import request
import json
from werkzeug.wrappers import Response

class ApiController(http.Controller):

    @http.route('/api/login', type='http', auth='none', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        try:
            # Decodificar directamente los datos de la solicitud
            data = json.loads(request.httprequest.data.decode('utf-8'))
            db = data.get('db')
            login = data.get('login')
            password = data.get('password')
            
            if not db or not login or not password:
                response_data = json.dumps({'error': 'Faltan credenciales'})
                return Response(response_data, status=400, mimetype='application/json', headers=[('Access-Control-Allow-Origin', '*')])
            
            uid = request.session.authenticate(db, login, password)
            if uid:
                response_data = json.dumps({'uid': uid, 'session_token': request.session.sid})
                return Response(response_data, status=200, mimetype='application/json', headers=[('Access-Control-Allow-Origin', '*')])
            else:
                response_data = json.dumps({'error': 'Autenticación fallida'})
                return Response(response_data, status=401, mimetype='application/json', headers=[('Access-Control-Allow-Origin', '*')])
        except Exception as e:
            response_data = json.dumps({'error': str(e)})
            return Response(response_data, status=500, mimetype='application/json', headers=[('Access-Control-Allow-Origin', '*')])


    
    @http.route('/api/test', auth='user', methods=['GET'], csrf=False)
    def test_endpoint(self, **kwargs):
        data = {
            'message': 'Este es un endpoint de prueba',
            'user': request.env.user.name,
            'extra_info': 'Aquí puedes añadir más datos como desees'
        }
        response_data = json.dumps(data)
        return request.make_response(response_data, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')])
    
    
    @http.route('/api/subnota/estudiante/<int:estudiante_id>', auth='user', methods=['GET'], csrf=False)
    def get_estudiante_data(self, estudiante_id, **kwargs):
        estudiante = request.env['pruebamjp.estudiante'].browse(estudiante_id)

        # Verifica si el estudiante existe
        if not estudiante.exists():
            response_data = json.dumps({'error': 'Estudiante no encontrado'})
            return request.make_response(response_data, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')], status=404)


        # Preparar datos del estudiante
        data = {
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'edad': estudiante.edad,
            'notas': [],
            'modalidades': set(),  # Utilizar un conjunto para evitar duplicados
            'cursos_materias': set()  # Utilizar un conjunto para evitar duplicados
        }

        # Agregar notas y otras informaciones
        for subnota in estudiante.subnota_ids:
            nota_data = {
                'nota': subnota.nota,
                'numero': subnota.numero,
                'curso_materia': {
                    'curso': subnota.curso_materia_id.curso_id.nombre,
                    'materia': subnota.curso_materia_id.materia_id.nombre
                }
            }
            data['notas'].append(nota_data)
            data['modalidades'].add(subnota.modalidad_gestion_id.nombre)
            curso_materia_data = (subnota.curso_materia_id.curso_id.nombre, subnota.curso_materia_id.materia_id.nombre)
            data['cursos_materias'].add(curso_materia_data)

        # Convertir conjuntos a listas antes de serializar a JSON
        data['modalidades'] = list(data['modalidades'])
        data['cursos_materias'] = list(data['cursos_materias'])

        # Serializar y devolver la respuesta
        response_data = json.dumps(data)
        return request.make_response(response_data, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')])
    
    
    # @http.route('/api/mis_estudiantes', auth='user', methods=['GET'], csrf=False)
    # def mis_estudiantes(self, **kwargs):
    #     usuario_actual = request.env.user
    #     tutor = request.env['pruebamjp.tutor'].search([('usuario_id', '=', usuario_actual.id)], limit=1)

    #     if not tutor:
    #         response_data = json.dumps({'error': 'Tutor no encontrado'})
    #         return request.make_response(response_data, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')], status=404)

    #     estudiantes = []
    #     for estudiante_tutor in tutor.estudiante_tutor_ids:
    #         estudiante_data = {
    #             'nombre': estudiante_tutor.estudiante_id.nombre,
    #             'apellido': estudiante_tutor.estudiante_id.apellido,
    #             'edad': estudiante_tutor.estudiante_id.edad,
    #         }
    #         estudiantes.append(estudiante_data)

    #     response_data = json.dumps({'estudiantes': estudiantes})
    #     return request.make_response(response_data, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')])
    
    
    # @http.route('/api/estudiante/<int:estudiante_id>/curso/<int:curso_id>/notas', auth='user', methods=['GET'], csrf=False)
    # def get_notas_curso(self, estudiante_id, curso_id, **kwargs):
    #     try:
    #         estudiante = request.env['pruebamjp.estudiante'].browse(estudiante_id)
    #         if not estudiante.exists():
    #             return request.make_response(json.dumps({'error': 'Estudiante no encontrado'}), status=404, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')])

    #         curso = request.env['pruebamjp.curso'].browse(curso_id)
    #         if not curso.exists():
    #             return request.make_response(json.dumps({'error': 'Curso no encontrado'}), status=404, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')])

    #         # Diccionario para almacenar la información de las notas y subnotas
    #         materia_notas = []

    #         # Obtener todos los curso_materia para el curso especificado
    #         for cm in curso.curso_materia_ids:
    #             # Filtrar las notas y subnotas para el estudiante en el curso_materia actual
    #             notas = request.env['pruebamjp.nota'].search([('curso_materia_id', '=', cm.id), ('estudiante_id', '=', estudiante.id)])
    #             subnotas = request.env['pruebamjp.subnota'].search([('curso_materia_id', '=', cm.id), ('estudiante_id', '=', estudiante.id)])

    #             # Preparar la información para la respuesta
    #             notas_info = [nota.nota for nota in notas]
    #             subnotas_info = [{'nota': subnota.nota, 'numero': subnota.numero} for subnota in subnotas]
    #             materia_notas.append({
    #                 'materia': cm.materia_id.nombre,
    #                 'notas': notas_info,
    #                 'subnotas': subnotas_info
    #             })

    #         # Devolver la respuesta
    #         return request.make_response(json.dumps(materia_notas), headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')])
    #     except Exception as e:
    #         return request.make_response(json.dumps({'error': str(e)}), status=500, headers=[('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')])
        
        