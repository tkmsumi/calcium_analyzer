# calcium_analyzer

calcium-analyzer-v10f.plのpython版です。
[original paper](https://www.nature.com/articles/nprot.2010.169)

# Use
git cloneかdownloadでcalcium_analyzer.pyを作業用スクリプトと同じフォルダに入れて以下のように記述します。
```python
from calcium_analyzer import calcium_analyzer
analyzer = calcium_analyzer()
analyzer.run(filepath)
```

filepathはImageJのMulti measureで得られたファイル（通常Results.xls）のパスを入れてください。

以下のように書くとperlのスクリプトと同じ値が得られます: 
```python
Mean = analyzer.Mean
F_0 = analyzer.F_0
RFU = analyzer.RFU
sm_RFU = analyzer.sm_RFU
diff = analyzer.diff
```

