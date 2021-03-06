# Exciton Diffusion

## Requirements
<p>
Python 3.6-3.8 on Linux <br>
Python 3.7-3.8 on Mac <br>
To get other requirements, run <br>
<code>
  make init
</code>
To ensure the code is running properly run <br>
<code>
  make test
</code>
</p>

## Running the Code
<p>
To run the code, run the command
<code>
make input=&ltinput.txt&gt &ltOUTPUT&rt
</code>
The options for &ltOUTPUT&rt are csv, graph, and animate.
</p>

## Input File
<p>
Input file should consist of a first line of conditions, followed by a list of sites.<br>
Conditions line should be of format:<br>
<code>
&ltsystemtype&gt  &ltdimension&gt &ltratetype&gt &ltmodeltype&gt &ltstarttime&gt &ltendtime&gt
</code>
Sites are of format:<br>
<code>
&ltsitetype&gt &ltspecifications&gt coord1 coord2 coord3
</code>

</p>

### Options
<p>
systemtype: crystal <br>
dimension: 1, 2, 3 <br>
ratetype: marcus, arrhenius <br>
modeltype: kmc <br>
start/endtime are in picoseconds <br>
sitetype: pointparticle, molecule


## Build the report PDF
Please make sure a working LaTeX environment (in particular `pdflatex`() is available on your system.

1. Run `git submodule update --init` to synchronize the report's source code repo.
2. Run `make report` to build the report PDF, which will be in `report/main.pdf`.
