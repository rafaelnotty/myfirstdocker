from flask import render_template
import numpy as np
import pandas as pd
""" 
Prueba Docstring
    """
arr = np.arange(1,5)
df = pd.DataFrame({'fecha': ['50/22/20', '5/23/20', '5/24/20'], 'valor1': [10, 20, 30], 'valor2': [15, 25, 35]})
#print(str(df.columns.tolist()))
#print(str(list(arr)))
print(df.to_html())
#render_template('tabla.html', table=table)
#render_template('index.html', table=table)
