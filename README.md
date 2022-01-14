<div>
  <h2>What is loc script for?</h2>
  <p>LOC (lines of code) is very simple counting script made in python.</p>
</div>

<div>
  <h2>How can I run this?</h2>
  <p>It's very simple just run start.py and pass in parameters.</p>
</div>

```
D:\loc>python start.py -h

usage: start.py [-h] -e E [E ...] directory

positional arguments:
  directory     Name of folder or directory u wish to scan

options:
  -h, --help    show this help message and exit
  -e E [E ...]  Extensions u wish to scan for
```
<p>Eg</p>

```
D:\loc>python start.py D:\loc  -e .py
FULL LINES |     BLANK |     TOTAL | FILE
-----------|-----------|--------------------
        44 |        17 |        61 | .\loc.py
        11 |         6 |        17 | .\start.py
           EVERYTHING TOTAL
         ---------|---------
            .py         78 LINES TOTAL
```
