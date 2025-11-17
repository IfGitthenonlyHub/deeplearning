import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY29uc3RyYWluZWRTdWJzZXRTdW0oc2VsZiwgbnVtczogTGlzdFtpbnRdLCBrOiBpbnQpIC0+IGludDoKICAgICAgICBkcCA9IFtuIGZvciBuIGluIG51bXNdCiAgICAgICAgaGVhcCA9IFsoLW51bXNbMF0sIDApXQogICAgICAgIGZvciBqIGluIHJhbmdlKDEsIGxlbihudW1zKSk6CiAgICAgICAgICAgIHdoaWxlIGhlYXBbMF1bMV0gPCBqIC0gazoKICAgICAgICAgICAgICAgIGhlYXBxLmhlYXBwb3AoaGVhcCkKICAgICAgICAgICAgZHBbal0gPSBtYXgoZHBbal0sIC1oZWFwWzBdWzBdICsgbnVtc1tqXSkKICAgICAgICAgICAgaGVhcHEuaGVhcHB1c2goaGVhcCwgKC1kcFtqXSwgaikpCiAgICAgICAgcmV0dXJuIG1heChkcCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
