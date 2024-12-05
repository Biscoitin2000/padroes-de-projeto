    O padrão Factory é um padrão criacional que fornece uma interface para criar objetos em uma classe-mãe, permitindo que as subclasses alterem o tipo de objetos criados.





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


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

int main() {
    char tipoNotificacao[10];

    printf("Digite o tipo de notificação (SMS/Email): ");
    scanf("%s", tipoNotificacao);

    Notification* notificacao = createNotification(tipoNotificacao);

    if (notificacao) {
        notificacao->send(notificacao, "Olá! Esta é uma mensagem de teste.");
        free(notificacao);
    } else {
        printf("Tipo de notificação inválido!\n");
    }

    return 0;
}
