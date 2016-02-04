# http://toomanyideas.net/2013/improve-sublime-text-2-part-1.html
# Bind this to super+0 in order to reset the font to the default after
# having zoomed in / out using super +/-
import sublime
import sublime_plugin


class ResetFontSizeToUserDefaultsCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        s = sublime.load_settings("Preferences.sublime-settings")

        if s.has('default_font_size'):
            s.set('font_size', s.get('default_font_size'))
            sublime.save_settings("Preferences.sublime-settings")