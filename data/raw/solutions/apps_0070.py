import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dCA9IGxhbWJkYTogc3lzLnN0ZGluLnJlYWRsaW5lKCkucnN0cmlwKCkKZGVmIGNhbGMobiwgaywgQSk6CiAgICBYID0gW1swXSAqIDI2IGZvciBfIGluIHJhbmdlKChrKzEpLy8yKV0KICAgIGZvciBpLCBhIGluIGVudW1lcmF0ZShBKToKICAgICAgICBqID0gaSAlIGsKICAgICAgICBqID0gbWluKGosIGstMS1qKQogICAgICAgIFhbal1bYV0gKz0gMQogICAgcmV0dXJuIHN1bShbc3VtKHgpIC0gbWF4KHgpIGZvciB4IGluIFhdKQoKVCA9IGludChpbnB1dCgpKQpmb3IgXyBpbiByYW5nZShUKToKICAgIE4sIEsgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBTID0gW29yZChhKSAtIDk3IGZvciBhIGluIGlucHV0KCldCiAgICBwcmludChjYWxjKE4sIEssIFMpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
