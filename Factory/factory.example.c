//    O padrão Factory é um padrão criacional que fornece uma interface para criar objetos em uma classe-mãe, permitindo que as subclasses alterem o tipo de objetos criados.
//
//    Resolve problemas de acoplamento reduzindo-os, o cliente depende apenas da interface ou classe base. A Factory abstrai o processo de criação, tornando o cliente independente de implementações concretas.
//    Resolve problema de encapsulamento, encapsula toda a lógica de criação dentro da Factory, deixando o cliente com um código mais simples e limpo.
//
//    Vantagens:
//         --> Facilita a reutilização de código, já que o cliente não precisa conhecer os detalhes das classes concretas.
//         --> Permite adicionar novos produtos facilmente sem modificar o código existente.
//    Desvantagens:
//         --> Pode aumentar a complexidade inicial do código ao introduzir várias classes.
//    
//    Quando usar:
//          Se criar objetos requer lógica complexa, como inicializações, validações ou configurações adicionais. 
//          Se o tipo exato de objeto a ser criado só é conhecido em tempo de execução, com base em entradas do usuário, configuração ou estado.
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
