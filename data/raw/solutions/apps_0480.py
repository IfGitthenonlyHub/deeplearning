import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtV2F5cyhzZWxmLCBzdGVwczogaW50LCBuOiBpbnQpIC0+IGludDoKICAgICAgICBBID0gWzAsIDFdCiAgICAgICAgbW9kPTEwICoqIDkgKyA3CiAgICAgICAgZm9yIHQgaW4gcmFuZ2Uoc3RlcHMpOgogICAgICAgICAgICBBWzE6XSA9IFtzdW0oQVtpIC0gMTppICsgMl0pICUgbW9kIGZvciBpIGluIHJhbmdlKDEsIG1pbihuICsgMSwgdCArIDMpKV0KICAgICAgICByZXR1cm4gQVsxXSAlIG1vZA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
