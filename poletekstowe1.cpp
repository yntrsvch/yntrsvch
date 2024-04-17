#include <iostream>
#include <windows.h>
#include <conio.h>

const int WIDTH = 20; // Szerokość pola tekstowego
const int HEIGHT = 1; // Wysokość pola tekstowego (wiersze)
const int MAX_INPUT_LENGTH = WIDTH - 1; // Maksymalna długość wprowadzanego tekstu

// Ustawia pozycję kursora w konsoli
void setCursorPosition(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

// Ustawia kolor tekstu w konsoli
void setConsoleColor(WORD color) {
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
}

// Rysuje pole tekstowe na ekranie konsoli
void drawTextField(int x, int y) {
    setCursorPosition(x, y);
    for (int i = 0; i < WIDTH; ++i) {
        std::cout << "-";
    }
    setCursorPosition(x, y + HEIGHT);
    for (int i = 0; i < WIDTH; ++i) {
        std::cout << "-";
    }
}

// Czyści pole tekstowe na ekranie konsoli
void clearTextField(int x, int y) {
    setCursorPosition(x, y);
    for (int i = 0; i < WIDTH; ++i) {
        std::cout << " ";
    }
    setCursorPosition(x, y + HEIGHT);
    for (int i = 0; i < WIDTH; ++i) {
        std::cout << " ";
    }
}

// Obsługuje wprowadzanie tekstu przez użytkownika
void handleInput(int x, int y) {
    char input[MAX_INPUT_LENGTH + 1] = { 0 }; // Tablica przechowująca wprowadzany tekst (+1 dla znaku null)
    int cursorPos = 0; // Aktualna pozycja kursora

    while (true) {
        setCursorPosition(x + cursorPos, y); // Ustawienie pozycji kursora

        char ch = _getch(); // Pobranie pojedynczego znaku

        if (ch == 27) { // ESC - Wyjście z pętli
            break;
        }
        else if (ch == 8) { // Backspace - Usunięcie poprzedniego znaku
            if (cursorPos > 0) {
                --cursorPos;
                input[cursorPos] = ' ';
                setCursorPosition(x + cursorPos, y);
                std::cout << " ";
            }
        }
        else if (ch == 75 && cursorPos > 0) { // Lewa strzałka - Przesunięcie kursora w lewo
            --cursorPos;
        }
        else if (ch == 77 && cursorPos < MAX_INPUT_LENGTH && input[cursorPos] != 0) { // Prawa strzałka - Przesunięcie kursora w prawo
            ++cursorPos;
        }
        else if (cursorPos < MAX_INPUT_LENGTH && (ch >= 32 && ch <= 126)) { // Drukowalny znak - Dodanie do tablicy wprowadzanego tekstu
            input[cursorPos] = ch;
            std::cout << ch;
            ++cursorPos;
        }
    }
}

int main() {
    // Narysuj pole tekstowe na ekranie
    drawTextField(10, 5);

    // Obsłuż wprowadzanie tekstu przez użytkownika
    handleInput(11, 6);

    return 0;
}

