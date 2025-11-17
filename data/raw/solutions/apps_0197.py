import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgaXNWYWxpZChzZWxmLCBzOiBzdHIpIC0+IGJvb2w6CiAgICAgICAgd2hpbGUgcy5maW5kKCdhYmMnKSA+PSAwOgogICAgICAgICAgICBzID0gcy5yZXBsYWNlKCdhYmMnLCAnJykKICAgICAgICByZXR1cm4gcyA9PSAnJw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
