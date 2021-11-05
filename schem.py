import schemdraw
from schemdraw import logic
import schemdraw.elements as elm
#logic.Not()

d = schemdraw.Drawing()
d.add(elm.Resistor())
d.add(elm.Capacitor())
d.add(elm.Diode())
d.draw()
d.save('circuit_schem.svg')
