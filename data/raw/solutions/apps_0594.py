import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("bixtPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQpsPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQppbmMsZW5jPTAsMApmb3IgaSBpbiByYW5nZSgwLGxlbihsKSk6CiBpbmM9bWF4KGxbaV0saW5jK2xbaV0pCiBlbmM9bWF4KGVuYyxpbmMpCnJlc3VsdD1zdW0obCktZW5jCnByaW50KHJlc3VsdCtlbmMvbSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
