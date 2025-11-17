import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgc3VtRm91ckRpdmlzb3JzKHNlbGYsIG51bXM6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIGRlZiBjb21wdXRlKG4pOgogICAgICAgICAgICBzID0gc2V0KCkKICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgMSArIGludChuKiowLjUpKToKICAgICAgICAgICAgICAgIGlmIG4gJSBpID09IDA6CiAgICAgICAgICAgICAgICAgICAgcy5hZGQoaSkKICAgICAgICAgICAgICAgICAgICBzLmFkZChuIC8vIGkpCiAgICAgICAgICAgIHJldHVybiBzdW0ocykgaWYgbGVuKHMpID09IDQgZWxzZSAwCiAgICAgICAgcmV0dXJuIHN1bShjb21wdXRlKGkpIGZvciBpIGluIG51bXMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
