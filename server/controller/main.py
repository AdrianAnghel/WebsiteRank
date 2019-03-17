from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
from server.helper.url_parser import *
from server.helper.dict_array import *
from server.helper.sorted_list_creation import *

parameter = "SESSIONID"


all_values = {}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        current_time = datetime.datetime.now()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b' All time top: \n')
        self.wfile.write(bytes(str(create_top(all_values)), encoding='utf8'))

        self.wfile.write(b'\n Last minute top: \n')
        self.wfile.write(bytes(str(create_top_from_last_minute(all_values, current_time)), encoding='utf8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('ascii').strip()

        if body is None or body == '':
            print("Wrong argument")
            self.send_response(400)
            self.end_headers()
            return


        session_id = get_parameter_from_url(body, parameter)
        root_domain = get_root_domain(body)

        if (root_domain is None or root_domain == '') or (session_id is None or session_id == ''):
            print("No root domain or session_id")
            self.send_response(400)
            self.end_headers()
            return

        # Basic logging
        print("Received post request message " + body)
        print("Session id is: " + session_id)
        print("Domain is " + root_domain)

        # Sending response
        self.send_response(200)
        self.end_headers()

        current_time = datetime.datetime.now()

        if root_domain not in all_values:
            all_values[root_domain] = [[session_id, current_time]]
            print("Added entry")
        elif check_last_time(all_values[root_domain], current_time, session_id):
            all_values[root_domain].append([session_id, current_time])
            print("Added new entry")

        return



httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
