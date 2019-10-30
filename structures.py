polder=0 #try without polder-type first
reference="/home/bjartel/papers/SGDD-OXA48/5dtkA.pdb"
contour=2.5 #sigma level
carving= 2 #distance from atoms that map is contoured
if polder:
	amplitudes="crystal/dataset/mFo-DFc_polder"
	phases="crystal/dataset/PHImFo-DFc_polder"
else:
	amplitudes="crystal/dataset/mFo-DFc_omit"
	phases="crystal/dataset/PHImFo-DFc_omit"
import sys

sys.path.append("/home/bjartel/bin/pymol/ext/lib/python2.7/")

import pymol
pymol.finish_launching()

import __main__
__main__.pymol_argv = ['pymol','-qc'] # Pymol: quiet and no GUI
from time import sleep

import csv
csvfile="structures.csv"
csvreader = csv.DictReader(open(csvfile),delimiter=",")

stickresidues = (250,244,211,214,105,70,209,208)

for structure in csvreader:
	pymol.cmd.reinitialize()
	pymol.cmd.set("valence")
	pymol.cmd.bg_color("white")
	pymol.cmd.load(reference,"reference")
	if structure["chain"]:
		chain=structure["chain"]
	else:
		chain="A"
	pdbid=structure["pdbid"]
	pymol.cmd.load(structure["pdbfile"],"coordinates")
	pymol.cmd.extract("chainofinterest","chain %s and object coordinates" % chain)
	pymol.cmd.disable("coordinates")
	pymol.cmd.alignto("reference")
	pymol.cmd.disable("reference") #no longer needed
	pymol.cmd.load("%s_1.ccp4" % structure["Name"] ,"mapfile") #_2 for omit, _1 for polder
	pymol.cmd.hide("all")
	pymol.cmd.matrix_copy("chainofinterest","mapfile")
	pymol.cmd.map_double("mapfile") #Enable for prettier maps, disabled for debugging
	pymol.cmd.extract("ligand","resn %s and chain %s" % (pdbid,chain))
	pymol.cmd.isomesh("meshmap","mapfile",contour,"ligand",carve=carving)
	pymol.cmd.color("grey50","meshmap")
	pymol.cmd.set("mesh_width",0.5)
	pymol.cmd.set("ray_trace_fog",0)
	pymol.cmd.set("depth_cue",0)
	pymol.cmd.set("ray_shadows",0)
	pymol.cmd.show("sticks","ligand and not h.")
#	pymol.cmd.show("cartoon","chainofinterest")
	pymol.cmd.set("transparency", 0.5)
	pymol.cmd.set("surface_color","cyan")
	pymol.cmd.show("surface","chainofinterest")
	for residue in stickresidues:
		pymol.cmd.select("residueselection","resi %i and not (name C,O,N and not pro/n)" % residue)
		pymol.cmd.show("sticks","residueselection and not (name N,C,O)")
	pymol.cmd.hide("sticks","h.")
	pymol.cmd.color("pink","alt B") #color alternative 
	pymol.cmd.set("sphere_scale",0.2)
	pymol.cmd.show("spheres","resn HOH within 5 of ligand")
	pymol.cmd.distance("hbonds","chainofinterest","ligand",3.2,2)
	pymol.cmd.hide("labels")
	pymol.cmd.set_view("(-0.6934636235237122, -0.23585866391658783, 0.6807906627655029, -0.5805761218070984, 0.7424745559692383, -0.3341514766216278, -0.42665964365005493, -0.6269726753234863, -0.6518124938011169, 0.00011520832777023315, 0.0005027921870350838, -53.577293395996094, 6.098320007324219, 42.98721694946289, 145.5330810546875, 20.930614471435547, 86.49679565429688, -20.0)")
	#pymol.cmd.set_view("(-0.4473198652267456, 0.21177254617214203, 0.8689364790916443, -0.8923373818397522, -0.04018060863018036, -0.4495733380317688, -0.060292284935712814, -0.9764880537986755, 0.20694825053215027, 0.0002776682376861572, 0.0012887492775917053, -67.44996643066406, -8.547574996948242, 48.38296890258789, 137.3772430419922, -143.72804260253906, 278.7226257324219, -20.0)")

	pymol.cmd.png("%s-%s-polder.png" %(structure["Name"],chain),width=1080,ray=1,quiet=1) #reenable ray for prettyness
	pymol.cmd.save("2D/%s.pdb" %structure["Name"],"chainofinterest or ligand")	
	pymol.stored.occ=0
	pymol.stored.atoms=0
	pymol.cmd.iterate("ligand","pymol.stored.occ=pymol.stored.occ+q") # Adds up occupancies for each atom, inspired by Gregor Hagelueken's average_b.py from pymolwiki
	pymol.cmd.iterate("ligand","pymol.stored.atoms=pymol.stored.atoms+1") # Counts atoms in ligand
	pymol.stored.occ=pymol.stored.occ/pymol.stored.atoms #Per atom average
	print("%s,%.2f"%(pdbid,pymol.stored.occ))
	sleep(0.5) # (in seconds)
	
	





#print dir(pymol.cmd)



#pymol.cmd.load_mtz("/home/bjartel/xray/derivates/ABML/ABML-1-05/Polder_8/ABML-1-05_refine_6_polder_map_coeffs.mtz","mapfile",amplitudes,phases)



#for index in [1,2,3]:
#    # Desired pymol commands here to produce and save figures

