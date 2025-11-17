import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IHN0ZGluCmlucHV0ID0gc3RkaW4ucmVhZGxpbmUKCmRlZiBtYXhfcG9zX2NvaW5zKG4pOgoJYSA9IDAKCXdoaWxlIG4gIT0gMDoKCQlpZiBuID09IDQ6CgkJCWEgKz0gMwoJCQluID0gMAoJCQljb250aW51ZQoJCWlmIG4gJSA0ID09IDA6CgkJCW4gLT0gMgoJCQlhICs9IDEKCQllbHNlOgoJCQlhICs9IG4gLy8gMgoJCQluID0gbiAvLyAyIC0gMQoJcmV0dXJuIGEKCmZvciBfIGluIHJhbmdlKGludChpbnB1dCgpKSk6CgluID0gaW50KGlucHV0KCkpCglwcmludChtYXhfcG9zX2NvaW5zKG4pIGlmIG4gJSAyID09IDAgZWxzZSBuIC0gbWF4X3Bvc19jb2lucyhuIC0gMSkp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
