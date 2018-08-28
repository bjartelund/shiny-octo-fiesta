#!/bin/bash
code=$1
echo "Code: $code"
SMILES=$2
echo "Smiles: $SMILES"
pdbfile=$3
echo "pdbfile: $pdbfile" 
datafile=$4
echo "datafile: $datafile" 
pdbid=$5
Name=$6
find /home/bjartel/xray/derivates/ -name table1_*|grep $Name
echo "table1 dir:?"
read table1dir
cp $table1dir/Table1.csv .
cp ../data_template_general_ESRF.cif $code-info.cif
python ../Table1csv2mmcif.py Table1.csv >> $code-info.cif
echo "IC50:"
read ic50
echo "Kd:"
read kd
python ../bindingassay.py $SMILES $ic50 $kd >> $code-info.cif
grep "unmerged_data" $table1dir/table_one.eff
echo "manual intervention - check for wavelength, date, beamline"
read -p "Wavelength?" wavelength
read -p "Date of collection? e.g 2013-11-13. " dateofcollection
sed -i "s/0.91841/$wavelength/" $code-info.cif
sed -i "s/2013-11-13/$dateofcollection/" $code-info.cif
sed -i "s/OXA-48 IN COMPLEX WITH/OXA-48 IN COMPLEX WITH COMPOUND $code/" $code-info.cif
#elbow.get_new_ligand_code
newcode=$(elbow.get_new_ligand_code|python -c "import sys; [sys.stdout.write(line[-4:]) for line in sys.stdin]")
#read -p "new random ligand " newcode
formula=$(cctbx.python ../SMILEStoformula.py $SMILES)
echo "loop_" >> $code-info.cif
echo "_pdbx_chem_comp_depositor_info.ordinal" >> $code-info.cif
echo "_pdbx_chem_comp_depositor_info.comp_id"  >> $code-info.cif
echo "_pdbx_chem_comp_depositor_info.formula" >> $code-info.cif
echo "_pdbx_chem_comp_depositor_info.descriptor" >> $code-info.cif
echo "_pdbx_chem_comp_depositor_info.descriptor_type"  >> $code-info.cif
echo "1 $newcode '$formula' $SMILES SMILES"  >> $code-info.cif
echo $pdbfile|perl -wnE "say for /Refine_[0-9]{1,3}/g"
read -p "Refine-id:" refineid
echo "_refine.entry_id $refineid"  >> $code-info.cif
echo "_refine.pdbx_refine_id $refineid" >> $code-info.cif

vim $code-info.cif
pdb_extract -r PHENIX -IPDB $pdbfile -iENT $code-info.cif -o $code.mmcif
pdb_extract_sf -rt I -rp mtz -w $wavelength -IDAT $datafile -o $code\_sf.mmcif
sed -i "s/_diffrn_radiation_wavelength.wavelength   ./_diffrn_radiation_wavelength.wavelength   $wavelength/" $code\_sf.mmcif
echo "manual check of sf wavelength"
read wait
vim $code\_sf.mmcif

sed -i s/$pdbid/$newcode/g $code.mmcif
awk '1;/data extraction/{getline this<"../software";print this;getline this<"../software";print this;getline this<"../software";print this}' $code.mmcif > $code.mmcif.bak
mv $code.mmcif.bak $code.mmcif

echo "label: " $code >> index.txt
echo "model: " $code.mmcif >> index.txt
echo "sf: "  $code\_sf.mmcif >> index.txt


echo "finished"
