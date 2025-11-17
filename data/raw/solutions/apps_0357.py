import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4RGlzdFRvQ2xvc2VzdChzZWxmLCBzZWF0czogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgcmVzLCBsYXN0LCBuID0gMCwgLTEsIGxlbihzZWF0cykKICAgICAgICBmb3IgaSBpbiByYW5nZShuKToKICAgICAgICAgICAgaWYgc2VhdHNbaV06CiAgICAgICAgICAgICAgICByZXMgPSBtYXgocmVzLCBpIGlmIGxhc3QgPCAwIGVsc2UgKGkgLSBsYXN0KSAvLyAyKQogICAgICAgICAgICAgICAgbGFzdCA9IGkKICAgICAgICByZXR1cm4gaW50KG1heChyZXMsIG4gLSBsYXN0IC0gMSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
