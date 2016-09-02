import sublime
import sublime_plugin
#view.run_command("remove_empty_lines")
def clearText(lines):
		x=""
		for line in lines:
			if len(line.strip()) > 0:
				x = x+line+"\n"
		return x
class RemoveEmptyLines(sublime_plugin.TextCommand):
	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		lines = [line for line in contents.splitlines()]
		self.view.replace(edit, sublime.Region(0, self.view.size()), clearText(lines))
		self.view.run_command("save")
		#see the following SO question
		#http://stackoverflow.com/questions/27475049/updating-the-tab-file-status-after-saving-in-a-sublime-text-plugin
		# Refresh the buffer and clear the dirty flag:
		sublime.set_timeout(lambda: self.view.run_command("revert"), 10)
