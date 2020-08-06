from channels.routing import ProtocolTypeRouter
from profiles.consumers import MyDiscordConsumer

application = ProtocolTypeRouter({
    'discord': MyDiscordConsumer,
})