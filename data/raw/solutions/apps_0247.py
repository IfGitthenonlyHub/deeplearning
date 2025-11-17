import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgZGVmIG1pblN1bU9mTGVuZ3RocyhzZWxmLCBhcnIsIHRhcmdldCk6CiAgICBpLCB3aW5kb3csIHJlc3VsdCA9IDAsIDAsIGZsb2F0KCdpbmYnKQogICAgcHJlbWluID0gW2Zsb2F0KCdpbmYnKV0gKiBsZW4oYXJyKQogICAgCiAgICBmb3IgaiwgbnVtIGluIGVudW1lcmF0ZShhcnIpOgogICAgICB3aW5kb3cgKz0gbnVtCiAgICAgIHdoaWxlIHdpbmRvdyA+IHRhcmdldDoKICAgICAgICB3aW5kb3cgLT0gYXJyW2ldCiAgICAgICAgaSArPSAxCiAgICAgIGlmIHdpbmRvdyA9PSB0YXJnZXQ6CiAgICAgICAgY3VyciA9IGogLSBpICsgMQogICAgICAgIHJlc3VsdCA9IG1pbihyZXN1bHQsIGN1cnIgKyBwcmVtaW5baSAtIDFdKQogICAgICAgIHByZW1pbltqXSA9IG1pbihjdXJyLCBwcmVtaW5baiAtIDFdKQogICAgICBlbHNlOgogICAgICAgIHByZW1pbltqXSA9IHByZW1pbltqIC0gMV0KCiAgICByZXR1cm4gcmVzdWx0IGlmIHJlc3VsdCA8IGZsb2F0KCdpbmYnKSBlbHNlIC0x").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
