#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct transaction {
    char date[20];
    char description[100];
    float amount;
    struct transaction *next;
};

struct transaction* addtoempty(struct transaction *head, char *date, char *desc, float amount) {
    struct transaction *temp = malloc(sizeof(struct transaction));
    strcpy(temp->date, date);
    strcpy(temp->description, desc);
    temp->amount = amount;
    temp->next = NULL;
    return temp;
}

struct transaction* addtoend(struct transaction* head, char *date, char *desc, float amount) {
    struct transaction *temp = malloc(sizeof(struct transaction));
    strcpy(temp->date, date);
    strcpy(temp->description, desc);
    temp->amount = amount;
    temp->next = NULL;

    struct transaction* tp = head;
    while (tp->next != NULL) {
        tp = tp->next;
    }
    tp->next = temp;
    return head;
}

struct transaction* createlist(struct transaction* head) {
    int n;
    char des[100], date[20];
    float amount;

    printf("Enter the number of transactions:\n");
    scanf("%d", &n);
    getchar(); // consume leftover newline

    if (n == 0) return head;

    // First transaction
    printf("Enter the DATE (DD-MM-YYYY): ");
    fgets(date, sizeof(date), stdin);
    date[strcspn(date, "\n")] = '\0';

    printf("Enter the DESCRIPTION: ");
    fgets(des, sizeof(des), stdin);
    des[strcspn(des, "\n")] = '\0';

    printf("Enter the AMOUNT: ");
    scanf("%f", &amount);
    getchar(); // consume leftover newline

    head = addtoempty(head, date, des, amount);

    // Remaining transactions
    for (int i = 1; i < n; i++) {
        printf("Enter the DATE (DD-MM-YYYY): ");
        fgets(date, sizeof(date), stdin);
        date[strcspn(date, "\n")] = '\0';

        printf("Enter the DESCRIPTION: ");
        fgets(des, sizeof(des), stdin);
        des[strcspn(des, "\n")] = '\0';

        printf("Enter the AMOUNT: ");
        scanf("%f", &amount);
        getchar(); // consume newline

        head = addtoend(head, date, des, amount);
    }

    return head;
}

void print(struct transaction *head) {
    if (head == NULL) {
        printf("There are no transactions.\n");
    } else {
        struct transaction* temp = head;
        printf("\nDATE\t\tDESCRIPTION\t\tAMOUNT\n");
        printf("------------------------------------------------------\n");
        while (temp != NULL) {
            printf("%-15s %-20s %.2f\n", temp->date, temp->description, temp->amount);
            temp = temp->next;
        }
    }
}

int main() {
    struct transaction *head = NULL;
    head = createlist(head);
    print(head);
    return 0;
}
