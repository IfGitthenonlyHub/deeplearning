import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("JycnQXV0aG9yLSBBa3NoaXQgTW9uZ2EnJycKdD1pbnQoaW5wdXQoKSkKZm9yIF8gaW4gcmFuZ2UodCk6CiAgICBuLGs9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiAgICBhcnI9W2ludCh4KSBmb3IgeCBpbiBpbnB1dCgpLnNwbGl0KCldCiAgICBtPW1pbihhcnIpCiAgICBhbnM9MAogICAgZm9yIGkgaW4gYXJyOgogICAgICAgIGFucys9KGstaSkvL20KICAgIHByaW50KGFucy0oay1tKS8vbSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
