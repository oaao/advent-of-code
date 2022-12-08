# advent-of-code

Advent of Code exercises as found on <http://adventofcode.com/>.

---

Also provides the binary `aoc` for templating out paths and exercises:

```bash
$ ./aoc init <language> <year> [max_day]
```

`aoc init` generates directories, exercise templates with language-appropriate headers, and blank input files.

>The utility cannot overwrite (it will first `set -o noclobber` as a failsafe).
>
>Edit `VALID_LANGS` and `EXTENSIONS` as necessary for your desired languages.

```bash
$ ./aoc init python 2021
# ...
$ ls python/2021 | wc -l
31
$ ls python/2021/01
01.py  input
$ cat python/2021/01/01.py
"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/1
"""
```
