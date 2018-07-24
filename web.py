from flask import Flask, json, request
import vk

app = Flask(__name__)

confirmation_token = '6d75c23e'
returning = 'hello'
token = 'bddeddc0f08b56addc83768d464cea4246ecb5e1b2c9b5df894900aeb84dcec396cc77eae7a5b6062bd6f'
app_id = 6630979
_wait_for_sender = []

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    print(data)

    session = vk.Session()
    api = vk.API(session, v=5.0)
    user_id = data['object']['user_id']
    message = data['object']['body']
    

    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':

        

        if message == 'ok':
            sender_vkid = user_id
        elif message == 'send me':
            api.send_message(user_id=481116745, access_token=token, message='lol')
        else:
            response = 'Я на отправил запрос к {0}. Необходимо зайти на эту страницу и подтвердить добавление.'.format(message)

            auth_link = 'https://oauth.vk.com/authorize?client_id={app_id}&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,messages,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token '.format(
                app_id=228)  # TODO INSERT CORRECT TOKEN

            api.send_message(user_id=message, access_token=token, message='heh')#'Вашу страницу добавляют для рассылки, для подтверждения этого надо пройти по этой ссылке {0}, скопировать ссылку из адресной строки и отправить мне обратно.'.format(auth_link))

            _wait_for_sender.append(message)

@app.route('/', methods=['GET'])
def index():
  print('index')
  return returning

if __name__ == "__main__":
        app.run()
