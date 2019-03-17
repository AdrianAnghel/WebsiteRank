from urllib.parse import urlparse
from urllib.parse import parse_qs
import re

def get_root_domain(url):
    try:
        #Striping /
        url_without_protocol = url.split("/")[2]

        # Striping . and ?
        main_url_elements = re.split('\.|\?', url_without_protocol)

        return main_url_elements[1] + "." + main_url_elements[2]
    except:
        return None

def get_parameter_from_url(url, parameter):
    try:
        parsed = urlparse(url)
        return parse_qs(parsed.query)[parameter][0]
    except:
        return None