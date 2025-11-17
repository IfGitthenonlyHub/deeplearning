import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4RnJlcShzZWxmLCBzOiBzdHIsIG1heExldHRlcnM6IGludCwgbWluU2l6ZTogaW50LCBtYXhTaXplOiBpbnQpIC0+IGludDoKICAgICAgICBjb3VudCA9IGNvbGxlY3Rpb25zLkNvdW50ZXIoc1tpOmkrbWluU2l6ZV0gZm9yIGkgaW4gcmFuZ2UobGVuKHMpLW1pblNpemUrMSkpCiAgICAgICAgcmV0dXJuIG1heChbY291bnRbd10gZm9yIHcgaW4gY291bnQgaWYgbGVuKHNldCh3KSkgPD0gbWF4TGV0dGVyc10gK1swXSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
