import os

def add_virtual_env_segment():
    env = os.getenv('VIRTUAL_ENV')
    if env is None:
        return

    if os.path.basename(env) == "__":
        dirName = os.path.dirname(env)
        baseName = os.path.basename(dirName)
        vEnv = "[%s]" % baseName
    else:
        baseName = os.path.basename(env)
        vEnv = "(%s)" % baseName
    bg = Color.VIRTUAL_ENV_BG
    fg = Color.VIRTUAL_ENV_FG
    powerline.append(vEnv, fg, bg)

add_virtual_env_segment()
