from rdkit import Chem
import sys
import re
from  rdkit.Chem.rdMolDescriptors import CalcMolFormula
formula = CalcMolFormula(Chem.MolFromSmiles(sys.argv[1]))
print re.sub(r'([a-z]*)([A-Z])',r'\1 \2',formula).lstrip()
