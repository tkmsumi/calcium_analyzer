# calcium_analyzer

python version of calcium-analyzer-v10f.pl


# Use
Copy the calcium_analyzer.py in the same directory as your python script and wright
```python
from calcium_analyzer import calcium_analyzer
analyzer = calciumanalyzer
analyzer.run(filepath)
```

The filepath is a path of Multi measure data from ImageJ usually named Results.xls.

Then you can get the same data as perl code as: 
```python
Mean = analyzer.Mean
F_0 = analyzer.F_0
RFU = analyzer.RFU
sm_RFU = analyzer.sm_RFU
diff = analyzer.diff
```

# Problem
The current code generates the different [sm_RFU, diff] from that perl code generates.
The exponential_filter is something wrong.
