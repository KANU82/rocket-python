import logging

from rocketchat.calls.base import RocketChatBase

logger = logging.getLogger(__name__)


class GetPrivateRoomHistory(RocketChatBase):
    endpoint = '/api/v1/groups.history'

    def build_endpoint(self, **kwargs):
        if 'oldest' in kwargs:
            return '{endpoint}?roomId={room_id}&oldest={oldest}&count={message_count}'.format(
                endpoint=self.endpoint,
                oldest=kwargs.get('oldest'),
                room_id=kwargs.get('room_id'),
                message_count=kwargs.get('message_count'))
        else:
            return '{endpoint}?roomId={room_id}'.format(
                endpoint=self.endpoint,
                room_id=kwargs.get('room_id')
            )

    def post_response(self, result):
        return result
