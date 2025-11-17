import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAKICAgICBkZWYgbWluU3ViQXJyYXlMZW4oc2VsZiwgcywgbnVtcyk6CiAgICAgICAgIHRvdGFsID0gbGVmdCA9IDAKICAgICAgICAgcmVzdWx0ID0gbGVuKG51bXMpICsgMQogICAgICAgICBmb3IgcmlnaHQsIG4gaW4gZW51bWVyYXRlKG51bXMpOgogICAgICAgICAgICAgdG90YWwgKz0gbgogICAgICAgICAgICAgd2hpbGUgdG90YWwgPj0gczoKICAgICAgICAgICAgICAgICByZXN1bHQgPSBtaW4ocmVzdWx0LCByaWdodCAtIGxlZnQgKyAxKQogICAgICAgICAgICAgICAgIHRvdGFsIC09IG51bXNbbGVmdF0KICAgICAgICAgICAgICAgICBsZWZ0ICs9IDEKICAgICAgICAgcmV0dXJuIHJlc3VsdCBpZiByZXN1bHQgPD0gbGVuKG51bXMpIGVsc2UgMA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
