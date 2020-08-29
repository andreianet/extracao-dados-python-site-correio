######----Fonte:https://pycep-correios.readthedocs.io/pt/develop/
import pycep_correios
from pycep_correios.exceptions import BaseException
import pandas as pd

try:
    endereco = pycep_correios.get_cep_from_address(
        state='SP', city='Marilia', street='Rua Nove de Julho')

except BaseException as exec:
    print(exec.message)





print(endereco)