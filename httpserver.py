import logging
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/root/handshakes", **kwargs)

class HttpServerPlugin(plugins.Plugin):
    __author__ = 'Hades'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'HTTP Server Plugin'

    def on_loaded(self):
        logging.info("HttpServerPlugin loaded")
        self.start_http_server()

    def on_unload(self, ui):
        self.stop_http_server()

    def start_http_server(self):
        try:
            server_address = ('', 8000)
            self.httpd = HTTPServer(server_address, MyHTTPRequestHandler)
            logging.info("Starting HTTP server on port 8000")
            self.httpd.serve_forever()

        except Exception as e:
            logging.error(f"Error starting HTTP server: {e}")

    def stop_http_server(self):
        try:
            if hasattr(self, 'httpd'):
                logging.error("Shutting Down HTTP Server.")
                self.httpd.shutdown()

        except Exception as e:
            logging.error(f"Error stopping HTTP server: {e}")

    def on_ui_setup(self, ui):
        ui.add_element('http_server', LabeledValue(color=BLACK, label='HTTP', value='localhost:8000',
                                                   position=(ui.width() / 2 - 50, ui.height() - 10),
                                                   label_font=fonts.Bold, text_font=fonts.Medium))

# Instantiate the plugin
http_server_plugin = HttpServerPlugin()
