import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgcmVtb3ZlRHVwbGljYXRlcyhzZWxmLCBzOiBzdHIsIGs6IGludCkgLT4gc3RyOgogICAgICAgIGR1cGxpY2F0ZXM9W2sqaSBmb3IgaSBpbiAnYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXonXQogICAgICAgIGNvdW50ZXI9MAogICAgICAgIHdoaWxlIGNvdW50ZXIhPWxlbihzKToKICAgICAgICAgICAgY291bnRlcj1sZW4ocykKICAgICAgICAgICAgZm9yIGkgaW4gZHVwbGljYXRlczoKICAgICAgICAgICAgICAgIHM9cy5yZXBsYWNlKGksJycpCiAgICAgICAgICAgICAgICAKICAgICAgICByZXR1cm4gcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
