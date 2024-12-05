#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Definição da interface para notificações
typedef struct Notification {
    void (*send)(struct Notification*, const char* message);
} Notification;

typedef struct SMSNotification {
    Notification base;
} SMSNotification;

void sendSMS(Notification* self, const char* message) {
    printf("Enviando SMS: %s\n", message);
}

SMSNotification* createSMSNotification() {
    SMSNotification* sms = (SMSNotification*)malloc(sizeof(SMSNotification));
    sms->base.send = sendSMS;
    return sms;
}

typedef struct EmailNotification {
    Notification base;
} EmailNotification;

void sendEmail(Notification* self, const char* message) {
    printf("Enviando Email: %s\n", message);
}
