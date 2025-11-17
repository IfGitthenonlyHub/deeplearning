import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("VCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZShUKToKICAgIE4sIE0gPSBtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpCiAgICBBID0gW2ludChhKS0xIGZvciBhIGluIGlucHV0KCkuc3BsaXQoKV0KICAgIEIgPSBbaW50KGEpLTEgZm9yIGEgaW4gaW5wdXQoKS5zcGxpdCgpXQogICAgCiAgICBYID0gWzBdICogTgogICAgZm9yIGksIGEgaW4gZW51bWVyYXRlKEEpOgogICAgICAgIFhbYV0gPSBpCiAgICBhbnMgPSAwCiAgICBtYSA9IC0xCiAgICBmb3IgaSwgYiBpbiBlbnVtZXJhdGUoQik6CiAgICAgICAgYW5zICs9IChYW2JdIC0gaSkgKiAyICsgMSBpZiBYW2JdID4gbWEgZWxzZSAxCiAgICAgICAgbWEgPSBtYXgobWEsIFhbYl0pCiAgICBwcmludChhbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
