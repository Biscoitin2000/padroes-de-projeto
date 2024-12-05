#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Definição da interface para notificações
typedef struct Notification {
    void (*send)(struct Notification*, const char* message);
} Notification;
