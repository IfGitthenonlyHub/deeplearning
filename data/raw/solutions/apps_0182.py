import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgJycnQ29tcGxleGl0eSBPKG4pJycnCiAKICAgICBkZWYgdHJhcChzZWxmLCBoZWlnaHQpOgogICAgICAgICBuID0gbGVuKGhlaWdodCkKICAgICAgICAgbCwgciwgd2F0ZXIsIG1pbkhlaWdodCA9IDAsIG4gLSAxLCAwLCAwCiAKICAgICAgICAgd2hpbGUgbCA8IHI6CiAgICAgICAgICAgICB3aGlsZSBsIDwgciBhbmQgaGVpZ2h0W2xdIDw9IG1pbkhlaWdodDoKICAgICAgICAgICAgICAgICB3YXRlciArPSBtaW5IZWlnaHQgLSBoZWlnaHRbbF0KICAgICAgICAgICAgICAgICBsICs9IDEKIAogICAgICAgICAgICAgd2hpbGUgciA+IGwgYW5kIGhlaWdodFtyXSA8PSBtaW5IZWlnaHQ6CiAgICAgICAgICAgICAgICAgd2F0ZXIgKz0gbWluSGVpZ2h0IC0gaGVpZ2h0W3JdCiAgICAgICAgICAgICAgICAgciAtPSAxCiAKICAgICAgICAgICAgIG1pbkhlaWdodCA9IG1pbihoZWlnaHRbbF0sIGhlaWdodFtyXSkKIAogICAgICAgICByZXR1cm4gd2F0ZXI=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
