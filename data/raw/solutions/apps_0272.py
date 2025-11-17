import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4Q2FuZGllcyhzZWxmLCBzdGF0dXMsIGNhbmRpZXMsIGtleXMsIGNvbnRhaW5lZEJveGVzLCBpbml0aWFsQm94ZXMpOgogICAgICAgIGJveGVzID0gc2V0KGluaXRpYWxCb3hlcykKICAgICAgICBiZnMgPSBbaSBmb3IgaSBpbiBib3hlcyBpZiBzdGF0dXNbaV1dCiAgICAgICAgZm9yIGkgaW4gYmZzOgogICAgICAgICAgICBmb3IgaiBpbiBjb250YWluZWRCb3hlc1tpXToKICAgICAgICAgICAgICAgIGJveGVzLmFkZChqKQogICAgICAgICAgICAgICAgaWYgc3RhdHVzW2pdOgogICAgICAgICAgICAgICAgICAgIGJmcy5hcHBlbmQoaikKICAgICAgICAgICAgZm9yIGogaW4ga2V5c1tpXToKICAgICAgICAgICAgICAgIGlmIHN0YXR1c1tqXSA9PSAwIGFuZCBqIGluIGJveGVzOgogICAgICAgICAgICAgICAgICAgIGJmcy5hcHBlbmQoaikKICAgICAgICAgICAgICAgIHN0YXR1c1tqXSA9IDEKICAgICAgICByZXR1cm4gc3VtKGNhbmRpZXNbaV0gZm9yIGkgaW4gYmZzKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
