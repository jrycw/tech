import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import random
    from collections.abc import Iterable

    import pandas as pd
    from great_tables import GT, html

    return GT, Iterable, html, pd, random


@app.cell
def _(Iterable):
    def render_widget(widget):
        if hasattr(widget, "_display_"):
            render_method = "_display_"
        elif hasattr(widget, "_repr_html_"):
            render_method = "_repr_html_"
        elif hasattr(widget, "_mime_"):
            render_method = "_mime_"
        else:
            raise ValueError("The object does not have a valid render method.")
        return getattr(widget, render_method)()

    def render_widgets(widgets):
        if not isinstance(widgets, Iterable):
            widgets = [widgets]
        return [render_widget(widget) for widget in widgets]

    def strify_widget_value(widget):
        return str(widget.value)

    def strify_widget_values(widgets):
        if not isinstance(widgets, Iterable):
            widgets = [widgets]
        return [strify_widget_value(w) for w in widgets]

    return render_widgets, strify_widget_values


@app.cell
def _(mo, random):
    switch = mo.ui.switch()
    checkbox = mo.ui.checkbox(label="check me")
    date = mo.ui.date()
    run_botton = mo.ui.run_button(label="Run")
    button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="increment"
    )
    number = mo.ui.number(1, 10)
    slider = mo.ui.slider(1, 10, 1)
    range_slider = mo.ui.range_slider(1, 10, 2, value=[2, 6])
    radio = mo.ui.radio(options=["Apples", "Oranges"], value="Apples")
    dropdown = mo.ui.dropdown(options=["Apples", "Oranges"], value="Apples")
    multiselect = mo.ui.multiselect(options=["Apples", "Oranges"])
    text = mo.ui.text(placeholder="placeholder...", debounce=False)
    text_area = mo.ui.text_area(placeholder="placeholder...", debounce=False)

    widgets = mo.ui.array(
        [
            switch,
            checkbox,
            date,
            run_botton,
            button,
            number,
            slider,
            range_slider,
            radio,
            dropdown,
            multiselect,
            text,
            text_area,
        ]
    )

    col_widget_link = [
        mo.md("[Switch](https://docs.marimo.io/api/inputs/switch/)"),
        mo.md("[CheckBox](https://docs.marimo.io/api/inputs/checkbox/)"),
        mo.md("[Date](https://docs.marimo.io/api/inputs/dates/)"),
        mo.md("[Run Button](https://docs.marimo.io/api/inputs/run_button/)"),
        mo.md("[Button](https://docs.marimo.io/api/inputs/button/)"),
        mo.md("[Number](https://docs.marimo.io/api/inputs/number/)"),
        mo.md("[Slider](https://docs.marimo.io/api/inputs/slider/)"),
        mo.md(
            "[Range Slider](https://docs.marimo.io/api/inputs/range_slider/)"
        ),
        mo.md("[Radio](https://docs.marimo.io/api/inputs/radio/)"),
        mo.md("[Dropdown](https://docs.marimo.io/api/inputs/dropdown/)"),
        mo.md("[MultiSelect](https://docs.marimo.io/api/inputs/multiselect/)"),
        mo.md("[Text](https://docs.marimo.io/api/inputs/text/)"),
        mo.md("[Text Area](https://docs.marimo.io/api/inputs/text_area/)"),
    ]

    col_code = [
        mo.accordion(
            {
                "switch = mo.ui.switch()": "`switch(value: bool = False, *, label: str = '', disabled: bool = False, on_change: Optional[Callable[[bool], None]] = None)`"
            }
        ),
        mo.accordion(
            {
                'checkbox = mo.ui.checkbox(label="check me")': "`checkbox(value: bool = False, *, label: str = '', disabled: bool = False, on_change: Optional[Callable[[bool], None]] = None)`"
            }
        ),
        mo.accordion(
            {
                "date = mo.ui.date()": "`date(start: Optional[date | str] = None, stop: Optional[date | str] = None, value: Optional[date | str] = None, *, label: str = '', on_change: Optional[Callable[[date], None]] = None, full_width: bool = False, disabled: bool = False)`"
            }
        ),
        mo.accordion(
            {
                'run_botton = mo.ui.run_button(label="Run")': "`run_button(kind: Literal['neutral', 'success', 'warn', 'danger'] = 'neutral', disabled: bool = False, tooltip: Optional[str] = None, *, label: str = 'click to run', on_change: Optional[Callable[[Any], None]] = None, full_width: bool = False, keyboard_shortcut: Optional[str] = None)`",
            }
        ),
        mo.accordion(
            {
                'button = mo.ui.button(value=0, on_click=lambda value: value + 1, label="increment")': "`button(on_click: Optional[Callable[[Any], Any]] = None, value: Optional[Any] = None, kind: Literal['neutral', 'success', 'warn', 'danger'] = 'neutral', disabled: bool = False, tooltip: Optional[str] = None, *, label: str = 'click here', on_change: Optional[Callable[[Any], None]] = None, full_width: bool = False, keyboard_shortcut: Optional[str] = None)`"
            }
        ),
        mo.accordion(
            {
                "number = mo.ui.number(1, 10)": "`number(start: Optional[float] = None, stop: Optional[float] = None, step: Optional[float] = None, value: Optional[float] = None, debounce: bool = False, *, label: str = '', on_change: Optional[Callable[[Optional[Numeric]], None]] = None, full_width: bool = False, disabled: bool = False)`"
            }
        ),
        mo.accordion(
            {
                "slider = mo.ui.slider(1, 10, 1)": "`slider(start: Optional[Numeric] = None, stop: Optional[Numeric] = None, step: Optional[Numeric] = None, value: Optional[Numeric] = None, debounce: bool = False, disabled: bool = False, orientation: Literal['horizontal', 'vertical'] = 'horizontal', show_value: bool = False, include_input: bool = False, steps: Optional[Sequence[Numeric]] = None, *, label: str = '', on_change: Optional[Callable[[Optional[Numeric]], None]] = None, full_width: bool = False)`"
            }
        ),
        mo.accordion(
            {
                "range_slider = mo.ui.range_slider(1, 10, 2, value=[2, 6])": "`range_slider(start: Optional[Numeric] = None, stop: Optional[Numeric] = None, step: Optional[Numeric] = None, value: Optional[Sequence[Numeric]] = None, debounce: bool = False, orientation: Literal['horizontal', 'vertical'] = 'horizontal', show_value: bool = False, steps: Optional[Sequence[Numeric]] = None, *, label: str = '', on_change: Optional[Callable[[Sequence[Numeric]], None]] = None, full_width: bool = False, disabled: bool = False)`"
            }
        ),
        mo.accordion(
            {
                'radio = mo.ui.radio(options=["Apples", "Oranges"], value="Apples")': "`radio(options: Sequence[str] | dict[str, Any], value: Optional[str] = None, inline: bool = False, *, label: str = '', on_change: Optional[Callable[[Any], None]] = None, disabled: bool = False)`"
            }
        ),
        mo.accordion(
            {
                'dropdown = mo.ui.dropdown(options=["Apples", "Oranges"], value="Apples")': "`dropdown(options: Sequence[Any] | dict[str, Any], value: Optional[Any] = None, allow_select_none: Optional[bool] = None, searchable: bool = False, *, label: str = '', on_change: Optional[Callable[[Any], None]] = None, full_width: bool = False)`"
            }
        ),
        mo.accordion(
            {
                'multiselect = mo.ui.multiselect(options=["Apples", "Oranges"])': "`multiselect(options: Sequence[Any] | dict[str, Any], value: Optional[Sequence[Any]] = None, *, label: str = '', on_change: Optional[Callable[[list[object]], None]] = None, full_width: bool = False, max_selections: Optional[int] = None)`"
            }
        ),
        mo.accordion(
            {
                'text = mo.ui.text(placeholder="placeholder...", debounce=False)': "`text(value: str = '', placeholder: str = '', kind: Literal['text', 'password', 'email', 'url'] = 'text', max_length: Optional[int] = None, disabled: bool = False, debounce: bool | int = True, *, label: str = '', on_change: Optional[Callable[[str], None]] = None, full_width: bool = False)`"
            }
        ),
        mo.accordion(
            {
                'text_area = mo.ui.text_area(placeholder="placeholder...", debounce=False)': "`text_area(value: str = '', placeholder: str = '', max_length: Optional[int] = None, disabled: bool = False, debounce: bool | int = True, rows: Optional[int] = None, *, label: str = '', on_change: Optional[Callable[[str], None]] = None, full_width: bool = False)`"
            }
        ),
    ]

    # table styling
    _style_number_start, _style_number_end = 1, 6
    style_widget = mo.ui.slider(
        _style_number_start,
        _style_number_end,
        value=random.randint(_style_number_start, _style_number_end),
        label="Style Number",
    )

    _colors = ["blue", "cyan", "pink", "green", "red", "gray"]
    color_widget = mo.ui.radio(
        options=_colors,
        value=random.choice(_colors),
        label="Style Color",
        inline=True,
    )
    return col_code, col_widget_link, color_widget, style_widget, widgets


@app.cell
def _(
    col_code,
    col_widget_link,
    pd,
    render_widgets,
    strify_widget_values,
    widgets,
):
    col_widget = render_widgets(widgets)
    col_value = strify_widget_values(widgets)

    data = {
        "link": col_widget_link,
        "widget": col_widget,
        "value": col_value,
        "code": col_code,
    }

    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(GT, color_widget, df, html, style_widget):
    gt = (
        GT(df)
        .cols_align("left")
        .opt_all_caps()
        .tab_header(html(style_widget), html(color_widget))
    )
    return (gt,)


@app.cell
def _(color_widget, gt, style_widget):
    (
        gt.opt_stylize(style=style_widget.value, color=color_widget.value)
        .opt_align_table_header("left")
        .cols_width({"widget": "20%"})
    )
    return


if __name__ == "__main__":
    app.run()
