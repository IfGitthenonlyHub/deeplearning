import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluSnVtcHMoc2VsZiwgYXJyOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBtYXAgPSBjb2xsZWN0aW9ucy5kZWZhdWx0ZGljdChsaXN0KQogICAgICAgIGZvciBpLCBhIGluIGVudW1lcmF0ZShhcnIpOgogICAgICAgICAgICBtYXBbYV0uYXBwZW5kKGkpCiAgICAgICAgCiAgICAgICAgdmlzaXRlZCwgdmlzaXRpbmcgPSB7LTF9LCB7MH0KICAgICAgICBmb3Igc3RlcHMgaW4gaXRlcnRvb2xzLmNvdW50KCk6CiAgICAgICAgICAgIHZpc2l0ZWQgfD0gdmlzaXRpbmcKICAgICAgICAgICAgaWYgbGVuKGFycikgLSAxIGluIHZpc2l0ZWQ6CiAgICAgICAgICAgICAgICByZXR1cm4gc3RlcHMKICAgICAgICAgICAgdmlzaXRpbmcgPSB7aiBmb3IgaSBpbiB2aXNpdGluZyBmb3IgaiBpbiBbaSAtIDEsIGkgKyAxXSArIG1hcC5wb3AoYXJyW2ldLCBbXSl9IC0gdmlzaXRlZA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
