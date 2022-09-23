import inspect
import keyword
import re

import black as blk
import click
import jinja2

from bmipy import Bmi

BMI_TEMPLATE = """# -*- coding: utf-8 -*-
{% if with_hints -%}
from typing import Tuple
{%- endif %}

from bmipy import Bmi
import numpy


class {{ name }}(Bmi):
{% for func in funcs %}
    def {{ func }}{{ funcs[func].sig }}:
        \"\"\"{{ funcs[func].doc }}\"\"\"
        raise NotImplementedError("{{ func }}")
{% endfor %}
"""


def _remove_hints_from_signature(signature):
    """Remove hint annotation from a signature."""
    params = []
    for name, param in signature.parameters.items():
        params.append(param.replace(annotation=inspect.Parameter.empty))
    return signature.replace(
        parameters=params, return_annotation=inspect.Signature.empty
    )


def _is_valid_class_name(name):
    p = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    return p.match(name) and not keyword.iskeyword(name)


def render_bmi(name, black=True, hints=True):
    """Render a template BMI implementation in Python

    Parameters
    ----------
    name : str
        Name of the new BMI class to implement.
    black : bool, optional
        If True, reformat the source using black styling.
    hints : bool, optiona
        If True, include type hint annotation.

    Returns
    -------
    str
        The contents of a new Python module that contains a template for
        a BMI implementation.
    """
    if _is_valid_class_name(name):
        env = jinja2.Environment()
        template = env.from_string(BMI_TEMPLATE)

        funcs = {}
        for func_name, func in inspect.getmembers(Bmi, inspect.isfunction):
            signature = inspect.signature(func)
            if not hints:
                signature = _remove_hints_from_signature(signature)
            funcs[func_name] = {"sig": signature, "doc": func.__doc__}

        contents = template.render(name=name, funcs=funcs, with_hints=hints)

        if black:
            contents = blk.format_file_contents(
                contents, fast=True, mode=blk.FileMode()
            )

        return contents
    else:
        raise ValueError("invalid class name ({0})".format(name))


@click.command()
@click.version_option()
@click.option("--black / --no-black", default=True, help="format output with black")
@click.option("--hints / --no-hints", default=True, help="include type hint annotation")
@click.argument("name")
@click.pass_context
def main(ctx, name, black, hints):
    """Render a template BMI implementation in Python for class NAME."""
    if _is_valid_class_name(name):
        print(render_bmi(name, black=black, hints=hints))
    else:
        click.secho(
            "💥 💔 💥 '{0}' is not a valid class name in Python".format(name),
            err=True,
            fg="red",
        )
        ctx.exit(code=1)
