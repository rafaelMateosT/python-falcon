#!/home/rafael/Escritorio/adapters-falcon/app/venv3/bin/python3
# EASY-INSTALL-ENTRY-SCRIPT: 'swagger-to==4.1.1','console_scripts','swagger_to_elm_client.py'
__requires__ = 'swagger-to==4.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('swagger-to==4.1.1', 'console_scripts', 'swagger_to_elm_client.py')()
    )
