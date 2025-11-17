import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHZhbGlkVXRmOChzZWxmLCBkYXRhKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIGRhdGE6IExpc3RbaW50XQogICAgICAgICA6cnR5cGU6IGJvb2wKICAgICAgICAgIiIiCiAgICAgICAgIGNvdW50ID0gMAogICAgICAgICBmb3IgbnVtIGluIGRhdGE6CiAgICAgICAgICAgICBpZiBjb3VudCA9PSAwOgogICAgICAgICAgICAgICAgIGlmIChudW0gPj4gNSkgPT0gMGIxMTA6IGNvdW50ID0gMQogICAgICAgICAgICAgICAgIGVsaWYgKG51bSA+PiA0KSA9PSAwYjExMTA6IGNvdW50ID0gMgogICAgICAgICAgICAgICAgIGVsaWYgKG51bSA+PiAzKSA9PSAwYjExMTEwOiBjb3VudCA9IDMKICAgICAgICAgICAgICAgICBlbGlmIChudW0gPj4gNyk6IHJldHVybiBGYWxzZQogICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICBpZiAobnVtID4+IDYpICE9IDBiMTA6IHJldHVybiBGYWxzZQogICAgICAgICAgICAgICAgIGNvdW50IC09IDEKICAgICAgICAgcmV0dXJuIGNvdW50ID09IDA=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
