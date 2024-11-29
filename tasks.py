from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/unit_tests", pty=True)
    ctx.run("robot src/story_tests", pty=True)
    ctx.run("pylint src", pty=True)