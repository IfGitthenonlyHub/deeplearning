import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToNCiAgICB0MT1pbnQoaW5wdXQoKSkNCiAgICB0YTE9bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpDQogICAgZDE9aW50KGlucHV0KCkpDQogICAgZGExPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQ0KICAgIHQyPWludChpbnB1dCgpKQ0KICAgIHRhMj1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkNCiAgICBkMj1pbnQoaW5wdXQoKSkNCiAgICBkYTI9bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpDQogICAgaWYoc2V0KHRhMikuaXNzdWJzZXQoc2V0KHRhMSkpIGFuZCBzZXQoZGEyKS5pc3N1YnNldChzZXQoZGExKSkpOg0KICAgICAgICBwcmludCgieWVzIikNCiAgICBlbHNlOg0KICAgICAgICBwcmludCgibm8iKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
