import curses
from curses import wrapper
import time
import random

class WpmTester:
	def __init__(self, stdscr):
		self.stdscr = stdscr


	def start_screen(self):
		self.stdscr.clear()
		self.stdscr.addstr("Welcome to the Speed Typing Test!")
		self.stdscr.addstr("\nPress any key to begin!")
		self.stdscr.refresh()
		self.stdscr.getkey()

	def display_text(self, target, current, wpm=0):
		self.stdscr.addstr(target)
		self.stdscr.addstr(1, 0, f"WPM: {wpm}")

		for i, char in enumerate(current):
			correct_char = target[i]
			color = curses.color_pair(1)
			if char != correct_char:
				color = curses.color_pair(2)
			self.stdscr.addstr(0, i, char, color)

	def load_text(self):
		with open("text.txt", "r") as f:
			lines = f.readlines()
			return random.choice(lines).strip()

	def wpm_test(self):
		target_text = "Hello this is some test text for this app!"
		current_text = []
		wpm = 0
		start_time = time.time()
		self.stdscr.nodelay(True)

		while True:
			time_elapsed = max(time.time() - start_time, 1)
			wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

			self.stdscr.clear()
			self.display_text(target_text, current_text, wpm)
			self.stdscr.refresh()

			if "".join(current_text) == target_text:
				self.stdscr.nodelay(False)
				break

			try:
				key = self.stdscr.getkey()
			except:
				continue

			if ord(key) == 27:
				break

			if key in ("KEY_BACKSPACE", '\b', "\x7f"):
				if len(current_text) > 0:
					current_text.pop()
			elif len(current_text) < len(target_text):
				current_text.append(key)


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	wpmTesterInstance = WpmTester(stdscr)

	wpmTesterInstance.start_screen()
	while True:
		wpmTesterInstance.wpm_test()
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)
