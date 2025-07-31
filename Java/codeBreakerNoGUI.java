package Java;

import java.util.*;

public class codeBreakerNoGUI {

    // VARIAVEIS PARA COLORIR OS TEXTOS
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";

    public static void main(String[] args) {
        // JOGO EM SI
        int round = 1;
        Scanner scanner = new Scanner(System.in);
        int[][] objective = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        Shuffle(objective);
        // PrintGrid(objective);
        while (round <= 7) {
            if (PlayerInput(scanner, objective)) {
                round = 10;
            } else {
                round += 1;
                if (round <= 7) {
                    System.out.println("You Lost");
                }
            }
        }
        scanner.close();
    }

    private static boolean PlayerInput(Scanner scanner, int[][] objective) {
        // CRIAÇÃO DO GRID DO JOGADOR
        int[][] gridInput = { { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 }, { 0, 0, 0 }, { 0, 0, 0 } };
        // COLETA DE INFORMAÇÕES
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("Number in [" + i + "][" + j + "]");
                String input = scanner.nextLine();
                // CHECAR SE O INPUT FOI UM NÚMERO
                try {
                    gridInput[i][j] = Integer.parseInt(input);
                } catch (NumberFormatException e) {
                    gridInput[i][j] = 0;
                }
            }
        }
        CheckHoriz(objective, gridInput);
        CheckVert(objective, gridInput);
        PrintInputGrid(gridInput);

        if (gridInput[3][0] == 3 && gridInput[3][1] == 3 && gridInput[3][2] == 3) {
            System.out.println("You Won");
            return true;
        } else {
            return false;
        }
    }

    private static void PrintInputGrid(int[][] gridInput) {
        // PRINTAR O GRID DO JOGADOR COM CORES PARA ENTENDER A LÓGICA
        for (int i = 0; i < gridInput.length; i++) {
            for (int j = 0; j < gridInput[i].length; j++) {
                if (i == 3 || j == 3) {
                    System.out.print(ANSI_GREEN + gridInput[i][j] + ANSI_RESET + " ");
                }
                if (i == 4 || j == 4) {
                    System.out.print(ANSI_YELLOW + gridInput[i][j] + ANSI_RESET + " ");
                }
                if (i != 3 && i != 4 && j != 3 && j != 4) {
                    System.out.print(gridInput[i][j] + " ");
                }
            }
            System.out.println();
        }
    }

    /*
     * DEBUG - CHECAR A GRID OBJETIVO
     * private static void PrintGrid(int[][] objective) {
     * System.out.println(Arrays.deepToString(objective).replace("], ",
     * "]\n").replace("[[", "[").replace("]]", "]"));
     * }
     */

    private static void Shuffle(int[][] objective) {
        // CRIAR A GRID QUE O JOGADOR TEM COMO OBJETIVO
        Random rng = new Random();

        for (int i = objective.length - 1; i > 0; i--) {
            for (int j = objective[i].length - 1; j > 0; j--) {
                int y = rng.nextInt(i + 1);
                int x = rng.nextInt(j + 1);

                int temp = objective[i][j];
                objective[i][j] = objective[y][x];
                objective[y][x] = temp;
            }
        }
    }

    private static void CheckVert(int[][] Grid, int[][] CheckGrid) {
        // VERIFICAR SE O JOGADOR ACERTOU ALGUM ELEMENTO NAS COLUNAS
        // HIT = ACERTO LUGAR ---- B = ACERTOU COLUNA, PORÉM ERROU LUGAR
        for (int i = 0; i < Grid.length; i++) {
            int hit = 0;
            int b = 0;
            int[] vertLine = { 0, 0, 0 };
            for (int j = 0; j < Grid.length; j++) {
                vertLine[j] = Grid[j][i];
            }
            for (int j = 0; j < Grid.length; j++) {
                if (contains(vertLine, CheckGrid[j][i])) {
                    if (Grid[j][i] == CheckGrid[j][i]) {
                        hit = hit + 1;
                    } else {
                        b = b + 1;
                    }
                }
            }
            CheckGrid[3][i] = hit;
            CheckGrid[4][i] = b;
        }
    }

    private static void CheckHoriz(int[][] Grid, int[][] CheckGrid) {
        // VERIFICAR SE O JOGADOR ACERTOU ALGUM ELEMENTO NAS LINHAS
        // HIT = ACERTO LUGAR ---- B = ACERTOU LINHAS, PORÉM ERROU LUGAR
        for (int i = 0; i < Grid.length; i++) {
            int hit = 0;
            int b = 0;
            for (int j = 0; j < Grid.length; j++) {
                if (contains(Grid[i], CheckGrid[i][j])) {
                    if (Grid[i][j] == CheckGrid[i][j]) {
                        hit = hit + 1;
                    } else {
                        b = b + 1;
                    }
                }
            }
            CheckGrid[i][3] = hit;
            CheckGrid[i][4] = b;
        }
    }

    public static boolean contains(final int[] arr, final int key) {
        // VERIFICAR SE ARRAY POSSUI ELEMENTO
        return Arrays.stream(arr).anyMatch(i -> i == key);
    }
}