import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQpmb3IgXyBpbiByYW5nZShpbnQoaW5wdXQoKSkpOgogIG4sIGsgPSBtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpCiAgcmVzID0gW1siMCJdICogbiBmb3IgXyBpbiByYW5nZShuKV0KICBpZiBrICUgbjogcHJpbnQoMikKICBlbHNlOiBwcmludCgwKQogIGZvciBkIGluIHJhbmdlKG4pOgogICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgIGlmIGsgPT0gMDogYnJlYWsKICAgICAgcmVzW2ldWyhpICsgZCkgJSBuXSA9ICIxIgogICAgICBrIC09IDEKICBmb3IgciBpbiByZXM6IHByaW50KCIiLmpvaW4ocikp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
