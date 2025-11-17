import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHJlbW92ZUtkaWdpdHMoc2VsZiwgbnVtLCBrKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG51bTogc3RyCiAgICAgICAgIDp0eXBlIGs6IGludAogICAgICAgICA6cnR5cGU6IHN0cgogICAgICAgICAiIiIKICAgICAgICAgb3V0PVtdCiAgICAgICAgIGZvciBkaWdpdCBpbiBudW06CiAgICAgICAgICAgICB3aGlsZSBrIGFuZCBvdXQgYW5kIG91dFstMV0gPiBkaWdpdDoKICAgICAgICAgICAgICAgICBvdXQucG9wKCkKICAgICAgICAgICAgICAgICBrLT0xCiAgICAgICAgICAgICBvdXQuYXBwZW5kKGRpZ2l0KQogICAgICAgICByZXR1cm4gJycuam9pbihvdXRbOi1rIG9yIE5vbmVdKS5sc3RyaXAoJzAnKSBvciAiMCI=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
