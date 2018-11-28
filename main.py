import os
import http.server as server


port= 8081
path = 'C:/OSM'

os.chdir(path=path)

with server.ThreadingHTTPServer(('', port), server.SimpleHTTPRequestHandler) as httpd:
    print('Start tileserver on port %d path [%s]' % (port, path))
    httpd.serve_forever()
