# Generates IIS ZPL labels from a list of asset numbers
# The input file should be a list of asset numbers, one per line
# The output file will be a ZPL file that can be sent to the printer using print.py

import sys
import re

# The preamble that sets up our template and the logo
prepend = """^XA^DFR:ASSET1.ZPL^FS^FT20,40^XGR:LOGO2^FS^FT140,40^A0N,30,30^FDPROPERTY OF^FS^FT140,100^A0N,60,60^FDASSET #^FS^FT140,155^A0N,60,50^FN1^FS^FT20,155^BXN,7,200^FN1^FS^FT140,190^A0N,30,30^FDII STANLEY CO., INC^FS^XZ
~DGR:LOGO2,360,12,0078C0,00FFC0,00FF80,01EF,03C2,07801FFF83F0,0F03FFFFFFC0,1E00279FFF,1F000780,0F800781C0F0FC1FEF0C,0FC00781C0F0FC1FE71C,07E00783E0F8FC1E0398,03F00783E0F8FC1E03F0,03F00783F0FCFC1E01F0,01F80783B0FCFC1E01F0,00FC0787B0EFFC1E00E0,00FE078730E7FC1FE0E0,007F078730E3FC1FE0E0,003F878F18E3FC1E00E0,003FC78F18E1FC1E00E0,001FE78FFCE0FC1E00E0,000FE78FFCE0FC1E00E0,040FF79E0CE0FC1E00E0,0E07E79E0CE0FFDFE0E8,0F03C7BC0EE0FFDFE0FC,1F83C000000000000006,3FEF3FFFFFFFFFFFFFFF,3FFF7FFFFFFFFFFFFFFF,7FFEFFFFFFFFFFFFFFFF80,7FFCFFFFFFFFFFFFFFFFC0,
"""

# The ZPL that will be repeated for each line in the input file
label = "^XA^XFR:ASSET1.ZPL^FS^FN1^FD*^FS^XZ"

# The postamble that restates our template and logo, just in case the ZPL is loaded in reverse
postpend = prepend

# The regex that inserts the asset number into the label after the ^FD
regex = r"(\^FD)(\*)(\^FS)"


# The input file path. Hardcoded for now
input_path = "input.txt"

# The ouptut file path. Hardcoded for now
output_path = "output.zpl"

# Read the input file
try:
    with open(input_path, 'r') as f:
        lines = f.readlines()
except:
    print("Unable to open input file")
    print("Please ensure a file named " + input_path + " exists in the current directory")
    print("The file should contain a list of asset numbers, one per line")
    sys.exit(1)

# Remove /n from each line
lines = [line.rstrip() for line in lines]

# Remove lines beginning with # (comments)
lines = [line for line in lines if not line.startswith("#")]

# Remove empty lines
lines = [line for line in lines if line]

# Insert the asset number into the label
lines = [re.sub(regex, r"\g<1>" + line + r"\g<3>", label) for line in lines]

# Write the output file
with open(output_path, 'w') as f:
    f.write(prepend)
    for line in lines:
        f.write(line)
        f.write("\n")
    f.write(postpend)

