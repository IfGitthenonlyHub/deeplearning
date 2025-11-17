import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluTnVtYmVyT2ZGcm9ncyhzZWxmLCBjcm9ha09mRnJvZ3M6IHN0cikgLT4gaW50OgogICAgICAgIHJlcyA9IGNyb2FraW5nID0gYyA9IHIgPSBvID0gYSA9IGsgPSAwCiAgICAgICAgZm9yIHggaW4gY3JvYWtPZkZyb2dzOgogICAgICAgICAgICBpZiB4ID09ICdjJzoKICAgICAgICAgICAgICAgIGMsIGNyb2FraW5nID0gYysxLCBjcm9ha2luZysxCiAgICAgICAgICAgICAgICByZXMgPSBtYXgocmVzLCBjcm9ha2luZykKICAgICAgICAgICAgZWxpZiB4ID09ICdyJzogciArPSAxCiAgICAgICAgICAgIGVsaWYgeCA9PSAnbyc6IG8gKz0gMQogICAgICAgICAgICBlbGlmIHggPT0gJ2EnOiBhICs9IDEKICAgICAgICAgICAgZWxzZTogaywgY3JvYWtpbmcgPSBrKzEsIGNyb2FraW5nLTEKICAgICAgICAgICAgaWYgYyA8IHIgb3IgciA8IG8gb3IgbyA8IGEgb3IgYSA8IGs6IHJldHVybiAtMSAKICAgICAgICAKICAgICAgICByZXR1cm4gcmVzIGlmIGMgPT0gciA9PSBvID09IGEgPT0gayBhbmQgY3JvYWtpbmcgPT0gMCBlbHNlIC0x").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
