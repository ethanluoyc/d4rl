import nox

mujoco_py_dep = "https://github.com/ethanluoyc/mujoco-py/releases/download/v2.1.2.14%2Bmanylinux/mujoco_py-2.1.2.14+manylinux-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"

@nox.session(python=["3.10"])
def tests(session):
    session.install(".", "pytest", mujoco_py_dep)
    with session.chdir("tests"):
        session.run("python", "-m",  "pytest", "--capture=no")
