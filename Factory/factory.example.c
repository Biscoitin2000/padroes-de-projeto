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

EmailNotification* createEmailNotification() {
    EmailNotification* email = (EmailNotification*)malloc(sizeof(EmailNotification));
    email->base.send = sendEmail;
    return email;
}

Notification* createNotification(const char* type) {
    if (strcmp(type, "SMS") == 0) {
        return (Notification*)createSMSNotification();
    } else if (strcmp(type, "Email") == 0) {
        return (Notification*)createEmailNotification();
    }
    return NULL;
}

