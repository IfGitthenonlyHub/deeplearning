import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CgogICAgZGVmIGtDb25jYXRlbmF0aW9uTWF4U3VtKHNlbGYsIGFycjogTGlzdFtpbnRdLCBrOiBpbnQsIG1vZCA9IDEwICoqIDkgKyA3KSAtPiBpbnQ6CiAgICAgICAgZGVmIEthZGFuZShhcnIsIHJlcyA9IDAsIGN1ciA9IDApOgogICAgICAgICAgICBmb3IgbnVtIGluIGFycjoKICAgICAgICAgICAgICAgIGN1ciA9IG1heChudW0sIG51bSArIGN1cikKICAgICAgICAgICAgICAgIHJlcyA9IG1heChyZXMsIGN1cikKICAgICAgICAgICAgcmV0dXJuIHJlcwogICAgICAgIHJldHVybiAoKGsgLSAyKSAqIG1heChzdW0oYXJyKSwgMCkgKyBLYWRhbmUoYXJyICogMikpICUgbW9kIGlmIGsgPiAxIGVsc2UgS2FkYW5lKGFycikgJSBtb2Q=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
