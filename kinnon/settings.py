
"""
Módulo para configurações
"""
import os


__version__ = '0.0.0'

LISA = 'http://104.237.1.145:2154/graphql/'
URL = os.environ.get('BACKEND_URL')
TOKEN = os.environ.get('TOKEN')

