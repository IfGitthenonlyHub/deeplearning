import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGlpKCk6CiAgICByZXR1cm4gaW50KGlucHV0KCkpCmRlZiBtaSgpOgogICAgcmV0dXJuIGxpc3QobWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKSkKZGVmIGxpKCk6CiAgICByZXR1cm4gbGlzdChtaSgpKQoKZm9yIF8gaW4gcmFuZ2UoaWkoKSk6CiAgICBuID0gaWkoKQogICAgYSA9IFsobGkoKSArIFtpXSkgZm9yIGkgaW4gcmFuZ2UobildCiAgICBhLnNvcnQoKQogICAgYW5zID0gWzJdICogbgogICAgcHIgPSBhWzBdWzBdCiAgICBmb3IgbCwgciwgaSBpbiBhOgogICAgICAgIGlmIGwgPiBwcjoKICAgICAgICAgICAgYnJlYWsKICAgICAgICBhbnNbaV0gPSAxCiAgICAgICAgcHIgPSBtYXgocHIsIHIpCiAgICBpZiAyIGluIGFuczoKICAgICAgICBwcmludCgqYW5zKQogICAgZWxzZToKICAgICAgICBwcmludCgtMSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
