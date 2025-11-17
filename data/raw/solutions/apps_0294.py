import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHRvdGFsTlF1ZWVucyhzZWxmLCBuKToKICAgICAgICAgZGVmIGRmcyhsc3QsIHh5X2RpZiwgeHlfc3VtKToKICAgICAgICAgICAgIHA9bGVuKGxzdCkKICAgICAgICAgICAgIGlmIHA9PW46IHJlcy5hcHBlbmQobHN0KQogICAgICAgICAgICAgZm9yIHEgaW4gcmFuZ2Uobik6CiAgICAgICAgICAgICAgICAgaWYgKHEgbm90IGluIGxzdCkgYW5kIChwLXEgbm90IGluIHh5X2RpZikgYW5kIChwK3Egbm90IGluIHh5X3N1bSk6CiAgICAgICAgICAgICAgICAgICAgIGRmcyhsc3QrW3FdLCB4eV9kaWYrW3AtcV0sIHh5X3N1bSArW3ArcV0pCiAgICAgICAgICAgICAKICAgICAgICAgcmVzPVtdCiAgICAgICAgIGRmcyhbXSxbXSxbXSkKICAgICAgICAgcmV0dXJuIGxlbihyZXMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
