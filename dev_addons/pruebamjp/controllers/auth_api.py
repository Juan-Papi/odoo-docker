# academic_management/controllers/auth_api.py
from odoo import http
from odoo.http import request
import json
from werkzeug.wrappers import Response
import jwt
import datetime
import logging

_logger = logging.getLogger(__name__)

CORS = "*"


class AuthAPI(http.Controller):

    secret_key = "hola"

    @http.route("/api/auth/login", auth="public", type="json", methods=["POST"])
    def authenticate(self, **kwargs):
        try:
            params = json.loads(request.httprequest.data)
            username = params.get("username")
            password = params.get("password")

            # Autenticar el usuario con el nombre de la base de datos actual
            uid = request.session.authenticate(
                request.env.cr.dbname, username, password
            )
            if uid is not False:  # Verificar si la autenticación fue exitosa
                user = request.env["res.users"].browse(uid)

                payload = {
                    "user_id": user.id,
                    "exp": datetime.datetime.now()
                    + datetime.timedelta(hours=2),  # Token expira en 2 horas
                }
                token = jwt.encode(payload, self.secret_key, algorithm="HS256")
                _logger.info("Token creado correctamente para el usuario %s", username)

                response_data = {
                    "success": True,
                    "message": "Usuario autenticado con éxito.",
                    "data": {
                        "user_id": user.id,
                        "user_name": user.name,
                        "user_email": user.email,
                        "token": token,
                    },
                }
                return response_data

            _logger.error("Credenciales inválidas para el usuario %s", username)
            return {"error": "Credenciales no válidas"}
        except Exception as e:
            _logger.exception("Error en el proceso de autenticación: %s", str(e))
            return {
                "error": "Error Interno del Servidor",
                "message": str(e),
                "success": False,
            }

    def _response_with_cors(self, data, status=200):
        response = request.make_response(json.dumps(data), headers=[
            ("Content-Type", "application/json"),
            ("Access-Control-Allow-Origin", CORS),
        ])
        response.status_code = status
        return response

    @http.route("/api/students/by_tutor", auth="public", methods=["GET"])
    def get_students_by_tutor(self):
        token = request.httprequest.headers.get("Authorization")
        if not token:
            _logger.error("Token faltante en la solicitud")
            return self._response_with_cors({
                "error": "Token faltante",
                "success": False,
            }, 401)

        if token.startswith("Bearer "):
            token = token.split(" ")[1]  # Obtener solo el token, sin el prefijo 'Bearer '

        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            user_id = payload.get("user_id")

            # Verificar que el usuario es un tutor
            tutor = request.env["pruebamjp.tutor"].sudo().search([('usuario_id', '=', user_id)])
            if not tutor:
                _logger.error("El usuario con ID %s no es tutor", user_id)
                return self._response_with_cors({
                    "error": "Usuario no autorizado",
                    "message": "El usuario no es tutor",
                    "success": False,
                }, 403)

            # Obtener los estudiantes relacionados con el tutor
            estudiantes = []
            for estudiante_tutor in tutor.estudiante_tutor:
                estudiante = estudiante_tutor.estudiante
                estudiantes.append({
                    "id": estudiante.id,
                    "nombre": estudiante.nombre,
                    "apellido": estudiante.apellido,
                    "edad": estudiante.edad,
                    # Incluir otros campos según necesidad
                })

            return self._response_with_cors({
                "success": True,
                "data": estudiantes,
            })

        except jwt.ExpiredSignatureError:
            _logger.error("Token expirado")
            return self._response_with_cors({
                "error": "Token expirado",
                "success": False,
            }, 403)
        except jwt.InvalidTokenError:
            _logger.error("Token inválido")
            return self._response_with_cors({
                "error": "Token inválido",
                "success": False,
            }, 403)
        except Exception as e:
            _logger.exception("Error al procesar la solicitud: %s", str(e))
            return self._response_with_cors({
                "error": "Error Interno del Servidor",
                "message": str(e),
                "success": False,
            }, 500)
            
    
    @http.route("/api/auth/check-status", auth="public", methods=["GET"])
    def check_auth_status(self):
        token = request.httprequest.headers.get('Authorization')
        if not token:
            _logger.error("Token faltante en la solicitud")
            return self._response_with_cors({
                'error': 'Token missing',
                'success': False
            }, 401)

        if token.startswith("Bearer "):
            token = token.split(" ")[1]  # Eliminar el prefijo 'Bearer '

        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            user_id = payload.get("user_id")

            user = request.env['res.users'].sudo().search([('id', '=', user_id)], limit=1)
            if not user:
                _logger.error("No se encontró el usuario con ID: %s", user_id)
                return self._response_with_cors({
                    'error': 'Invalid token',
                    'message': 'User not found',
                    'success': False
                }, 401)

            # Crear un nuevo token para el usuario
            new_payload = {
                "user_id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # Token expira en 2 horas
            }
            new_token = jwt.encode(new_payload, self.secret_key, algorithm="HS256")

            # Crear la respuesta con los datos del usuario y el nuevo token
            response_data = {
                'success': True,
                'data': {
                    'user_id': user.id,
                    'user_name': user.name,
                    'user_email': user.login,
                    'token': new_token
                }
            }
            return self._response_with_cors(response_data)

        except jwt.ExpiredSignatureError:
            _logger.error("Token expirado")
            return self._response_with_cors({
                'error': 'Token expired',
                'success': False
            }, 401)
        except jwt.InvalidTokenError:
            _logger.error("Token inválido")
            return self._response_with_cors({
                'error': 'Invalid token',
                'success': False
            }, 401)
        except Exception as e:
            _logger.exception("Error al procesar la solicitud: %s", str(e))
            return self._response_with_cors({
                'error': 'Internal Server Error',
                'message': str(e),
                'success': False
            }, 500)
    