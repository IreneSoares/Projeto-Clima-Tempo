
from alertas.codigo import *

bd = Banco('bdteste')
print("alertaclientes", bd.existBD())


from alertas.codigo import *

bd = Banco('alertaclientes')
bd.createTable()


from alertas.codigo import *

bd = Banco('alertaclientes')
bd.insert('Ana Maria', +12, 12,985263214, +12, 12,985263214, 'anamaria@gmail.com', 'anamaria@gmail.com', 'jacarei', 'whatssap')
bd.insert('Pedro Paulo', +29, 12,985263214, +12, 12,985263214, 'anamaria@gmail.com', 'anamaria@gmail.com', 'são paulo','whatssap')
bd.insert('Mara Lima', +25, 12,985263214, +12, 12,985263214, 'anamaria@gmail.com', 'anamaria@gmail.com', 'caçapava', 'whatssap')
bd.select()