# Exciton Diffusion

## Requirements
<p>
Python 3.6-3.8 on Linux <br>
Python 3.7-3.8 on Mac <br>
To get other requirements, run <br>
<code>
  make
</code>
</p>

## Running the Code
<p>
To run the code, run the command
<code>
python driver.py input.txt output.txt
</code>
where input.txt is input of the correct format (discussed below),</br>
and output.txt is a file that will contain the output.<br>
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
start/endtime are in picoseconds

