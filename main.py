from http.server import BaseHTTPRequestHandler, HTTPServer

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/test':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'12')
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=TestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Serving on port 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
