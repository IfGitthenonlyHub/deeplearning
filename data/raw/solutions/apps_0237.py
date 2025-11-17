import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtU3ViYXJyYXlzV2l0aFN1bShzZWxmLCBBLCBTKToKICAgICAgICBjID0gY29sbGVjdGlvbnMuQ291bnRlcih7MDogMX0pCiAgICAgICAgcHN1bSA9IHJlcyA9IDAKICAgICAgICBmb3IgaSBpbiBBOgogICAgICAgICAgICBwc3VtICs9IGkKICAgICAgICAgICAgcmVzICs9IGNbcHN1bSAtIFNdCiAgICAgICAgICAgIGNbcHN1bV0gKz0gMQogICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
