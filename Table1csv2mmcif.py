import csv
import sys

csvfile=sys.argv[1] #assuming first argument is csv
#Based on  http://stackoverflow.com/a/35829533 by Tim Pietzcker
dict1 = {}

with open(csvfile, "rb") as infile:
	reader = csv.reader(infile)
	headers = next(reader)[1:]
	for row in reader:
		dict1[row[0]] = row[1]


def overall(value):
	return value[:value.index("(")-1]

def inner(value):
	return value[value.index("(")+1:-1]
#resolution-range
rr=dict1["Resolution range"]
highres=float(rr[rr.index("-")+2:rr.index("(")-1])
lowres=float(rr[:rr.index("-")-2])
innerlow=inner(rr)[:inner(rr).rindex("-")-1]
#Overall statistics
print """_reflns.entry_id UNNAMED
_reflns.pdbx_diffrn_id 1"""
print "_reflns.d_resolution_high %.2f" % highres
print "_reflns.d_resolution_low %.2f" % lowres

print "_reflns.number_obs %s" % overall(dict1['Total reflections'])

print "_reflns.percent_possible_obs %s" % overall(dict1["Completeness (%)"])
print "_reflns.pdbx_Rmerge_I_obs %s" % overall(dict1["R-merge"])
print "_reflns.pdbx_Rrim_I_all %.2f" % float(overall(dict1["R-meas"]))
print "_reflns.pdbx_redundancy %s" % overall(dict1["Multiplicity"])
print "_reflns.pdbx_netI_over_sigmaI %s" % overall(dict1["Mean I/sigma(I)"])

#inner-shell
print "_reflns_shell.pdbx_diffrn_id 1"
print "_reflns_shell.d_res_high %.2f"%highres
print "_reflns_shell.d_res_low %.2f" %float(innerlow)
print "_reflns_shell.number_unique_obs %s" % inner(dict1['Total reflections'])
print "_reflns_shell.percent_possible_obs %s" % inner(dict1["Completeness (%)"])
print "_reflns_shell.Rmerge_I_obs %s"% inner(dict1["R-merge"])
print "_reflns_shell.pdbx_Rrim_I_all %.2f" % float(inner(dict1["R-meas"]))
print "_reflns_shell.pdbx_redundancy %s"%inner(dict1["Multiplicity"])
print "_reflns_shell.pdbx_netI_over_sigmaI_obs %s"%inner(dict1["Mean I/sigma(I)"])

print "_refine.ls_d_res_high  %.2f"%highres    
print "_refine.ls_d_res_low  %.2f" %lowres
print "_refine.ls_number_reflns_obs %s" %overall(dict1['Reflections used in refinement'])
print "_refine.ls_percent_reflns_obs %.2f"% float(overall(dict1['Completeness (%)']))
print "_refine.ls_number_reflns_R_free %s"% overall(dict1['Reflections used for R-free'])

print "_refine.ls_R_factor_R_work %s" % overall(dict1["R-work"])
print "_refine.ls_R_factor_R_free %s" % overall(dict1["R-free"])
print "_refine.ls_shell.d_res_high  %.2f"%highres    
print "_refine.ls_shell.d_res_low  %.2f" %float(innerlow)
print "_refine.ls_shell.percent_reflns_obs %s" % inner(dict1["Completeness (%)"])
print "_refine.ls_shell.number_reflns_R_work %s" % inner(dict1['Reflections used in refinement'])
print "_refine.ls_shell.R_factor_R_work %s" % inner(dict1["R-work"])
print "_refine.ls_shell.R_factor_R_free %s" % inner(dict1["R-free"])
print "_refine.ls_shell.number_reflns_R_free %s" % inner(dict1["Reflections used for R-free"])
a,b,c,al,be,ga=dict1["Unit cell"].split(" ")

#print "_cell.entry_id UNNAMED\n*_cell.length_a %s\n*_cell.length_b %s\n*_cell.length_c %s\n*_cell.angle_alpha %s\n*_cell.angle_beta %s\n*_cell.angle_gamma %s\n" % (a,b,c,al,be,ga)
