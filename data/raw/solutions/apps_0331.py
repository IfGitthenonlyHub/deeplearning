import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgYW5nbGVDbG9jayhzZWxmLCBob3VyOiBpbnQsIG1pbnV0ZXM6IGludCkgLT4gZmxvYXQ6CiAgICAgICAgbWludXRlc19udW0gPSBtaW51dGVzLzUKICAgICAgICBob3VyICs9IG1pbnV0ZXMvNjAKICAgICAgICBhbmdsZSA9IGFicyhob3VyIC0gbWludXRlc19udW0pKjMwCiAgICAgICAgcmV0dXJuIG1pbigzNjAtYW5nbGUsIGFuZ2xlKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
