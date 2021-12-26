from bokeh.plotting import figure, output_file, show


output_file('grafica.html')
fig = figure()

x_vals = list(range(int(input("Cuantos valores quiere graficar?: "))))

y_vals = [int(input(f'Valor y para {str(i)}: '))for i in x_vals]

fig.line(x_vals, y_vals)
show(fig)