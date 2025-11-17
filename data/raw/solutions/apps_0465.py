import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1pbkN1dChzZWxmLCBzKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHM6IHN0cgogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgaWYgcyA9PSBzWzo6LTFdOgogICAgICAgICAgICAgcmV0dXJuIDAKICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgbGVuKHMpKToKICAgICAgICAgICAgIGlmIHNbOmldID09IHNbOmldWzo6LTFdIGFuZCBzW2k6XSA9PSBzW2k6XVs6Oi0xXToKICAgICAgICAgICAgICAgICByZXR1cm4gMQogICAgICAgICAKICAgICAgICAgY3V0ID0gW3ggZm9yIHggaW4gcmFuZ2UoLTEsIGxlbihzKSldCiAgICAgICAgIGZvciBpIGluIHJhbmdlKGxlbihzKSk6CiAgICAgICAgICAgICBqPTAKICAgICAgICAgICAgIHdoaWxlIGkgLSBqID49IDAgYW5kIGkgKyBqIDwgbGVuKHMpIGFuZCBzW2kgLSBqXSA9PSBzW2kgKyBqXToKICAgICAgICAgICAgICAgICBjdXRbaSArIGogKyAxXSA9IG1pbihjdXRbaSArIGogKyAxXSwgY3V0W2kgLSBqXSArIDEpCiAgICAgICAgICAgICAgICAgaiArPSAxCiAgICAgICAgICAgICBqPTAKICAgICAgICAgICAgIHdoaWxlIGkgLSBqID49IDAgYW5kIGkgKyBqICsgMSA8IGxlbihzKSBhbmQgc1tpIC0gal0gPT0gc1tpICsgaiArIDFdOgogICAgICAgICAgICAgICAgIGN1dFtpICsgaiArIDJdID0gbWluKGN1dFtpICsgaiArIDJdLCBjdXRbaSAtIGpdICsgMSkKICAgICAgICAgICAgICAgICBqICs9IDEKICAgICAgICAgcmV0dXJuIGN1dFstMV0=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
