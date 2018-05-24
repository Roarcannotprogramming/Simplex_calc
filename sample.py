# encoding=utf-8
import Simplex_model_class as model


def simplex_exec(simplex):
    #simplex.step_1()
    simplex.step_2()


if __name__ == "__main__":
    # A = [[2, 2, 1, 0, 0],
    #      [4, 0, 0, 1, 0],
    #      [0, 5, 0, 0, 1]]
    #
    # b = [12, 16, 15]
    #
    # c = [2, 3, 0, 0, 0]

    # A = [[2, 2, 1, 0, 0, 0],
    #      [1, 2, 0, 1, 0, 0],
    #      [4, 0, 0, 0, 1, 0],
    #      [0, 4, 0, 0, 0, 1]]
    #
    # b = [12, 8, 16, 12]
    #
    # c = [2, 3, 0, 0, 0, 0]

    # A = [[3, 4, 1, 0],
    #      [5, 2, 0, 1]]
    #
    # b = [9, 8]
    #
    # c = [10, 5, 0, 0]

    A = [[0, 5, 1, 0, 0],
         [6, 2, 0, 1, 0],
         [1, 1, 0, 0, 1]]

    b = [15, 24, 5]

    c = [2, 1, 0, 0, 0]

    simplex = model.SimplexModel(A, b, c)
    simplex_exec(simplex)




