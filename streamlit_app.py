import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Zaspa - w danych',
    page_icon='https://pl.wikipedia.org/wiki/Herb_Gda%C5%84ska#/media/Plik:POL_Gda%C5%84sk_COA.svg', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.


# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# Zaspa - w danych

Celem tego projektu jest pokazanie Zaspy oraz jej wyzwan od strony danych.
'''

# Add some spacing
''
''

st.subheader(":umbrella_with_rain_drops: Pogoda")
