import marimo

__generated_with = "0.14.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import polars as pl
    from great_tables import GT, html, md

    return GT, html, pl


@app.cell
def _(pl):
    tasks = [
        "Set DEBUG = False",
        "Configure ALLOWED_HOSTS",
        "Set up a secret key",
        "Collect static files",
        "Apply database migrations",
        "Set up gunicorn or uWSGI",
        "Configure reverse proxy (e.g., Nginx)",
        "Secure the database",
        "Set up HTTPS (SSL)",
        "Configure logging & monitoring",
    ]

    notes = [
        "Never deploy with DEBUG = True ⚠️",
        "Include your domain(s) or IP address 🌐",
        "Use a strong, secure key from an environment variable 🔐",
        "Run `python manage.py collectstatic` 📦",
        "Run `python manage.py migrate` 🗃️",
        "Use as a WSGI server in production 🔄",
        "Serve static/media files and forward to WSGI server 🧭",
        "Use strong credentials, disable remote root login 🛡️",
        "Use Let's Encrypt or your own certificate 🔒",
        "Track errors and app performance 📊",
    ]

    n_row = len(tasks)
    status = ["☐"] * n_row
    data = {"Status": status, "Task": tasks, "Notes": notes}

    df = pl.DataFrame(data)
    return df, n_row


@app.cell
def _(mo, n_row):
    status_widget = mo.ui.switch()
    status_widgets = mo.ui.array([status_widget] * n_row)
    return (status_widgets,)


@app.function
def create_bar(
    x: float,
    max_width: int,
    height: int,
    background_color1: str,
    background_color2: str,
) -> str:
    width = round(max_width * x, 2)
    px_width = f"{width}px"
    return f"""\
    <div style="width: {max_width}px; background-color: {background_color1};">\
        <div style="height:{height}px;width:{px_width};background-color:{background_color2};"></div>\
    </div>\
    """


@app.cell
def _(GT, df, html, n_row, pl, status_widgets):
    done_count = sum(s.value for s in status_widgets)

    gt = (
        GT(
            df.with_columns(
                pl.Series(
                    [status._repr_html_() for status in status_widgets]
                ).alias("Status")
            )
        )
        .tab_source_note(f"{done_count} / {n_row}")
        .tab_source_note(
            html(
                create_bar(
                    done_count / n_row,
                    max_width=750,
                    height=20,
                    background_color1="lightgray",
                    background_color2="#66CDAA",
                )
            )
        )
        .tab_header("✅ Django Deployment Checklist")
        .opt_stylize(color="cyan", style=4)
    )
    gt
    return


if __name__ == "__main__":
    app.run()
