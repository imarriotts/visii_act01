from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl 

# Datos de entrada
complejos = ['Hawaiian Club', 'French Riviera', 'Bahamas Beach', 'Hawaiian Club',
             'French Riviera', 'Bahamas Beach', 'Hawaiian Club', 'French Riviera', 'Bahamas Beach']
años = ['1993', '1993', '1993', '1994', '1994', '1994', '1995', '1995', '1995']
ingresos = [450000, 225000, 245000, 475000,
            240000, 205000, 390000, 205000, 345000]


# Crear el dataframe
df = pd.DataFrame({'Complejo': complejos, 'Año': años, 'Ingreso': ingresos})

sns.set_style("white")
# Crear la primera visualización
sns.barplot(x='Complejo', y='Ingreso', hue='Año',
            data=df, palette=sns.color_palette("deep", 3))
plt.title('Ingresos de complejos hoteleros')
plt.ylabel('Ingresos')
plt.legend(loc='upper right', fontsize=8)
plt.savefig("barplot.png")
plt.close()
# Crear la segunda visualización
sns.lineplot(x='Año', y='Ingreso', hue='Complejo',
             data=df, palette=sns.color_palette("deep", 3))
plt.title('Ingresos de complejos hoteleros')
plt.ylabel('Ingresos')
plt.legend(loc='upper right', fontsize=8)
plt.savefig("lineplot.png")
plt.close()
# Crear la tercera visualización
pivot_table = pd.pivot_table(df, values='Ingreso', index=[
                             'Complejo'], columns=['Año'], aggfunc=np.sum)
# Crear el gráfico
sns.set_palette("deep", 3)
ax = pivot_table.plot(kind='bar', stacked=True)
plt.title('Ingresos de complejos hoteleros')
plt.xticks(rotation=0)
plt.ylabel('Ingresos (K)')
formatter = FuncFormatter(lambda y, _: '{:.0f}K'.format(y/1000))
ax.yaxis.set_major_formatter(formatter)
plt.savefig("barplotstack.png")
plt.close()
