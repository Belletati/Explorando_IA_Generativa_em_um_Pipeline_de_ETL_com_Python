import os
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server

PORT = int(os.getenv('PORT', 8000))  
os.chdir('static')  

httpd = Server(("", PORT), Handler)
try:
    print(f"Start serving at port {PORT}" )
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()   