#3CuN2, 4 of them so 12CuN8, this was the moledcule my dad asked me to make
from ase import Atoms
from ase.calculators.emt import EMT
from ase.visualize import view
import math
nPositions = [(math.sin(45)*8,0,-4),(math.sin(45)*-8,0,-4),(0,math.sin(45)*-8,4),(0,math.sin(45)*8,4),(math.sin(45)*8,0,4),(math.sin(45)*-8,0,4),(0,math.sin(45)*-8,-4),(0,math.sin(45)*8,-4)]
NMolecule = Atoms('8N', positions=nPositions)
NMolecule.calc = EMT()
e_N3 = NMolecule.get_potential_energy()
cuPositions = [(4,4,4),(-4,4,4),(-4,-4,4),(-4,-4,-4),(4,-4,4),(4,-4,-4),(4,4,-4),(-4,4,-4),(math.sin(45)*8,0,0),(math.sin(45)*-8,0,0),(0,math.sin(45)*-8,0),(0,math.sin(45)*8,0)]
CuMolecule = Atoms('12Cu', positions=cuPositions) # basically every tuple is the position of the atoms
CuMolecule.calc = EMT()
e_Cu = CuMolecule.get_potential_energy()

combinedMolecule = NMolecule + CuMolecule #note we can add the two molecules toegther

# Visualize the combined molecule with adjusted camera position
view(combinedMolecule)



