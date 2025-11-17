import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluRGF5cyhzZWxmLCBibG9vbURheTogTGlzdFtpbnRdLCBtOiBpbnQsIGs6IGludCkgLT4gaW50OgogICAgICAgIGlmIGxlbihibG9vbURheSkgPCBtICogazogcmV0dXJuIC0xCiAgICAgICAgbCwgciA9IDEsIG1heChibG9vbURheSkKICAgICAgICB3aGlsZSBsIDwgcjoKICAgICAgICAgICAgcCwgY3VyciwgY250ID0gbCArIChyIC0gbCkgLy8gMiwgMCwgMAogICAgICAgICAgICBmb3IgeCBpbiBibG9vbURheToKICAgICAgICAgICAgICAgIGN1cnIgPSBjdXJyICsgMSBpZiB4IDw9IHAgZWxzZSAwCiAgICAgICAgICAgICAgICBpZiBjdXJyID49IGs6CiAgICAgICAgICAgICAgICAgICAgY250LCBjdXJyID0gY250KzEsIGN1cnIgLSBrCiAgICAgICAgICAgIGlmIGNudCA8IG06IGwgPSBwKzEKICAgICAgICAgICAgZWxzZTogciA9IHAKICAgICAgICByZXR1cm4gbA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
