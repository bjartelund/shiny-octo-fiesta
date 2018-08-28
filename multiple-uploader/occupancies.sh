INPUT=merged.csv
OLDIFS=$IFS
IFS=,
exec 3<$INPUT
while read -u 3 SMILES newcode oldcode Name pIC50 pIC50stderror Hillcoefficient KD KDstderror pdbid pdbfile datafile omitmap chain
do
echo "Name is $newcode"
/home/bjartel/bin/pymol/pymol -c -q $pdbfile -d "cmd.iterate('resn $pdbid','print q')" -d "quit"|tail -n +4|head -n-1|awk -F : '{sum+=$1} END {print 'Aveocc',sum/NR}'
done 
IFS=$OLDIFS
