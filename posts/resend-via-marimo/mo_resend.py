import marimo

__generated_with = "0.14.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    from html import escape
    import polars as pl
    import resend
    return escape, mo, resend


@app.cell
def _(escape, resend):
    def send_email(d: dict[str, str]) -> None:
        """
        https://resend.com/docs/send-with-python
        """
        resend.api_key = d["RESEND_API_KEY"]
        from_ = d["from_"]
        to = [mail.strip() for mail in d["to"].split(",")]
        subject = d["subject"]
        html_ = escape(d["content"]).replace("\n", "<br>")

        params: resend.Emails.SendParams = {
            "from": from_,
            "to": to,
            "subject": subject,
            "html": html_,
        }

        email = resend.Emails.send(params)
    return (send_email,)


@app.cell
def _(mo, send_email):
    # Create a form with multiple eleme
    form = (
        mo.md(
            """
        **marimo mail**
        {RESEND_API_KEY}

        {from_}

        {to}

        {subject}

        {content}
    """
        )
        .batch(
            RESEND_API_KEY=mo.ui.text(
                label="RESEND_API_KEY", kind="password", full_width=True
            ),
            from_=mo.ui.text(label="From", kind="email", full_width=True),
            to=mo.ui.text(label="To", kind="email", full_width=True),
            subject=mo.ui.text(label="Subject", full_width=True),
            content=mo.ui.text_area(full_width=True),
        )
        .form(show_clear_button=True, on_change=send_email)
    )
    form
    return


if __name__ == "__main__":
    app.run()
