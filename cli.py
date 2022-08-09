import typer
import alembic.config

app = typer.Typer()

@app.command()
def say_hello():
    """
    Say hello to
    """
    nama = typer.prompt("what's your name: ")
    print(f"hello {nama}")


@app.command()
def refresh_initial():
    """
    Drop All Migration -> Migrate Database -> initial-data
    """
    alembic_args = ["downgrade", "base"]
    alembic.config.main(argv=alembic_args)
    alembic_args = ["upgrade", "head"]
    alembic.config.main(argv=alembic_args)

if __name__ == "__main__":
    app()
