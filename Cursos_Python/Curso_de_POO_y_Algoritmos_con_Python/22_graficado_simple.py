from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("Graficado_simple.html")
    fig = figure()

    total_vals = int(input("Cuantos valores quieres graficar"))
    x_values = list(range(total_vals))
    y_values = []

    for i in x_values:
        val = int(input(f'Valor y para {i}'))
        y_values.append(val)

    fig.line(x_values, y_values, line_width = 2)
    show(fig)