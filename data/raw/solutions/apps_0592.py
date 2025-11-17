import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("RCA9IHt9CgpkZWYgZyhzKToKICBpZiBzIGluIEQ6IHJldHVybiBEW3NdCiAgCiAgdmFscyA9IHNldCgpCiAgbCA9IGxlbihzKQogIGZvciBpIGluIHJhbmdlKGwpOgogICAgZm9yIGogaW4gcmFuZ2UoMSwgbCsxIC0gaSk6CiAgICAgIHN1YiA9IHNbaSA6IGkral0KICAgICAgaWYgc3ViIGluIERJQzoKICAgICAgICB2YWxzLmFkZChnKHNbOmldKSBeIGcoc1tpK2o6XSkpCiAgCiAgaSA9IDAKICB3aGlsZSAxOgogICAgaWYgbm90IGkgaW4gdmFsczoKICAgICAgYnJlYWsKICAgIGkgKz0gMQogIERbc10gPSBpCiAgcmV0dXJuIERbc10KClQgPSBpbnQoaW5wdXQoIiIpKQpmb3IgdCBpbiByYW5nZShUKToKICBzID0gaW5wdXQoIiIpCiAgZF9sZW4gPSBpbnQoaW5wdXQoIiIpKQogIERJQyA9IHNldCgpCiAgZm9yIGkgaW4gcmFuZ2UoZF9sZW4pOgogICAgRElDLmFkZChpbnB1dCgiIikpCiAgRCA9IHt9CiAgcHJpbnQoIlRlZGR5IiBpZiBnKHMpIGVsc2UgIlRyYWN5Iik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
