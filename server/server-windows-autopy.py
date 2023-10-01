import sys
import libi2dx
from os import path
import keyboard
from configparser import ConfigParser

def toggle(key, state):
	print(key, state)
	if state:
		keyboard.press(key)
	else:
		keyboard.release(key)

class I2DXWebSocketAutoPy(libi2dx.I2DXWebSocket):
	def toggle_key(self, key_id, state, player):
		try:
			toggle(libi2dx.config.get('keymap_player%s' % player, key_id), state)
		except ConfigParser.NoOptionError:
			print("key map not found for %s, player %s" % (key_id, player))

if __name__ == "__main__":
	libi2dx.serve(I2DXWebSocketAutoPy)
