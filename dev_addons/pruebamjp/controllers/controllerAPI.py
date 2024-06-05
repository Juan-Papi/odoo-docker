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
                'modalidad': subnota.modalidad,
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