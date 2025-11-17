import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IG1hdGgKCnQgPSBpbnQoaW5wdXQoKSkKCmEgPSBbLTEsIDAsIDFdCgpmb3IgaSBpbiByYW5nZSg2MSk6CiB0ZW1wID0gYVstMV0gKyBhWy0yXQogdGVtcCA9IHRlbXAlMTAKIGEuYXBwZW5kKHRlbXApCiAKZm9yIF8gaW4gcmFuZ2UodCk6CiBuID0gaW50KGlucHV0KCkpCiAKIG4gPSBpbnQobWF0aC5sb2cobiwgMikpCiAKIG4gPSAoMioqbiklNjAKIHByaW50KGFbbl0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
