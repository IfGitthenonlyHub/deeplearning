import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBiaXNlY3QgaW1wb3J0IGJpc2VjdF9sZWZ0IGFzIGJsCmM9W10KZGVmIGdlbihuLG56KToKICAgIGlmIGxlbihuKT49MTk6CiAgICAgICAgcmV0dXJuCiAgICBub25sb2NhbCBjCiAgICBjLmFwcGVuZChpbnQobikpCiAgICBpZiBuej09MzoKICAgICAgICBuKz0iMCIKICAgICAgICBnZW4obixueikKICAgICAgICByZXR1cm4KICAgIGdlbihuKyIwIixueikKICAgIGZvciBpIGluICgiMTIzNDU2Nzg5Iik6CiAgICAgICAgZ2VuKG4raSxueisxKQpmb3IgaSBpbiAoIjEyMzQ1Njc4OSIpOgogICAgZ2VuKGksMSkKYy5hcHBlbmQoMTAqKjE4KQpjLnNvcnQoKQpuPWludChpbnB1dCgpKQpmb3IgaSBpbiByYW5nZShuKToKICAgIGEsYj1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKICAgIHg9bWluKGJsKGMsYiksbGVuKGMpLTEpCiAgICB5PWJsKGMsYSkKICAgIGlmIHg9PXkgYW5kIGI8Y1t4XToKICAgICAgICBwcmludCgwKQogICAgZWxpZiAoY1t4XT09YiBhbmQgY1t5XT09YSkgb3IgY1t4XT09YjoKICAgICAgICBwcmludCh4LXkrMSkKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoeC15KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
