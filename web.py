from flask import Flask, json, request
import vk

app = Flask(__name__)

confirmation_token = '6d75c23e'
returning = 'hello'
token = 'bddeddc0f08b56addc83768d464cea4246ecb5e1b2c9b5df894900aeb84dcec396cc77eae7a5b6062bd6f'

@app.route('/', methods=['POST'])
def processing():
        #Распаковываем json из пришедшего POST-запроса
    returning = 'post'
    print(request.data)
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
        api.messages.send(access_token=token, user_id=user_id, message='Привет, я новый бот!')
        # Сообщение о том, что обработка прошла успешно
        return 'ok'

@app.route('/', methods=['GET'])
def index():
  print('index')
  return returning

if __name__ == "__main__":
        app.run()
