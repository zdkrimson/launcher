import webview
import modelfetch

syshost=modelfetch.system.Model

class Api:
	def get_host(self):
	    return syshost

api = Api()
webview.create_window('zdkrimson', background_color="#210202", url="index.html", js_api=api)
webview.start(private_mode=False, debug=True)