package com.company;

import java.util.Scanner;

public class Main {
    // Создаем двух игроков. При выборе команд "left" или "right" добавляем игроку 15 очков
    public static void main(String[] args) {
        Player player_1 = new Player("Maks");
        Player player_2 = new Player("Oleg");
        Scanner points = new Scanner(System.in);
        int i;
        i = points.nextInt();
        if (i == 1) {
            player_1.player_points += 15;
        }
        if (i == 2) {
            player_2.player_points += 15;
        }
        System.out.println(player_1.player_points);
        System.out.print(player_2.player_points);


    }

}
