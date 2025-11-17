import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWVyZ2VTdG9uZXMoc2VsZiwgc3RvbmVzOiBMaXN0W2ludF0sIEs6IGludCkgLT4gaW50OgogICAgICAgIG4gPSBsZW4oc3RvbmVzKQogICAgICAgIGlmIChuIC0gMSkgJSAoSyAtIDEpICE9IDA6CiAgICAgICAgICAgIHJldHVybiAtMQogICAgICAgIHByZWZpeCA9IFswXQogICAgICAgIGZvciBzIGluIHN0b25lczoKICAgICAgICAgICAgcHJlZml4LmFwcGVuZChwcmVmaXhbLTFdICsgcykKICAgICAgICBAbHJ1X2NhY2hlKE5vbmUpCiAgICAgICAgZGVmIGRwKGksIGopOgogICAgICAgICAgICBpZiBqIC0gaSArIDEgPCBLOgogICAgICAgICAgICAgICAgcmV0dXJuIDAKICAgICAgICAgICAgcmVzID0gMAogICAgICAgICAgICBpZiAoaiAtIGkpICUgKEsgLSAxKSA9PSAwOgogICAgICAgICAgICAgICAgcmVzID0gcHJlZml4W2orMV0gLSBwcmVmaXhbaV0KICAgICAgICAgICAgcmV0dXJuIHJlcyArIG1pbihkcChpLCBtaWQpICsgZHAobWlkKzEsIGopIGZvciBtaWQgaW4gcmFuZ2UoaSwgaiwgSyAtIDEpKQogICAgICAgIHJldHVybiBkcCgwLCBuIC0gMSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
