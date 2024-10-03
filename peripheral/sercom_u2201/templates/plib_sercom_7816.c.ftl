<#--
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
-->
<#if USART_7816_ENABLE == true>
<#if core.PORT_API_PREFIX??>
<#assign PLIB_NAME  = core.PORT_API_PREFIX?string>
<#assign PLIB_NAME_LC  = core.PORT_API_PREFIX?lower_case>

<#assign RESET_PIN = PLIB_NAME + "_PIN_" + USART_7816_RESET>
<#assign VCC_SUPPLY_PIN = PLIB_NAME + "_PIN_" + USART_7816_VCC_ENABLE>
<#assign CARD_DETECT_PIN = PLIB_NAME + "_PIN_" + USART_7816_CARD_DETECT>
</#if>
</#if>

<#if (USART_7816_ENABLE == true) && (USART_7816_RESET != "SYS_PORT_PIN_NONE")>
void ${SERCOM_INSTANCE_NAME}_iso7816_icc_power_on( void )
{
    ${PLIB_NAME}_PinWrite(${RESET_PIN}, true);
}

void ${SERCOM_INSTANCE_NAME}_iso7816_icc_power_off( void )
{
    ${PLIB_NAME}_PinWrite(${RESET_PIN}, false);
}
</#if>

<#if (USART_7816_ENABLE == true) && (USART_7816_CARD_DETECT != "SYS_PORT_PIN_NONE")>
bool ${SERCOM_INSTANCE_NAME}_iso7816_card_detect(void)
{
    if(${PLIB_NAME}_PinRead(${CARD_DETECT_PIN}) == true){
        return true;
    }else{
        return false;
    }
}
</#if>

<#if (USART_7816_ENABLE == true) && (USART_7816_VCC_ENABLE != "SYS_PORT_PIN_NONE")>
void ${SERCOM_INSTANCE_NAME}_iso7816_vcc_enable( void )
{
    ${PLIB_NAME}_PinWrite(${VCC_SUPPLY_PIN}, true);
}

void ${SERCOM_INSTANCE_NAME}_iso7816_vcc_disable( void )
{
    ${PLIB_NAME}_PinWrite(${VCC_SUPPLY_PIN}, false);
}
</#if>

<#if (USART_7816_ENABLE == true)>
static uint32_t receive_timeoutcount(void)
{
    return ((CPU_CLOCK_FREQUENCY/OUTPUT_CLOCK)*40000U);
}

static uint32_t reset_waitcount(void)
{
    return ((CPU_CLOCK_FREQUENCY/OUTPUT_CLOCK)*400U);
}
</#if>

<#if (USART_7816_ENABLE == true) && (USART_7816_RESET != "PORT_PIN_NONE")>
void ${SERCOM_INSTANCE_NAME}_iso7816_cold_reset(void)
{
    uint32_t i, rst_wait_time;

    rst_wait_time = reset_waitcount();

    /* tb: wait 400 cycles */
    for (i = 0; i < rst_wait_time; i++) {
    }

    //Read all the leftover data from card
    while(${SERCOM_INSTANCE_NAME}_USART_ReadByte() != 0){
    }

    //usart_reset_status(ISO7816_USART);

    /*ISO7816 reset iterations*/
    if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_ITER_Msk) != 0U)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS |= SERCOM_USART_INT_STATUS_ITER_Msk;
    }

    //Enable Reset pin to high
    ${SERCOM_INSTANCE_NAME}_iso7816_icc_power_on();
}

void ${SERCOM_INSTANCE_NAME}_iso7816_warm_reset(void)
{
    uint32_t count, rst_wait_time;

    rst_wait_time = reset_waitcount();

    //Enable Reset pin to high
    ${SERCOM_INSTANCE_NAME}_iso7816_icc_power_off();

    /* tb: wait 400 cycles */
    for (count = 0; count < rst_wait_time; count++) {
    }

    //Read all the leftover data from card
    while(${SERCOM_INSTANCE_NAME}_USART_ReadByte() != 0){
    }

    //usart_reset_status(ISO7816_USART);

    /*ISO7816 reset iterations*/
    if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_ITER_Msk) != 0U)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS |= SERCOM_USART_INT_STATUS_ITER_Msk;
    }

    //Enable Reset pin to high
    ${SERCOM_INSTANCE_NAME}_iso7816_icc_power_on();
}
</#if>

void ${SERCOM_INSTANCE_NAME}_iso7816_decode_atr(uint8_t *p_atr)
{
    uint32_t index;
    uint8_t j, y, HB_count, uc_offset;

    index = 2;

    /*Interface Bytes*/
    y = p_atr[1] & 0xF0U;

    /* Read ATR Ti. */
    uc_offset = 1;
    while (y != 0U) {
        if ((y & 0x10U) == 0X10U) { /* TA[i] */
            index++;
        }
        if ((y & 0x20U) == 0X20U){ /* TB[i] */
            index++;
        }
        if ((y & 0x40U) == 0X40U) { /* TC[i] */
            index++;
        }
        if ((y & 0x80U) == 0X80U) { /* TD[i] */
            y = p_atr[index++] & 0xF0U;
        } else {
            y = 0;
        }
        uc_offset++;
    }

    /*Historical Bytes*/
    HB_count = p_atr[1] & 0x0FU;
    for (j = 0; j < HB_count; j++) {
        index++;
    }
}

static uint8_t ${SERCOM_INSTANCE_NAME}_iso7816_get_char(uint8_t *p_char_received)
{
    uint32_t timeout = 0, rx_timeout;

    rx_timeout = receive_timeoutcount();

    if (usart_state == USART_SEND)
    {
        while (${SERCOM_INSTANCE_NAME}_USART_TransmitComplete() != true){
        }

        ${SERCOM_INSTANCE_NAME}_USART_TransmitterDisable();

        /*ISO7816 reset iterations*/
        if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_ITER_Msk) != 0U)
        {
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS |= SERCOM_USART_INT_STATUS_ITER_Msk;
        }

        ${SERCOM_INSTANCE_NAME}_USART_ReceiverEnable();

        usart_state = USART_RCV;
    }

    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) == 0U)
    {
        if (timeout++ > rx_timeout) {
            return (0);
        }
    }

    *p_char_received = (uint8_t)${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA;

    return (1);

}

static void ${SERCOM_INSTANCE_NAME}_iso7816_send_char(uint8_t uc_char)
{

    if (usart_state == USART_RCV)
    {
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & SERCOM_USART_INT_INTFLAG_RXC_Msk) != 0U)
        {
            (void)${SERCOM_INSTANCE_NAME}_USART_ReadByte();
        }

        /*ISO7816 reset iterations*/
        if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & SERCOM_USART_INT_STATUS_ITER_Msk) != 0U)
        {
            ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS |= SERCOM_USART_INT_STATUS_ITER_Msk;
        }

        ${SERCOM_INSTANCE_NAME}_USART_TransmitterEnable();
        usart_state = USART_SEND;
    }

    while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_INTFLAG & (uint8_t)SERCOM_USART_INT_INTFLAG_DRE_Msk) == 0U)
    {
        /* Do nothing */
    }

    ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_DATA = uc_char;

}

uint8_t ${SERCOM_INSTANCE_NAME}_iso7816_data_read_atr( uint8_t *p_atr )
{
    uint8_t j, response_length, uc_value;
    uint8_t status;

    if((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB & SERCOM_USART_INT_CTRLB_TXEN_Msk) == SERCOM_USART_INT_CTRLB_TXEN_Msk)
    {
        ${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_CTRLB &= ~SERCOM_USART_INT_CTRLB_TXEN_Msk;

    /* Wait for sync */
    <#if SERCOM_SYNCBUSY = false>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_STATUS & (uint16_t)SERCOM_USART_INT_STATUS_SYNCBUSY_Msk) == (uint16_t)SERCOM_USART_INT_STATUS_SYNCBUSY_Msk)
        {
            /* Do nothing */
        }
    <#else>
        while((${SERCOM_INSTANCE_NAME}_REGS->USART_INT.SERCOM_SYNCBUSY) != 0U)
        {
            /* Do nothing */
        }
    </#if>

        usart_state = USART_RCV;
    }

    /* Read ATR TS. */
    (void)${SERCOM_INSTANCE_NAME}_iso7816_get_char(&p_atr[0]);

    /* Read ATR T0. */
    status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&p_atr[1]);
    if (status == 0U)
    {
            return 0;
    }

    uc_value = p_atr[1] & 0xF0U;
    response_length = 2;

    /* Read ATR Ti. */
    while (uc_value != 0U) {
        if ((uc_value & 0x10U) == 0x10U) { /* TA[response_length] */
            status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&p_atr[response_length++]);
            if (status == 0U)
            {
                    return 0;
            }
        }

        if ((uc_value & 0x20U) == 0x20U) { /* TB[response_length] */
            status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&p_atr[response_length++]);
            if (status == 0U)
            {
                    return 0;
            }
        }

        if ((uc_value & 0x40U) == 0x40U) { /* TC[response_length] */
            status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&p_atr[response_length++]);
            if (status == 0U)
            {
                    return 0;
            }
        }

        if ((uc_value & 0x80U) == 0X80U) { /* TD[response_length] */
            status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&p_atr[response_length]);
            if (status == 0U)
            {
                    return 0;
            }

            uc_value = p_atr[response_length++] & 0xF0U;
        } else {
            uc_value = 0;
        }
    }

    /* Historical Bytes. */
    uc_value = p_atr[1] & 0x0FU;
    for (j = 0; j < uc_value; j++) {
        status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&p_atr[response_length++]);
        if (status == 0U)
        {
                return 0;
        }
    }

    return (response_length);
}

uint16_t ${SERCOM_INSTANCE_NAME}_iso7816_xfr_block_tpdu( uint8_t *apdu_cmd_buffer, uint8_t *apdu_res_buffer, const size_t apdu_cmd_length )
{
    uint16_t us_ne_nc, cmd_index = 4;
    uint16_t resp_index = 0;
    uint8_t sw1_rcvd = 0, cmd_type, status;
    uint8_t proc_byte, dummy_byte=0;

    ${SERCOM_INSTANCE_NAME}_iso7816_send_char(apdu_cmd_buffer[0]);    /* CLA */
    ${SERCOM_INSTANCE_NAME}_iso7816_send_char(apdu_cmd_buffer[1]);    /* INS */
    ${SERCOM_INSTANCE_NAME}_iso7816_send_char(apdu_cmd_buffer[2]);    /* P1 */
    ${SERCOM_INSTANCE_NAME}_iso7816_send_char(apdu_cmd_buffer[3]);    /* P2 */
    ${SERCOM_INSTANCE_NAME}_iso7816_send_char(apdu_cmd_buffer[4]);    /* P3 */

    /* Handle the four structures of command APDU. */
    switch (apdu_cmd_length)
    {
        case CMD_LEN_4:

            cmd_type = CASE1;
            us_ne_nc = 0;

            break;

        case CMD_LEN_5:

            cmd_type = CASE2;
            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5, only Standard Le */
            if (us_ne_nc == 0U)
            {
                us_ne_nc = 256;
            }
            break;

        case CMD_LEN_6:

            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5, only Standard Lc */
            cmd_type = CASE3;

            break;

        case CMD_LEN_7:

            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5 */
            if (us_ne_nc == 0U)
            {
                cmd_type = CASE2;
                us_ne_nc = ((uint16_t)apdu_cmd_buffer[5] << 8) + (uint16_t)apdu_cmd_buffer[6];          /*Extended Le */
            }
            else
            {
                cmd_type = CASE3;                                                                       /*Standard Lc*/
            }
            break;

        default:

            us_ne_nc = apdu_cmd_buffer[4];                                                              /* C5 */

            if (us_ne_nc == 0U)
            {
                cmd_type = CASE3;
                us_ne_nc = ((uint16_t)apdu_cmd_buffer[5] << 8) + (uint16_t)apdu_cmd_buffer[6];          /*Extended Lc */
            }
            else
            {
                cmd_type = CASE3;                                                                       /*Standard Lc*/
            }

            break;
    }

    /* Handle Procedure Bytes. */
    do{
        /* Dummy Read - Start */
        (void)${SERCOM_INSTANCE_NAME}_iso7816_get_char(&dummy_byte);
        (void)${SERCOM_INSTANCE_NAME}_iso7816_get_char(&dummy_byte);
        (void)${SERCOM_INSTANCE_NAME}_iso7816_get_char(&dummy_byte);
        /* Dummy Read - End */

        status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&proc_byte);
        if(status == 0U)
        {
            return 0;
        }

        /* Handle NULL. */
        if (ISO_NULL_VAL == proc_byte) {
            continue;
        }
        /* Handle sw1. */
        else if (((proc_byte & 0xF0U) == 0x60U) || ((proc_byte & 0xF0U) == 0x90U))
        {
            sw1_rcvd = 1;
        }
        /* Handle INS. */
        else if (apdu_cmd_buffer[1] == proc_byte)
        {
            if (cmd_type == CASE2)
            {
                /* Receive data from card. */
                do {
                    status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&apdu_res_buffer[resp_index]);
                    resp_index++;
                } while (0U != --us_ne_nc);
            }
            else
            {
                /* Send data. */
                do {
                    cmd_index++;
                    ${SERCOM_INSTANCE_NAME}_iso7816_send_char(apdu_cmd_buffer[cmd_index]);
                } while (0U != --us_ne_nc);

                /* Dummy Read - Start */
                status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&dummy_byte);
                status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&dummy_byte);
                /* Dummy Read - End */
            }
        }
        /* Handle INS ^ 0xff. */
        else if ((apdu_cmd_buffer[1] ^ 0xffU) == proc_byte)
        {
            if (cmd_type == CASE2)
            {
                /* receive data from card. */
                status = ${SERCOM_INSTANCE_NAME}_iso7816_get_char(&apdu_res_buffer[resp_index]);
                resp_index++;
            }
            else
            {
                ${SERCOM_INSTANCE_NAME}_iso7816_send_char(apdu_cmd_buffer[cmd_index]);
                cmd_index++;
            }
            us_ne_nc--;
        }
        else
        {
            break;
        }
    } while (us_ne_nc != 0U);

    /* Status Bytes. */
    if (sw1_rcvd == 0U)
    {
        (void)${SERCOM_INSTANCE_NAME}_iso7816_get_char(&apdu_res_buffer[resp_index]);                 /* sw1_rcvd */
        resp_index++;
    }
    else
    {
        apdu_res_buffer[resp_index] = proc_byte;
        resp_index++;
    }
    (void)${SERCOM_INSTANCE_NAME}_iso7816_get_char(&apdu_res_buffer[resp_index]);                     /* SW2 */

    resp_index++;

    return (resp_index);

}
