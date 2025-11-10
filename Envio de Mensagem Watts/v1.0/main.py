#pip install pywhatkit

import pywhatkit as kit
from datetime import datetime

# Ver Data Atual
Data_Atual = datetime.now()

# Mensagem Padrão
kit.sendwhatmsg_instantly(
    "+555194261577",
    "Olá Joseph. Eu vim através do GitHub"
)

# Em caso de usar 2x telas, sempre usar na tela principal
# Não roda na segunda tela por causa do PyAutoGui

# Mensagem Agendada
# Mensagem deve ter no minímo de 2min para cima de espera, caso contrário é considerado mensagem estantânea
kit.sendwhatmsg(
    "+555194261577",
    "Olá Joseph. Eu vim através do GitHub ➡ mensagem Agendada",
    # Usar Biblioteca DateTime
    # Hora
    Data_Atual.hour,
    # Minuto
    Data_Atual.minute + 5 # Enviar mensagem daqui á 5min
)