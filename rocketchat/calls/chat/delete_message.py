from rocketchat.calls.base import PostMixin, RocketChatBase


class DeletePrivateRoomMessage(PostMixin,RocketChatBase):
    endpoint = '/api/v1/chat.delete'
    
    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return {'text': kwargs.get('message'), 'roomId': kwargs.get('room_id'), 'msgId':kwargs.get('message_id')}
