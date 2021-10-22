import sys
from flask import render_template, redirect, url_for, request, abort


def index():
    return render_template('inicio/index.html')
