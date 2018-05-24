import Simplex_model_class as model


def simplex_exec(simplex):
    simplex.step_2()


if __name__ == "__main__":

    A = eval(input("Input your Coefficient Matrix: \n # Sample \n [[2, 2, 1, 0, 0], [4, 0, 0, 1, 0], [0, 5, 0, 0, 1]] \n"))
    b = eval(input("Input your Non-homogeneous Items(Vector): \n # Sample \n [12, 16, 15] \n"))
    c = eval(input("Input your max z Coefficient Items(Vector): \n # Sample \n [2, 3, 0, 0, 0] \n"))

    simplex = model.SimplexModel(A, b, c)
    simplex_exec(simplex)
