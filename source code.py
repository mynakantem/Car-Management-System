#include <windows.h>
#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
#include<string.h>
#include<ctype.h>
#include<direct.h>
#include<time.h>
void mainmenu();
void addcars();
void removecars();
void editlist();
void searchcars();
void carlist();
int getdata();
int checkplate(int t);
struct car
{
int plate;
char company[20];
char make_model[20];
char chasis[20];
char engine[20];
char avail[20];
};
struct car a;
COORD coord = { 0, 0 };
COORD max_res, cursor_size;
void gotoxy(int x, int y)
{
coord.X = x; coord.Y = y;
SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),
coord);
}
void delay(unsigned int mseconds)
{
clock_t goal = mseconds + clock();
while (goal > clock());
}
FILE *fp, *ft, *fs;
int main()
{
system(" title Car Management System");
system(" color 1A");
char array[50] = { "CAR MANAGEMENT SYSTEM" };
gotoxy(35, 10);
for (int x = 0; x < 21; x++)
{
printf("%c", array[x]);
delay(200);
}
gotoxy(38, 15);
printf("Loading......");
delay(4000);
mainmenu();
}
void mainmenu()
{
system(" color 5F ");
system("cls");
int choice;
gotoxy(20, 3);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2 MAIN MENU
\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
gotoxy(20, 5);
printf("\xDB\xDB\xDB\xDB\xB2 1- Add cars");
gotoxy(20, 7);
printf("\xDB\xDB\xDB\xDB\xB2 2- Remove cars");
gotoxy(20, 9);
printf("\xDB\xDB\xDB\xDB\xB2 3- Search cars");
gotoxy(20, 11);
printf("\xDB\xDB\xDB\xDB\xB2 4- View car list");
gotoxy(20, 13);
printf("\xDB\xDB\xDB\xDB\xB2 5- Edit availability info");
gotoxy(20, 15);
printf("\xDB\xDB\xDB\xDB\xB2 6- Close application");
printf("\n\n\n\t\t\tEnter choice: ");
switch (getch())
{
case '1':
addcars();
break;
case '2':
removecars();
break;
case '3':
searchcars();
break;
case '4':
carlist();
break;
case '5':
editlist();
break;
case '6':
{
system("cls");
gotoxy(16, 3);
printf("Thanks for using the Program..");
gotoxy(10, 7);
printf("Exiting in 5 second...........>");
//flushall();
delay(5000);
exit(0);
}
default:
{
gotoxy(10, 23);
printf("\aWrong Entry!!Please re-entered correct
option");
if (getch())
mainmenu();
}}
}
void addcars()
{
char choice = ' ';
system("cls");
system(" color 2F ");
gotoxy(20, 3);
printf("Press any key to enter data.");
gotoxy(20, 4);
printf("Press backspace to go back to main menu.");
if (getch() == 8)
mainmenu();
else
{
system("cls");
fp = fopen("car.txt", "ab+");
if (getdata() == 1)
{
fseek(fp, 0, SEEK_END);
fwrite(&a, sizeof(a), 1, fp);
fclose(fp);
gotoxy(21, 14);
printf("The record is successfully saved");
gotoxy(21, 15);
printf("Save any more?(Y / N):");
choice = getch();
if (choice == 'n')
mainmenu();
else if (choice == 'y')
addcars();
}
}
}
int getdata()
{
int t;
gotoxy(20, 3);
printf("Enter the Information Below");
gotoxy(20, 4);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2\xB2\xB2\xB2\xB2");
gotoxy(20, 5);
printf("\xB2"); gotoxy(55, 5); printf("\xB2");
gotoxy(20, 6);
printf("\xB2"); gotoxy(55, 6); printf("\xB2");
gotoxy(20, 7);
printf("\xB2"); gotoxy(55, 7); printf("\xB2");
gotoxy(20, 8);
printf("\xB2"); gotoxy(55, 8); printf("\xB2");
gotoxy(20, 9);
printf("\xB2"); gotoxy(55, 9); printf("\xB2");
gotoxy(20, 10);
printf("\xB2"); gotoxy(55, 10); printf("\xB2");
gotoxy(20, 11);
printf("\xB2"); gotoxy(55, 11); printf("\xB2");
gotoxy(20, 12);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
gotoxy(21, 5);
printf("Plate #:\t");
gotoxy(30, 5);
scanf("%d", &t);
if (checkplate(t) == 0)
{
gotoxy(21, 13);
printf("\aThe car already exists\a");
getch();
mainmenu();
return 0;
}
a.plate = t;
gotoxy(21, 6);
printf("Company:");
gotoxy(30, 6);
scanf("%s", a.company);
gotoxy(21, 7);
printf("Make & Model:"); gotoxy(35, 7);
scanf("%s", a.make_model);
gotoxy(21, 8);
printf("Chassis #:"); gotoxy(32, 8);
scanf("%s", a.chasis);
gotoxy(21, 9);
printf("Engine #:"); gotoxy(31, 9);
scanf("%s", a.engine);
gotoxy(21, 10);
printf("Availability:"); gotoxy(35, 10);
scanf("%s", &a.avail);
return 1;
}
int checkplate(int t)
{
rewind(fp);
while (fread(&a, sizeof(a), 1, fp) == 1)
if (a.plate == t)
return 0;
return 1;
}
void removecars()
{
system("cls");
system("color 2A");
int c = 0;
int d, e;
int i;
gotoxy(20, 4);
printf("**** Remove cars ****");
char another = 'y';
while (another == 'y')
{
system("cls");
gotoxy(15, 6);
printf("Enter Plate # to be removed: ");
scanf("%d", &d);
fp = fopen("car.txt", "rb+");
while (fread(&a, sizeof(a), 1, fp) == 1)
{
if (checkplate(d) == 0)
{
gotoxy(15, 7);
printf("The car is available.");
gotoxy(15, 8);
printf("Plate #: %d", a.plate);
gotoxy(15, 9);
printf("Company: %s", a.company);
gotoxy(15, 10);
printf("Make % Model: %s", a.make_model);
gotoxy(15, 11);
printf("Chassis #: %s", a.chasis);
gotoxy(15, 12);
printf("Engine #: %s", a.engine);
gotoxy(15, 13);
printf("Car Removed: ");
a.avail[0] = 'R';
a.avail[1] = 'E';
a.avail[2] = 'M';
a.avail[3] = 'O';
a.avail[4] = 'V';
a.avail[5] = 'E';
a.avail[6] = 'D';
gotoxy(15, 16);
printf("The car is removed");
fseek(fp, ftell(fp) - sizeof(a), 0);
fwrite(&a, sizeof(a), 1, fp);
fclose(fp);
c = 1;
}
if (c == 0)
{
gotoxy(15, 9);
printf("No record found.");
}
}
gotoxy(15, 17);
printf("Modify another record?(Y/N): ");
fflush(stdin);
another = getch();
if (another == 'n')
mainmenu();
}
}
void searchcars()
{
char findcar;
system("color 2A");
system("cls");
int d;
gotoxy(18, 8);
printf("***************************** Search Cars
*********************************");
gotoxy(20, 10);
printf("\xDB\xDB\xDB\xB2 1. Search By Plate #.");
gotoxy(20, 12);
printf("\xDB\xDB\xDB\xB2 2. Search By Company.");
gotoxy(20, 16);
printf("Press backspace to return to main menu.");
gotoxy(20, 18);
printf("Enter Your Choice: ");
fp = fopen("car.txt", "rb+"); //open file for reading propose
rewind(fp); //move pointer at the begining of file
switch (getch())
{
case '1':
{
system("cls");
gotoxy(25, 4);
printf("**** Search Cars By Plate# ****");
gotoxy(20, 5);
printf("Enter the Plate #: ");
scanf("%d", &d);
gotoxy(20, 7);
printf("Searching........");
while (fread(&a, sizeof(a), 1, fp) == 1)
{
if (a.plate == d)
{
delay(2);
gotoxy(20, 7);
printf("The car is available");
gotoxy(20, 8);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
gotoxy(20, 9);
printf("\xB2 Plate #: %d", a.plate);
gotoxy(47, 9); printf("\xB2");
gotoxy(20, 10);
printf("\xB2 Company: %s", a.company);
gotoxy(47, 10); printf("\xB2");
gotoxy(20, 11);
printf("\xB2 Make & Model: %s ",
a.make_model); gotoxy(47, 11); printf("\xB2");
gotoxy(20, 12);
printf("\xB2 Chassis #: %s ", a.chasis);
gotoxy(47, 12); printf("\xB2"); gotoxy(47, 11); printf("\xB2");
gotoxy(20, 13);
printf("\xB2 Engine #: %s", a.engine);
gotoxy(47, 13); printf("\xB2");
gotoxy(20, 14);
printf("\xB2 Availability: %s ", a.avail);
gotoxy(47, 14); printf("\xB2");
gotoxy(20, 15);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
findcar = 't';
}
}
if (findcar != 't') //checks whether conditiion enters
inside loop or not
{
gotoxy(20, 8);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2\xB2\xB2");
gotoxy(20, 9); printf("\xB2"); gotoxy(38, 9);
printf("\xB2");
gotoxy(20, 10);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2\xB2\xB2");
gotoxy(22, 9); printf("\aNo Record Found");
}
gotoxy(20, 17);
printf("Try another search?(Y/N): ");
if (getch() == 'y')
searchcars();
else
mainmenu();
break;
}
case '2':
{
char s[15];
system("cls");
gotoxy(25, 4);
printf("**** Search Cars By Company ****");
gotoxy(20, 5);
printf("Enter Company Name: ");
scanf("%s", s);
int d = 0;
int j = 10;
fp = fopen("car.txt", "rb");
while (fread(&a, sizeof(a), 1, fp) == 1)
{
if (strcmp(a.company, (s)) == 0) //checks whether
a.name is equal to s or not
{
gotoxy(20, 7);
printf("Search results ");
gotoxy(3, 8);
printf("Plate # Company Make &
Model Chassis # Engine # Availability ");
gotoxy(3, j);
printf("%d", a.plate);
gotoxy(15, j);
printf("%s", a.company);
gotoxy(26, j);
printf("%s", a.make_model);
gotoxy(47, j);
printf("%s", a.chasis);
gotoxy(53, j);
printf("%s", a.engine);
gotoxy(76, j);
printf("%s", a.avail);
j++;
d++;
}
}
if (d == 0)
{
gotoxy(20, 8);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2\xB2\xB2");
gotoxy(20, 9); printf("\xB2"); gotoxy(38, 9);
printf("\xB2");
gotoxy(20, 10);
printf("\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB
2\xB2\xB2\xB2");
gotoxy(22, 9); printf("\aNo Record Found");
}
gotoxy(20, j + 2);
printf("Try another search?(Y/N): ");
if (getch() == 'y')
searchcars();
else
mainmenu();
break;
}
case 8:
{
mainmenu();
}
default:
getch();
searchcars();
}
fclose(fp);
}
void editlist()
{
system("cls");
system("color 2A");
int c = 0;
int d, e;
gotoxy(20, 4);
printf("**** Edit Car Availability ****");
char another = 'y';
while (another == 'y')
{
system("cls");
gotoxy(15, 6);
printf("Enter Plate # to be edited: ");
scanf("%d", &d);
fp = fopen("car.txt", "rb+");
while (fread(&a, sizeof(a), 1, fp) == 1)
{
if (checkplate(d) == 0)
{
gotoxy(15, 7);
printf("The car is available.");
gotoxy(15, 8);
printf("Plate #: %d", a.plate);
gotoxy(15, 9);
printf("Company: %s", a.company);
gotoxy(15, 10);
printf("Make % Model: %s", a.make_model);
gotoxy(15, 11);
printf("Chassis #: %s", a.chasis);
gotoxy(15, 12);
printf("Engine #: %s", a.engine);
gotoxy(15, 13);
printf("Update availability info: ");
scanf("%s", &a.avail);
gotoxy(15, 16);
printf("The record is modified");
fseek(fp, ftell(fp) - sizeof(a), 0);
fwrite(&a, sizeof(a), 1, fp);
fclose(fp);
c = 1;
}
if (c == 0)
{
gotoxy(15, 9);
printf("No record found.");
}
}
gotoxy(15, 17);
printf("Modify another record?(Y/N): ");
fflush(stdin);
another = getch();
if (another == 'n')
mainmenu();
}
}
void carlist()
{
int j = 4;
system("cls");
system(" color 3B ");
gotoxy(1, 1);
printf(" ************************************ Car List
*************************************");
gotoxy(3, 2);
printf("Plate # Company Make & Model Chassis #
Engine # Availability ");
fp = fopen("car.txt", "rb");
while (fread(&a, sizeof(a), 1, fp) == 1)
{
gotoxy(3, j);
printf("%d", a.plate);
gotoxy(15, j);
printf("%s", a.company);
gotoxy(26, j);
printf("%s", a.make_model);
gotoxy(47, j);
printf("%s", a.chasis);
gotoxy(63, j);
printf("%s", a.engine);
gotoxy(76, j);
printf("%s", a.avail);
j++;
}
printf("\n\n\n Press enter to return to main menu.");
if (getchar())
mainmenu();
}
