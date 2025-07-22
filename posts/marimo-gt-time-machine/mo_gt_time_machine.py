import marimo

__generated_with = "0.14.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import copy
    import inspect
    from functools import wraps
    from typing import Callable, Self

    import pandas as pd
    from great_tables import GT, html
    from great_tables.data import airquality

    return Callable, GT, Self, airquality, copy, html, inspect, wraps


@app.cell
def _(Callable, GT, Self, copy, html, inspect, wraps):
    def get_allowed_member_names() -> list[str]:
        """
        Manually constructing the list —
        it would be great if Great Tables exposed the available method names.
        """
        return [
            "fmt",
            "fmt_number",
            "fmt_integer",
            "fmt_percent",
            "fmt_scientific",
            "fmt_currency",
            "fmt_bytes",
            "fmt_roman",
            "fmt_date",
            "fmt_time",
            "fmt_datetime",
            "fmt_markdown",
            "fmt_image",
            "fmt_icon",
            "fmt_flag",
            "fmt_units",
            "fmt_nanoplot",
            "data_color",
            "sub_missing",
            "sub_zero",
            "opt_stylize",
            "opt_align_table_header",
            "opt_all_caps",
            "opt_footnote_marks",
            "opt_row_striping",
            "opt_vertical_padding",
            "opt_horizontal_padding",
            "opt_table_outline",
            "opt_table_font",
            "cols_align",
            "cols_width",
            "cols_label",
            "cols_move",
            "cols_move_to_start",
            "cols_move_to_end",
            "cols_hide",
            "cols_unhide",
            "tab_header",
            "tab_source_note",
            "tab_spanner",
            "tab_stubhead",
            "tab_style",
            "tab_options",
            "row_group_order",
            "tab_stub",
            "with_id",
            "with_locale",
            "save",
            "show",
            "as_raw_html",
            "write_raw_html",
            "as_latex",
            "pipe",
        ]

    def lazify(cls: GT) -> GT:
        def add_to_pipeline(func: Callable[..., GT]) -> callable:
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                def inner(self):
                    return func(self, *args, **kwargs)

                # container for storing callable objects
                self._pipeline.append(inner)
                return self

            wrapper.__signature__ = inspect.signature(func)
            return wrapper

        for member_name in get_allowed_member_names():
            setattr(
                cls, member_name, add_to_pipeline(getattr(GT, member_name))
            )
        return cls

    @lazify
    class WigGT:
        def __init__(self, *args, widget, **kwargs):
            self._args = args
            self._widget = widget
            self._kwargs = kwargs
            self.set_to_init()

        @property
        def tables(self) -> list[GT]:
            return list(self._tables)  # return a new list

        def _widgetify(self, obj: GT) -> GT:
            return obj.tab_source_note(html(self._widget))

        def collect(self) -> Self:
            if not self._is_collect:
                new_obj = self._tables[0]  # don't use self._wtables[0]
                for f in self._pipeline:
                    new_obj = f(self=copy.copy(new_obj))
                    self._tables.append(new_obj)
                    self._wtables.append(self._widgetify(new_obj))
                self._is_collect = True
            return self

        def _repr_html_(self) -> str:
            try:
                obj = self._wtables[self._widget.value]
            except IndexError:
                obj = self._wtables[-1]

            if hasattr(obj, "_display_"):
                render_method = "_display_"
            elif hasattr(obj, "_repr_html_"):
                render_method = "_repr_html_"
            elif hasattr(obj, "_mime_"):
                render_method = "_mime_"
            else:
                raise AttributeError(
                    "The object does not have a valid render method."
                )
            return getattr(obj, render_method)()  # remember to invoke

        def set_to_init(self) -> None:
            if not getattr(self, "_pipeline", None):
                self._pipeline: list[callable] = []
            else:
                self._pipeline.clear()

            if not getattr(self, "_tables", None):
                self._tables = []
            else:
                self._tables.clear()

            if not getattr(self, "_wtables", None):
                self._wtables = []
            else:
                self._wtables.clear()

            obj = self._make_gt()
            self._tables.append(obj)
            self._wtables.append(self._widgetify(obj))
            self._is_collect = False

        def _make_gt(self) -> GT:
            return GT(*self._args, **self._kwargs)

    return (WigGT,)


@app.cell
def _(mo):
    time_widget = mo.ui.slider(start=0, stop=6, step=1, value=0, label="Step")
    time_widget
    return (time_widget,)


@app.cell
def _(WigGT, airquality, html, time_widget):
    # The lazy_wig_gt object is not interactive until collect() is called.
    lazy_wig_gt = (
        WigGT(airquality.head(10).assign(Year=1973), widget=time_widget)
        .opt_stylize(color="pink", style=2)
        .tab_header(
            title="New York Air Quality Measurements",
            subtitle="Daily measurements in New York City (May 1-10, 1973)",
        )
        .tab_spanner(label="Time", columns=["Year", "Month", "Day"])
        .tab_spanner(
            label="Measurement", columns=["Ozone", "Solar_R", "Wind", "Temp"]
        )
        .cols_move_to_start(columns=["Year", "Month", "Day"])
        .cols_label(
            Ozone=html("Ozone,<br>ppbV"),
            Solar_R=html("Solar R.,<br>cal/m<sup>2</sup>"),
            Wind=html("Wind,<br>mph"),
            Temp=html("Temp,<br>&deg;F"),
        )
    )
    lazy_wig_gt
    return (lazy_wig_gt,)


@app.cell
def _(lazy_wig_gt):
    # The wig_gt object is now interactive
    wig_gt = lazy_wig_gt.collect()
    wig_gt
    return (wig_gt,)


@app.cell
def _(wig_gt):
    # retrieve all `gt` tables
    wig_gt.tables
    return


if __name__ == "__main__":
    app.run()
