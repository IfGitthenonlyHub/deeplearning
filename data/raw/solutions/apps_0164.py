import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluSW50ZWdlcihzZWxmLCBudW06IHN0ciwgazogaW50KSAtPiBzdHI6CiAgICAgICAgaWYgayA8PSAwOgogICAgICAgICAgICByZXR1cm4gbnVtCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMTApOgogICAgICAgICAgICBpbmQgPSBudW0uZmluZChzdHIoaSkpCiAgICAgICAgICAgIGlmIDAgPD0gaW5kIDw9IGs6CiAgICAgICAgICAgICAgICByZXR1cm4gc3RyKG51bVtpbmRdKSArIHNlbGYubWluSW50ZWdlcihudW1bMDppbmRdICsgbnVtW2luZCsxOl0sIGsgLSBpbmQpCiAgICAgICAgcmV0dXJuIG51bQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
