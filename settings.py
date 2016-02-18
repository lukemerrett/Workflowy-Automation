# Fill these in using your own local_settings.py file in the same directory
workflowy_username = ""
workflowy_password = ""

try:
    from local_settings import *
except ImportError:
    pass
