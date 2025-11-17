import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBtYXRoIGltcG9ydCBnY2Qsc3FydApmb3IgXyBpbiByYW5nZShpbnQoaW5wdXQoKSkpOgogbixtID0gbWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiBsID0gbGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCiBnID0gMAogZm9yIGkgaW4gbDoKICBnID0gZ2NkKGcsaSkKIGlmKGc8bik6CiAgcHJpbnQobiAtIGcpCiAgY29udGludWUKIGYgPSAwCiBzID0gaW50KHNxcnQoZykpCiBmb3IgaSBpbiByYW5nZSgxLHMrMSk6CiAgaWYoZyVpID09IDApOgogICBpZihpIDw9IG4pOgogICAgZiA9IG1heChmLGkpCiAgIGlmKGcvL2kgPD0gbik6CiAgICBmID0gbWF4KGYsZy8vaSkKIHByaW50KG4gLSBmKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
