# Este código no se ejecuta. Solo sirve para guardar el procedimiento de ajustar el grado del polinomio

# Se crea una lista vacía en la que almacenar los valores de R
Rsqu_test = []

# Lista con los valores con los que se probará a hacer ajustes
order = [1,2,3,4]

# Bucle para probar todos los valores y ver cual se adapta mejor
for n in order:
    pr = PolynomialFeatures(degree=n)

    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])

    lr.fit(x_train_pr,y_train)

    Rsqu_test.append(lr.score(x_test_pr,y_test))