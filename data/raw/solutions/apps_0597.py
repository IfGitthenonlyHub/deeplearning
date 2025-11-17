import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZSh0KToKIG4gPSBpbnQoaW5wdXQoKSkKIGEsIGIgPSBbXSwgW10KIGZvciBfIGluIHJhbmdlKG4pOgogIHgsIGggPSBpbnB1dCgpLnNwbGl0KCkKICBhLmFwcGVuZChpbnQoeCkpCiAgYi5hcHBlbmQoaW50KGgpKQogYSA9IFt5IC0geCBmb3IgeCwgeSBpbiB6aXAoYSwgYVsxOl0pXQogYSA9IHNvcnRlZCh4ICsgeSBmb3IgeCwgeSBpbiB6aXAoWzBdICsgYSwgYSArIFswXSkpCiBwcmludChzdW0oeCAqIHkgZm9yIHgsIHkgaW4gemlwKGEsIHNvcnRlZChiKSkpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
