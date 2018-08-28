import sys
smiles=sys.argv[1]
ic50=int(sys.argv[2])*1000
kd=int(sys.argv[3])*1000
print("""loop_
_pdbx_binding_assay.id
_pdbx_binding_assay.target_sequence_one_letter_code
_pdbx_binding_assay.ligand_descriptor_type
_pdbx_binding_assay.ligand_descriptor
_pdbx_binding_assay.assay_type
_pdbx_binding_assay.assay_value_type
_pdbx_binding_assay.assay_value
_pdbx_binding_assay.assay_pH
_pdbx_binding_assay.assay_temperature
_pdbx_binding_assay.details""")
print("""1
;KEWQENKSWNAHFTEHKSQGVVVLWNENKQQGFTNNLKRANQAFLPASTFKIPNSLIALD
LGVVKDEHQVFKWDGQTRDIATWNRDHNLITAMKYSVVPVYQEFARQIGEARMSKMLHAF
DYGNEDISGNVDSFWLDGGIRISATEQISFLRKLYHNKLHVSERSQRIVKQAMLTEANGD
YIIRAKTGYSTRIEPKIGWWVGWVELDDNVWFFAMNMDMPTSDGLGLRQAITKEVLKQEK
IIP
;
SMILES '%s' 'competitive binding' IC50 %s  7.0  298.0 '100 pM OXA-48. Competition with 25 uM Nitrocefin, measured at 482 nm.'""" %(smiles,ic50))

print("""2
;AKEWQENKSWNAHFTEHKSQGVVVLWNENKQQGFTNNLKRANQAFLPASTFKIPNSLIALD
LGVVKDEHQVFKWDGQTRDIATWNRDHNLITAMKYSVVPVYQEFARQIGEARMSKMLHAF
DYGNEDISGNVDSFWLDGGIRISATEQISFLRKLYHNKLHVSERSQRIVKQAMLTEANGD
YIIRAKTGYSTRIEPKIGWWVGWVELDDNVWFFAMNMDMPTSDGLGLRQAITKEVLKQEK
IIP
;
SMILES '%s' 'surface plasmon resonance' Kd %s 7.0 298.0 'Amine-coupled OXA-48, Rmax adjusted for positive control.'""" %(smiles,kd))

