from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK - mission 1 alive from WSL\n")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Signe de vie from WSL\n")


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
