import subprocess

def get_python_version():
    proc = subprocess.Popen(['python', '-V'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )

    out,err = proc.communicate()
    if proc.returncode:
        raise Exception(f"Error exit {proc.returncode}")
    #if err:
    #    raise Exception(f"Error {err}")
    return out.decode('utf8') if out else err.decode('utf8')
