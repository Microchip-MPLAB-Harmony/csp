# Controller Area Network \(CAN\)

\[/topic/body/align \{"- topic/align "\}\) The CAN controller provides all the features required to implement the serial communication protocol CAN, the CAN specification as referred to by ISO/11898A \(2.0 Part A and 2.0 Part B\) for high speeds and ISO/11519-2 for low speeds. The CAN Controller is able to handle all types of frames \(Data, Remote, Error and Overload\) and achieves a bitrate of 1 Mbit/s. \(align\]

CAN controller accesses are made through configuration registers. 8<br />independent message objects \(mailboxes\) are implemented.

Any mailbox can be programmed as a reception buffer block \(even<br />non-consecutive buffers\). For the reception of defined messages, one or<br />several message objects can be masked without participating in the<br />buffer feature. An interrupt is generated when the buffer is full.<br />According to the mailbox configuration, the first message received can<br />be locked in the CAN controller registers until the application<br />acknowledges it, or this message can be discarded by new received<br />messages.

Any mailbox can be programmed for transmission. Several transmission<br />mailboxes can be enabled in the same time.

**Using The Library**

The CAN library supports the normal mode. The CAN Plib can transfer<br />message in a polling or an interrupt mode.

**CAN normal operation with polling**

The following example shows the CAN normal mode operation with polling<br />implementation.

```c
#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

/* LED Toggle */
#define LED_Toggle() LED_GREEN_Toggle()

void print_menu(void)
{
    printf(" ------------------------------ \r\n");   
    printf(" Press '1' to Transmit message \r\n");
    printf(" Press '2' to Receive message \r\n");
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t user_input = 0;
    uint32_t messageID = 0;
    uint8_t message[8];
    uint8_t messageLength = 0;
    uint32_t status = 0;
    
    uint8_t rx_message[8];
    uint32_t rx_messageID = 0;
    uint8_t rx_messageLength = 0;
    CAN_MSG_RX_ATTRIBUTE msgAttr = CAN_MSG_RX_DATA_FRAME;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

    LED_RED_Clear();
    LED_GREEN_Clear();
    LED_BLUE_Clear();

    printf(" ------------------------------ \r\n");
    printf("            CAN Demo            \r\n");
    printf(" ------------------------------ \r\n");
    
    print_menu();
    
    /* Prepare the message to send*/
    messageID = 0x469;
    messageLength = 8;
    for (uint8_t count = 8; count >=1; count--){
        message[count - 1] = count;
    }
    
    while ( true )
    {
        /* Maintain state machines of all polled Harmony modules. */
        scanf("%c", (char *) &user_input);
        
        switch (user_input)
        {
            case '1': 
                printf(" Transmitting Message:");
                if (CAN1_MessageTransmit(messageID, messageLength, message, CAN_MAILBOX_DATA_FRAME_TX) == true)
                {    
                    printf("Success \r\n");
                    LED_Toggle();
                }
                else
                {
                    printf("Failed \r\n");
                }             
                break;
            case '2':
                printf(" Waiting for message: \r\n");
                while (true)
                {
                    if (CAN1_InterruptGet(CAN_INTERRUPT_MB1_MASK))
                    {
                        /* Check CAN Status */
                        status = CAN1_ErrorGet();

                        if ((status & (CAN_ERROR_BOFF | CAN_ERROR_CERR |
                                        CAN_ERROR_SERR | CAN_ERROR_AERR |
                                        CAN_ERROR_FERR | CAN_ERROR_BERR)) == CAN_ERROR_NONE)
                        {
                            memset(rx_message, 0x00, sizeof(rx_message));
                            
                            /* Receive New Message */
                            if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE, &msgAttr) == true)  
                            {
                                printf(" New Message Received    \r\n");
                                status = CAN1_ErrorGet();
                                if ((status & (CAN_ERROR_BOFF | CAN_ERROR_CERR |
                                               CAN_ERROR_SERR | CAN_ERROR_AERR |
                                               CAN_ERROR_FERR | CAN_ERROR_BERR)) == CAN_ERROR_NONE)
                                {
                                    /* Print message to Console */
                                    uint8_t length = rx_messageLength;
                                    printf(" Message - ID : 0x%x Length : 0x%x ", (unsigned int) rx_messageID,(unsigned int) rx_messageLength);
                                    printf("Message : ");
                                    while(length)
                                    {
                                        printf("0x%x ", rx_message[rx_messageLength - length--]);
                                    }
                                    printf("\r\n");
                                    LED_Toggle();
                                    break;
                                }
                                else
                                {
                                    printf("Error in received message");
                                }
                            }
                            else
                            {
                                printf("Message Reception Failed \r");
                            }
                        }
                        else
                        {
                            printf("Error in last received message");
                        }
                    }
                }
                break;
            default:
                printf(" Invalid Input \r\n");
                break;
        }
        
        print_menu();
        
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**CAN normal operation with interrupt**

The following example shows the CAN normal mode operation with<br />interrupt implementation.

```c
#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

/* Application's state machine enum */
typedef enum
{
    APP_STATE_CAN_RECEIVE,
    APP_STATE_CAN_TRANSMIT,
    APP_STATE_CAN_IDLE,
    APP_STATE_CAN_USER_INPUT,
    APP_STATE_CAN_XFER_SUCCESSFUL,
    APP_STATE_CAN_XFER_ERROR
} APP_STATES;

/* LED Toggle */
#define LED_Toggle() LED_GREEN_Toggle()

/* Variable to save application state */
static APP_STATES state = APP_STATE_CAN_USER_INPUT;
/* Variable to save Tx/Rx transfer status and context */
static uint32_t status = 0;
static uint32_t xferContext = 0;
/* Variable to save Tx/Rx message */
static uint32_t messageID = 0;
static uint8_t message[8];
static uint8_t messageLength = 0;
static uint8_t rx_message[8];
static uint32_t rx_messageID = 0;
static uint8_t rx_messageLength = 0;
static CAN_MSG_RX_ATTRIBUTE msgAttr = CAN_MSG_RX_DATA_FRAME;

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

/* This function will be called by CAN PLIB when transfer is completed */
// *****************************************************************************
/* void APP_CAN_Callback(uintptr_t context)

  Summary:
    Function called by CAN PLIB upon transfer completion

  Description:
    This function will be called by CAN PLIB when transfer is completed.
    In this function, current state of the application is obtained by context
    parameter. Based on current state of the application and CAN error
    state, next state of the application is decided.

  Remarks:
    None.
*/
void APP_CAN_Callback(uintptr_t context)
{
    xferContext = context;

    /* Check CAN Status */
    status = CAN1_ErrorGet();

    if ((status & (CAN_ERROR_BOFF | CAN_ERROR_CERR |
                   CAN_ERROR_SERR | CAN_ERROR_AERR |
                   CAN_ERROR_FERR | CAN_ERROR_BERR)) == CAN_ERROR_NONE)
    {
        switch ((APP_STATES)context)
        {
            case APP_STATE_CAN_RECEIVE:
            case APP_STATE_CAN_TRANSMIT:
            {
                state = APP_STATE_CAN_XFER_SUCCESSFUL;
                break;
            }
            default:
                break;
        }
    }
    else
    {
        state = APP_STATE_CAN_XFER_ERROR;
    }
}

void print_menu(void)
{
    printf(" ------------------------------ \r\n");   
    printf(" Press '1' to Transmit message \r\n");
    printf(" Press '2' to Receive message \r\n");
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint8_t user_input = 0;
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    LED_RED_Clear();
    LED_GREEN_Clear();
    LED_BLUE_Clear();

    printf(" ------------------------------ \r\n");
    printf("            CAN Demo            \r\n");
    printf(" ------------------------------ \r\n");
    
    print_menu();
    
    /* Prepare the message to send*/
    messageID = 0x469;
    messageLength = 8;
    for (uint8_t count = 8; count >=1; count--){
        message[count - 1] = count;
    }
    
    while ( true )
    {
        if (state == APP_STATE_CAN_USER_INPUT)
        {
            /* Read user input */
            scanf("%c", (char *) &user_input);
            
            switch (user_input)
            {
                case '1': 
                    printf(" Transmitting Message:");
                    CAN1_TxCallbackRegister( APP_CAN_Callback, (uintptr_t)APP_STATE_CAN_TRANSMIT, CAN_MAILBOX_DATA_FRAME_TX );
                    state = APP_STATE_CAN_IDLE;
                    if (CAN1_MessageTransmit(messageID, messageLength, message, CAN_MAILBOX_DATA_FRAME_TX) == false)
                    {
                        printf("CAN1_MessageTransmit request has failed\r\n");
                    }             
                    break;
                case '2':
                    printf(" Waiting for message: \r\n");
                    CAN1_RxCallbackRegister( APP_CAN_Callback, (uintptr_t)APP_STATE_CAN_RECEIVE, CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE );
                    state = APP_STATE_CAN_IDLE;
                    memset(rx_message, 0x00, sizeof(rx_message));
                    /* Receive New Message */
                    if (CAN1_MessageReceive(&rx_messageID, &rx_messageLength, rx_message, 0, CAN_MAILBOX_DATA_FRAME_RX_OVERWRITE, &msgAttr) == false)  
                    {
                        printf("CAN1_MessageReceive request has failed\r\n");
                    }
                    break;
                default:
                    printf(" Invalid Input \r\n");
                    break;
            }
        }
        /* Check the application's current state. */
        switch (state)
        {
            case APP_STATE_CAN_IDLE:
            {
                /* Application can do other task here */
                break;
            }
            case APP_STATE_CAN_XFER_SUCCESSFUL:
            {
                if ((APP_STATES)xferContext == APP_STATE_CAN_RECEIVE)
                {
                    /* Print message to Console */
                    printf(" New Message Received    \r\n");
                    uint8_t length = rx_messageLength;
                    printf(" Message - ID : 0x%x Length : 0x%x ", (unsigned int) rx_messageID,(unsigned int) rx_messageLength);
                    printf("Message : ");
                    while(length)
                    {
                        printf("0x%x ", rx_message[rx_messageLength - length--]);
                    }
                    printf("\r\n");
                } 
                else if ((APP_STATES)xferContext == APP_STATE_CAN_TRANSMIT)
                {
                    printf("Success \r\n");
                }
                LED_Toggle();
                print_menu();
                state = APP_STATE_CAN_USER_INPUT;
                break;
            }
            case APP_STATE_CAN_XFER_ERROR:
            {
                if ((APP_STATES)xferContext == APP_STATE_CAN_RECEIVE)
                {
                    printf("Error in received message");
                }
                else
                {
                    printf("Failed \r\n");
                }
                print_menu();
                state = APP_STATE_CAN_USER_INPUT;
                break;
            }
            default:
                break;
        }
        
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Library Interface**

Controller Area Network peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|CANx\_Initialize|Initializes given instance of the CAN peripheral|
|CANx\_MessageTransmit|Transmits a message into CAN bus|
|CANx\_MessageReceive|Receives a message from CAN bus|
|CANx\_MessageAbort|Abort request for a Mailbox|
|CANx\_MessageIDSet|Set Message ID in mailbox|
|CANx\_MessageIDGet|Get Message ID from mailbox|
|CANx\_MessageAcceptanceMaskSet|Set Message acceptance identifier mask in mailbox|
|CANx\_MessageAcceptanceMaskGet|Get Message acceptance identifier mask from mailbox|
|CANx\_MessageTimestampGet|Get the message timestamp from a mailbox|
|CANx\_ErrorGet|Returns the error during transfer|
|CANx\_ErrorCountGet|Returns the transmit and receive error count during transfer|
|CANx\_InterruptGet|Returns the Interrupt status|
|CANx\_InterruptEnable|Enables CAN Interrupt|
|CANx\_InterruptDisable|Disables CAN Interrupt|
|CANx\_MailboxIsReady|Returns true if Mailbox is ready otherwise false|
|CANx\_TxCallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the given CAN's Tx transfer events occur|
|CANx\_RxCallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the given CAN's Rx transfer events occur|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|CAN\_MAILBOX\_TX\_ATTRIBUTE|Enum|CAN Mailbox TX Attribute for Transmit mailbox, Producer Tx Mailbox and Consumer Tx Mailbox|
|CAN\_MAILBOX\_RX\_ATTRIBUTE|Enum|CAN Mailbox RX Attribute for Reception Mailbox, Reception Mailbox with overwrite, Consumer Rx Mailbox and Producer Rx Mailbox|
|CAN\_MSG\_RX\_ATTRIBUTE|Enum|CAN Message RX Attribute for Data Frame and Remote Frame|
|CAN\_MAILBOX\_NUM|Enum|CAN Mailbox Number|
|CAN\_MAILBOX\_MASK|Enum|CAN Mailbox Mask|
|CAN\_ERROR|Enum|CAN Transfer Error data type|
|CAN\_INTERRUPT\_MASK|Enum|CAN Interrupt Mask|
|CAN\_MAILBOX\_STATE|Enum|CAN Mailbox State|
|CAN\_CALLBACK|Typedef|CAN Callback Function Pointer|
|CAN\_RX\_MSG|Struct|CAN PLib Object structure|
|CAN\_MAILBOX\_CALLBACK|Struct|CAN transfer event callback structure|

-   **[CANx\_Initialize Function](GUID-3E146A1F-2790-4E35-9A57-92D94CDA1B7A.md)**  

-   **[CANx\_MessageTransmit Function](GUID-F8FB08F1-1020-4E0E-B699-D668F76EE4CC.md)**  

-   **[CANx\_MessageReceive Function](GUID-AB451CE2-D96C-445A-8F97-8B9565AB2BF7.md)**  

-   **[CANx\_MessageAbort Function](GUID-4E46CDAF-9154-41A4-A3E5-F3534521CF18.md)**  

-   **[CANx\_MessageIDSet Function](GUID-881C1657-399B-4FCC-BD1B-7D538C9642DA.md)**  

-   **[CANx\_MessageIDGet Function](GUID-75E7AC5C-B28E-42F7-A680-3D545011FCB0.md)**  

-   **[CANx\_MessageAcceptanceMaskSet Function](GUID-967DDBA6-A71B-423D-87D7-B87797AF72B7.md)**  

-   **[CANx\_MessageAcceptanceMaskGet Function](GUID-4F5A48D4-3659-46F7-BA84-F455B5E7B60B.md)**  

-   **[CANx\_MessageTimestampGet Function](GUID-48B0DA32-7EA1-415E-928A-78925C64AE2A.md)**  

-   **[CANx\_ErrorGet Function](GUID-132D09D6-406E-49B7-893E-81AC3DA848DF.md)**  

-   **[CANx\_ErrorCountGet Function](GUID-C47468D6-2A6E-41E6-B936-72567DF52D2B.md)**  

-   **[CANx\_InterruptGet Function](GUID-403171E7-428F-41E9-99DB-0EAF210A1BB4.md)**  

-   **[CANx\_InterruptEnable Function](GUID-CD3C76F0-1201-424D-B74E-06A809072985.md)**  

-   **[CANx\_InterruptDisable Function](GUID-B7BC3C42-0ED4-4AD5-9A14-C25A4BB0DE02.md)**  

-   **[CANx\_MailboxIsReady Function](GUID-C7435509-620C-4036-829B-AE6A1ACF9D20.md)**  

-   **[CANx\_TxCallbackRegister Function](GUID-A945965B-3051-4483-899C-CE2A48E33980.md)**  

-   **[CANx\_RxCallbackRegister Function](GUID-9F45FA79-6B54-4FE4-A22A-C63BE09F5AD7.md)**  

-   **[CAN\_MAILBOX\_TX\_ATTRIBUTE Enum](GUID-508212E8-15D1-464A-AE6B-BF4435A5054D.md)**  

-   **[CAN\_MAILBOX\_RX\_ATTRIBUTE Enum](GUID-7F9573E7-C2C8-42FE-BAF4-9C7A7452AD2A.md)**  

-   **[CAN\_MSG\_RX\_ATTRIBUTE Enum](GUID-20996A65-0DB6-4F9C-8F3E-85FAB957A382.md)**  

-   **[CAN\_MAILBOX\_NUM Enum](GUID-9A78EC61-16AC-4872-9881-2890980D223C.md)**  

-   **[CAN\_MAILBOX\_MASK Enum](GUID-F9934A75-0185-4166-B846-21E5B2F91317.md)**  

-   **[CAN\_ERROR Enum](GUID-3D3073B7-75FE-4ED4-8A1D-BE7E1B6EECFF.md)**  

-   **[CAN\_INTERRUPT\_MASK Enum](GUID-008CE3FF-5278-4CBC-9FE9-01362724FD2E.md)**  

-   **[CAN\_MAILBOX\_STATE Enum](GUID-4170328D-6337-4AF6-ADFC-B7AE08C081F4.md)**  

-   **[CAN\_CALLBACK Typedef](GUID-277F12E1-A067-4703-9CAD-AC4BB3EF3236.md)**  

-   **[CAN\_RX\_MSG Struct](GUID-9A522C44-0D81-49DA-BB12-3A35F47C234F.md)**  

-   **[CAN\_MAILBOX\_CALLBACK Struct](GUID-956110ED-768A-452B-BE64-76E0532E788C.md)**  


**Parent topic:**[SAM 9X60 Peripheral Libraries](GUID-CCAAC7F0-6BA8-4630-91AE-69718D188CBF.md)

