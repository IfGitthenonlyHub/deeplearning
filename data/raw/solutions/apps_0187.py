import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluT3BlcmF0aW9uc01heFByb2ZpdChzZWxmLCBjOiBMaXN0W2ludF0sIGI6IGludCwgcjogaW50KSAtPiBpbnQ6CiAgICAgIG4gPSBsZW4oYykKICAgICAgaSA9IDAKICAgICAgcmVzdCA9IDAKICAgICAgbWF4X3ZhbCwgbWF4X2kgPSAwLCAtMgogICAgICB2YWwgPSAwCiAgICAgIHdoaWxlIGk8biBvciByZXN0ID4gMDoKICAgICAgICBpZiBpIDwgbjoKICAgICAgICAgIHJlc3QgKz0gY1tpXQogICAgICAgIHAgPSBtaW4ocmVzdCwgNCkKICAgICAgICB2YWwgKz0gcCAqIGIgLSByCiAgICAgICAgaWYgdmFsID4gbWF4X3ZhbDoKICAgICAgICAgIG1heF92YWwgPSB2YWwKICAgICAgICAgIG1heF9pID0gaQogICAgICAgIHJlc3QgLT0gcAogICAgICAgIGkgKz0gMSAgCiAgICAgIHJldHVybiBtYXhfaSArIDE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
