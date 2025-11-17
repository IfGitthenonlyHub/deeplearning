import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCgpkZWYgbWFpbigpOgogTiA9IGludChpbnB1dCgpKQogd2hpbGUgVHJ1ZToKICB0cnk6CiAgIFggPSBpbnB1dCgpCiAgZXhjZXB0OgogICBicmVhawogIEggPSBsaXN0KG1hcChpbnQsIFguc3BsaXQoKSkpCiAgQyA9IDAKICB3aGlsZSBIOgogICBlID0gSC5wb3AoMCkKICAgSDIsIEMxLCBDMiA9IGxpc3QoSCksIGUsIDAKICAgZm9yIGkgaW4gcmFuZ2UobGVuKEgyKSk6CiAgICBpZiBIMltpXSA+IGUtMToKICAgICBDMiArPSBIMltpXS0oZS0xKQogICAgIEgyW2ldID0gZS0xCiAgICNwcmludCBDK0MyLCBIMiwgQytDMSwgSAogICBpZiBDMSA8PSBDMjoKICAgIEMgKz0gQzEKICAgZWxzZToKICAgIEMgKz0gQzIKICAgIEggPSBIMgogIHByaW50KEMpCgptYWluKCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
