1. Run Relaxation
2. Run static calculations NSW = 0 and for bader with VTST use LAECHG = .TRUE. in the INCAR file >> output bader charges using Henkelman group algorithm 
3. Run $ chgsum.pl AECCAR0 AECCAR2  
4. Run $ bader CHGCAR -ref CHGCAR_sum >> output is ACF.dat etc...
5. Run pos2xyz.pl CONTCAR >> output is CONTCAR.xyz
6. Run add_partialCharges_xyz.py CONTCAR.xyz ACF.dat

If the add_partialCharges_xyz.py script does not have the valence of the atom of interest then add manually. Use ZVAL from the POTCAR as the value for valence #.


Additional scripts that can be useful.
automatedbader.sh is a script that can automate the process 3 to 4 
getpartialcharges.sh is a script to get the partial charges of the atoms you want and runs over various directories.
automates process 6 and picks the atoms of interest given the atom number.
Note -step 2 can be incorporated in the first relaxation. 

This can work if the VASP version has the vtst tools plugin installed. 
in cartesius
module load vasp/5.4.4-plugins 
