import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICBOID0gaW50KGlucHV0KCkpCiAgQSA9IFtpbnQoeCkgZm9yIHggaW4gaW5wdXQoKS5zcGxpdCgpXQogIGxhc3QgPSBpID0gaiA9IDEKICBhbnMgPSBueHQgPSBjdXIgPSAwCiAgd2hpbGUgaiA8IE46CiAgICB3aGlsZSBqIDwgTi0xIGFuZCBBW2orMV0gPiBBW2pdOgogICAgICBqICs9IDEKICAgIGlmIGN1ciA9PSAwOgogICAgICBhbnMgKz0gMQogICAgbnh0ICs9IGogLSBpICsgMQogICAgaiArPSAxCiAgICBpID0gagogICAgY3VyICs9IDEKICAgIGlmIGN1ciA9PSBsYXN0OgogICAgICBsYXN0ID0gbnh0CiAgICAgIG54dCA9IGN1ciA9IDAKCiAgcHJpbnQoYW5zKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
