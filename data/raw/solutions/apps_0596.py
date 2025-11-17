import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIGkgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4saz1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKICAgIGlmKG4hPTApOgogICAgICAgIGQ9KGstMSkvLzIKICAgICAgICB6PW4qKjIrKGsvLzIpKigyKm4pK2QqKGQrMSkKICAgICAgICB6PXolKDEwKio5KzcpCiAgICAgICAgcHJpbnQoeikKICAgIGVsc2U6CiAgICAgICAgej1rKihrLTEpCiAgICAgICAgej16JSgxMCoqOSs3KQogICAgICAgIHByaW50KHop").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
