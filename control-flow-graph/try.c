int main() {
    int i, grade = 0;
    printf (" Enter points: \n");
    scanf ("%d", &i);
    if (i >= 50 && i <= 60)
	 grade = 5;
    else if (i > 50 && i <= 60)
	 grade = 6;
    else if (i > 60 && i <= 70)
	 grade = 7;
    else if (i > 70 && i <= 80)
	 grade = 8;
    else if (i > 80 && i <= 90)
	 grade = 9;
    else if (i > 90 && i <= 100)
	 grade = 10;
    char sign = ' ';
    if (grade) {
        int p = i % 10;
        if (grade != 5) {
            if (p >= 1 && p <= 3)
                sign = '-';
            else if (grade != 10 && (p >= 8 || p == 0))
                sign = '+';
        }
        printf (" The grade is %d%c. \n", grade, sign);

    }
    return 0;
}
