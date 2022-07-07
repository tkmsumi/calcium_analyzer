# calcium_analyzer

Python version of calcium-analyzer-v10f.pl
[original paper](https://www.nature.com/articles/nprot.2010.169)

# Use
Copy the calcium_analyzer.py in the same directory as your python script and wright
```python
from calcium_analyzer import calcium_analyzer
analyzer = calcium_analyzer()
analyzer.run(filepath)
```

The filepath is a path of Multi measure data from ImageJ usually named Results.xls.

Then you can get the same data as that from perl code as: 
```python
Mean = analyzer.Mean
F_0 = analyzer.F_0
RFU = analyzer.RFU
sm_RFU = analyzer.sm_RFU
diff = analyzer.diff
```

