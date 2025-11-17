import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtU3BsaXRzKHNlbGYsIHM6IHN0cikgLT4gaW50OgogICAgICAgIGN1ciwgaCA9IENvdW50ZXIoKSwgQ291bnRlcihzKQogICAgICAgIGNudCA9IDAKICAgICAgICBmb3IgYyBpbiBzOgogICAgICAgICAgICBoW2NdIC09IDEKICAgICAgICAgICAgY3VyW2NdICs9IDEKICAgICAgICAgICAgaWYgaFtjXSA9PSAwOiBkZWwgaFtjXQogICAgICAgICAgICBjbnQgKz0gbGVuKGgpID09IGxlbihjdXIpIAogICAgICAgIHJldHVybiBjbnQ=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
