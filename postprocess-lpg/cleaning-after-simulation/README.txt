The clean scripts are based on a slightly modified version of the cleaning script from vtst, vclean.sh. 
-----workflow--------
Run after the optimazation inside the main dir.
1. cleanvasp_recursively.py
    -It runs vclean3.sh and calls bader.sh and vcleanlpg.sh
    -bader.sh cleans the charge files and does tha charge sums using VTST tool scripts.
    -vcleanlpg.sh deletes and zips large files and moves them to another directory. In this case to the arxiv dir.
Run after frequency analysis inside the FREQS dir. 
2.  clean_freqs_recursively.py