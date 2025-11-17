import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZyYWN0aW9uVG9EZWNpbWFsKHNlbGYsIG51bWVyYXRvciwgZGVub21pbmF0b3IpOgogICAgICAgICBuLCByZW1haW5kZXIgPSBkaXZtb2QoYWJzKG51bWVyYXRvciksIGFicyhkZW5vbWluYXRvcikpCiAgICAgICAgIHNpZ24gPSAnLScgaWYgbnVtZXJhdG9yKmRlbm9taW5hdG9yIDwgMCBlbHNlICcnCiAgICAgICAgIHJlc3VsdCA9IFtzaWduK3N0cihuKSwgJy4nXQogICAgICAgICBzdGFjayA9IFtdCiAgICAgICAgIHdoaWxlIHJlbWFpbmRlciBub3QgaW4gc3RhY2s6CiAgICAgICAgICAgICBzdGFjay5hcHBlbmQocmVtYWluZGVyKQogICAgICAgICAgICAgbiwgcmVtYWluZGVyID0gZGl2bW9kKHJlbWFpbmRlcioxMCwgYWJzKGRlbm9taW5hdG9yKSkKICAgICAgICAgICAgIHJlc3VsdC5hcHBlbmQoc3RyKG4pKQogCiAgICAgICAgIGlkeCA9IHN0YWNrLmluZGV4KHJlbWFpbmRlcikKICAgICAgICAgcmVzdWx0Lmluc2VydChpZHgrMiwgJygnKQogICAgICAgICByZXN1bHQuYXBwZW5kKCcpJykKICAgICAgICAgcmV0dXJuICcnLmpvaW4ocmVzdWx0KS5yZXBsYWNlKCcoMCknLCAnJykucnN0cmlwKCcuJyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
