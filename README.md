# csvxref
Add secondary cross references between CSV files

This does something similar to a VLOOKUP() in Excel; it looks up a field value from the primary CSV
file in the secondary CSV file, and when it finds a match, it picks the value from another field
in the secondary CSV file, and adds this as a new column.

Parameters:
- -f The main input file, which will be replaced with the output. The original file will be saved with a tilde character appended to the name.
- -s The secondary, lookup file
- -v The column name (in the input file) of the value to be looked up
- -L The column name of the lookup value in the secondary file
- -k The name of the column to copy from the secondary file, to the new column in the output file
- -n The name of the new column in the output file
- -D Default value to use when the lookup value isn't found. Default is no value
- -d CSV dialect to write to the outfile. Default is "excel", but try "unix"

Try it with the included sample files!

```
./csvxref.py -f insample.csv -s secsample.csv -v Fruit -L Description -k Key -n FruitID -d unix
```


Included is a little hack called 'addguid.py' that can add a GUID column to a CSV file.

Parameters:
- -f The main input file, which will be replaced with the output. The original file will be saved with a tilde character appended to the name.
- -n The name of the new GUID column in the output file
- -d CSV dialect to write to the outfile. Default is "excel", but try "unix"
