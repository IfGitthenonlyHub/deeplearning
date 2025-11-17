import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgY29udGFpbnNDeWNsZShzZWxmLCBncmlkOiBMaXN0W0xpc3Rbc3RyXV0pIC0+IGJvb2w6CiAgICAgICAgdmlzaXRlZCA9IHNldCgpCiAgICAgICAgZGVmIGRmcyhpLCBqLCBwcmVfaSwgcHJlX2opOgogICAgICAgICAgICB2aXNpdGVkLmFkZCgoaSwgaikpCiAgICAgICAgICAgIGZvciB4LCB5IGluIFsoMCwgLTEpLCAoMCwgMSksICgtMSwgMCksICgxLCAwKV06CiAgICAgICAgICAgICAgICBpZiAwIDw9IHggKyBpIDwgbGVuKGdyaWQpIGFuZCAwIDw9IHkgKyBqIDwgbGVuKGdyaWRbMF0pIGFuZCBncmlkW2ldW2pdID09IGdyaWRbaSArIHhdW2ogKyB5XSBhbmQgKGkgKyB4ICE9IHByZV9pIG9yIGogKyB5ICE9IHByZV9qKToKICAgICAgICAgICAgICAgICAgICBpZiAoaSArIHgsIGogKyB5KSBpbiB2aXNpdGVkIG9yIGRmcyhpICsgeCwgaiArIHksIGksIGopOgogICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgIAogICAgICAgIGZvciBpIGluIHJhbmdlKGxlbihncmlkKSk6CiAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKGxlbihncmlkW2ldKSk6CiAgICAgICAgICAgICAgICBpZiAoaSwgaikgbm90IGluIHZpc2l0ZWQ6CiAgICAgICAgICAgICAgICAgICAgaWYgZGZzKGksIGosIC0xLCAtMSk6CiAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
