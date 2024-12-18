import base64

usuario = "meu-usuario"
senha   = "senha-secreta"

auth_string = f'{usuario}:{senha}'.encode()
auth_string = base64.b64encode(auth_string)

print(auth_string)