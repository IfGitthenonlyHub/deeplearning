import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBoZWFwcSBpbXBvcnQgKgpjbGFzcyBTb2x1dGlvbjoKICAgIGRlZiBzaG9ydGVzdFN1YmFycmF5KHNlbGYsIEEsIEspOgogICAgICAgIGhlYXAsIGN1clMsIGFucyA9IFsoMCwgLTEpXSwgMCwgZmxvYXQoJ2luZicpCiAgICAgICAgZm9yIGksIHYgaW4gZW51bWVyYXRlKEEpOgogICAgICAgICAgICBjdXJTICs9IHYKICAgICAgICAgICAgd2hpbGUgaGVhcCBhbmQgY3VyUyAtIGhlYXBbMF1bMF0gPj0gSzoKICAgICAgICAgICAgICAgIGFucyA9IG1pbihhbnMsIGkgLSBoZWFwcG9wKGhlYXApWzFdKQogICAgICAgICAgICBoZWFwcHVzaChoZWFwLCAoY3VyUywgaSkpCiAgICAgICAgcmV0dXJuIGFucyBpZiBhbnMgIT0gZmxvYXQoJ2luZicpIGVsc2UgLTE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
