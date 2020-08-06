from channels_discord.consumers import DiscordConsumer

class MyDiscordConsumer(DiscordConsumer):
    def ready(self):
        """
        Optional hook for actions on connection to Discord
        """
        print('You are now connected to discord!')

    def my_custom_message(self):
        """
        Use built-in functions to send basic discord actions
        """
        self.send_action('dm', user_id='238881265946722304', text='your message')