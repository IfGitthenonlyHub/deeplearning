import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4U3ViYXJyYXlTdW1DaXJjdWxhcihzZWxmLCBBOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBpZiBtYXgoQSkgPD0gMDogcmV0dXJuIG1heChBKQogICAgICAgIGVuZG1heCA9IFtpIGZvciBpIGluIEFdCiAgICAgICAgZW5kbWluID0gW2kgZm9yIGkgaW4gQV0KICAgICAgICBmb3IgaSBpbiByYW5nZShsZW4oQSktMSk6CiAgICAgICAgICAgIGlmIGVuZG1heFtpXSA+IDA6IGVuZG1heFtpKzFdICs9IGVuZG1heFtpXQogICAgICAgICAgICBpZiBlbmRtaW5baV0gPCAwOiBlbmRtaW5baSsxXSArPSBlbmRtaW5baV0KICAgICAgICByZXR1cm4gbWF4KG1heChlbmRtYXgpLCBzdW0oQSkgLSBtaW4oZW5kbWluKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
