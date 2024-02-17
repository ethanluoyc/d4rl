import nox

@nox.session(python=["3.10"])
def tests(session):
    session.install(".", "pytest", "six")
    with session.chdir("tests"):
        session.run("python", "-m",  "pytest", "--capture=no")

