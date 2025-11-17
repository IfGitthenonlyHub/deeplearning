import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGRlY29kZVN0cmluZyhzZWxmLCBzKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHM6IHN0cgogICAgICAgICA6cnR5cGU6IHN0cgogICAgICAgICAiIiIKICAgICAgICAgc3RhY2sgPSBbXQogICAgICAgICBzdGFjay5hcHBlbmQoWyIiLCAxXSkKICAgICAgICAgbnVtID0gIiIKICAgICAgICAgZm9yIGNoIGluIHM6CiAgICAgICAgICAgICBpZiBjaC5pc2RpZ2l0KCk6CiAgICAgICAgICAgICAgIG51bSArPSBjaAogICAgICAgICAgICAgZWxpZiBjaCA9PSAnWyc6CiAgICAgICAgICAgICAgICAgc3RhY2suYXBwZW5kKFsiIiwgaW50KG51bSldKQogICAgICAgICAgICAgICAgIG51bSA9ICIiCiAgICAgICAgICAgICBlbGlmIGNoID09ICddJzoKICAgICAgICAgICAgICAgICBzdCwgayA9IHN0YWNrLnBvcCgpCiAgICAgICAgICAgICAgICAgc3RhY2tbLTFdWzBdICs9IHN0KmsKICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgc3RhY2tbLTFdWzBdICs9IGNoCiAgICAgICAgIHJldHVybiBzdGFja1swXVswXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
