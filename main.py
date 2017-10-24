import remi.gui as gui
from remi import start, App
from threading import Timer
import subprocess

class MyApp(App):
	def __init__(self, *args):
		self.main_frame = gui.Widget(width='100%', margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
		super(MyApp, self).__init__(*args)

	def main(self):
		container = gui.Widget(width='100%', margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
		self.append_menubar(container)
		container.append(self.main_frame)
		return container

	def append_menubar(self, container):
		#menubar
		menu = gui.Menu(width='100%', height='30px')
		menu_index = gui.MenuItem('Index', width=100, height=30)
		menu_editor = gui.MenuItem('Editor', width=100, height=30)
		menu_bash = gui.MenuItem("Bash", width=100, height=30)
		menu_ftp = gui.MenuItem("FTP", width=100, height=30)
		menu_index.set_on_click_listener(self.menu_index_clicked)
		menu_editor.set_on_click_listener(self.menu_editor_clicked)
		menu_bash.set_on_click_listener(self.menu_bash_clicked)
		menu_ftp.set_on_click_listener(self.menu_ftp_clicked)

		menu.append(menu_index)
		menu.append(menu_bash)
		menu.append(menu_editor)
		menu.append(menu_ftp)
		menubar = gui.MenuBar(width='100%', height='30px')
		menubar.append(menu)
		container.append(menubar)
		return container

	def menu_index_clicked(self, widget):
		self.main_frame = gui.Widget(width='100%', margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
		pass
	def menu_editor_clicked(self, widget):
		pass
	def menu_bash_clicked(self, widget):
		self.main_frame = gui.Widget(width='100%', margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
		hbox = gui.HBox(width='100%', height=30)
		out = gui.Label("", width="100%", height=30*15, margin='10px')
		txt = gui.TextInput(width='100%', height=30, margin='10px')
		but = gui.Button(text="Confirm", height=30, width=80)

		hbox.append(txt)
		hbox.append(but)
		self.main_frame.append(out)
		self.main_frame.append(hbox)
		self.main()
		pass
	def menu_ftp_clicked(self, widget):
		pass

if __name__ == "__main__":
	# starts the webserver
	# optional parameters
	# start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)

	start(MyApp, debug=True, start_browser=True)
