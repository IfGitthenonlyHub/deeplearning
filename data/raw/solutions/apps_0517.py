import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("biwgbSA9IG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkKcCwgbWVtID0gMywgW10KcmVzID0gMioqbiAtIDIKaWYgbiAlIDIgPT0gMDoKICAgIHJlcyAtPSAyCndoaWxlIHAgPCBuOgogICAgaWYgbm90IGFueShwICUgZSA9PSAwIGZvciBlIGluIG1lbSkgYW5kIG4gJSBwID09IDAgOgogICAgICAgIG1lbS5hcHBlbmQocCkKICAgICAgICByZXMgLT0gMioqcCAtIDIKICAgICAgICAKICAgIHAgKz0yCiAgICAgICAgCnByaW50KHJlcyAlIG0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
