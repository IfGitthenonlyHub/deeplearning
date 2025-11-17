import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYga0xlbmd0aEFwYXJ0KHNlbGYsIG51bXM6IExpc3RbaW50XSwgazogaW50KSAtPiBib29sOgogICAgICAgIHhzID0gW2kgZm9yIGksIG4gaW4gZW51bWVyYXRlKG51bXMpIGlmIG5dCiAgICAgICAgcmV0dXJuIGFsbCh5LXggPiBrIGZvciB4LHkgaW4gemlwKHhzLCB4c1sxOl0pKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
