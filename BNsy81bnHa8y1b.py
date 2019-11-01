from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
 
vk = vk_api.VkApi(token="67830553b755540f91bbae17f891947080351051b6da16a7b5c766c85d0e6faa18a467a00955beea26fae")
 
vk._auth_token()
 
vk.get_api()
 
longpoll = VkBotLongPoll(vk, "188229739")
 
while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id != event.object.from_id:
                if event.object.text.lower() == "Дарова":
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": event.object.text,
                                                "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text.lower() == "привет":
                    vk.method("messages.send", {"user_id": event.object.from_id, "message": event.object.text,
                                                "random_id": 0})
