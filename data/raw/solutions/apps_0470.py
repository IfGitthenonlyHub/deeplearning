import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgdGhyZWVTdW1NdWx0aShzZWxmLCBBOiBMaXN0W2ludF0sIHRhcmdldDogaW50KSAtPiBpbnQ6CiAgICAgICAgZDEgPSBjb2xsZWN0aW9ucy5kZWZhdWx0ZGljdChpbnQpCiAgICAgICAgZDIgPSBjb2xsZWN0aW9ucy5kZWZhdWx0ZGljdChpbnQpCiAgICAgICAgYW5zID0gMAogICAgICAgIGZvciBpIGluIEE6CiAgICAgICAgICAgIGFucyArPSBkMlt0YXJnZXQgLSBpXQogICAgICAgICAgICAKICAgICAgICAgICAgZm9yIGogaW4gZDE6IAogICAgICAgICAgICAgICAgZDJbaiArIGldICs9IGQxW2pdCiAgICAgICAgICAgIAogICAgICAgICAgICBkMVtpXSArPSAxCiAgICAgICAgCiAgICAgICAgcmV0dXJuIGFucyAlIGludCgxZTkgKyA3KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
