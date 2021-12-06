Advent of Code exercises as found on http://adventofcode.com/.

---

If you're here just for `aoc` (the CLI utility in project root),

```bash
$ ./aoc init {year} {language} 
```

`aoc init` generates the complete set of directories & daily exercise templates and blank input files, including adding language-appropriate header comments containing each exercise URL.


```bash
$ ./aoc init 2021 python
# ...
$ ls 2021/python | wc -l
31
$ ls 2021/python/01
01.py  input
$ cat 2021/python/01/01.py
"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/1
"""
```

Edit `VALID_LANGS` and `EXTENSIONS` as necessary for your desired languages (implemented to safeguard against typos).

The utility does not overwrite (in fact, as a failsafe, it `set -o noclobber` before anything else). 
