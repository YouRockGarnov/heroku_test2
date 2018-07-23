from flask import Flask

app = Flask(__name__)

confirmation_token = '6d75c23e'

@app.route('/', methods=['POST'])
def processing():
        #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.0)
        user_id = data['object']['user_id']
        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!')
        # Сообщение о том, что обработка прошла успешно
        return 'ok'

@app.route('/')
def index():
  return 'hello'
