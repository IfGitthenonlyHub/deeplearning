import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyBjb29rIHlvdXIgZGlzaCBoZXJlCmZvciBpIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiBuLGI9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiBhbnM9cm91bmQobi8oMipiKSkqKG4tYipyb3VuZCgobi8oMipiKSkpKTsKIHByaW50KGFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
