import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1vbm90b25lSW5jcmVhc2luZ0RpZ2l0cyhzZWxmLCBOKToKICAgICAgICAgTiA9IHN0cihOKQogICAgICAgICBMID0gbGVuKE4pCiAgICAgICAgIGZvciBpIGluIHJhbmdlKEwgLSAxKToKICAgICAgICAgICAgIGlmIE5baV0gPiBOW2kgKyAxXToKICAgICAgICAgICAgICAgICByZXR1cm4gc2VsZi5tb25vdG9uZUluY3JlYXNpbmdEaWdpdHMoaW50KE5bOmldICsgc3RyKGludChOW2ldKSAtIDEpICsgJzknICogKEwgLSBpIC0gMSkpKQogICAgICAgICByZXR1cm4gaW50KE4p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
