import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwoKdCA9IGludChpbnB1dCgpKQoKZGVmIGcoYSxiKToKIGlmIChhID4gYik6CiAgdG1wID0gYQogIGEgPSBiCiAgYiA9IHRtcAogaWYgKGIgPT0gYSk6CiAgcmV0dXJuIDAKIGlmIChiICUgYSA9PSAwKToKICByZXR1cm4gaW50KGIvYSktMQogciA9IGcoYiVhLGEpCiBxID0gaW50KGIvYSkKIGlmIChyID49IHEpOgogIHJldHVybiBxLTEKIGVsc2U6CiAgcmV0dXJuIHEKCmRlZiBtZXgoeCk6CiBuID0gbGVuKGxpc3QoeC5rZXlzKCkpKQogZm9yIGkgaW4gcmFuZ2Uobik6CiAgaWYgKGkgbm90IGluIHgpOgogICByZXR1cm4gaQogcmV0dXJuIGkKCmRlZiBnMihhLGIpOgogaWYgKGEgPT0gYik6CiAgcmV0dXJuIDAKIGlmIChhID4gYik6CiAgdG1wID0gYQogIGEgPSBiCiAgYiA9IHRtcAogaWYgKGIgJSBhID09IDApOgogIHJldHVybiBpbnQoYi9hKS0xCiBxID0gaW50KGIvYSkKIHggPSB7fQogciA9IGIgJSBhCiBmb3IgaSBpbiByYW5nZShxKToKICB4W2cyKHIraSphLGEpXSA9IFRydWUKIHJldHVybiBtZXgoeCkKCiNwcmludChzdHIoZyg2LDMzKSkrIiAiK3N0cihnMig2LDMzKSkpCgp3aGlsZSAodCk6CgogbiA9IGludChpbnB1dCgpKQogeCA9IDAKIHdoaWxlIChuKToKICBsaW5lID0gaW5wdXQoKS5zcGxpdCgpCiAgYSA9IGludChsaW5lWzBdKQogIGIgPSBpbnQobGluZVsxXSkKICB4IF49IGcoYSxiKQogIG4gLT0gMQogaWYgKHgpOgogIHN5cy5zdGRvdXQud3JpdGUoIllFU1xuIikKIGVsc2U6CiAgc3lzLnN0ZG91dC53cml0ZSgiTk9cbiIpCiAjcHJpbnQoc3RyKGcoYSxiKSkgKyAiICIgKyBzdHIoZzIoYSxiKSkpCiB0IC09IDE=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
