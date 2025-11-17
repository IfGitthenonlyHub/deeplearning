import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgdGlsaW5nUmVjdGFuZ2xlKHNlbGYsIG46IGludCwgbTogaW50KSAtPiBpbnQ6CiAgICAgICAgCiAgICAgICAgQGxydV9jYWNoZShOb25lKQogICAgICAgIGRlZiBoZWxwZXIoaGVpZ2h0cyk6CiAgICAgICAgICAgIG1oID0gbWluKGhlaWdodHMpCiAgICAgICAgICAgIGlmIG1oID09IG46CiAgICAgICAgICAgICAgICByZXR1cm4gMAogICAgICAgICAgICAKICAgICAgICAgICAgcmV0ID0gZmxvYXQoJ2luZicpCiAgICAgICAgICAgIGogPSBoZWlnaHRzLmluZGV4KG1oKQogICAgICAgICAgICB3ID0gMQogICAgICAgICAgICB3aGlsZSBtaCArIHcgPD0gbiBhbmQgaiArIHcgLSAxIDwgbSBhbmQgaGVpZ2h0c1tqICsgdyAtIDFdID09IG1oOgogICAgICAgICAgICAgICAgcmV0ID0gbWluKHJldCwgMSArIGhlbHBlcihoZWlnaHRzWzpqXSArIChtaCArIHcsKSAqIHcgKyBoZWlnaHRzW2ogKyB3Ol0pKQogICAgICAgICAgICAgICAgdyArPSAxCiAgICAgICAgICAgIAogICAgICAgICAgICByZXR1cm4gcmV0CiAgICAgICAgICAgIAogICAgICAgIHJldHVybiBoZWxwZXIoKDAsKSAqIG0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
