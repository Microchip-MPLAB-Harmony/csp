/**
 * \brief Component description for FLEXCOM
 *
 * © 2019 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software and any derivatives
 * exclusively with Microchip products. It is your responsibility to comply with third party license
 * terms applicable to your use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER EXPRESS, IMPLIED OR STATUTORY,
 * APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND
 * FITNESS FOR A PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, INCIDENTAL OR CONSEQUENTIAL
 * LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF
 * MICROCHIP HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE FULLEST EXTENT
 * ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT
 * EXCEED THE AMOUNT OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *
 */

/* file generated from device description version 2019-06-11T20:50:29Z */
#ifndef _SAMRH71_FLEXCOM_COMPONENT_H_
#define _SAMRH71_FLEXCOM_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR FLEXCOM                                      */
/* ************************************************************************** */

/* -------- FLEXCOM_FLEX_MR : (FLEXCOM Offset: 0x00) (R/W 32) FLEXCOM Mode Register -------- */
#define FLEXCOM_FLEX_MR_OPMODE_Pos            _U_(0)                                         /**< (FLEXCOM_FLEX_MR) FLEXCOM Operating Mode Position */
#define FLEXCOM_FLEX_MR_OPMODE_Msk            (_U_(0x3) << FLEXCOM_FLEX_MR_OPMODE_Pos)       /**< (FLEXCOM_FLEX_MR) FLEXCOM Operating Mode Mask */
#define FLEXCOM_FLEX_MR_OPMODE(value)         (FLEXCOM_FLEX_MR_OPMODE_Msk & ((value) << FLEXCOM_FLEX_MR_OPMODE_Pos))
#define   FLEXCOM_FLEX_MR_OPMODE_NO_COM_Val   _U_(0x0)                                       /**< (FLEXCOM_FLEX_MR) No communication  */
#define   FLEXCOM_FLEX_MR_OPMODE_USART_Val    _U_(0x1)                                       /**< (FLEXCOM_FLEX_MR) All UART related protocols are selected (RS232, RS485, IrDA, ISO7816, LIN, LON)SPI/TWI related registers are not accessible and have no impact on IOs.  */
#define   FLEXCOM_FLEX_MR_OPMODE_SPI_Val      _U_(0x2)                                       /**< (FLEXCOM_FLEX_MR) SPI operating mode is selected.USART/TWI related registers are not accessible and have no impact on IOs.  */
#define   FLEXCOM_FLEX_MR_OPMODE_TWI_Val      _U_(0x3)                                       /**< (FLEXCOM_FLEX_MR) All TWI related protocols are selected (TWI, SMBus).USART/SPI related registers are not accessible and have no impact on IOs.  */
#define FLEXCOM_FLEX_MR_OPMODE_NO_COM         (FLEXCOM_FLEX_MR_OPMODE_NO_COM_Val << FLEXCOM_FLEX_MR_OPMODE_Pos) /**< (FLEXCOM_FLEX_MR) No communication Position  */
#define FLEXCOM_FLEX_MR_OPMODE_USART          (FLEXCOM_FLEX_MR_OPMODE_USART_Val << FLEXCOM_FLEX_MR_OPMODE_Pos) /**< (FLEXCOM_FLEX_MR) All UART related protocols are selected (RS232, RS485, IrDA, ISO7816, LIN, LON)SPI/TWI related registers are not accessible and have no impact on IOs. Position  */
#define FLEXCOM_FLEX_MR_OPMODE_SPI            (FLEXCOM_FLEX_MR_OPMODE_SPI_Val << FLEXCOM_FLEX_MR_OPMODE_Pos) /**< (FLEXCOM_FLEX_MR) SPI operating mode is selected.USART/TWI related registers are not accessible and have no impact on IOs. Position  */
#define FLEXCOM_FLEX_MR_OPMODE_TWI            (FLEXCOM_FLEX_MR_OPMODE_TWI_Val << FLEXCOM_FLEX_MR_OPMODE_Pos) /**< (FLEXCOM_FLEX_MR) All TWI related protocols are selected (TWI, SMBus).USART/SPI related registers are not accessible and have no impact on IOs. Position  */
#define FLEXCOM_FLEX_MR_Msk                   _U_(0x00000003)                                /**< (FLEXCOM_FLEX_MR) Register Mask  */


/* -------- FLEXCOM_FLEX_RHR : (FLEXCOM Offset: 0x10) ( R/ 32) FLEXCOM Receive Holding Register -------- */
#define FLEXCOM_FLEX_RHR_RXDATA_Pos           _U_(0)                                         /**< (FLEXCOM_FLEX_RHR) Receive Data Position */
#define FLEXCOM_FLEX_RHR_RXDATA_Msk           (_U_(0xFFFF) << FLEXCOM_FLEX_RHR_RXDATA_Pos)   /**< (FLEXCOM_FLEX_RHR) Receive Data Mask */
#define FLEXCOM_FLEX_RHR_RXDATA(value)        (FLEXCOM_FLEX_RHR_RXDATA_Msk & ((value) << FLEXCOM_FLEX_RHR_RXDATA_Pos))
#define FLEXCOM_FLEX_RHR_Msk                  _U_(0x0000FFFF)                                /**< (FLEXCOM_FLEX_RHR) Register Mask  */


/* -------- FLEXCOM_FLEX_THR : (FLEXCOM Offset: 0x20) (R/W 32) FLEXCOM Transmit Holding Register -------- */
#define FLEXCOM_FLEX_THR_TXDATA_Pos           _U_(0)                                         /**< (FLEXCOM_FLEX_THR) Transmit Data Position */
#define FLEXCOM_FLEX_THR_TXDATA_Msk           (_U_(0xFFFF) << FLEXCOM_FLEX_THR_TXDATA_Pos)   /**< (FLEXCOM_FLEX_THR) Transmit Data Mask */
#define FLEXCOM_FLEX_THR_TXDATA(value)        (FLEXCOM_FLEX_THR_TXDATA_Msk & ((value) << FLEXCOM_FLEX_THR_TXDATA_Pos))
#define FLEXCOM_FLEX_THR_Msk                  _U_(0x0000FFFF)                                /**< (FLEXCOM_FLEX_THR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_CR : (FLEXCOM Offset: 0x200) ( /W 32) USART Control Register -------- */
#define FLEXCOM_FLEX_US_CR_RSTRX_Pos          _U_(2)                                         /**< (FLEXCOM_FLEX_US_CR) Reset Receiver Position */
#define FLEXCOM_FLEX_US_CR_RSTRX_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_RSTRX_Pos)     /**< (FLEXCOM_FLEX_US_CR) Reset Receiver Mask */
#define FLEXCOM_FLEX_US_CR_RSTTX_Pos          _U_(3)                                         /**< (FLEXCOM_FLEX_US_CR) Reset Transmitter Position */
#define FLEXCOM_FLEX_US_CR_RSTTX_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_RSTTX_Pos)     /**< (FLEXCOM_FLEX_US_CR) Reset Transmitter Mask */
#define FLEXCOM_FLEX_US_CR_RXEN_Pos           _U_(4)                                         /**< (FLEXCOM_FLEX_US_CR) Receiver Enable Position */
#define FLEXCOM_FLEX_US_CR_RXEN_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_CR_RXEN_Pos)      /**< (FLEXCOM_FLEX_US_CR) Receiver Enable Mask */
#define FLEXCOM_FLEX_US_CR_RXDIS_Pos          _U_(5)                                         /**< (FLEXCOM_FLEX_US_CR) Receiver Disable Position */
#define FLEXCOM_FLEX_US_CR_RXDIS_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_RXDIS_Pos)     /**< (FLEXCOM_FLEX_US_CR) Receiver Disable Mask */
#define FLEXCOM_FLEX_US_CR_TXEN_Pos           _U_(6)                                         /**< (FLEXCOM_FLEX_US_CR) Transmitter Enable Position */
#define FLEXCOM_FLEX_US_CR_TXEN_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_CR_TXEN_Pos)      /**< (FLEXCOM_FLEX_US_CR) Transmitter Enable Mask */
#define FLEXCOM_FLEX_US_CR_TXDIS_Pos          _U_(7)                                         /**< (FLEXCOM_FLEX_US_CR) Transmitter Disable Position */
#define FLEXCOM_FLEX_US_CR_TXDIS_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_TXDIS_Pos)     /**< (FLEXCOM_FLEX_US_CR) Transmitter Disable Mask */
#define FLEXCOM_FLEX_US_CR_RSTSTA_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_US_CR) Reset Status Bits Position */
#define FLEXCOM_FLEX_US_CR_RSTSTA_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_RSTSTA_Pos)    /**< (FLEXCOM_FLEX_US_CR) Reset Status Bits Mask */
#define FLEXCOM_FLEX_US_CR_STTBRK_Pos         _U_(9)                                         /**< (FLEXCOM_FLEX_US_CR) Start Break Position */
#define FLEXCOM_FLEX_US_CR_STTBRK_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_STTBRK_Pos)    /**< (FLEXCOM_FLEX_US_CR) Start Break Mask */
#define FLEXCOM_FLEX_US_CR_STPBRK_Pos         _U_(10)                                        /**< (FLEXCOM_FLEX_US_CR) Stop Break Position */
#define FLEXCOM_FLEX_US_CR_STPBRK_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_STPBRK_Pos)    /**< (FLEXCOM_FLEX_US_CR) Stop Break Mask */
#define FLEXCOM_FLEX_US_CR_STTTO_Pos          _U_(11)                                        /**< (FLEXCOM_FLEX_US_CR) Clear TIMEOUT Flag and Start Timeout After Next Character Received Position */
#define FLEXCOM_FLEX_US_CR_STTTO_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_STTTO_Pos)     /**< (FLEXCOM_FLEX_US_CR) Clear TIMEOUT Flag and Start Timeout After Next Character Received Mask */
#define FLEXCOM_FLEX_US_CR_SENDA_Pos          _U_(12)                                        /**< (FLEXCOM_FLEX_US_CR) Send Address Position */
#define FLEXCOM_FLEX_US_CR_SENDA_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_SENDA_Pos)     /**< (FLEXCOM_FLEX_US_CR) Send Address Mask */
#define FLEXCOM_FLEX_US_CR_RSTIT_Pos          _U_(13)                                        /**< (FLEXCOM_FLEX_US_CR) Reset Iterations Position */
#define FLEXCOM_FLEX_US_CR_RSTIT_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_RSTIT_Pos)     /**< (FLEXCOM_FLEX_US_CR) Reset Iterations Mask */
#define FLEXCOM_FLEX_US_CR_RSTNACK_Pos        _U_(14)                                        /**< (FLEXCOM_FLEX_US_CR) Reset Non Acknowledge Position */
#define FLEXCOM_FLEX_US_CR_RSTNACK_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_CR_RSTNACK_Pos)   /**< (FLEXCOM_FLEX_US_CR) Reset Non Acknowledge Mask */
#define FLEXCOM_FLEX_US_CR_RETTO_Pos          _U_(15)                                        /**< (FLEXCOM_FLEX_US_CR) Start Timeout Immediately Position */
#define FLEXCOM_FLEX_US_CR_RETTO_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_RETTO_Pos)     /**< (FLEXCOM_FLEX_US_CR) Start Timeout Immediately Mask */
#define FLEXCOM_FLEX_US_CR_RTSEN_Pos          _U_(18)                                        /**< (FLEXCOM_FLEX_US_CR) Request to Send Enable Position */
#define FLEXCOM_FLEX_US_CR_RTSEN_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CR_RTSEN_Pos)     /**< (FLEXCOM_FLEX_US_CR) Request to Send Enable Mask */
#define FLEXCOM_FLEX_US_CR_RTSDIS_Pos         _U_(19)                                        /**< (FLEXCOM_FLEX_US_CR) Request to Send Disable Position */
#define FLEXCOM_FLEX_US_CR_RTSDIS_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_RTSDIS_Pos)    /**< (FLEXCOM_FLEX_US_CR) Request to Send Disable Mask */
#define FLEXCOM_FLEX_US_CR_LINABT_Pos         _U_(20)                                        /**< (FLEXCOM_FLEX_US_CR) Abort LIN Transmission Position */
#define FLEXCOM_FLEX_US_CR_LINABT_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_LINABT_Pos)    /**< (FLEXCOM_FLEX_US_CR) Abort LIN Transmission Mask */
#define FLEXCOM_FLEX_US_CR_LINWKUP_Pos        _U_(21)                                        /**< (FLEXCOM_FLEX_US_CR) Send LIN Wakeup Signal Position */
#define FLEXCOM_FLEX_US_CR_LINWKUP_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_CR_LINWKUP_Pos)   /**< (FLEXCOM_FLEX_US_CR) Send LIN Wakeup Signal Mask */
#define FLEXCOM_FLEX_US_CR_TXFCLR_Pos         _U_(24)                                        /**< (FLEXCOM_FLEX_US_CR) Transmit FIFO Clear Position */
#define FLEXCOM_FLEX_US_CR_TXFCLR_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_TXFCLR_Pos)    /**< (FLEXCOM_FLEX_US_CR) Transmit FIFO Clear Mask */
#define FLEXCOM_FLEX_US_CR_RXFCLR_Pos         _U_(25)                                        /**< (FLEXCOM_FLEX_US_CR) Receive FIFO Clear Position */
#define FLEXCOM_FLEX_US_CR_RXFCLR_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_RXFCLR_Pos)    /**< (FLEXCOM_FLEX_US_CR) Receive FIFO Clear Mask */
#define FLEXCOM_FLEX_US_CR_TXFLCLR_Pos        _U_(26)                                        /**< (FLEXCOM_FLEX_US_CR) Transmit FIFO Lock CLEAR Position */
#define FLEXCOM_FLEX_US_CR_TXFLCLR_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_CR_TXFLCLR_Pos)   /**< (FLEXCOM_FLEX_US_CR) Transmit FIFO Lock CLEAR Mask */
#define FLEXCOM_FLEX_US_CR_REQCLR_Pos         _U_(28)                                        /**< (FLEXCOM_FLEX_US_CR) Request to Clear the Comparison Trigger Position */
#define FLEXCOM_FLEX_US_CR_REQCLR_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_REQCLR_Pos)    /**< (FLEXCOM_FLEX_US_CR) Request to Clear the Comparison Trigger Mask */
#define FLEXCOM_FLEX_US_CR_FIFOEN_Pos         _U_(30)                                        /**< (FLEXCOM_FLEX_US_CR) FIFO Enable Position */
#define FLEXCOM_FLEX_US_CR_FIFOEN_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CR_FIFOEN_Pos)    /**< (FLEXCOM_FLEX_US_CR) FIFO Enable Mask */
#define FLEXCOM_FLEX_US_CR_FIFODIS_Pos        _U_(31)                                        /**< (FLEXCOM_FLEX_US_CR) FIFO Disable Position */
#define FLEXCOM_FLEX_US_CR_FIFODIS_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_CR_FIFODIS_Pos)   /**< (FLEXCOM_FLEX_US_CR) FIFO Disable Mask */
#define FLEXCOM_FLEX_US_CR_Msk                _U_(0xD73CFFFC)                                /**< (FLEXCOM_FLEX_US_CR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_MR : (FLEXCOM Offset: 0x204) (R/W 32) USART Mode Register -------- */
#define FLEXCOM_FLEX_US_MR_USART_MODE_Pos     _U_(0)                                         /**< (FLEXCOM_FLEX_US_MR) USART Mode of Operation Position */
#define FLEXCOM_FLEX_US_MR_USART_MODE_Msk     (_U_(0xF) << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) USART Mode of Operation Mask */
#define FLEXCOM_FLEX_US_MR_USART_MODE(value)  (FLEXCOM_FLEX_US_MR_USART_MODE_Msk & ((value) << FLEXCOM_FLEX_US_MR_USART_MODE_Pos))
#define   FLEXCOM_FLEX_US_MR_USART_MODE_NORMAL_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MR) Normal mode  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_RS485_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MR) RS485  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_HW_HANDSHAKING_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MR) Hardware handshaking  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_IS07816_T_0_Val _U_(0x4)                                       /**< (FLEXCOM_FLEX_US_MR) IS07816 Protocol: T = 0  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_IS07816_T_1_Val _U_(0x6)                                       /**< (FLEXCOM_FLEX_US_MR) IS07816 Protocol: T = 1  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_IRDA_Val _U_(0x8)                                       /**< (FLEXCOM_FLEX_US_MR) IrDA  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_LON_Val _U_(0x9)                                       /**< (FLEXCOM_FLEX_US_MR) LON  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_LIN_MASTER_Val _U_(0xA)                                       /**< (FLEXCOM_FLEX_US_MR) LIN Master mode  */
#define   FLEXCOM_FLEX_US_MR_USART_MODE_LIN_SLAVE_Val _U_(0xB)                                       /**< (FLEXCOM_FLEX_US_MR) LIN Slave mode  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_NORMAL  (FLEXCOM_FLEX_US_MR_USART_MODE_NORMAL_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) Normal mode Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_RS485   (FLEXCOM_FLEX_US_MR_USART_MODE_RS485_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) RS485 Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_HW_HANDSHAKING (FLEXCOM_FLEX_US_MR_USART_MODE_HW_HANDSHAKING_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) Hardware handshaking Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_IS07816_T_0 (FLEXCOM_FLEX_US_MR_USART_MODE_IS07816_T_0_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) IS07816 Protocol: T = 0 Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_IS07816_T_1 (FLEXCOM_FLEX_US_MR_USART_MODE_IS07816_T_1_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) IS07816 Protocol: T = 1 Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_IRDA    (FLEXCOM_FLEX_US_MR_USART_MODE_IRDA_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) IrDA Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_LON     (FLEXCOM_FLEX_US_MR_USART_MODE_LON_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) LON Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_LIN_MASTER (FLEXCOM_FLEX_US_MR_USART_MODE_LIN_MASTER_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) LIN Master mode Position  */
#define FLEXCOM_FLEX_US_MR_USART_MODE_LIN_SLAVE (FLEXCOM_FLEX_US_MR_USART_MODE_LIN_SLAVE_Val << FLEXCOM_FLEX_US_MR_USART_MODE_Pos) /**< (FLEXCOM_FLEX_US_MR) LIN Slave mode Position  */
#define FLEXCOM_FLEX_US_MR_USCLKS_Pos         _U_(4)                                         /**< (FLEXCOM_FLEX_US_MR) Clock Selection Position */
#define FLEXCOM_FLEX_US_MR_USCLKS_Msk         (_U_(0x3) << FLEXCOM_FLEX_US_MR_USCLKS_Pos)    /**< (FLEXCOM_FLEX_US_MR) Clock Selection Mask */
#define FLEXCOM_FLEX_US_MR_USCLKS(value)      (FLEXCOM_FLEX_US_MR_USCLKS_Msk & ((value) << FLEXCOM_FLEX_US_MR_USCLKS_Pos))
#define   FLEXCOM_FLEX_US_MR_USCLKS_MCK_Val   _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MR) Peripheral clock is selected  */
#define   FLEXCOM_FLEX_US_MR_USCLKS_DIV_Val   _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MR) Peripheral clock divided (DIV = 8) is selected  */
#define   FLEXCOM_FLEX_US_MR_USCLKS_GCLK_Val  _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MR) PMC generic clock is selected. If the SCK pin is driven (CLKO = 1), the CD field must be greater than 1.  */
#define   FLEXCOM_FLEX_US_MR_USCLKS_SCK_Val   _U_(0x3)                                       /**< (FLEXCOM_FLEX_US_MR) External pin SCK is selected  */
#define FLEXCOM_FLEX_US_MR_USCLKS_MCK         (FLEXCOM_FLEX_US_MR_USCLKS_MCK_Val << FLEXCOM_FLEX_US_MR_USCLKS_Pos) /**< (FLEXCOM_FLEX_US_MR) Peripheral clock is selected Position  */
#define FLEXCOM_FLEX_US_MR_USCLKS_DIV         (FLEXCOM_FLEX_US_MR_USCLKS_DIV_Val << FLEXCOM_FLEX_US_MR_USCLKS_Pos) /**< (FLEXCOM_FLEX_US_MR) Peripheral clock divided (DIV = 8) is selected Position  */
#define FLEXCOM_FLEX_US_MR_USCLKS_GCLK        (FLEXCOM_FLEX_US_MR_USCLKS_GCLK_Val << FLEXCOM_FLEX_US_MR_USCLKS_Pos) /**< (FLEXCOM_FLEX_US_MR) PMC generic clock is selected. If the SCK pin is driven (CLKO = 1), the CD field must be greater than 1. Position  */
#define FLEXCOM_FLEX_US_MR_USCLKS_SCK         (FLEXCOM_FLEX_US_MR_USCLKS_SCK_Val << FLEXCOM_FLEX_US_MR_USCLKS_Pos) /**< (FLEXCOM_FLEX_US_MR) External pin SCK is selected Position  */
#define FLEXCOM_FLEX_US_MR_CHRL_Pos           _U_(6)                                         /**< (FLEXCOM_FLEX_US_MR) Character Length Position */
#define FLEXCOM_FLEX_US_MR_CHRL_Msk           (_U_(0x3) << FLEXCOM_FLEX_US_MR_CHRL_Pos)      /**< (FLEXCOM_FLEX_US_MR) Character Length Mask */
#define FLEXCOM_FLEX_US_MR_CHRL(value)        (FLEXCOM_FLEX_US_MR_CHRL_Msk & ((value) << FLEXCOM_FLEX_US_MR_CHRL_Pos))
#define   FLEXCOM_FLEX_US_MR_CHRL_5_BIT_Val   _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MR) Character length is 5 bits  */
#define   FLEXCOM_FLEX_US_MR_CHRL_6_BIT_Val   _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MR) Character length is 6 bits  */
#define   FLEXCOM_FLEX_US_MR_CHRL_7_BIT_Val   _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MR) Character length is 7 bits  */
#define   FLEXCOM_FLEX_US_MR_CHRL_8_BIT_Val   _U_(0x3)                                       /**< (FLEXCOM_FLEX_US_MR) Character length is 8 bits  */
#define FLEXCOM_FLEX_US_MR_CHRL_5_BIT         (FLEXCOM_FLEX_US_MR_CHRL_5_BIT_Val << FLEXCOM_FLEX_US_MR_CHRL_Pos) /**< (FLEXCOM_FLEX_US_MR) Character length is 5 bits Position  */
#define FLEXCOM_FLEX_US_MR_CHRL_6_BIT         (FLEXCOM_FLEX_US_MR_CHRL_6_BIT_Val << FLEXCOM_FLEX_US_MR_CHRL_Pos) /**< (FLEXCOM_FLEX_US_MR) Character length is 6 bits Position  */
#define FLEXCOM_FLEX_US_MR_CHRL_7_BIT         (FLEXCOM_FLEX_US_MR_CHRL_7_BIT_Val << FLEXCOM_FLEX_US_MR_CHRL_Pos) /**< (FLEXCOM_FLEX_US_MR) Character length is 7 bits Position  */
#define FLEXCOM_FLEX_US_MR_CHRL_8_BIT         (FLEXCOM_FLEX_US_MR_CHRL_8_BIT_Val << FLEXCOM_FLEX_US_MR_CHRL_Pos) /**< (FLEXCOM_FLEX_US_MR) Character length is 8 bits Position  */
#define FLEXCOM_FLEX_US_MR_SYNC_Pos           _U_(8)                                         /**< (FLEXCOM_FLEX_US_MR) Synchronous Mode Select Position */
#define FLEXCOM_FLEX_US_MR_SYNC_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_MR_SYNC_Pos)      /**< (FLEXCOM_FLEX_US_MR) Synchronous Mode Select Mask */
#define FLEXCOM_FLEX_US_MR_PAR_Pos            _U_(9)                                         /**< (FLEXCOM_FLEX_US_MR) Parity Type Position */
#define FLEXCOM_FLEX_US_MR_PAR_Msk            (_U_(0x7) << FLEXCOM_FLEX_US_MR_PAR_Pos)       /**< (FLEXCOM_FLEX_US_MR) Parity Type Mask */
#define FLEXCOM_FLEX_US_MR_PAR(value)         (FLEXCOM_FLEX_US_MR_PAR_Msk & ((value) << FLEXCOM_FLEX_US_MR_PAR_Pos))
#define   FLEXCOM_FLEX_US_MR_PAR_EVEN_Val     _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MR) Even parity  */
#define   FLEXCOM_FLEX_US_MR_PAR_ODD_Val      _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MR) Odd parity  */
#define   FLEXCOM_FLEX_US_MR_PAR_SPACE_Val    _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MR) Parity forced to 0 (Space)  */
#define   FLEXCOM_FLEX_US_MR_PAR_MARK_Val     _U_(0x3)                                       /**< (FLEXCOM_FLEX_US_MR) Parity forced to 1 (Mark)  */
#define   FLEXCOM_FLEX_US_MR_PAR_NO_Val       _U_(0x4)                                       /**< (FLEXCOM_FLEX_US_MR) No parity  */
#define   FLEXCOM_FLEX_US_MR_PAR_MULTIDROP_Val _U_(0x6)                                       /**< (FLEXCOM_FLEX_US_MR) Multidrop mode  */
#define FLEXCOM_FLEX_US_MR_PAR_EVEN           (FLEXCOM_FLEX_US_MR_PAR_EVEN_Val << FLEXCOM_FLEX_US_MR_PAR_Pos) /**< (FLEXCOM_FLEX_US_MR) Even parity Position  */
#define FLEXCOM_FLEX_US_MR_PAR_ODD            (FLEXCOM_FLEX_US_MR_PAR_ODD_Val << FLEXCOM_FLEX_US_MR_PAR_Pos) /**< (FLEXCOM_FLEX_US_MR) Odd parity Position  */
#define FLEXCOM_FLEX_US_MR_PAR_SPACE          (FLEXCOM_FLEX_US_MR_PAR_SPACE_Val << FLEXCOM_FLEX_US_MR_PAR_Pos) /**< (FLEXCOM_FLEX_US_MR) Parity forced to 0 (Space) Position  */
#define FLEXCOM_FLEX_US_MR_PAR_MARK           (FLEXCOM_FLEX_US_MR_PAR_MARK_Val << FLEXCOM_FLEX_US_MR_PAR_Pos) /**< (FLEXCOM_FLEX_US_MR) Parity forced to 1 (Mark) Position  */
#define FLEXCOM_FLEX_US_MR_PAR_NO             (FLEXCOM_FLEX_US_MR_PAR_NO_Val << FLEXCOM_FLEX_US_MR_PAR_Pos) /**< (FLEXCOM_FLEX_US_MR) No parity Position  */
#define FLEXCOM_FLEX_US_MR_PAR_MULTIDROP      (FLEXCOM_FLEX_US_MR_PAR_MULTIDROP_Val << FLEXCOM_FLEX_US_MR_PAR_Pos) /**< (FLEXCOM_FLEX_US_MR) Multidrop mode Position  */
#define FLEXCOM_FLEX_US_MR_NBSTOP_Pos         _U_(12)                                        /**< (FLEXCOM_FLEX_US_MR) Number of Stop Bits Position */
#define FLEXCOM_FLEX_US_MR_NBSTOP_Msk         (_U_(0x3) << FLEXCOM_FLEX_US_MR_NBSTOP_Pos)    /**< (FLEXCOM_FLEX_US_MR) Number of Stop Bits Mask */
#define FLEXCOM_FLEX_US_MR_NBSTOP(value)      (FLEXCOM_FLEX_US_MR_NBSTOP_Msk & ((value) << FLEXCOM_FLEX_US_MR_NBSTOP_Pos))
#define   FLEXCOM_FLEX_US_MR_NBSTOP_1_BIT_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MR) 1 stop bit  */
#define   FLEXCOM_FLEX_US_MR_NBSTOP_1_5_BIT_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MR) 1.5 stop bit (SYNC = 0) or reserved (SYNC = 1)  */
#define   FLEXCOM_FLEX_US_MR_NBSTOP_2_BIT_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MR) 2 stop bits  */
#define FLEXCOM_FLEX_US_MR_NBSTOP_1_BIT       (FLEXCOM_FLEX_US_MR_NBSTOP_1_BIT_Val << FLEXCOM_FLEX_US_MR_NBSTOP_Pos) /**< (FLEXCOM_FLEX_US_MR) 1 stop bit Position  */
#define FLEXCOM_FLEX_US_MR_NBSTOP_1_5_BIT     (FLEXCOM_FLEX_US_MR_NBSTOP_1_5_BIT_Val << FLEXCOM_FLEX_US_MR_NBSTOP_Pos) /**< (FLEXCOM_FLEX_US_MR) 1.5 stop bit (SYNC = 0) or reserved (SYNC = 1) Position  */
#define FLEXCOM_FLEX_US_MR_NBSTOP_2_BIT       (FLEXCOM_FLEX_US_MR_NBSTOP_2_BIT_Val << FLEXCOM_FLEX_US_MR_NBSTOP_Pos) /**< (FLEXCOM_FLEX_US_MR) 2 stop bits Position  */
#define FLEXCOM_FLEX_US_MR_CHMODE_Pos         _U_(14)                                        /**< (FLEXCOM_FLEX_US_MR) Channel Mode Position */
#define FLEXCOM_FLEX_US_MR_CHMODE_Msk         (_U_(0x3) << FLEXCOM_FLEX_US_MR_CHMODE_Pos)    /**< (FLEXCOM_FLEX_US_MR) Channel Mode Mask */
#define FLEXCOM_FLEX_US_MR_CHMODE(value)      (FLEXCOM_FLEX_US_MR_CHMODE_Msk & ((value) << FLEXCOM_FLEX_US_MR_CHMODE_Pos))
#define   FLEXCOM_FLEX_US_MR_CHMODE_NORMAL_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MR) Normal mode  */
#define   FLEXCOM_FLEX_US_MR_CHMODE_AUTOMATIC_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MR) Automatic Echo. Receiver input is connected to the TXD pin.  */
#define   FLEXCOM_FLEX_US_MR_CHMODE_LOCAL_LOOPBACK_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MR) Local Loopback. Transmitter output is connected to the Receiver Input.  */
#define   FLEXCOM_FLEX_US_MR_CHMODE_REMOTE_LOOPBACK_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_US_MR) Remote Loopback. RXD pin is internally connected to the TXD pin.  */
#define FLEXCOM_FLEX_US_MR_CHMODE_NORMAL      (FLEXCOM_FLEX_US_MR_CHMODE_NORMAL_Val << FLEXCOM_FLEX_US_MR_CHMODE_Pos) /**< (FLEXCOM_FLEX_US_MR) Normal mode Position  */
#define FLEXCOM_FLEX_US_MR_CHMODE_AUTOMATIC   (FLEXCOM_FLEX_US_MR_CHMODE_AUTOMATIC_Val << FLEXCOM_FLEX_US_MR_CHMODE_Pos) /**< (FLEXCOM_FLEX_US_MR) Automatic Echo. Receiver input is connected to the TXD pin. Position  */
#define FLEXCOM_FLEX_US_MR_CHMODE_LOCAL_LOOPBACK (FLEXCOM_FLEX_US_MR_CHMODE_LOCAL_LOOPBACK_Val << FLEXCOM_FLEX_US_MR_CHMODE_Pos) /**< (FLEXCOM_FLEX_US_MR) Local Loopback. Transmitter output is connected to the Receiver Input. Position  */
#define FLEXCOM_FLEX_US_MR_CHMODE_REMOTE_LOOPBACK (FLEXCOM_FLEX_US_MR_CHMODE_REMOTE_LOOPBACK_Val << FLEXCOM_FLEX_US_MR_CHMODE_Pos) /**< (FLEXCOM_FLEX_US_MR) Remote Loopback. RXD pin is internally connected to the TXD pin. Position  */
#define FLEXCOM_FLEX_US_MR_MSBF_Pos           _U_(16)                                        /**< (FLEXCOM_FLEX_US_MR) Bit Order Position */
#define FLEXCOM_FLEX_US_MR_MSBF_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_MR_MSBF_Pos)      /**< (FLEXCOM_FLEX_US_MR) Bit Order Mask */
#define FLEXCOM_FLEX_US_MR_MODE9_Pos          _U_(17)                                        /**< (FLEXCOM_FLEX_US_MR) 9-bit Character Length Position */
#define FLEXCOM_FLEX_US_MR_MODE9_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_MR_MODE9_Pos)     /**< (FLEXCOM_FLEX_US_MR) 9-bit Character Length Mask */
#define FLEXCOM_FLEX_US_MR_CLKO_Pos           _U_(18)                                        /**< (FLEXCOM_FLEX_US_MR) Clock Output Select Position */
#define FLEXCOM_FLEX_US_MR_CLKO_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_MR_CLKO_Pos)      /**< (FLEXCOM_FLEX_US_MR) Clock Output Select Mask */
#define FLEXCOM_FLEX_US_MR_OVER_Pos           _U_(19)                                        /**< (FLEXCOM_FLEX_US_MR) Oversampling Mode Position */
#define FLEXCOM_FLEX_US_MR_OVER_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_MR_OVER_Pos)      /**< (FLEXCOM_FLEX_US_MR) Oversampling Mode Mask */
#define FLEXCOM_FLEX_US_MR_INACK_Pos          _U_(20)                                        /**< (FLEXCOM_FLEX_US_MR) Inhibit Non Acknowledge Position */
#define FLEXCOM_FLEX_US_MR_INACK_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_MR_INACK_Pos)     /**< (FLEXCOM_FLEX_US_MR) Inhibit Non Acknowledge Mask */
#define FLEXCOM_FLEX_US_MR_DSNACK_Pos         _U_(21)                                        /**< (FLEXCOM_FLEX_US_MR) Disable Successive NACK Position */
#define FLEXCOM_FLEX_US_MR_DSNACK_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_MR_DSNACK_Pos)    /**< (FLEXCOM_FLEX_US_MR) Disable Successive NACK Mask */
#define FLEXCOM_FLEX_US_MR_VAR_SYNC_Pos       _U_(22)                                        /**< (FLEXCOM_FLEX_US_MR) Variable Synchronization of Command/Data Sync Start Frame Delimiter Position */
#define FLEXCOM_FLEX_US_MR_VAR_SYNC_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_MR_VAR_SYNC_Pos)  /**< (FLEXCOM_FLEX_US_MR) Variable Synchronization of Command/Data Sync Start Frame Delimiter Mask */
#define FLEXCOM_FLEX_US_MR_INVDATA_Pos        _U_(23)                                        /**< (FLEXCOM_FLEX_US_MR) Inverted Data Position */
#define FLEXCOM_FLEX_US_MR_INVDATA_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_MR_INVDATA_Pos)   /**< (FLEXCOM_FLEX_US_MR) Inverted Data Mask */
#define FLEXCOM_FLEX_US_MR_MAX_ITERATION_Pos  _U_(24)                                        /**< (FLEXCOM_FLEX_US_MR) Maximum Number of Automatic Iteration Position */
#define FLEXCOM_FLEX_US_MR_MAX_ITERATION_Msk  (_U_(0x7) << FLEXCOM_FLEX_US_MR_MAX_ITERATION_Pos) /**< (FLEXCOM_FLEX_US_MR) Maximum Number of Automatic Iteration Mask */
#define FLEXCOM_FLEX_US_MR_MAX_ITERATION(value) (FLEXCOM_FLEX_US_MR_MAX_ITERATION_Msk & ((value) << FLEXCOM_FLEX_US_MR_MAX_ITERATION_Pos))
#define FLEXCOM_FLEX_US_MR_FILTER_Pos         _U_(28)                                        /**< (FLEXCOM_FLEX_US_MR) Receive Line Filter Position */
#define FLEXCOM_FLEX_US_MR_FILTER_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_MR_FILTER_Pos)    /**< (FLEXCOM_FLEX_US_MR) Receive Line Filter Mask */
#define FLEXCOM_FLEX_US_MR_MAN_Pos            _U_(29)                                        /**< (FLEXCOM_FLEX_US_MR) Manchester Encoder/Decoder Enable Position */
#define FLEXCOM_FLEX_US_MR_MAN_Msk            (_U_(0x1) << FLEXCOM_FLEX_US_MR_MAN_Pos)       /**< (FLEXCOM_FLEX_US_MR) Manchester Encoder/Decoder Enable Mask */
#define FLEXCOM_FLEX_US_MR_MODSYNC_Pos        _U_(30)                                        /**< (FLEXCOM_FLEX_US_MR) Manchester Synchronization Mode Position */
#define FLEXCOM_FLEX_US_MR_MODSYNC_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_MR_MODSYNC_Pos)   /**< (FLEXCOM_FLEX_US_MR) Manchester Synchronization Mode Mask */
#define FLEXCOM_FLEX_US_MR_ONEBIT_Pos         _U_(31)                                        /**< (FLEXCOM_FLEX_US_MR) Start Frame Delimiter Selector Position */
#define FLEXCOM_FLEX_US_MR_ONEBIT_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_MR_ONEBIT_Pos)    /**< (FLEXCOM_FLEX_US_MR) Start Frame Delimiter Selector Mask */
#define FLEXCOM_FLEX_US_MR_Msk                _U_(0xF7FFFFFF)                                /**< (FLEXCOM_FLEX_US_MR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_IER : (FLEXCOM Offset: 0x208) ( /W 32) USART Interrupt Enable Register -------- */
#define FLEXCOM_FLEX_US_IER_RXRDY_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_IER) RXRDY Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_RXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IER_RXRDY_Pos)    /**< (FLEXCOM_FLEX_US_IER) RXRDY Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_TXRDY_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_US_IER) TXRDY Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_TXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IER_TXRDY_Pos)    /**< (FLEXCOM_FLEX_US_IER) TXRDY Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_RXBRK_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_US_IER) Receiver Break Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_RXBRK_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IER_RXBRK_Pos)    /**< (FLEXCOM_FLEX_US_IER) Receiver Break Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_OVRE_Pos          _U_(5)                                         /**< (FLEXCOM_FLEX_US_IER) Overrun Error Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_OVRE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IER_OVRE_Pos)     /**< (FLEXCOM_FLEX_US_IER) Overrun Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_FRAME_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_US_IER) Framing Error Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_FRAME_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IER_FRAME_Pos)    /**< (FLEXCOM_FLEX_US_IER) Framing Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_PARE_Pos          _U_(7)                                         /**< (FLEXCOM_FLEX_US_IER) Parity Error Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_PARE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IER_PARE_Pos)     /**< (FLEXCOM_FLEX_US_IER) Parity Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_TIMEOUT_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_US_IER) Timeout Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_TIMEOUT_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_IER_TIMEOUT_Pos)  /**< (FLEXCOM_FLEX_US_IER) Timeout Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_TXEMPTY_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_US_IER) TXEMPTY Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_TXEMPTY_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_IER_TXEMPTY_Pos)  /**< (FLEXCOM_FLEX_US_IER) TXEMPTY Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_ITER_Pos          _U_(10)                                        /**< (FLEXCOM_FLEX_US_IER) Max number of Repetitions Reached Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_ITER_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IER_ITER_Pos)     /**< (FLEXCOM_FLEX_US_IER) Max number of Repetitions Reached Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_NACK_Pos          _U_(13)                                        /**< (FLEXCOM_FLEX_US_IER) Non Acknowledge Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_NACK_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IER_NACK_Pos)     /**< (FLEXCOM_FLEX_US_IER) Non Acknowledge Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_CTSIC_Pos         _U_(19)                                        /**< (FLEXCOM_FLEX_US_IER) Clear to Send Input Change Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_CTSIC_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IER_CTSIC_Pos)    /**< (FLEXCOM_FLEX_US_IER) Clear to Send Input Change Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_CMP_Pos           _U_(22)                                        /**< (FLEXCOM_FLEX_US_IER) Comparison Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_CMP_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_IER_CMP_Pos)      /**< (FLEXCOM_FLEX_US_IER) Comparison Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_MANE_Pos          _U_(24)                                        /**< (FLEXCOM_FLEX_US_IER) Manchester Error Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IER_MANE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IER_MANE_Pos)     /**< (FLEXCOM_FLEX_US_IER) Manchester Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IER_Msk               _U_(0x014827E7)                                /**< (FLEXCOM_FLEX_US_IER) Register Mask  */

/* LIN mode */
#define FLEXCOM_FLEX_US_IER_LIN_Msk         _U_(0x00000000)                                 /**< (FLEXCOM_FLEX_US_IER_LIN) Register Mask  */


/* -------- FLEXCOM_FLEX_US_IDR : (FLEXCOM Offset: 0x20C) ( /W 32) USART Interrupt Disable Register -------- */
#define FLEXCOM_FLEX_US_IDR_RXRDY_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_IDR) RXRDY Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_RXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IDR_RXRDY_Pos)    /**< (FLEXCOM_FLEX_US_IDR) RXRDY Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_TXRDY_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_US_IDR) TXRDY Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_TXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IDR_TXRDY_Pos)    /**< (FLEXCOM_FLEX_US_IDR) TXRDY Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_RXBRK_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_US_IDR) Receiver Break Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_RXBRK_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IDR_RXBRK_Pos)    /**< (FLEXCOM_FLEX_US_IDR) Receiver Break Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_OVRE_Pos          _U_(5)                                         /**< (FLEXCOM_FLEX_US_IDR) Overrun Error Interrupt Enable Position */
#define FLEXCOM_FLEX_US_IDR_OVRE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IDR_OVRE_Pos)     /**< (FLEXCOM_FLEX_US_IDR) Overrun Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_IDR_FRAME_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_US_IDR) Framing Error Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_FRAME_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IDR_FRAME_Pos)    /**< (FLEXCOM_FLEX_US_IDR) Framing Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_PARE_Pos          _U_(7)                                         /**< (FLEXCOM_FLEX_US_IDR) Parity Error Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_PARE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IDR_PARE_Pos)     /**< (FLEXCOM_FLEX_US_IDR) Parity Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_TIMEOUT_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_US_IDR) Timeout Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_TIMEOUT_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_IDR_TIMEOUT_Pos)  /**< (FLEXCOM_FLEX_US_IDR) Timeout Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_TXEMPTY_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_US_IDR) TXEMPTY Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_TXEMPTY_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_IDR_TXEMPTY_Pos)  /**< (FLEXCOM_FLEX_US_IDR) TXEMPTY Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_ITER_Pos          _U_(10)                                        /**< (FLEXCOM_FLEX_US_IDR) Max Number of Repetitions Reached Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_ITER_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IDR_ITER_Pos)     /**< (FLEXCOM_FLEX_US_IDR) Max Number of Repetitions Reached Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_NACK_Pos          _U_(13)                                        /**< (FLEXCOM_FLEX_US_IDR) Non Acknowledge Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_NACK_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IDR_NACK_Pos)     /**< (FLEXCOM_FLEX_US_IDR) Non Acknowledge Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_CTSIC_Pos         _U_(19)                                        /**< (FLEXCOM_FLEX_US_IDR) Clear to Send Input Change Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_CTSIC_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IDR_CTSIC_Pos)    /**< (FLEXCOM_FLEX_US_IDR) Clear to Send Input Change Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_CMP_Pos           _U_(22)                                        /**< (FLEXCOM_FLEX_US_IDR) Comparison Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_CMP_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_IDR_CMP_Pos)      /**< (FLEXCOM_FLEX_US_IDR) Comparison Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_MANE_Pos          _U_(24)                                        /**< (FLEXCOM_FLEX_US_IDR) Manchester Error Interrupt Disable Position */
#define FLEXCOM_FLEX_US_IDR_MANE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IDR_MANE_Pos)     /**< (FLEXCOM_FLEX_US_IDR) Manchester Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_IDR_Msk               _U_(0x014827E7)                                /**< (FLEXCOM_FLEX_US_IDR) Register Mask  */

/* LIN mode */
#define FLEXCOM_FLEX_US_IDR_LIN_Msk         _U_(0x00000000)                                 /**< (FLEXCOM_FLEX_US_IDR_LIN) Register Mask  */


/* -------- FLEXCOM_FLEX_US_IMR : (FLEXCOM Offset: 0x210) ( R/ 32) USART Interrupt Mask Register -------- */
#define FLEXCOM_FLEX_US_IMR_RXRDY_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_IMR) RXRDY Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_RXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IMR_RXRDY_Pos)    /**< (FLEXCOM_FLEX_US_IMR) RXRDY Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_TXRDY_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_US_IMR) TXRDY Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_TXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IMR_TXRDY_Pos)    /**< (FLEXCOM_FLEX_US_IMR) TXRDY Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_RXBRK_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_US_IMR) Receiver Break Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_RXBRK_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IMR_RXBRK_Pos)    /**< (FLEXCOM_FLEX_US_IMR) Receiver Break Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_OVRE_Pos          _U_(5)                                         /**< (FLEXCOM_FLEX_US_IMR) Overrun Error Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_OVRE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IMR_OVRE_Pos)     /**< (FLEXCOM_FLEX_US_IMR) Overrun Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_FRAME_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_US_IMR) Framing Error Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_FRAME_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IMR_FRAME_Pos)    /**< (FLEXCOM_FLEX_US_IMR) Framing Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_PARE_Pos          _U_(7)                                         /**< (FLEXCOM_FLEX_US_IMR) Parity Error Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_PARE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IMR_PARE_Pos)     /**< (FLEXCOM_FLEX_US_IMR) Parity Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_TIMEOUT_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_US_IMR) Timeout Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_TIMEOUT_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_IMR_TIMEOUT_Pos)  /**< (FLEXCOM_FLEX_US_IMR) Timeout Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_TXEMPTY_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_US_IMR) TXEMPTY Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_TXEMPTY_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_IMR_TXEMPTY_Pos)  /**< (FLEXCOM_FLEX_US_IMR) TXEMPTY Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_ITER_Pos          _U_(10)                                        /**< (FLEXCOM_FLEX_US_IMR) Max Number of Repetitions Reached Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_ITER_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IMR_ITER_Pos)     /**< (FLEXCOM_FLEX_US_IMR) Max Number of Repetitions Reached Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_NACK_Pos          _U_(13)                                        /**< (FLEXCOM_FLEX_US_IMR) Non Acknowledge Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_NACK_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IMR_NACK_Pos)     /**< (FLEXCOM_FLEX_US_IMR) Non Acknowledge Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_CTSIC_Pos         _U_(19)                                        /**< (FLEXCOM_FLEX_US_IMR) Clear to Send Input Change Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_CTSIC_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_IMR_CTSIC_Pos)    /**< (FLEXCOM_FLEX_US_IMR) Clear to Send Input Change Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_CMP_Pos           _U_(22)                                        /**< (FLEXCOM_FLEX_US_IMR) Comparison Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_CMP_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_IMR_CMP_Pos)      /**< (FLEXCOM_FLEX_US_IMR) Comparison Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_MANE_Pos          _U_(24)                                        /**< (FLEXCOM_FLEX_US_IMR) Manchester Error Interrupt Mask Position */
#define FLEXCOM_FLEX_US_IMR_MANE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_IMR_MANE_Pos)     /**< (FLEXCOM_FLEX_US_IMR) Manchester Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_IMR_Msk               _U_(0x014827E7)                                /**< (FLEXCOM_FLEX_US_IMR) Register Mask  */

/* LIN mode */
#define FLEXCOM_FLEX_US_IMR_LIN_Msk         _U_(0x00000000)                                 /**< (FLEXCOM_FLEX_US_IMR_LIN) Register Mask  */


/* -------- FLEXCOM_FLEX_US_CSR : (FLEXCOM Offset: 0x214) ( R/ 32) USART Channel Status Register -------- */
#define FLEXCOM_FLEX_US_CSR_RXRDY_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_CSR) Receiver Ready (cleared by reading FLEX_US_RHR) Position */
#define FLEXCOM_FLEX_US_CSR_RXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CSR_RXRDY_Pos)    /**< (FLEXCOM_FLEX_US_CSR) Receiver Ready (cleared by reading FLEX_US_RHR) Mask */
#define FLEXCOM_FLEX_US_CSR_TXRDY_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_US_CSR) Transmitter Ready (cleared by writing FLEX_US_THR) Position */
#define FLEXCOM_FLEX_US_CSR_TXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CSR_TXRDY_Pos)    /**< (FLEXCOM_FLEX_US_CSR) Transmitter Ready (cleared by writing FLEX_US_THR) Mask */
#define FLEXCOM_FLEX_US_CSR_RXBRK_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_US_CSR) Break Received/End of Break Position */
#define FLEXCOM_FLEX_US_CSR_RXBRK_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CSR_RXBRK_Pos)    /**< (FLEXCOM_FLEX_US_CSR) Break Received/End of Break Mask */
#define FLEXCOM_FLEX_US_CSR_OVRE_Pos          _U_(5)                                         /**< (FLEXCOM_FLEX_US_CSR) Overrun Error Position */
#define FLEXCOM_FLEX_US_CSR_OVRE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CSR_OVRE_Pos)     /**< (FLEXCOM_FLEX_US_CSR) Overrun Error Mask */
#define FLEXCOM_FLEX_US_CSR_FRAME_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_US_CSR) Framing Error Position */
#define FLEXCOM_FLEX_US_CSR_FRAME_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CSR_FRAME_Pos)    /**< (FLEXCOM_FLEX_US_CSR) Framing Error Mask */
#define FLEXCOM_FLEX_US_CSR_PARE_Pos          _U_(7)                                         /**< (FLEXCOM_FLEX_US_CSR) Parity Error Position */
#define FLEXCOM_FLEX_US_CSR_PARE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CSR_PARE_Pos)     /**< (FLEXCOM_FLEX_US_CSR) Parity Error Mask */
#define FLEXCOM_FLEX_US_CSR_TIMEOUT_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_US_CSR) Receiver Timeout Position */
#define FLEXCOM_FLEX_US_CSR_TIMEOUT_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_CSR_TIMEOUT_Pos)  /**< (FLEXCOM_FLEX_US_CSR) Receiver Timeout Mask */
#define FLEXCOM_FLEX_US_CSR_TXEMPTY_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_US_CSR) Transmitter Empty (cleared by writing FLEX_US_THR) Position */
#define FLEXCOM_FLEX_US_CSR_TXEMPTY_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_CSR_TXEMPTY_Pos)  /**< (FLEXCOM_FLEX_US_CSR) Transmitter Empty (cleared by writing FLEX_US_THR) Mask */
#define FLEXCOM_FLEX_US_CSR_ITER_Pos          _U_(10)                                        /**< (FLEXCOM_FLEX_US_CSR) Max Number of Repetitions Reached Position */
#define FLEXCOM_FLEX_US_CSR_ITER_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CSR_ITER_Pos)     /**< (FLEXCOM_FLEX_US_CSR) Max Number of Repetitions Reached Mask */
#define FLEXCOM_FLEX_US_CSR_NACK_Pos          _U_(13)                                        /**< (FLEXCOM_FLEX_US_CSR) Non Acknowledge Interrupt Position */
#define FLEXCOM_FLEX_US_CSR_NACK_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CSR_NACK_Pos)     /**< (FLEXCOM_FLEX_US_CSR) Non Acknowledge Interrupt Mask */
#define FLEXCOM_FLEX_US_CSR_CTSIC_Pos         _U_(19)                                        /**< (FLEXCOM_FLEX_US_CSR) Clear to Send Input Change Flag Position */
#define FLEXCOM_FLEX_US_CSR_CTSIC_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_CSR_CTSIC_Pos)    /**< (FLEXCOM_FLEX_US_CSR) Clear to Send Input Change Flag Mask */
#define FLEXCOM_FLEX_US_CSR_CMP_Pos           _U_(22)                                        /**< (FLEXCOM_FLEX_US_CSR) Comparison Status Position */
#define FLEXCOM_FLEX_US_CSR_CMP_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_CSR_CMP_Pos)      /**< (FLEXCOM_FLEX_US_CSR) Comparison Status Mask */
#define FLEXCOM_FLEX_US_CSR_CTS_Pos           _U_(23)                                        /**< (FLEXCOM_FLEX_US_CSR) Image of CTS Input Position */
#define FLEXCOM_FLEX_US_CSR_CTS_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_CSR_CTS_Pos)      /**< (FLEXCOM_FLEX_US_CSR) Image of CTS Input Mask */
#define FLEXCOM_FLEX_US_CSR_MANE_Pos          _U_(24)                                        /**< (FLEXCOM_FLEX_US_CSR) Manchester Error Position */
#define FLEXCOM_FLEX_US_CSR_MANE_Msk          (_U_(0x1) << FLEXCOM_FLEX_US_CSR_MANE_Pos)     /**< (FLEXCOM_FLEX_US_CSR) Manchester Error Mask */
#define FLEXCOM_FLEX_US_CSR_Msk               _U_(0x01C827E7)                                /**< (FLEXCOM_FLEX_US_CSR) Register Mask  */

/* LIN mode */
#define FLEXCOM_FLEX_US_CSR_LIN_Msk         _U_(0x00000000)                                 /**< (FLEXCOM_FLEX_US_CSR_LIN) Register Mask  */


/* -------- FLEXCOM_FLEX_US_RHR : (FLEXCOM Offset: 0x218) ( R/ 32) USART Receive Holding Register -------- */
#define FLEXCOM_FLEX_US_RHR_RXCHR_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_RHR) Received Character Position */
#define FLEXCOM_FLEX_US_RHR_RXCHR_Msk         (_U_(0x1FF) << FLEXCOM_FLEX_US_RHR_RXCHR_Pos)  /**< (FLEXCOM_FLEX_US_RHR) Received Character Mask */
#define FLEXCOM_FLEX_US_RHR_RXCHR(value)      (FLEXCOM_FLEX_US_RHR_RXCHR_Msk & ((value) << FLEXCOM_FLEX_US_RHR_RXCHR_Pos))
#define FLEXCOM_FLEX_US_RHR_RXSYNH_Pos        _U_(15)                                        /**< (FLEXCOM_FLEX_US_RHR) Received Sync Position */
#define FLEXCOM_FLEX_US_RHR_RXSYNH_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_RHR_RXSYNH_Pos)   /**< (FLEXCOM_FLEX_US_RHR) Received Sync Mask */
#define FLEXCOM_FLEX_US_RHR_Msk               _U_(0x000081FF)                                /**< (FLEXCOM_FLEX_US_RHR) Register Mask  */

/* FIFO_MULTI_DATA mode */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR0_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_US_RHR) Received Character Position */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR0_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR0_Pos) /**< (FLEXCOM_FLEX_US_RHR) Received Character Mask */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR0(value) (FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR0_Msk & ((value) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR0_Pos))
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR1_Pos _U_(8)                                         /**< (FLEXCOM_FLEX_US_RHR) Received Character Position */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR1_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR1_Pos) /**< (FLEXCOM_FLEX_US_RHR) Received Character Mask */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR1(value) (FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR1_Msk & ((value) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR1_Pos))
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR2_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_US_RHR) Received Character Position */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR2_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR2_Pos) /**< (FLEXCOM_FLEX_US_RHR) Received Character Mask */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR2(value) (FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR2_Msk & ((value) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR2_Pos))
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR3_Pos _U_(24)                                        /**< (FLEXCOM_FLEX_US_RHR) Received Character Position */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR3_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR3_Pos) /**< (FLEXCOM_FLEX_US_RHR) Received Character Mask */
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR3(value) (FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR3_Msk & ((value) << FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_RXCHR3_Pos))
#define FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA_Msk _U_(0xFFFFFFFF)                                 /**< (FLEXCOM_FLEX_US_RHR_FIFO_MULTI_DATA) Register Mask  */


/* -------- FLEXCOM_FLEX_US_THR : (FLEXCOM Offset: 0x21C) ( /W 32) USART Transmit Holding Register -------- */
#define FLEXCOM_FLEX_US_THR_TXCHR_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Position */
#define FLEXCOM_FLEX_US_THR_TXCHR_Msk         (_U_(0x1FF) << FLEXCOM_FLEX_US_THR_TXCHR_Pos)  /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Mask */
#define FLEXCOM_FLEX_US_THR_TXCHR(value)      (FLEXCOM_FLEX_US_THR_TXCHR_Msk & ((value) << FLEXCOM_FLEX_US_THR_TXCHR_Pos))
#define FLEXCOM_FLEX_US_THR_TXSYNH_Pos        _U_(15)                                        /**< (FLEXCOM_FLEX_US_THR) Sync Field to be Transmitted Position */
#define FLEXCOM_FLEX_US_THR_TXSYNH_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_THR_TXSYNH_Pos)   /**< (FLEXCOM_FLEX_US_THR) Sync Field to be Transmitted Mask */
#define FLEXCOM_FLEX_US_THR_Msk               _U_(0x000081FF)                                /**< (FLEXCOM_FLEX_US_THR) Register Mask  */

/* FIFO_MULTI_DATA mode */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR0_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Position */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR0_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR0_Pos) /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Mask */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR0(value) (FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR0_Msk & ((value) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR0_Pos))
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR1_Pos _U_(8)                                         /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Position */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR1_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR1_Pos) /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Mask */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR1(value) (FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR1_Msk & ((value) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR1_Pos))
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR2_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Position */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR2_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR2_Pos) /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Mask */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR2(value) (FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR2_Msk & ((value) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR2_Pos))
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR3_Pos _U_(24)                                        /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Position */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR3_Msk (_U_(0xFF) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR3_Pos) /**< (FLEXCOM_FLEX_US_THR) Character to be Transmitted Mask */
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR3(value) (FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR3_Msk & ((value) << FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_TXCHR3_Pos))
#define FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA_Msk _U_(0xFFFFFFFF)                                 /**< (FLEXCOM_FLEX_US_THR_FIFO_MULTI_DATA) Register Mask  */


/* -------- FLEXCOM_FLEX_US_BRGR : (FLEXCOM Offset: 0x220) (R/W 32) USART Baud Rate Generator Register -------- */
#define FLEXCOM_FLEX_US_BRGR_CD_Pos           _U_(0)                                         /**< (FLEXCOM_FLEX_US_BRGR) Clock Divider Position */
#define FLEXCOM_FLEX_US_BRGR_CD_Msk           (_U_(0xFFFF) << FLEXCOM_FLEX_US_BRGR_CD_Pos)   /**< (FLEXCOM_FLEX_US_BRGR) Clock Divider Mask */
#define FLEXCOM_FLEX_US_BRGR_CD(value)        (FLEXCOM_FLEX_US_BRGR_CD_Msk & ((value) << FLEXCOM_FLEX_US_BRGR_CD_Pos))
#define FLEXCOM_FLEX_US_BRGR_FP_Pos           _U_(16)                                        /**< (FLEXCOM_FLEX_US_BRGR) Fractional Part Position */
#define FLEXCOM_FLEX_US_BRGR_FP_Msk           (_U_(0x7) << FLEXCOM_FLEX_US_BRGR_FP_Pos)      /**< (FLEXCOM_FLEX_US_BRGR) Fractional Part Mask */
#define FLEXCOM_FLEX_US_BRGR_FP(value)        (FLEXCOM_FLEX_US_BRGR_FP_Msk & ((value) << FLEXCOM_FLEX_US_BRGR_FP_Pos))
#define FLEXCOM_FLEX_US_BRGR_Msk              _U_(0x0007FFFF)                                /**< (FLEXCOM_FLEX_US_BRGR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_RTOR : (FLEXCOM Offset: 0x224) (R/W 32) USART Receiver Timeout Register -------- */
#define FLEXCOM_FLEX_US_RTOR_TO_Pos           _U_(0)                                         /**< (FLEXCOM_FLEX_US_RTOR) Timeout Value Position */
#define FLEXCOM_FLEX_US_RTOR_TO_Msk           (_U_(0x1FFFF) << FLEXCOM_FLEX_US_RTOR_TO_Pos)  /**< (FLEXCOM_FLEX_US_RTOR) Timeout Value Mask */
#define FLEXCOM_FLEX_US_RTOR_TO(value)        (FLEXCOM_FLEX_US_RTOR_TO_Msk & ((value) << FLEXCOM_FLEX_US_RTOR_TO_Pos))
#define FLEXCOM_FLEX_US_RTOR_Msk              _U_(0x0001FFFF)                                /**< (FLEXCOM_FLEX_US_RTOR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_TTGR : (FLEXCOM Offset: 0x228) (R/W 32) USART Transmitter Timeguard Register -------- */
#define FLEXCOM_FLEX_US_TTGR_TG_Pos           _U_(0)                                         /**< (FLEXCOM_FLEX_US_TTGR) Timeguard Value Position */
#define FLEXCOM_FLEX_US_TTGR_TG_Msk           (_U_(0xFF) << FLEXCOM_FLEX_US_TTGR_TG_Pos)     /**< (FLEXCOM_FLEX_US_TTGR) Timeguard Value Mask */
#define FLEXCOM_FLEX_US_TTGR_TG(value)        (FLEXCOM_FLEX_US_TTGR_TG_Msk & ((value) << FLEXCOM_FLEX_US_TTGR_TG_Pos))
#define FLEXCOM_FLEX_US_TTGR_Msk              _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_US_TTGR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_FIDI : (FLEXCOM Offset: 0x240) (R/W 32) USART FI DI Ratio Register -------- */
#define FLEXCOM_FLEX_US_FIDI_FI_DI_RATIO_Pos  _U_(0)                                         /**< (FLEXCOM_FLEX_US_FIDI) FI Over DI Ratio Value Position */
#define FLEXCOM_FLEX_US_FIDI_FI_DI_RATIO_Msk  (_U_(0xFFFF) << FLEXCOM_FLEX_US_FIDI_FI_DI_RATIO_Pos) /**< (FLEXCOM_FLEX_US_FIDI) FI Over DI Ratio Value Mask */
#define FLEXCOM_FLEX_US_FIDI_FI_DI_RATIO(value) (FLEXCOM_FLEX_US_FIDI_FI_DI_RATIO_Msk & ((value) << FLEXCOM_FLEX_US_FIDI_FI_DI_RATIO_Pos))
#define FLEXCOM_FLEX_US_FIDI_Msk              _U_(0x0000FFFF)                                /**< (FLEXCOM_FLEX_US_FIDI) Register Mask  */


/* -------- FLEXCOM_FLEX_US_NER : (FLEXCOM Offset: 0x244) ( R/ 32) USART Number of Errors Register -------- */
#define FLEXCOM_FLEX_US_NER_NB_ERRORS_Pos     _U_(0)                                         /**< (FLEXCOM_FLEX_US_NER) Number of Errors Position */
#define FLEXCOM_FLEX_US_NER_NB_ERRORS_Msk     (_U_(0xFF) << FLEXCOM_FLEX_US_NER_NB_ERRORS_Pos) /**< (FLEXCOM_FLEX_US_NER) Number of Errors Mask */
#define FLEXCOM_FLEX_US_NER_NB_ERRORS(value)  (FLEXCOM_FLEX_US_NER_NB_ERRORS_Msk & ((value) << FLEXCOM_FLEX_US_NER_NB_ERRORS_Pos))
#define FLEXCOM_FLEX_US_NER_Msk               _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_US_NER) Register Mask  */


/* -------- FLEXCOM_FLEX_US_IF : (FLEXCOM Offset: 0x24C) (R/W 32) USART IrDA Filter Register -------- */
#define FLEXCOM_FLEX_US_IF_IRDA_FILTER_Pos    _U_(0)                                         /**< (FLEXCOM_FLEX_US_IF) IrDA Filter Position */
#define FLEXCOM_FLEX_US_IF_IRDA_FILTER_Msk    (_U_(0xFF) << FLEXCOM_FLEX_US_IF_IRDA_FILTER_Pos) /**< (FLEXCOM_FLEX_US_IF) IrDA Filter Mask */
#define FLEXCOM_FLEX_US_IF_IRDA_FILTER(value) (FLEXCOM_FLEX_US_IF_IRDA_FILTER_Msk & ((value) << FLEXCOM_FLEX_US_IF_IRDA_FILTER_Pos))
#define FLEXCOM_FLEX_US_IF_Msk                _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_US_IF) Register Mask  */


/* -------- FLEXCOM_FLEX_US_MAN : (FLEXCOM Offset: 0x250) (R/W 32) USART Manchester Configuration Register -------- */
#define FLEXCOM_FLEX_US_MAN_TX_PL_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_MAN) Transmitter Preamble Length Position */
#define FLEXCOM_FLEX_US_MAN_TX_PL_Msk         (_U_(0xF) << FLEXCOM_FLEX_US_MAN_TX_PL_Pos)    /**< (FLEXCOM_FLEX_US_MAN) Transmitter Preamble Length Mask */
#define FLEXCOM_FLEX_US_MAN_TX_PL(value)      (FLEXCOM_FLEX_US_MAN_TX_PL_Msk & ((value) << FLEXCOM_FLEX_US_MAN_TX_PL_Pos))
#define FLEXCOM_FLEX_US_MAN_TX_PP_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_US_MAN) Transmitter Preamble Pattern Position */
#define FLEXCOM_FLEX_US_MAN_TX_PP_Msk         (_U_(0x3) << FLEXCOM_FLEX_US_MAN_TX_PP_Pos)    /**< (FLEXCOM_FLEX_US_MAN) Transmitter Preamble Pattern Mask */
#define FLEXCOM_FLEX_US_MAN_TX_PP(value)      (FLEXCOM_FLEX_US_MAN_TX_PP_Msk & ((value) << FLEXCOM_FLEX_US_MAN_TX_PP_Pos))
#define   FLEXCOM_FLEX_US_MAN_TX_PP_ALL_ONE_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '1's  */
#define   FLEXCOM_FLEX_US_MAN_TX_PP_ALL_ZERO_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '0's  */
#define   FLEXCOM_FLEX_US_MAN_TX_PP_ZERO_ONE_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '01's  */
#define   FLEXCOM_FLEX_US_MAN_TX_PP_ONE_ZERO_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '10's  */
#define FLEXCOM_FLEX_US_MAN_TX_PP_ALL_ONE     (FLEXCOM_FLEX_US_MAN_TX_PP_ALL_ONE_Val << FLEXCOM_FLEX_US_MAN_TX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '1's Position  */
#define FLEXCOM_FLEX_US_MAN_TX_PP_ALL_ZERO    (FLEXCOM_FLEX_US_MAN_TX_PP_ALL_ZERO_Val << FLEXCOM_FLEX_US_MAN_TX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '0's Position  */
#define FLEXCOM_FLEX_US_MAN_TX_PP_ZERO_ONE    (FLEXCOM_FLEX_US_MAN_TX_PP_ZERO_ONE_Val << FLEXCOM_FLEX_US_MAN_TX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '01's Position  */
#define FLEXCOM_FLEX_US_MAN_TX_PP_ONE_ZERO    (FLEXCOM_FLEX_US_MAN_TX_PP_ONE_ZERO_Val << FLEXCOM_FLEX_US_MAN_TX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '10's Position  */
#define FLEXCOM_FLEX_US_MAN_TX_MPOL_Pos       _U_(12)                                        /**< (FLEXCOM_FLEX_US_MAN) Transmitter Manchester Polarity Position */
#define FLEXCOM_FLEX_US_MAN_TX_MPOL_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_MAN_TX_MPOL_Pos)  /**< (FLEXCOM_FLEX_US_MAN) Transmitter Manchester Polarity Mask */
#define FLEXCOM_FLEX_US_MAN_RX_PL_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_US_MAN) Receiver Preamble Length Position */
#define FLEXCOM_FLEX_US_MAN_RX_PL_Msk         (_U_(0xF) << FLEXCOM_FLEX_US_MAN_RX_PL_Pos)    /**< (FLEXCOM_FLEX_US_MAN) Receiver Preamble Length Mask */
#define FLEXCOM_FLEX_US_MAN_RX_PL(value)      (FLEXCOM_FLEX_US_MAN_RX_PL_Msk & ((value) << FLEXCOM_FLEX_US_MAN_RX_PL_Pos))
#define FLEXCOM_FLEX_US_MAN_RX_PP_Pos         _U_(24)                                        /**< (FLEXCOM_FLEX_US_MAN) Receiver Preamble Pattern detected Position */
#define FLEXCOM_FLEX_US_MAN_RX_PP_Msk         (_U_(0x3) << FLEXCOM_FLEX_US_MAN_RX_PP_Pos)    /**< (FLEXCOM_FLEX_US_MAN) Receiver Preamble Pattern detected Mask */
#define FLEXCOM_FLEX_US_MAN_RX_PP(value)      (FLEXCOM_FLEX_US_MAN_RX_PP_Msk & ((value) << FLEXCOM_FLEX_US_MAN_RX_PP_Pos))
#define   FLEXCOM_FLEX_US_MAN_RX_PP_ALL_ONE_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '1's  */
#define   FLEXCOM_FLEX_US_MAN_RX_PP_ALL_ZERO_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '0's  */
#define   FLEXCOM_FLEX_US_MAN_RX_PP_ZERO_ONE_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '01's  */
#define   FLEXCOM_FLEX_US_MAN_RX_PP_ONE_ZERO_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '10's  */
#define FLEXCOM_FLEX_US_MAN_RX_PP_ALL_ONE     (FLEXCOM_FLEX_US_MAN_RX_PP_ALL_ONE_Val << FLEXCOM_FLEX_US_MAN_RX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '1's Position  */
#define FLEXCOM_FLEX_US_MAN_RX_PP_ALL_ZERO    (FLEXCOM_FLEX_US_MAN_RX_PP_ALL_ZERO_Val << FLEXCOM_FLEX_US_MAN_RX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '0's Position  */
#define FLEXCOM_FLEX_US_MAN_RX_PP_ZERO_ONE    (FLEXCOM_FLEX_US_MAN_RX_PP_ZERO_ONE_Val << FLEXCOM_FLEX_US_MAN_RX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '01's Position  */
#define FLEXCOM_FLEX_US_MAN_RX_PP_ONE_ZERO    (FLEXCOM_FLEX_US_MAN_RX_PP_ONE_ZERO_Val << FLEXCOM_FLEX_US_MAN_RX_PP_Pos) /**< (FLEXCOM_FLEX_US_MAN) The preamble is composed of '10's Position  */
#define FLEXCOM_FLEX_US_MAN_RX_MPOL_Pos       _U_(28)                                        /**< (FLEXCOM_FLEX_US_MAN) Receiver Manchester Polarity Position */
#define FLEXCOM_FLEX_US_MAN_RX_MPOL_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_MAN_RX_MPOL_Pos)  /**< (FLEXCOM_FLEX_US_MAN) Receiver Manchester Polarity Mask */
#define FLEXCOM_FLEX_US_MAN_ONE_Pos           _U_(29)                                        /**< (FLEXCOM_FLEX_US_MAN) Must Be Set to 1 Position */
#define FLEXCOM_FLEX_US_MAN_ONE_Msk           (_U_(0x1) << FLEXCOM_FLEX_US_MAN_ONE_Pos)      /**< (FLEXCOM_FLEX_US_MAN) Must Be Set to 1 Mask */
#define FLEXCOM_FLEX_US_MAN_DRIFT_Pos         _U_(30)                                        /**< (FLEXCOM_FLEX_US_MAN) Drift Compensation Position */
#define FLEXCOM_FLEX_US_MAN_DRIFT_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_MAN_DRIFT_Pos)    /**< (FLEXCOM_FLEX_US_MAN) Drift Compensation Mask */
#define FLEXCOM_FLEX_US_MAN_RXIDLEV_Pos       _U_(31)                                        /**< (FLEXCOM_FLEX_US_MAN) Receiver Idle Value Position */
#define FLEXCOM_FLEX_US_MAN_RXIDLEV_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_MAN_RXIDLEV_Pos)  /**< (FLEXCOM_FLEX_US_MAN) Receiver Idle Value Mask */
#define FLEXCOM_FLEX_US_MAN_Msk               _U_(0xF30F130F)                                /**< (FLEXCOM_FLEX_US_MAN) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LINMR : (FLEXCOM Offset: 0x254) (R/W 32) USART LIN Mode Register -------- */
#define FLEXCOM_FLEX_US_LINMR_NACT_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_US_LINMR) LIN Node Action Position */
#define FLEXCOM_FLEX_US_LINMR_NACT_Msk        (_U_(0x3) << FLEXCOM_FLEX_US_LINMR_NACT_Pos)   /**< (FLEXCOM_FLEX_US_LINMR) LIN Node Action Mask */
#define FLEXCOM_FLEX_US_LINMR_NACT(value)     (FLEXCOM_FLEX_US_LINMR_NACT_Msk & ((value) << FLEXCOM_FLEX_US_LINMR_NACT_Pos))
#define   FLEXCOM_FLEX_US_LINMR_NACT_PUBLISH_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_LINMR) The USART transmits the response.  */
#define   FLEXCOM_FLEX_US_LINMR_NACT_SUBSCRIBE_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_LINMR) The USART receives the response.  */
#define   FLEXCOM_FLEX_US_LINMR_NACT_IGNORE_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_LINMR) The USART does not transmit and does not receive the response.  */
#define FLEXCOM_FLEX_US_LINMR_NACT_PUBLISH    (FLEXCOM_FLEX_US_LINMR_NACT_PUBLISH_Val << FLEXCOM_FLEX_US_LINMR_NACT_Pos) /**< (FLEXCOM_FLEX_US_LINMR) The USART transmits the response. Position  */
#define FLEXCOM_FLEX_US_LINMR_NACT_SUBSCRIBE  (FLEXCOM_FLEX_US_LINMR_NACT_SUBSCRIBE_Val << FLEXCOM_FLEX_US_LINMR_NACT_Pos) /**< (FLEXCOM_FLEX_US_LINMR) The USART receives the response. Position  */
#define FLEXCOM_FLEX_US_LINMR_NACT_IGNORE     (FLEXCOM_FLEX_US_LINMR_NACT_IGNORE_Val << FLEXCOM_FLEX_US_LINMR_NACT_Pos) /**< (FLEXCOM_FLEX_US_LINMR) The USART does not transmit and does not receive the response. Position  */
#define FLEXCOM_FLEX_US_LINMR_PARDIS_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_US_LINMR) Parity Disable Position */
#define FLEXCOM_FLEX_US_LINMR_PARDIS_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_PARDIS_Pos) /**< (FLEXCOM_FLEX_US_LINMR) Parity Disable Mask */
#define FLEXCOM_FLEX_US_LINMR_CHKDIS_Pos      _U_(3)                                         /**< (FLEXCOM_FLEX_US_LINMR) Checksum Disable Position */
#define FLEXCOM_FLEX_US_LINMR_CHKDIS_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_CHKDIS_Pos) /**< (FLEXCOM_FLEX_US_LINMR) Checksum Disable Mask */
#define FLEXCOM_FLEX_US_LINMR_CHKTYP_Pos      _U_(4)                                         /**< (FLEXCOM_FLEX_US_LINMR) Checksum Type Position */
#define FLEXCOM_FLEX_US_LINMR_CHKTYP_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_CHKTYP_Pos) /**< (FLEXCOM_FLEX_US_LINMR) Checksum Type Mask */
#define FLEXCOM_FLEX_US_LINMR_DLM_Pos         _U_(5)                                         /**< (FLEXCOM_FLEX_US_LINMR) Data Length Mode Position */
#define FLEXCOM_FLEX_US_LINMR_DLM_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_DLM_Pos)    /**< (FLEXCOM_FLEX_US_LINMR) Data Length Mode Mask */
#define FLEXCOM_FLEX_US_LINMR_FSDIS_Pos       _U_(6)                                         /**< (FLEXCOM_FLEX_US_LINMR) Frame Slot Mode Disable Position */
#define FLEXCOM_FLEX_US_LINMR_FSDIS_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_FSDIS_Pos)  /**< (FLEXCOM_FLEX_US_LINMR) Frame Slot Mode Disable Mask */
#define FLEXCOM_FLEX_US_LINMR_WKUPTYP_Pos     _U_(7)                                         /**< (FLEXCOM_FLEX_US_LINMR) Wakeup Signal Type Position */
#define FLEXCOM_FLEX_US_LINMR_WKUPTYP_Msk     (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_WKUPTYP_Pos) /**< (FLEXCOM_FLEX_US_LINMR) Wakeup Signal Type Mask */
#define FLEXCOM_FLEX_US_LINMR_DLC_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_US_LINMR) Data Length Control Position */
#define FLEXCOM_FLEX_US_LINMR_DLC_Msk         (_U_(0xFF) << FLEXCOM_FLEX_US_LINMR_DLC_Pos)   /**< (FLEXCOM_FLEX_US_LINMR) Data Length Control Mask */
#define FLEXCOM_FLEX_US_LINMR_DLC(value)      (FLEXCOM_FLEX_US_LINMR_DLC_Msk & ((value) << FLEXCOM_FLEX_US_LINMR_DLC_Pos))
#define FLEXCOM_FLEX_US_LINMR_PDCM_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_US_LINMR) DMAC Mode Position */
#define FLEXCOM_FLEX_US_LINMR_PDCM_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_PDCM_Pos)   /**< (FLEXCOM_FLEX_US_LINMR) DMAC Mode Mask */
#define FLEXCOM_FLEX_US_LINMR_SYNCDIS_Pos     _U_(17)                                        /**< (FLEXCOM_FLEX_US_LINMR) Synchronization Disable Position */
#define FLEXCOM_FLEX_US_LINMR_SYNCDIS_Msk     (_U_(0x1) << FLEXCOM_FLEX_US_LINMR_SYNCDIS_Pos) /**< (FLEXCOM_FLEX_US_LINMR) Synchronization Disable Mask */
#define FLEXCOM_FLEX_US_LINMR_Msk             _U_(0x0003FFFF)                                /**< (FLEXCOM_FLEX_US_LINMR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LINIR : (FLEXCOM Offset: 0x258) (R/W 32) USART LIN Identifier Register -------- */
#define FLEXCOM_FLEX_US_LINIR_IDCHR_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_US_LINIR) Identifier Character Position */
#define FLEXCOM_FLEX_US_LINIR_IDCHR_Msk       (_U_(0xFF) << FLEXCOM_FLEX_US_LINIR_IDCHR_Pos) /**< (FLEXCOM_FLEX_US_LINIR) Identifier Character Mask */
#define FLEXCOM_FLEX_US_LINIR_IDCHR(value)    (FLEXCOM_FLEX_US_LINIR_IDCHR_Msk & ((value) << FLEXCOM_FLEX_US_LINIR_IDCHR_Pos))
#define FLEXCOM_FLEX_US_LINIR_Msk             _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_US_LINIR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LINBRR : (FLEXCOM Offset: 0x25C) ( R/ 32) USART LIN Baud Rate Register -------- */
#define FLEXCOM_FLEX_US_LINBRR_LINCD_Pos      _U_(0)                                         /**< (FLEXCOM_FLEX_US_LINBRR) Clock Divider after Synchronization Position */
#define FLEXCOM_FLEX_US_LINBRR_LINCD_Msk      (_U_(0xFFFF) << FLEXCOM_FLEX_US_LINBRR_LINCD_Pos) /**< (FLEXCOM_FLEX_US_LINBRR) Clock Divider after Synchronization Mask */
#define FLEXCOM_FLEX_US_LINBRR_LINCD(value)   (FLEXCOM_FLEX_US_LINBRR_LINCD_Msk & ((value) << FLEXCOM_FLEX_US_LINBRR_LINCD_Pos))
#define FLEXCOM_FLEX_US_LINBRR_LINFP_Pos      _U_(16)                                        /**< (FLEXCOM_FLEX_US_LINBRR) Fractional Part after Synchronization Position */
#define FLEXCOM_FLEX_US_LINBRR_LINFP_Msk      (_U_(0x7) << FLEXCOM_FLEX_US_LINBRR_LINFP_Pos) /**< (FLEXCOM_FLEX_US_LINBRR) Fractional Part after Synchronization Mask */
#define FLEXCOM_FLEX_US_LINBRR_LINFP(value)   (FLEXCOM_FLEX_US_LINBRR_LINFP_Msk & ((value) << FLEXCOM_FLEX_US_LINBRR_LINFP_Pos))
#define FLEXCOM_FLEX_US_LINBRR_Msk            _U_(0x0007FFFF)                                /**< (FLEXCOM_FLEX_US_LINBRR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONMR : (FLEXCOM Offset: 0x260) (R/W 32) USART LON Mode Register -------- */
#define FLEXCOM_FLEX_US_LONMR_COMMT_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONMR) LON comm_type Parameter Value Position */
#define FLEXCOM_FLEX_US_LONMR_COMMT_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_LONMR_COMMT_Pos)  /**< (FLEXCOM_FLEX_US_LONMR) LON comm_type Parameter Value Mask */
#define FLEXCOM_FLEX_US_LONMR_COLDET_Pos      _U_(1)                                         /**< (FLEXCOM_FLEX_US_LONMR) LON Collision Detection Feature Position */
#define FLEXCOM_FLEX_US_LONMR_COLDET_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_LONMR_COLDET_Pos) /**< (FLEXCOM_FLEX_US_LONMR) LON Collision Detection Feature Mask */
#define FLEXCOM_FLEX_US_LONMR_TCOL_Pos        _U_(2)                                         /**< (FLEXCOM_FLEX_US_LONMR) Terminate Frame upon Collision Notification Position */
#define FLEXCOM_FLEX_US_LONMR_TCOL_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_LONMR_TCOL_Pos)   /**< (FLEXCOM_FLEX_US_LONMR) Terminate Frame upon Collision Notification Mask */
#define FLEXCOM_FLEX_US_LONMR_CDTAIL_Pos      _U_(3)                                         /**< (FLEXCOM_FLEX_US_LONMR) LON Collision Detection on Frame Tail Position */
#define FLEXCOM_FLEX_US_LONMR_CDTAIL_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_LONMR_CDTAIL_Pos) /**< (FLEXCOM_FLEX_US_LONMR) LON Collision Detection on Frame Tail Mask */
#define FLEXCOM_FLEX_US_LONMR_DMAM_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_US_LONMR) LON DMA Mode Position */
#define FLEXCOM_FLEX_US_LONMR_DMAM_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_LONMR_DMAM_Pos)   /**< (FLEXCOM_FLEX_US_LONMR) LON DMA Mode Mask */
#define FLEXCOM_FLEX_US_LONMR_LCDS_Pos        _U_(5)                                         /**< (FLEXCOM_FLEX_US_LONMR) LON Collision Detection Source Position */
#define FLEXCOM_FLEX_US_LONMR_LCDS_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_LONMR_LCDS_Pos)   /**< (FLEXCOM_FLEX_US_LONMR) LON Collision Detection Source Mask */
#define FLEXCOM_FLEX_US_LONMR_EOFS_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_US_LONMR) End of Frame Condition Size Position */
#define FLEXCOM_FLEX_US_LONMR_EOFS_Msk        (_U_(0xFF) << FLEXCOM_FLEX_US_LONMR_EOFS_Pos)  /**< (FLEXCOM_FLEX_US_LONMR) End of Frame Condition Size Mask */
#define FLEXCOM_FLEX_US_LONMR_EOFS(value)     (FLEXCOM_FLEX_US_LONMR_EOFS_Msk & ((value) << FLEXCOM_FLEX_US_LONMR_EOFS_Pos))
#define FLEXCOM_FLEX_US_LONMR_Msk             _U_(0x00FF003F)                                /**< (FLEXCOM_FLEX_US_LONMR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONPR : (FLEXCOM Offset: 0x264) (R/W 32) USART LON Preamble Register -------- */
#define FLEXCOM_FLEX_US_LONPR_LONPL_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONPR) LON Preamble Length Position */
#define FLEXCOM_FLEX_US_LONPR_LONPL_Msk       (_U_(0x3FFF) << FLEXCOM_FLEX_US_LONPR_LONPL_Pos) /**< (FLEXCOM_FLEX_US_LONPR) LON Preamble Length Mask */
#define FLEXCOM_FLEX_US_LONPR_LONPL(value)    (FLEXCOM_FLEX_US_LONPR_LONPL_Msk & ((value) << FLEXCOM_FLEX_US_LONPR_LONPL_Pos))
#define FLEXCOM_FLEX_US_LONPR_Msk             _U_(0x00003FFF)                                /**< (FLEXCOM_FLEX_US_LONPR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONDL : (FLEXCOM Offset: 0x268) (R/W 32) USART LON Data Length Register -------- */
#define FLEXCOM_FLEX_US_LONDL_LONDL_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONDL) LON Data Length Position */
#define FLEXCOM_FLEX_US_LONDL_LONDL_Msk       (_U_(0xFF) << FLEXCOM_FLEX_US_LONDL_LONDL_Pos) /**< (FLEXCOM_FLEX_US_LONDL) LON Data Length Mask */
#define FLEXCOM_FLEX_US_LONDL_LONDL(value)    (FLEXCOM_FLEX_US_LONDL_LONDL_Msk & ((value) << FLEXCOM_FLEX_US_LONDL_LONDL_Pos))
#define FLEXCOM_FLEX_US_LONDL_Msk             _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_US_LONDL) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONL2HDR : (FLEXCOM Offset: 0x26C) (R/W 32) USART LON L2HDR Register -------- */
#define FLEXCOM_FLEX_US_LONL2HDR_BLI_Pos      _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONL2HDR) LON Backlog Increment Position */
#define FLEXCOM_FLEX_US_LONL2HDR_BLI_Msk      (_U_(0x3F) << FLEXCOM_FLEX_US_LONL2HDR_BLI_Pos) /**< (FLEXCOM_FLEX_US_LONL2HDR) LON Backlog Increment Mask */
#define FLEXCOM_FLEX_US_LONL2HDR_BLI(value)   (FLEXCOM_FLEX_US_LONL2HDR_BLI_Msk & ((value) << FLEXCOM_FLEX_US_LONL2HDR_BLI_Pos))
#define FLEXCOM_FLEX_US_LONL2HDR_ALTP_Pos     _U_(6)                                         /**< (FLEXCOM_FLEX_US_LONL2HDR) LON Alternate Path Bit Position */
#define FLEXCOM_FLEX_US_LONL2HDR_ALTP_Msk     (_U_(0x1) << FLEXCOM_FLEX_US_LONL2HDR_ALTP_Pos) /**< (FLEXCOM_FLEX_US_LONL2HDR) LON Alternate Path Bit Mask */
#define FLEXCOM_FLEX_US_LONL2HDR_PB_Pos       _U_(7)                                         /**< (FLEXCOM_FLEX_US_LONL2HDR) LON Priority Bit Position */
#define FLEXCOM_FLEX_US_LONL2HDR_PB_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_LONL2HDR_PB_Pos)  /**< (FLEXCOM_FLEX_US_LONL2HDR) LON Priority Bit Mask */
#define FLEXCOM_FLEX_US_LONL2HDR_Msk          _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_US_LONL2HDR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONBL : (FLEXCOM Offset: 0x270) ( R/ 32) USART LON Backlog Register -------- */
#define FLEXCOM_FLEX_US_LONBL_LONBL_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONBL) LON Node Backlog Value Position */
#define FLEXCOM_FLEX_US_LONBL_LONBL_Msk       (_U_(0x3F) << FLEXCOM_FLEX_US_LONBL_LONBL_Pos) /**< (FLEXCOM_FLEX_US_LONBL) LON Node Backlog Value Mask */
#define FLEXCOM_FLEX_US_LONBL_LONBL(value)    (FLEXCOM_FLEX_US_LONBL_LONBL_Msk & ((value) << FLEXCOM_FLEX_US_LONBL_LONBL_Pos))
#define FLEXCOM_FLEX_US_LONBL_Msk             _U_(0x0000003F)                                /**< (FLEXCOM_FLEX_US_LONBL) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONB1TX : (FLEXCOM Offset: 0x274) (R/W 32) USART LON Beta1 Tx Register -------- */
#define FLEXCOM_FLEX_US_LONB1TX_BETA1TX_Pos   _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONB1TX) LON Beta1 Length after Transmission Position */
#define FLEXCOM_FLEX_US_LONB1TX_BETA1TX_Msk   (_U_(0xFFFFFF) << FLEXCOM_FLEX_US_LONB1TX_BETA1TX_Pos) /**< (FLEXCOM_FLEX_US_LONB1TX) LON Beta1 Length after Transmission Mask */
#define FLEXCOM_FLEX_US_LONB1TX_BETA1TX(value) (FLEXCOM_FLEX_US_LONB1TX_BETA1TX_Msk & ((value) << FLEXCOM_FLEX_US_LONB1TX_BETA1TX_Pos))
#define FLEXCOM_FLEX_US_LONB1TX_Msk           _U_(0x00FFFFFF)                                /**< (FLEXCOM_FLEX_US_LONB1TX) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONB1RX : (FLEXCOM Offset: 0x278) (R/W 32) USART LON Beta1 Rx Register -------- */
#define FLEXCOM_FLEX_US_LONB1RX_BETA1RX_Pos   _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONB1RX) LON Beta1 Length after Reception Position */
#define FLEXCOM_FLEX_US_LONB1RX_BETA1RX_Msk   (_U_(0xFFFFFF) << FLEXCOM_FLEX_US_LONB1RX_BETA1RX_Pos) /**< (FLEXCOM_FLEX_US_LONB1RX) LON Beta1 Length after Reception Mask */
#define FLEXCOM_FLEX_US_LONB1RX_BETA1RX(value) (FLEXCOM_FLEX_US_LONB1RX_BETA1RX_Msk & ((value) << FLEXCOM_FLEX_US_LONB1RX_BETA1RX_Pos))
#define FLEXCOM_FLEX_US_LONB1RX_Msk           _U_(0x00FFFFFF)                                /**< (FLEXCOM_FLEX_US_LONB1RX) Register Mask  */


/* -------- FLEXCOM_FLEX_US_LONPRIO : (FLEXCOM Offset: 0x27C) (R/W 32) USART LON Priority Register -------- */
#define FLEXCOM_FLEX_US_LONPRIO_PSNB_Pos      _U_(0)                                         /**< (FLEXCOM_FLEX_US_LONPRIO) LON Priority Slot Number Position */
#define FLEXCOM_FLEX_US_LONPRIO_PSNB_Msk      (_U_(0x7F) << FLEXCOM_FLEX_US_LONPRIO_PSNB_Pos) /**< (FLEXCOM_FLEX_US_LONPRIO) LON Priority Slot Number Mask */
#define FLEXCOM_FLEX_US_LONPRIO_PSNB(value)   (FLEXCOM_FLEX_US_LONPRIO_PSNB_Msk & ((value) << FLEXCOM_FLEX_US_LONPRIO_PSNB_Pos))
#define FLEXCOM_FLEX_US_LONPRIO_NPS_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_US_LONPRIO) LON Node Priority Slot Position */
#define FLEXCOM_FLEX_US_LONPRIO_NPS_Msk       (_U_(0x7F) << FLEXCOM_FLEX_US_LONPRIO_NPS_Pos) /**< (FLEXCOM_FLEX_US_LONPRIO) LON Node Priority Slot Mask */
#define FLEXCOM_FLEX_US_LONPRIO_NPS(value)    (FLEXCOM_FLEX_US_LONPRIO_NPS_Msk & ((value) << FLEXCOM_FLEX_US_LONPRIO_NPS_Pos))
#define FLEXCOM_FLEX_US_LONPRIO_Msk           _U_(0x00007F7F)                                /**< (FLEXCOM_FLEX_US_LONPRIO) Register Mask  */


/* -------- FLEXCOM_FLEX_US_IDTTX : (FLEXCOM Offset: 0x280) (R/W 32) USART LON IDT Tx Register -------- */
#define FLEXCOM_FLEX_US_IDTTX_IDTTX_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_US_IDTTX) LON Indeterminate Time after Transmission (comm_type = 1 mode only) Position */
#define FLEXCOM_FLEX_US_IDTTX_IDTTX_Msk       (_U_(0xFFFFFF) << FLEXCOM_FLEX_US_IDTTX_IDTTX_Pos) /**< (FLEXCOM_FLEX_US_IDTTX) LON Indeterminate Time after Transmission (comm_type = 1 mode only) Mask */
#define FLEXCOM_FLEX_US_IDTTX_IDTTX(value)    (FLEXCOM_FLEX_US_IDTTX_IDTTX_Msk & ((value) << FLEXCOM_FLEX_US_IDTTX_IDTTX_Pos))
#define FLEXCOM_FLEX_US_IDTTX_Msk             _U_(0x00FFFFFF)                                /**< (FLEXCOM_FLEX_US_IDTTX) Register Mask  */


/* -------- FLEXCOM_FLEX_US_IDTRX : (FLEXCOM Offset: 0x284) (R/W 32) USART LON IDT Rx Register -------- */
#define FLEXCOM_FLEX_US_IDTRX_IDTRX_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_US_IDTRX) LON Indeterminate Time after Reception (comm_type = 1 mode only) Position */
#define FLEXCOM_FLEX_US_IDTRX_IDTRX_Msk       (_U_(0xFFFFFF) << FLEXCOM_FLEX_US_IDTRX_IDTRX_Pos) /**< (FLEXCOM_FLEX_US_IDTRX) LON Indeterminate Time after Reception (comm_type = 1 mode only) Mask */
#define FLEXCOM_FLEX_US_IDTRX_IDTRX(value)    (FLEXCOM_FLEX_US_IDTRX_IDTRX_Msk & ((value) << FLEXCOM_FLEX_US_IDTRX_IDTRX_Pos))
#define FLEXCOM_FLEX_US_IDTRX_Msk             _U_(0x00FFFFFF)                                /**< (FLEXCOM_FLEX_US_IDTRX) Register Mask  */


/* -------- FLEXCOM_FLEX_US_ICDIFF : (FLEXCOM Offset: 0x288) (R/W 32) USART IC DIFF Register -------- */
#define FLEXCOM_FLEX_US_ICDIFF_ICDIFF_Pos     _U_(0)                                         /**< (FLEXCOM_FLEX_US_ICDIFF) IC Differentiator Number Position */
#define FLEXCOM_FLEX_US_ICDIFF_ICDIFF_Msk     (_U_(0xF) << FLEXCOM_FLEX_US_ICDIFF_ICDIFF_Pos) /**< (FLEXCOM_FLEX_US_ICDIFF) IC Differentiator Number Mask */
#define FLEXCOM_FLEX_US_ICDIFF_ICDIFF(value)  (FLEXCOM_FLEX_US_ICDIFF_ICDIFF_Msk & ((value) << FLEXCOM_FLEX_US_ICDIFF_ICDIFF_Pos))
#define FLEXCOM_FLEX_US_ICDIFF_Msk            _U_(0x0000000F)                                /**< (FLEXCOM_FLEX_US_ICDIFF) Register Mask  */


/* -------- FLEXCOM_FLEX_US_CMPR : (FLEXCOM Offset: 0x290) (R/W 32) USART Comparison Register -------- */
#define FLEXCOM_FLEX_US_CMPR_VAL1_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_CMPR) First Comparison Value for Received Character Position */
#define FLEXCOM_FLEX_US_CMPR_VAL1_Msk         (_U_(0x1FF) << FLEXCOM_FLEX_US_CMPR_VAL1_Pos)  /**< (FLEXCOM_FLEX_US_CMPR) First Comparison Value for Received Character Mask */
#define FLEXCOM_FLEX_US_CMPR_VAL1(value)      (FLEXCOM_FLEX_US_CMPR_VAL1_Msk & ((value) << FLEXCOM_FLEX_US_CMPR_VAL1_Pos))
#define FLEXCOM_FLEX_US_CMPR_CMPMODE_Pos      _U_(12)                                        /**< (FLEXCOM_FLEX_US_CMPR) Comparison Mode Position */
#define FLEXCOM_FLEX_US_CMPR_CMPMODE_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_CMPR_CMPMODE_Pos) /**< (FLEXCOM_FLEX_US_CMPR) Comparison Mode Mask */
#define   FLEXCOM_FLEX_US_CMPR_CMPMODE_FLAG_ONLY_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_CMPR) Any character is received and comparison function drives CMP flag.  */
#define   FLEXCOM_FLEX_US_CMPR_CMPMODE_START_CONDITION_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_CMPR) Comparison condition must be met to start reception.  */
#define FLEXCOM_FLEX_US_CMPR_CMPMODE_FLAG_ONLY (FLEXCOM_FLEX_US_CMPR_CMPMODE_FLAG_ONLY_Val << FLEXCOM_FLEX_US_CMPR_CMPMODE_Pos) /**< (FLEXCOM_FLEX_US_CMPR) Any character is received and comparison function drives CMP flag. Position  */
#define FLEXCOM_FLEX_US_CMPR_CMPMODE_START_CONDITION (FLEXCOM_FLEX_US_CMPR_CMPMODE_START_CONDITION_Val << FLEXCOM_FLEX_US_CMPR_CMPMODE_Pos) /**< (FLEXCOM_FLEX_US_CMPR) Comparison condition must be met to start reception. Position  */
#define FLEXCOM_FLEX_US_CMPR_CMPPAR_Pos       _U_(14)                                        /**< (FLEXCOM_FLEX_US_CMPR) Compare Parity Position */
#define FLEXCOM_FLEX_US_CMPR_CMPPAR_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_CMPR_CMPPAR_Pos)  /**< (FLEXCOM_FLEX_US_CMPR) Compare Parity Mask */
#define FLEXCOM_FLEX_US_CMPR_VAL2_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_US_CMPR) Second Comparison Value for Received Character Position */
#define FLEXCOM_FLEX_US_CMPR_VAL2_Msk         (_U_(0x1FF) << FLEXCOM_FLEX_US_CMPR_VAL2_Pos)  /**< (FLEXCOM_FLEX_US_CMPR) Second Comparison Value for Received Character Mask */
#define FLEXCOM_FLEX_US_CMPR_VAL2(value)      (FLEXCOM_FLEX_US_CMPR_VAL2_Msk & ((value) << FLEXCOM_FLEX_US_CMPR_VAL2_Pos))
#define FLEXCOM_FLEX_US_CMPR_Msk              _U_(0x01FF51FF)                                /**< (FLEXCOM_FLEX_US_CMPR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_FMR : (FLEXCOM Offset: 0x2A0) (R/W 32) USART FIFO Mode Register -------- */
#define FLEXCOM_FLEX_US_FMR_TXRDYM_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_US_FMR) Transmitter Ready Mode Position */
#define FLEXCOM_FLEX_US_FMR_TXRDYM_Msk        (_U_(0x3) << FLEXCOM_FLEX_US_FMR_TXRDYM_Pos)   /**< (FLEXCOM_FLEX_US_FMR) Transmitter Ready Mode Mask */
#define FLEXCOM_FLEX_US_FMR_TXRDYM(value)     (FLEXCOM_FLEX_US_FMR_TXRDYM_Msk & ((value) << FLEXCOM_FLEX_US_FMR_TXRDYM_Pos))
#define   FLEXCOM_FLEX_US_FMR_TXRDYM_ONE_DATA_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_FMR) TXRDY will be at level '1' when at least one data can be written in the Transmit FIFO  */
#define   FLEXCOM_FLEX_US_FMR_TXRDYM_TWO_DATA_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_FMR) TXRDY will be at level '1' when at least two data can be written in the Transmit FIFO  */
#define   FLEXCOM_FLEX_US_FMR_TXRDYM_FOUR_DATA_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_FMR) TXRDY will be at level '1' when at least four data can be written in the Transmit FIFO  */
#define FLEXCOM_FLEX_US_FMR_TXRDYM_ONE_DATA   (FLEXCOM_FLEX_US_FMR_TXRDYM_ONE_DATA_Val << FLEXCOM_FLEX_US_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_US_FMR) TXRDY will be at level '1' when at least one data can be written in the Transmit FIFO Position  */
#define FLEXCOM_FLEX_US_FMR_TXRDYM_TWO_DATA   (FLEXCOM_FLEX_US_FMR_TXRDYM_TWO_DATA_Val << FLEXCOM_FLEX_US_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_US_FMR) TXRDY will be at level '1' when at least two data can be written in the Transmit FIFO Position  */
#define FLEXCOM_FLEX_US_FMR_TXRDYM_FOUR_DATA  (FLEXCOM_FLEX_US_FMR_TXRDYM_FOUR_DATA_Val << FLEXCOM_FLEX_US_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_US_FMR) TXRDY will be at level '1' when at least four data can be written in the Transmit FIFO Position  */
#define FLEXCOM_FLEX_US_FMR_RXRDYM_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_US_FMR) Receiver Ready Mode Position */
#define FLEXCOM_FLEX_US_FMR_RXRDYM_Msk        (_U_(0x3) << FLEXCOM_FLEX_US_FMR_RXRDYM_Pos)   /**< (FLEXCOM_FLEX_US_FMR) Receiver Ready Mode Mask */
#define FLEXCOM_FLEX_US_FMR_RXRDYM(value)     (FLEXCOM_FLEX_US_FMR_RXRDYM_Msk & ((value) << FLEXCOM_FLEX_US_FMR_RXRDYM_Pos))
#define   FLEXCOM_FLEX_US_FMR_RXRDYM_ONE_DATA_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_US_FMR) RXRDY will be at level '1' when at least one unread data is in the Receive FIFO  */
#define   FLEXCOM_FLEX_US_FMR_RXRDYM_TWO_DATA_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_US_FMR) RXRDY will be at level '1' when at least two unread data are in the Receive FIFO  */
#define   FLEXCOM_FLEX_US_FMR_RXRDYM_FOUR_DATA_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_US_FMR) RXRDY will be at level '1' when at least four unread data are in the Receive FIFO  */
#define FLEXCOM_FLEX_US_FMR_RXRDYM_ONE_DATA   (FLEXCOM_FLEX_US_FMR_RXRDYM_ONE_DATA_Val << FLEXCOM_FLEX_US_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_US_FMR) RXRDY will be at level '1' when at least one unread data is in the Receive FIFO Position  */
#define FLEXCOM_FLEX_US_FMR_RXRDYM_TWO_DATA   (FLEXCOM_FLEX_US_FMR_RXRDYM_TWO_DATA_Val << FLEXCOM_FLEX_US_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_US_FMR) RXRDY will be at level '1' when at least two unread data are in the Receive FIFO Position  */
#define FLEXCOM_FLEX_US_FMR_RXRDYM_FOUR_DATA  (FLEXCOM_FLEX_US_FMR_RXRDYM_FOUR_DATA_Val << FLEXCOM_FLEX_US_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_US_FMR) RXRDY will be at level '1' when at least four unread data are in the Receive FIFO Position  */
#define FLEXCOM_FLEX_US_FMR_FRTSC_Pos         _U_(7)                                         /**< (FLEXCOM_FLEX_US_FMR) FIFO RTS Pin Control enable (Hardware Handshaking mode only) Position */
#define FLEXCOM_FLEX_US_FMR_FRTSC_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_FMR_FRTSC_Pos)    /**< (FLEXCOM_FLEX_US_FMR) FIFO RTS Pin Control enable (Hardware Handshaking mode only) Mask */
#define FLEXCOM_FLEX_US_FMR_TXFTHRES_Pos      _U_(8)                                         /**< (FLEXCOM_FLEX_US_FMR) Transmit FIFO Threshold Position */
#define FLEXCOM_FLEX_US_FMR_TXFTHRES_Msk      (_U_(0x3F) << FLEXCOM_FLEX_US_FMR_TXFTHRES_Pos) /**< (FLEXCOM_FLEX_US_FMR) Transmit FIFO Threshold Mask */
#define FLEXCOM_FLEX_US_FMR_TXFTHRES(value)   (FLEXCOM_FLEX_US_FMR_TXFTHRES_Msk & ((value) << FLEXCOM_FLEX_US_FMR_TXFTHRES_Pos))
#define FLEXCOM_FLEX_US_FMR_RXFTHRES_Pos      _U_(16)                                        /**< (FLEXCOM_FLEX_US_FMR) Receive FIFO Threshold Position */
#define FLEXCOM_FLEX_US_FMR_RXFTHRES_Msk      (_U_(0x3F) << FLEXCOM_FLEX_US_FMR_RXFTHRES_Pos) /**< (FLEXCOM_FLEX_US_FMR) Receive FIFO Threshold Mask */
#define FLEXCOM_FLEX_US_FMR_RXFTHRES(value)   (FLEXCOM_FLEX_US_FMR_RXFTHRES_Msk & ((value) << FLEXCOM_FLEX_US_FMR_RXFTHRES_Pos))
#define FLEXCOM_FLEX_US_FMR_RXFTHRES2_Pos     _U_(24)                                        /**< (FLEXCOM_FLEX_US_FMR) Receive FIFO Threshold 2 Position */
#define FLEXCOM_FLEX_US_FMR_RXFTHRES2_Msk     (_U_(0x3F) << FLEXCOM_FLEX_US_FMR_RXFTHRES2_Pos) /**< (FLEXCOM_FLEX_US_FMR) Receive FIFO Threshold 2 Mask */
#define FLEXCOM_FLEX_US_FMR_RXFTHRES2(value)  (FLEXCOM_FLEX_US_FMR_RXFTHRES2_Msk & ((value) << FLEXCOM_FLEX_US_FMR_RXFTHRES2_Pos))
#define FLEXCOM_FLEX_US_FMR_Msk               _U_(0x3F3F3FB3)                                /**< (FLEXCOM_FLEX_US_FMR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_FLR : (FLEXCOM Offset: 0x2A4) ( R/ 32) USART FIFO Level Register -------- */
#define FLEXCOM_FLEX_US_FLR_TXFL_Pos          _U_(0)                                         /**< (FLEXCOM_FLEX_US_FLR) Transmit FIFO Level Position */
#define FLEXCOM_FLEX_US_FLR_TXFL_Msk          (_U_(0x3F) << FLEXCOM_FLEX_US_FLR_TXFL_Pos)    /**< (FLEXCOM_FLEX_US_FLR) Transmit FIFO Level Mask */
#define FLEXCOM_FLEX_US_FLR_TXFL(value)       (FLEXCOM_FLEX_US_FLR_TXFL_Msk & ((value) << FLEXCOM_FLEX_US_FLR_TXFL_Pos))
#define FLEXCOM_FLEX_US_FLR_RXFL_Pos          _U_(16)                                        /**< (FLEXCOM_FLEX_US_FLR) Receive FIFO Level Position */
#define FLEXCOM_FLEX_US_FLR_RXFL_Msk          (_U_(0x3F) << FLEXCOM_FLEX_US_FLR_RXFL_Pos)    /**< (FLEXCOM_FLEX_US_FLR) Receive FIFO Level Mask */
#define FLEXCOM_FLEX_US_FLR_RXFL(value)       (FLEXCOM_FLEX_US_FLR_RXFL_Msk & ((value) << FLEXCOM_FLEX_US_FLR_RXFL_Pos))
#define FLEXCOM_FLEX_US_FLR_Msk               _U_(0x003F003F)                                /**< (FLEXCOM_FLEX_US_FLR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_FIER : (FLEXCOM Offset: 0x2A8) ( /W 32) USART FIFO Interrupt Enable Register -------- */
#define FLEXCOM_FLEX_US_FIER_TXFEF_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_US_FIER) TXFEF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIER_TXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FIER) TXFEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_TXFFF_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_US_FIER) TXFFF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIER_TXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FIER) TXFFF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_TXFTHF_Pos       _U_(2)                                         /**< (FLEXCOM_FLEX_US_FIER) TXFTHF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FIER_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FIER) TXFTHF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_RXFEF_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_US_FIER) RXFEF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIER_RXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FIER) RXFEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_RXFFF_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_US_FIER) RXFFF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIER_RXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FIER) RXFFF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_RXFTHF_Pos       _U_(5)                                         /**< (FLEXCOM_FLEX_US_FIER) RXFTHF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FIER_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FIER) RXFTHF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_TXFPTEF_Pos      _U_(6)                                         /**< (FLEXCOM_FLEX_US_FIER) TXFPTEF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIER_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FIER) TXFPTEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_RXFPTEF_Pos      _U_(7)                                         /**< (FLEXCOM_FLEX_US_FIER) RXFPTEF Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIER_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FIER) RXFPTEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_RXFTHF2_Pos      _U_(9)                                         /**< (FLEXCOM_FLEX_US_FIER) RXFTHF2 Interrupt Enable Position */
#define FLEXCOM_FLEX_US_FIER_RXFTHF2_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIER_RXFTHF2_Pos) /**< (FLEXCOM_FLEX_US_FIER) RXFTHF2 Interrupt Enable Mask */
#define FLEXCOM_FLEX_US_FIER_Msk              _U_(0x000002FF)                                /**< (FLEXCOM_FLEX_US_FIER) Register Mask  */


/* -------- FLEXCOM_FLEX_US_FIDR : (FLEXCOM Offset: 0x2AC) ( /W 32) USART FIFO Interrupt Disable Register -------- */
#define FLEXCOM_FLEX_US_FIDR_TXFEF_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_US_FIDR) TXFEF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_TXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FIDR) TXFEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_TXFFF_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_US_FIDR) TXFFF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_TXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FIDR) TXFFF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_TXFTHF_Pos       _U_(2)                                         /**< (FLEXCOM_FLEX_US_FIDR) TXFTHF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FIDR) TXFTHF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_RXFEF_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_US_FIDR) RXFEF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_RXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FIDR) RXFEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_RXFFF_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_US_FIDR) RXFFF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_RXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FIDR) RXFFF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_RXFTHF_Pos       _U_(5)                                         /**< (FLEXCOM_FLEX_US_FIDR) RXFTHF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FIDR) RXFTHF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_TXFPTEF_Pos      _U_(6)                                         /**< (FLEXCOM_FLEX_US_FIDR) TXFPTEF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FIDR) TXFPTEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_RXFPTEF_Pos      _U_(7)                                         /**< (FLEXCOM_FLEX_US_FIDR) RXFPTEF Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FIDR) RXFPTEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_RXFTHF2_Pos      _U_(9)                                         /**< (FLEXCOM_FLEX_US_FIDR) RXFTHF2 Interrupt Disable Position */
#define FLEXCOM_FLEX_US_FIDR_RXFTHF2_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIDR_RXFTHF2_Pos) /**< (FLEXCOM_FLEX_US_FIDR) RXFTHF2 Interrupt Disable Mask */
#define FLEXCOM_FLEX_US_FIDR_Msk              _U_(0x000002FF)                                /**< (FLEXCOM_FLEX_US_FIDR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_FIMR : (FLEXCOM Offset: 0x2B0) ( R/ 32) USART FIFO Interrupt Mask Register -------- */
#define FLEXCOM_FLEX_US_FIMR_TXFEF_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_US_FIMR) TXFEF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_TXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FIMR) TXFEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_TXFFF_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_US_FIMR) TXFFF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_TXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FIMR) TXFFF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_TXFTHF_Pos       _U_(2)                                         /**< (FLEXCOM_FLEX_US_FIMR) TXFTHF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FIMR) TXFTHF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_RXFEF_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_US_FIMR) RXFEF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_RXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FIMR) RXFEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_RXFFF_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_US_FIMR) RXFFF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_RXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FIMR) RXFFF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_RXFTHF_Pos       _U_(5)                                         /**< (FLEXCOM_FLEX_US_FIMR) RXFTHF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FIMR) RXFTHF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_TXFPTEF_Pos      _U_(6)                                         /**< (FLEXCOM_FLEX_US_FIMR) TXFPTEF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FIMR) TXFPTEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_RXFPTEF_Pos      _U_(7)                                         /**< (FLEXCOM_FLEX_US_FIMR) RXFPTEF Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FIMR) RXFPTEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_RXFTHF2_Pos      _U_(9)                                         /**< (FLEXCOM_FLEX_US_FIMR) RXFTHF2 Interrupt Mask Position */
#define FLEXCOM_FLEX_US_FIMR_RXFTHF2_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FIMR_RXFTHF2_Pos) /**< (FLEXCOM_FLEX_US_FIMR) RXFTHF2 Interrupt Mask Mask */
#define FLEXCOM_FLEX_US_FIMR_Msk              _U_(0x000002FF)                                /**< (FLEXCOM_FLEX_US_FIMR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_FESR : (FLEXCOM Offset: 0x2B4) ( R/ 32) USART FIFO Event Status Register -------- */
#define FLEXCOM_FLEX_US_FESR_TXFEF_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Empty Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Position */
#define FLEXCOM_FLEX_US_FESR_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FESR_TXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Empty Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Mask */
#define FLEXCOM_FLEX_US_FESR_TXFFF_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Full Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Position */
#define FLEXCOM_FLEX_US_FESR_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FESR_TXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Full Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Mask */
#define FLEXCOM_FLEX_US_FESR_TXFTHF_Pos       _U_(2)                                         /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Threshold Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Position */
#define FLEXCOM_FLEX_US_FESR_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FESR_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Threshold Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Mask */
#define FLEXCOM_FLEX_US_FESR_RXFEF_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Empty Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Position */
#define FLEXCOM_FLEX_US_FESR_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FESR_RXFEF_Pos)   /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Empty Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Mask */
#define FLEXCOM_FLEX_US_FESR_RXFFF_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Full Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Position */
#define FLEXCOM_FLEX_US_FESR_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_US_FESR_RXFFF_Pos)   /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Full Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Mask */
#define FLEXCOM_FLEX_US_FESR_RXFTHF_Pos       _U_(5)                                         /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Threshold Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Position */
#define FLEXCOM_FLEX_US_FESR_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_US_FESR_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Threshold Flag (cleared by writing the FLEX_US_CR.RSTSTA bit) Mask */
#define FLEXCOM_FLEX_US_FESR_TXFPTEF_Pos      _U_(6)                                         /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Pointer Error Flag Position */
#define FLEXCOM_FLEX_US_FESR_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FESR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Pointer Error Flag Mask */
#define FLEXCOM_FLEX_US_FESR_RXFPTEF_Pos      _U_(7)                                         /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Pointer Error Flag Position */
#define FLEXCOM_FLEX_US_FESR_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FESR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Pointer Error Flag Mask */
#define FLEXCOM_FLEX_US_FESR_TXFLOCK_Pos      _U_(8)                                         /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Lock Position */
#define FLEXCOM_FLEX_US_FESR_TXFLOCK_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FESR_TXFLOCK_Pos) /**< (FLEXCOM_FLEX_US_FESR) Transmit FIFO Lock Mask */
#define FLEXCOM_FLEX_US_FESR_RXFTHF2_Pos      _U_(9)                                         /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Threshold Flag 2 (cleared by writing the FLEX_US_CR.RSTSTA bit) Position */
#define FLEXCOM_FLEX_US_FESR_RXFTHF2_Msk      (_U_(0x1) << FLEXCOM_FLEX_US_FESR_RXFTHF2_Pos) /**< (FLEXCOM_FLEX_US_FESR) Receive FIFO Threshold Flag 2 (cleared by writing the FLEX_US_CR.RSTSTA bit) Mask */
#define FLEXCOM_FLEX_US_FESR_Msk              _U_(0x000003FF)                                /**< (FLEXCOM_FLEX_US_FESR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_WPMR : (FLEXCOM Offset: 0x2E4) (R/W 32) USART Write Protection Mode Register -------- */
#define FLEXCOM_FLEX_US_WPMR_WPEN_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_WPMR) Write Protection Enable Position */
#define FLEXCOM_FLEX_US_WPMR_WPEN_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_WPMR_WPEN_Pos)    /**< (FLEXCOM_FLEX_US_WPMR) Write Protection Enable Mask */
#define FLEXCOM_FLEX_US_WPMR_WPKEY_Pos        _U_(8)                                         /**< (FLEXCOM_FLEX_US_WPMR) Write Protection Key Position */
#define FLEXCOM_FLEX_US_WPMR_WPKEY_Msk        (_U_(0xFFFFFF) << FLEXCOM_FLEX_US_WPMR_WPKEY_Pos) /**< (FLEXCOM_FLEX_US_WPMR) Write Protection Key Mask */
#define FLEXCOM_FLEX_US_WPMR_WPKEY(value)     (FLEXCOM_FLEX_US_WPMR_WPKEY_Msk & ((value) << FLEXCOM_FLEX_US_WPMR_WPKEY_Pos))
#define   FLEXCOM_FLEX_US_WPMR_WPKEY_PASSWD_Val _U_(0x555341)                                  /**< (FLEXCOM_FLEX_US_WPMR) Writing any other value in this field aborts the write operation of bit WPEN. Always reads as 0.  */
#define FLEXCOM_FLEX_US_WPMR_WPKEY_PASSWD     (FLEXCOM_FLEX_US_WPMR_WPKEY_PASSWD_Val << FLEXCOM_FLEX_US_WPMR_WPKEY_Pos) /**< (FLEXCOM_FLEX_US_WPMR) Writing any other value in this field aborts the write operation of bit WPEN. Always reads as 0. Position  */
#define FLEXCOM_FLEX_US_WPMR_Msk              _U_(0xFFFFFF01)                                /**< (FLEXCOM_FLEX_US_WPMR) Register Mask  */


/* -------- FLEXCOM_FLEX_US_WPSR : (FLEXCOM Offset: 0x2E8) ( R/ 32) USART Write Protection Status Register -------- */
#define FLEXCOM_FLEX_US_WPSR_WPVS_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_US_WPSR) Write Protection Violation Status Position */
#define FLEXCOM_FLEX_US_WPSR_WPVS_Msk         (_U_(0x1) << FLEXCOM_FLEX_US_WPSR_WPVS_Pos)    /**< (FLEXCOM_FLEX_US_WPSR) Write Protection Violation Status Mask */
#define FLEXCOM_FLEX_US_WPSR_WPVSRC_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_US_WPSR) Write Protection Violation Source Position */
#define FLEXCOM_FLEX_US_WPSR_WPVSRC_Msk       (_U_(0xFFFF) << FLEXCOM_FLEX_US_WPSR_WPVSRC_Pos) /**< (FLEXCOM_FLEX_US_WPSR) Write Protection Violation Source Mask */
#define FLEXCOM_FLEX_US_WPSR_WPVSRC(value)    (FLEXCOM_FLEX_US_WPSR_WPVSRC_Msk & ((value) << FLEXCOM_FLEX_US_WPSR_WPVSRC_Pos))
#define FLEXCOM_FLEX_US_WPSR_Msk              _U_(0x00FFFF01)                                /**< (FLEXCOM_FLEX_US_WPSR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_CR : (FLEXCOM Offset: 0x400) ( /W 32) SPI Control Register -------- */
#define FLEXCOM_FLEX_SPI_CR_SPIEN_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_CR) SPI Enable Position */
#define FLEXCOM_FLEX_SPI_CR_SPIEN_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_SPIEN_Pos)    /**< (FLEXCOM_FLEX_SPI_CR) SPI Enable Mask */
#define FLEXCOM_FLEX_SPI_CR_SPIDIS_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_CR) SPI Disable Position */
#define FLEXCOM_FLEX_SPI_CR_SPIDIS_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_SPIDIS_Pos)   /**< (FLEXCOM_FLEX_SPI_CR) SPI Disable Mask */
#define FLEXCOM_FLEX_SPI_CR_SWRST_Pos         _U_(7)                                         /**< (FLEXCOM_FLEX_SPI_CR) SPI Software Reset Position */
#define FLEXCOM_FLEX_SPI_CR_SWRST_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_SWRST_Pos)    /**< (FLEXCOM_FLEX_SPI_CR) SPI Software Reset Mask */
#define FLEXCOM_FLEX_SPI_CR_REQCLR_Pos        _U_(12)                                        /**< (FLEXCOM_FLEX_SPI_CR) Request to Clear the Comparison Trigger Position */
#define FLEXCOM_FLEX_SPI_CR_REQCLR_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_REQCLR_Pos)   /**< (FLEXCOM_FLEX_SPI_CR) Request to Clear the Comparison Trigger Mask */
#define FLEXCOM_FLEX_SPI_CR_TXFCLR_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_CR) Transmit FIFO Clear Position */
#define FLEXCOM_FLEX_SPI_CR_TXFCLR_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_TXFCLR_Pos)   /**< (FLEXCOM_FLEX_SPI_CR) Transmit FIFO Clear Mask */
#define FLEXCOM_FLEX_SPI_CR_RXFCLR_Pos        _U_(17)                                        /**< (FLEXCOM_FLEX_SPI_CR) Receive FIFO Clear Position */
#define FLEXCOM_FLEX_SPI_CR_RXFCLR_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_RXFCLR_Pos)   /**< (FLEXCOM_FLEX_SPI_CR) Receive FIFO Clear Mask */
#define FLEXCOM_FLEX_SPI_CR_LASTXFER_Pos      _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_CR) Last Transfer Position */
#define FLEXCOM_FLEX_SPI_CR_LASTXFER_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_LASTXFER_Pos) /**< (FLEXCOM_FLEX_SPI_CR) Last Transfer Mask */
#define FLEXCOM_FLEX_SPI_CR_FIFOEN_Pos        _U_(30)                                        /**< (FLEXCOM_FLEX_SPI_CR) FIFO Enable Position */
#define FLEXCOM_FLEX_SPI_CR_FIFOEN_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_FIFOEN_Pos)   /**< (FLEXCOM_FLEX_SPI_CR) FIFO Enable Mask */
#define FLEXCOM_FLEX_SPI_CR_FIFODIS_Pos       _U_(31)                                        /**< (FLEXCOM_FLEX_SPI_CR) FIFO Disable Position */
#define FLEXCOM_FLEX_SPI_CR_FIFODIS_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CR_FIFODIS_Pos)  /**< (FLEXCOM_FLEX_SPI_CR) FIFO Disable Mask */
#define FLEXCOM_FLEX_SPI_CR_Msk               _U_(0xC1031083)                                /**< (FLEXCOM_FLEX_SPI_CR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_MR : (FLEXCOM Offset: 0x404) (R/W 32) SPI Mode Register -------- */
#define FLEXCOM_FLEX_SPI_MR_MSTR_Pos          _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_MR) Master/Slave Mode Position */
#define FLEXCOM_FLEX_SPI_MR_MSTR_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_MSTR_Pos)     /**< (FLEXCOM_FLEX_SPI_MR) Master/Slave Mode Mask */
#define FLEXCOM_FLEX_SPI_MR_PS_Pos            _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_MR) Peripheral Select Position */
#define FLEXCOM_FLEX_SPI_MR_PS_Msk            (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_PS_Pos)       /**< (FLEXCOM_FLEX_SPI_MR) Peripheral Select Mask */
#define FLEXCOM_FLEX_SPI_MR_PCSDEC_Pos        _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_MR) Chip Select Decode Position */
#define FLEXCOM_FLEX_SPI_MR_PCSDEC_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_PCSDEC_Pos)   /**< (FLEXCOM_FLEX_SPI_MR) Chip Select Decode Mask */
#define FLEXCOM_FLEX_SPI_MR_BRSRCCLK_Pos      _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_MR) Bit Rate Source Clock Position */
#define FLEXCOM_FLEX_SPI_MR_BRSRCCLK_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_BRSRCCLK_Pos) /**< (FLEXCOM_FLEX_SPI_MR) Bit Rate Source Clock Mask */
#define   FLEXCOM_FLEX_SPI_MR_BRSRCCLK_PERIPH_CLK_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_MR) The peripheral clock is the source clock for the bit rate generation.  */
#define   FLEXCOM_FLEX_SPI_MR_BRSRCCLK_GCLK_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_MR) GCLK is the source clock for the bit rate generation, thus the bit rate can be independent of the core/peripheral clock.  */
#define FLEXCOM_FLEX_SPI_MR_BRSRCCLK_PERIPH_CLK (FLEXCOM_FLEX_SPI_MR_BRSRCCLK_PERIPH_CLK_Val << FLEXCOM_FLEX_SPI_MR_BRSRCCLK_Pos) /**< (FLEXCOM_FLEX_SPI_MR) The peripheral clock is the source clock for the bit rate generation. Position  */
#define FLEXCOM_FLEX_SPI_MR_BRSRCCLK_GCLK     (FLEXCOM_FLEX_SPI_MR_BRSRCCLK_GCLK_Val << FLEXCOM_FLEX_SPI_MR_BRSRCCLK_Pos) /**< (FLEXCOM_FLEX_SPI_MR) GCLK is the source clock for the bit rate generation, thus the bit rate can be independent of the core/peripheral clock. Position  */
#define FLEXCOM_FLEX_SPI_MR_MODFDIS_Pos       _U_(4)                                         /**< (FLEXCOM_FLEX_SPI_MR) Mode Fault Detection Position */
#define FLEXCOM_FLEX_SPI_MR_MODFDIS_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_MODFDIS_Pos)  /**< (FLEXCOM_FLEX_SPI_MR) Mode Fault Detection Mask */
#define FLEXCOM_FLEX_SPI_MR_WDRBT_Pos         _U_(5)                                         /**< (FLEXCOM_FLEX_SPI_MR) Wait Data Read Before Transfer Position */
#define FLEXCOM_FLEX_SPI_MR_WDRBT_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_WDRBT_Pos)    /**< (FLEXCOM_FLEX_SPI_MR) Wait Data Read Before Transfer Mask */
#define FLEXCOM_FLEX_SPI_MR_LLB_Pos           _U_(7)                                         /**< (FLEXCOM_FLEX_SPI_MR) Local Loopback Enable Position */
#define FLEXCOM_FLEX_SPI_MR_LLB_Msk           (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_LLB_Pos)      /**< (FLEXCOM_FLEX_SPI_MR) Local Loopback Enable Mask */
#define FLEXCOM_FLEX_SPI_MR_LBHPC_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_MR) Last Bit Half Period Compatibility Position */
#define FLEXCOM_FLEX_SPI_MR_LBHPC_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_LBHPC_Pos)    /**< (FLEXCOM_FLEX_SPI_MR) Last Bit Half Period Compatibility Mask */
#define FLEXCOM_FLEX_SPI_MR_CMPMODE_Pos       _U_(12)                                        /**< (FLEXCOM_FLEX_SPI_MR) Comparison Mode Position */
#define FLEXCOM_FLEX_SPI_MR_CMPMODE_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_MR_CMPMODE_Pos)  /**< (FLEXCOM_FLEX_SPI_MR) Comparison Mode Mask */
#define   FLEXCOM_FLEX_SPI_MR_CMPMODE_FLAG_ONLY_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_MR) Any character is received and comparison function drives CMP flag.  */
#define   FLEXCOM_FLEX_SPI_MR_CMPMODE_START_CONDITION_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_MR) Comparison condition must be met to start reception of all incoming characters until REQCLR is set.  */
#define FLEXCOM_FLEX_SPI_MR_CMPMODE_FLAG_ONLY (FLEXCOM_FLEX_SPI_MR_CMPMODE_FLAG_ONLY_Val << FLEXCOM_FLEX_SPI_MR_CMPMODE_Pos) /**< (FLEXCOM_FLEX_SPI_MR) Any character is received and comparison function drives CMP flag. Position  */
#define FLEXCOM_FLEX_SPI_MR_CMPMODE_START_CONDITION (FLEXCOM_FLEX_SPI_MR_CMPMODE_START_CONDITION_Val << FLEXCOM_FLEX_SPI_MR_CMPMODE_Pos) /**< (FLEXCOM_FLEX_SPI_MR) Comparison condition must be met to start reception of all incoming characters until REQCLR is set. Position  */
#define FLEXCOM_FLEX_SPI_MR_PCS_Pos           _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_MR) Peripheral Chip Select Position */
#define FLEXCOM_FLEX_SPI_MR_PCS_Msk           (_U_(0xF) << FLEXCOM_FLEX_SPI_MR_PCS_Pos)      /**< (FLEXCOM_FLEX_SPI_MR) Peripheral Chip Select Mask */
#define FLEXCOM_FLEX_SPI_MR_PCS(value)        (FLEXCOM_FLEX_SPI_MR_PCS_Msk & ((value) << FLEXCOM_FLEX_SPI_MR_PCS_Pos))
#define FLEXCOM_FLEX_SPI_MR_DLYBCS_Pos        _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_MR) Delay Between Chip Selects Position */
#define FLEXCOM_FLEX_SPI_MR_DLYBCS_Msk        (_U_(0xFF) << FLEXCOM_FLEX_SPI_MR_DLYBCS_Pos)  /**< (FLEXCOM_FLEX_SPI_MR) Delay Between Chip Selects Mask */
#define FLEXCOM_FLEX_SPI_MR_DLYBCS(value)     (FLEXCOM_FLEX_SPI_MR_DLYBCS_Msk & ((value) << FLEXCOM_FLEX_SPI_MR_DLYBCS_Pos))
#define FLEXCOM_FLEX_SPI_MR_Msk               _U_(0xFF0F11BF)                                /**< (FLEXCOM_FLEX_SPI_MR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_RDR : (FLEXCOM Offset: 0x408) ( R/ 32) SPI Receive Data Register -------- */
#define FLEXCOM_FLEX_SPI_RDR_RD_Pos           _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Position */
#define FLEXCOM_FLEX_SPI_RDR_RD_Msk           (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_RDR_RD_Pos)   /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Mask */
#define FLEXCOM_FLEX_SPI_RDR_RD(value)        (FLEXCOM_FLEX_SPI_RDR_RD_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_RD_Pos))
#define FLEXCOM_FLEX_SPI_RDR_PCS_Pos          _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_RDR) Peripheral Chip Select Position */
#define FLEXCOM_FLEX_SPI_RDR_PCS_Msk          (_U_(0xF) << FLEXCOM_FLEX_SPI_RDR_PCS_Pos)     /**< (FLEXCOM_FLEX_SPI_RDR) Peripheral Chip Select Mask */
#define FLEXCOM_FLEX_SPI_RDR_PCS(value)       (FLEXCOM_FLEX_SPI_RDR_PCS_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_PCS_Pos))
#define FLEXCOM_FLEX_SPI_RDR_Msk              _U_(0x000FFFFF)                                /**< (FLEXCOM_FLEX_SPI_RDR) Register Mask  */

/* FIFO_MULTI_DATA_8 mode */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_0_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Position */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_0_Msk (_U_(0xFF) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_0_Pos) /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Mask */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_0(value) (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_0_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_0_Pos))
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_1_Pos _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Position */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_1_Msk (_U_(0xFF) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_1_Pos) /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Mask */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_1(value) (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_1_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_1_Pos))
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_2_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Position */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_2_Msk (_U_(0xFF) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_2_Pos) /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Mask */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_2(value) (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_2_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_2_Pos))
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_3_Pos _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Position */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_3_Msk (_U_(0xFF) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_3_Pos) /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Mask */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_3(value) (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_3_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_RD8_3_Pos))
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8_Msk _U_(0xFFFFFFFF)                                 /**< (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_8) Register Mask  */

/* FIFO_MULTI_DATA_16 mode */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_0_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Position */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_0_Msk (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_0_Pos) /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Mask */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_0(value) (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_0_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_0_Pos))
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_1_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Position */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_1_Msk (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_1_Pos) /**< (FLEXCOM_FLEX_SPI_RDR) Receive Data Mask */
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_1(value) (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_1_Msk & ((value) << FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_RD16_1_Pos))
#define FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16_Msk _U_(0xFFFFFFFF)                                 /**< (FLEXCOM_FLEX_SPI_RDR_FIFO_MULTI_DATA_16) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_TDR : (FLEXCOM Offset: 0x40C) ( /W 32) SPI Transmit Data Register -------- */
#define FLEXCOM_FLEX_SPI_TDR_TD_Pos           _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_TDR) Transmit Data Position */
#define FLEXCOM_FLEX_SPI_TDR_TD_Msk           (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_TDR_TD_Pos)   /**< (FLEXCOM_FLEX_SPI_TDR) Transmit Data Mask */
#define FLEXCOM_FLEX_SPI_TDR_TD(value)        (FLEXCOM_FLEX_SPI_TDR_TD_Msk & ((value) << FLEXCOM_FLEX_SPI_TDR_TD_Pos))
#define FLEXCOM_FLEX_SPI_TDR_PCS_Pos          _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_TDR) Peripheral Chip Select Position */
#define FLEXCOM_FLEX_SPI_TDR_PCS_Msk          (_U_(0xF) << FLEXCOM_FLEX_SPI_TDR_PCS_Pos)     /**< (FLEXCOM_FLEX_SPI_TDR) Peripheral Chip Select Mask */
#define FLEXCOM_FLEX_SPI_TDR_PCS(value)       (FLEXCOM_FLEX_SPI_TDR_PCS_Msk & ((value) << FLEXCOM_FLEX_SPI_TDR_PCS_Pos))
#define FLEXCOM_FLEX_SPI_TDR_LASTXFER_Pos     _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_TDR) Last Transfer Position */
#define FLEXCOM_FLEX_SPI_TDR_LASTXFER_Msk     (_U_(0x1) << FLEXCOM_FLEX_SPI_TDR_LASTXFER_Pos) /**< (FLEXCOM_FLEX_SPI_TDR) Last Transfer Mask */
#define FLEXCOM_FLEX_SPI_TDR_Msk              _U_(0x010FFFFF)                                /**< (FLEXCOM_FLEX_SPI_TDR) Register Mask  */

/* FIFO_MULTI_DATA mode */
#define FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD0_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_TDR) Transmit Data Position */
#define FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD0_Msk (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD0_Pos) /**< (FLEXCOM_FLEX_SPI_TDR) Transmit Data Mask */
#define FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD0(value) (FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD0_Msk & ((value) << FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD0_Pos))
#define FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD1_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_TDR) Transmit Data Position */
#define FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD1_Msk (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD1_Pos) /**< (FLEXCOM_FLEX_SPI_TDR) Transmit Data Mask */
#define FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD1(value) (FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD1_Msk & ((value) << FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_TD1_Pos))
#define FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA_Msk _U_(0xFFFFFFFF)                                 /**< (FLEXCOM_FLEX_SPI_TDR_FIFO_MULTI_DATA) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_SR : (FLEXCOM Offset: 0x410) ( R/ 32) SPI Status Register -------- */
#define FLEXCOM_FLEX_SPI_SR_RDRF_Pos          _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_SR) Receive Data Register Full (cleared by reading FLEX_SPI_RDR) Position */
#define FLEXCOM_FLEX_SPI_SR_RDRF_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_RDRF_Pos)     /**< (FLEXCOM_FLEX_SPI_SR) Receive Data Register Full (cleared by reading FLEX_SPI_RDR) Mask */
#define FLEXCOM_FLEX_SPI_SR_TDRE_Pos          _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_SR) Transmit Data Register Empty (cleared by writing FLEX_SPI_TDR) Position */
#define FLEXCOM_FLEX_SPI_SR_TDRE_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_TDRE_Pos)     /**< (FLEXCOM_FLEX_SPI_SR) Transmit Data Register Empty (cleared by writing FLEX_SPI_TDR) Mask */
#define FLEXCOM_FLEX_SPI_SR_MODF_Pos          _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_SR) Mode Fault Error (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_MODF_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_MODF_Pos)     /**< (FLEXCOM_FLEX_SPI_SR) Mode Fault Error (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_OVRES_Pos         _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_SR) Overrun Error Status (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_OVRES_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_OVRES_Pos)    /**< (FLEXCOM_FLEX_SPI_SR) Overrun Error Status (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_NSSR_Pos          _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_SR) NSS Rising (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_NSSR_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_NSSR_Pos)     /**< (FLEXCOM_FLEX_SPI_SR) NSS Rising (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_TXEMPTY_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_SPI_SR) Transmission Registers Empty (cleared by writing FLEX_SPI_TDR) Position */
#define FLEXCOM_FLEX_SPI_SR_TXEMPTY_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_TXEMPTY_Pos)  /**< (FLEXCOM_FLEX_SPI_SR) Transmission Registers Empty (cleared by writing FLEX_SPI_TDR) Mask */
#define FLEXCOM_FLEX_SPI_SR_UNDES_Pos         _U_(10)                                        /**< (FLEXCOM_FLEX_SPI_SR) Underrun Error Status (Slave mode only) (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_UNDES_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_UNDES_Pos)    /**< (FLEXCOM_FLEX_SPI_SR) Underrun Error Status (Slave mode only) (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_CMP_Pos           _U_(11)                                        /**< (FLEXCOM_FLEX_SPI_SR) Comparison Status (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_CMP_Msk           (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_CMP_Pos)      /**< (FLEXCOM_FLEX_SPI_SR) Comparison Status (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_SFERR_Pos         _U_(12)                                        /**< (FLEXCOM_FLEX_SPI_SR) Slave Frame Error (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_SFERR_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_SFERR_Pos)    /**< (FLEXCOM_FLEX_SPI_SR) Slave Frame Error (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_SPIENS_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_SR) SPI Enable Status Position */
#define FLEXCOM_FLEX_SPI_SR_SPIENS_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_SPIENS_Pos)   /**< (FLEXCOM_FLEX_SPI_SR) SPI Enable Status Mask */
#define FLEXCOM_FLEX_SPI_SR_TXFEF_Pos         _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Empty Flag (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_TXFEF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_TXFEF_Pos)    /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Empty Flag (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_TXFFF_Pos         _U_(25)                                        /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Full Flag (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_TXFFF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_TXFFF_Pos)    /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Full Flag (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_TXFTHF_Pos        _U_(26)                                        /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Threshold Flag (cleared on read) Position */
#define FLEXCOM_FLEX_SPI_SR_TXFTHF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_TXFTHF_Pos)   /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Threshold Flag (cleared on read) Mask */
#define FLEXCOM_FLEX_SPI_SR_RXFEF_Pos         _U_(27)                                        /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Empty Flag Position */
#define FLEXCOM_FLEX_SPI_SR_RXFEF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_RXFEF_Pos)    /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Empty Flag Mask */
#define FLEXCOM_FLEX_SPI_SR_RXFFF_Pos         _U_(28)                                        /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Full Flag Position */
#define FLEXCOM_FLEX_SPI_SR_RXFFF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_RXFFF_Pos)    /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Full Flag Mask */
#define FLEXCOM_FLEX_SPI_SR_RXFTHF_Pos        _U_(29)                                        /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Threshold Flag Position */
#define FLEXCOM_FLEX_SPI_SR_RXFTHF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_RXFTHF_Pos)   /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Threshold Flag Mask */
#define FLEXCOM_FLEX_SPI_SR_TXFPTEF_Pos       _U_(30)                                        /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Pointer Error Flag Position */
#define FLEXCOM_FLEX_SPI_SR_TXFPTEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_TXFPTEF_Pos)  /**< (FLEXCOM_FLEX_SPI_SR) Transmit FIFO Pointer Error Flag Mask */
#define FLEXCOM_FLEX_SPI_SR_RXFPTEF_Pos       _U_(31)                                        /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Pointer Error Flag Position */
#define FLEXCOM_FLEX_SPI_SR_RXFPTEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_SR_RXFPTEF_Pos)  /**< (FLEXCOM_FLEX_SPI_SR) Receive FIFO Pointer Error Flag Mask */
#define FLEXCOM_FLEX_SPI_SR_Msk               _U_(0xFF011F0F)                                /**< (FLEXCOM_FLEX_SPI_SR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_IER : (FLEXCOM Offset: 0x414) ( /W 32) SPI Interrupt Enable Register -------- */
#define FLEXCOM_FLEX_SPI_IER_RDRF_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_IER) Receive Data Register Full Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_RDRF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_RDRF_Pos)    /**< (FLEXCOM_FLEX_SPI_IER) Receive Data Register Full Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_TDRE_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_IER) SPI Transmit Data Register Empty Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_TDRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_TDRE_Pos)    /**< (FLEXCOM_FLEX_SPI_IER) SPI Transmit Data Register Empty Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_MODF_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_IER) Mode Fault Error Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_MODF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_MODF_Pos)    /**< (FLEXCOM_FLEX_SPI_IER) Mode Fault Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_OVRES_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_IER) Overrun Error Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_OVRES_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_OVRES_Pos)   /**< (FLEXCOM_FLEX_SPI_IER) Overrun Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_NSSR_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_IER) NSS Rising Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_NSSR_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_NSSR_Pos)    /**< (FLEXCOM_FLEX_SPI_IER) NSS Rising Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_TXEMPTY_Pos      _U_(9)                                         /**< (FLEXCOM_FLEX_SPI_IER) Transmission Registers Empty Enable Position */
#define FLEXCOM_FLEX_SPI_IER_TXEMPTY_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_TXEMPTY_Pos) /**< (FLEXCOM_FLEX_SPI_IER) Transmission Registers Empty Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_UNDES_Pos        _U_(10)                                        /**< (FLEXCOM_FLEX_SPI_IER) Underrun Error Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_UNDES_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_UNDES_Pos)   /**< (FLEXCOM_FLEX_SPI_IER) Underrun Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_CMP_Pos          _U_(11)                                        /**< (FLEXCOM_FLEX_SPI_IER) Comparison Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_CMP_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_CMP_Pos)     /**< (FLEXCOM_FLEX_SPI_IER) Comparison Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_TXFEF_Pos        _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_IER) TXFEF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_TXFEF_Pos)   /**< (FLEXCOM_FLEX_SPI_IER) TXFEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_TXFFF_Pos        _U_(25)                                        /**< (FLEXCOM_FLEX_SPI_IER) TXFFF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_TXFFF_Pos)   /**< (FLEXCOM_FLEX_SPI_IER) TXFFF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_TXFTHF_Pos       _U_(26)                                        /**< (FLEXCOM_FLEX_SPI_IER) TXFTHF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_SPI_IER) TXFTHF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_RXFEF_Pos        _U_(27)                                        /**< (FLEXCOM_FLEX_SPI_IER) RXFEF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_RXFEF_Pos)   /**< (FLEXCOM_FLEX_SPI_IER) RXFEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_RXFFF_Pos        _U_(28)                                        /**< (FLEXCOM_FLEX_SPI_IER) RXFFF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_RXFFF_Pos)   /**< (FLEXCOM_FLEX_SPI_IER) RXFFF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_RXFTHF_Pos       _U_(29)                                        /**< (FLEXCOM_FLEX_SPI_IER) RXFTHF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_SPI_IER) RXFTHF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_TXFPTEF_Pos      _U_(30)                                        /**< (FLEXCOM_FLEX_SPI_IER) TXFPTEF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_SPI_IER) TXFPTEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_RXFPTEF_Pos      _U_(31)                                        /**< (FLEXCOM_FLEX_SPI_IER) RXFPTEF Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_IER_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IER_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_SPI_IER) RXFPTEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_IER_Msk              _U_(0xFF000F0F)                                /**< (FLEXCOM_FLEX_SPI_IER) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_IDR : (FLEXCOM Offset: 0x418) ( /W 32) SPI Interrupt Disable Register -------- */
#define FLEXCOM_FLEX_SPI_IDR_RDRF_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_IDR) Receive Data Register Full Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_RDRF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_RDRF_Pos)    /**< (FLEXCOM_FLEX_SPI_IDR) Receive Data Register Full Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_TDRE_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_IDR) SPI Transmit Data Register Empty Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_TDRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_TDRE_Pos)    /**< (FLEXCOM_FLEX_SPI_IDR) SPI Transmit Data Register Empty Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_MODF_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_IDR) Mode Fault Error Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_MODF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_MODF_Pos)    /**< (FLEXCOM_FLEX_SPI_IDR) Mode Fault Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_OVRES_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_IDR) Overrun Error Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_OVRES_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_OVRES_Pos)   /**< (FLEXCOM_FLEX_SPI_IDR) Overrun Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_NSSR_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_IDR) NSS Rising Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_NSSR_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_NSSR_Pos)    /**< (FLEXCOM_FLEX_SPI_IDR) NSS Rising Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_TXEMPTY_Pos      _U_(9)                                         /**< (FLEXCOM_FLEX_SPI_IDR) Transmission Registers Empty Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_TXEMPTY_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_TXEMPTY_Pos) /**< (FLEXCOM_FLEX_SPI_IDR) Transmission Registers Empty Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_UNDES_Pos        _U_(10)                                        /**< (FLEXCOM_FLEX_SPI_IDR) Underrun Error Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_UNDES_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_UNDES_Pos)   /**< (FLEXCOM_FLEX_SPI_IDR) Underrun Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_CMP_Pos          _U_(11)                                        /**< (FLEXCOM_FLEX_SPI_IDR) Comparison Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_CMP_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_CMP_Pos)     /**< (FLEXCOM_FLEX_SPI_IDR) Comparison Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_TXFEF_Pos        _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_IDR) TXFEF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_TXFEF_Pos)   /**< (FLEXCOM_FLEX_SPI_IDR) TXFEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_TXFFF_Pos        _U_(25)                                        /**< (FLEXCOM_FLEX_SPI_IDR) TXFFF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_TXFFF_Pos)   /**< (FLEXCOM_FLEX_SPI_IDR) TXFFF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_TXFTHF_Pos       _U_(26)                                        /**< (FLEXCOM_FLEX_SPI_IDR) TXFTHF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_SPI_IDR) TXFTHF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_RXFEF_Pos        _U_(27)                                        /**< (FLEXCOM_FLEX_SPI_IDR) RXFEF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_RXFEF_Pos)   /**< (FLEXCOM_FLEX_SPI_IDR) RXFEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_RXFFF_Pos        _U_(28)                                        /**< (FLEXCOM_FLEX_SPI_IDR) RXFFF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_RXFFF_Pos)   /**< (FLEXCOM_FLEX_SPI_IDR) RXFFF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_RXFTHF_Pos       _U_(29)                                        /**< (FLEXCOM_FLEX_SPI_IDR) RXFTHF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_SPI_IDR) RXFTHF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_TXFPTEF_Pos      _U_(30)                                        /**< (FLEXCOM_FLEX_SPI_IDR) TXFPTEF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_SPI_IDR) TXFPTEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_RXFPTEF_Pos      _U_(31)                                        /**< (FLEXCOM_FLEX_SPI_IDR) RXFPTEF Interrupt Disable Position */
#define FLEXCOM_FLEX_SPI_IDR_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IDR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_SPI_IDR) RXFPTEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_SPI_IDR_Msk              _U_(0xFF000F0F)                                /**< (FLEXCOM_FLEX_SPI_IDR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_IMR : (FLEXCOM Offset: 0x41C) ( R/ 32) SPI Interrupt Mask Register -------- */
#define FLEXCOM_FLEX_SPI_IMR_RDRF_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_IMR) Receive Data Register Full Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_RDRF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_RDRF_Pos)    /**< (FLEXCOM_FLEX_SPI_IMR) Receive Data Register Full Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_TDRE_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_IMR) SPI Transmit Data Register Empty Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_TDRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_TDRE_Pos)    /**< (FLEXCOM_FLEX_SPI_IMR) SPI Transmit Data Register Empty Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_MODF_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_IMR) Mode Fault Error Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_MODF_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_MODF_Pos)    /**< (FLEXCOM_FLEX_SPI_IMR) Mode Fault Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_OVRES_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_IMR) Overrun Error Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_OVRES_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_OVRES_Pos)   /**< (FLEXCOM_FLEX_SPI_IMR) Overrun Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_NSSR_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_IMR) NSS Rising Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_NSSR_Msk         (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_NSSR_Pos)    /**< (FLEXCOM_FLEX_SPI_IMR) NSS Rising Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_TXEMPTY_Pos      _U_(9)                                         /**< (FLEXCOM_FLEX_SPI_IMR) Transmission Registers Empty Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_TXEMPTY_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_TXEMPTY_Pos) /**< (FLEXCOM_FLEX_SPI_IMR) Transmission Registers Empty Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_UNDES_Pos        _U_(10)                                        /**< (FLEXCOM_FLEX_SPI_IMR) Underrun Error Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_UNDES_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_UNDES_Pos)   /**< (FLEXCOM_FLEX_SPI_IMR) Underrun Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_CMP_Pos          _U_(11)                                        /**< (FLEXCOM_FLEX_SPI_IMR) Comparison Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_CMP_Msk          (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_CMP_Pos)     /**< (FLEXCOM_FLEX_SPI_IMR) Comparison Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_TXFEF_Pos        _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_IMR) TXFEF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_TXFEF_Pos)   /**< (FLEXCOM_FLEX_SPI_IMR) TXFEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_TXFFF_Pos        _U_(25)                                        /**< (FLEXCOM_FLEX_SPI_IMR) TXFFF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_TXFFF_Pos)   /**< (FLEXCOM_FLEX_SPI_IMR) TXFFF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_TXFTHF_Pos       _U_(26)                                        /**< (FLEXCOM_FLEX_SPI_IMR) TXFTHF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_SPI_IMR) TXFTHF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_RXFEF_Pos        _U_(27)                                        /**< (FLEXCOM_FLEX_SPI_IMR) RXFEF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_RXFEF_Pos)   /**< (FLEXCOM_FLEX_SPI_IMR) RXFEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_RXFFF_Pos        _U_(28)                                        /**< (FLEXCOM_FLEX_SPI_IMR) RXFFF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_RXFFF_Pos)   /**< (FLEXCOM_FLEX_SPI_IMR) RXFFF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_RXFTHF_Pos       _U_(29)                                        /**< (FLEXCOM_FLEX_SPI_IMR) RXFTHF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_SPI_IMR) RXFTHF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_TXFPTEF_Pos      _U_(30)                                        /**< (FLEXCOM_FLEX_SPI_IMR) TXFPTEF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_SPI_IMR) TXFPTEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_RXFPTEF_Pos      _U_(31)                                        /**< (FLEXCOM_FLEX_SPI_IMR) RXFPTEF Interrupt Mask Position */
#define FLEXCOM_FLEX_SPI_IMR_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_IMR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_SPI_IMR) RXFPTEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_SPI_IMR_Msk              _U_(0xFF000F0F)                                /**< (FLEXCOM_FLEX_SPI_IMR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_CSR0 : (FLEXCOM Offset: 0x430) (R/W 32) SPI Chip Select Register 0 -------- */
#define FLEXCOM_FLEX_SPI_CSR0_CPOL_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_CSR0) Clock Polarity Position */
#define FLEXCOM_FLEX_SPI_CSR0_CPOL_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR0_CPOL_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR0) Clock Polarity Mask */
#define FLEXCOM_FLEX_SPI_CSR0_NCPHA_Pos       _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_CSR0) Clock Phase Position */
#define FLEXCOM_FLEX_SPI_CSR0_NCPHA_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR0_NCPHA_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR0) Clock Phase Mask */
#define FLEXCOM_FLEX_SPI_CSR0_CSNAAT_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_CSR0) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Position */
#define FLEXCOM_FLEX_SPI_CSR0_CSNAAT_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR0_CSNAAT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Mask */
#define FLEXCOM_FLEX_SPI_CSR0_CSAAT_Pos       _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_CSR0) Chip Select Active After Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR0_CSAAT_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR0_CSAAT_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR0) Chip Select Active After Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_SPI_CSR0) Bits Per Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_Msk        (_U_(0xF) << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR0) Bits Per Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR0_BITS(value)     (FLEXCOM_FLEX_SPI_CSR0_BITS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos))
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_8_BIT_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 8 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_9_BIT_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 9 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_10_BIT_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 10 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_11_BIT_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 11 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_12_BIT_Val _U_(0x4)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 12 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_13_BIT_Val _U_(0x5)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 13 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_14_BIT_Val _U_(0x6)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 14 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_15_BIT_Val _U_(0x7)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 15 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR0_BITS_16_BIT_Val _U_(0x8)                                       /**< (FLEXCOM_FLEX_SPI_CSR0) 16 bits for transfer  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_8_BIT      (FLEXCOM_FLEX_SPI_CSR0_BITS_8_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 8 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_9_BIT      (FLEXCOM_FLEX_SPI_CSR0_BITS_9_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 9 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_10_BIT     (FLEXCOM_FLEX_SPI_CSR0_BITS_10_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 10 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_11_BIT     (FLEXCOM_FLEX_SPI_CSR0_BITS_11_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 11 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_12_BIT     (FLEXCOM_FLEX_SPI_CSR0_BITS_12_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 12 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_13_BIT     (FLEXCOM_FLEX_SPI_CSR0_BITS_13_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 13 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_14_BIT     (FLEXCOM_FLEX_SPI_CSR0_BITS_14_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 14 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_15_BIT     (FLEXCOM_FLEX_SPI_CSR0_BITS_15_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 15 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_BITS_16_BIT     (FLEXCOM_FLEX_SPI_CSR0_BITS_16_BIT_Val << FLEXCOM_FLEX_SPI_CSR0_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) 16 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR0_SCBR_Pos        _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_CSR0) Serial Clock Bit Rate Position */
#define FLEXCOM_FLEX_SPI_CSR0_SCBR_Msk        (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR0_SCBR_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR0) Serial Clock Bit Rate Mask */
#define FLEXCOM_FLEX_SPI_CSR0_SCBR(value)     (FLEXCOM_FLEX_SPI_CSR0_SCBR_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR0_SCBR_Pos))
#define FLEXCOM_FLEX_SPI_CSR0_DLYBS_Pos       _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_CSR0) Delay Before SPCK Position */
#define FLEXCOM_FLEX_SPI_CSR0_DLYBS_Msk       (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR0_DLYBS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) Delay Before SPCK Mask */
#define FLEXCOM_FLEX_SPI_CSR0_DLYBS(value)    (FLEXCOM_FLEX_SPI_CSR0_DLYBS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR0_DLYBS_Pos))
#define FLEXCOM_FLEX_SPI_CSR0_DLYBCT_Pos      _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_CSR0) Delay Between Consecutive Transfers Position */
#define FLEXCOM_FLEX_SPI_CSR0_DLYBCT_Msk      (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR0_DLYBCT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR0) Delay Between Consecutive Transfers Mask */
#define FLEXCOM_FLEX_SPI_CSR0_DLYBCT(value)   (FLEXCOM_FLEX_SPI_CSR0_DLYBCT_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR0_DLYBCT_Pos))
#define FLEXCOM_FLEX_SPI_CSR0_Msk             _U_(0xFFFFFFFF)                                /**< (FLEXCOM_FLEX_SPI_CSR0) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_CSR1 : (FLEXCOM Offset: 0x434) (R/W 32) SPI Chip Select Register 1 -------- */
#define FLEXCOM_FLEX_SPI_CSR1_CPOL_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_CSR1) Clock Polarity Position */
#define FLEXCOM_FLEX_SPI_CSR1_CPOL_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR1_CPOL_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR1) Clock Polarity Mask */
#define FLEXCOM_FLEX_SPI_CSR1_NCPHA_Pos       _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_CSR1) Clock Phase Position */
#define FLEXCOM_FLEX_SPI_CSR1_NCPHA_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR1_NCPHA_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR1) Clock Phase Mask */
#define FLEXCOM_FLEX_SPI_CSR1_CSNAAT_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_CSR1) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Position */
#define FLEXCOM_FLEX_SPI_CSR1_CSNAAT_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR1_CSNAAT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Mask */
#define FLEXCOM_FLEX_SPI_CSR1_CSAAT_Pos       _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_CSR1) Chip Select Active After Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR1_CSAAT_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR1_CSAAT_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR1) Chip Select Active After Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_SPI_CSR1) Bits Per Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_Msk        (_U_(0xF) << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR1) Bits Per Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR1_BITS(value)     (FLEXCOM_FLEX_SPI_CSR1_BITS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos))
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_8_BIT_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 8 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_9_BIT_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 9 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_10_BIT_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 10 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_11_BIT_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 11 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_12_BIT_Val _U_(0x4)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 12 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_13_BIT_Val _U_(0x5)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 13 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_14_BIT_Val _U_(0x6)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 14 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_15_BIT_Val _U_(0x7)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 15 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR1_BITS_16_BIT_Val _U_(0x8)                                       /**< (FLEXCOM_FLEX_SPI_CSR1) 16 bits for transfer  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_8_BIT      (FLEXCOM_FLEX_SPI_CSR1_BITS_8_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 8 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_9_BIT      (FLEXCOM_FLEX_SPI_CSR1_BITS_9_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 9 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_10_BIT     (FLEXCOM_FLEX_SPI_CSR1_BITS_10_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 10 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_11_BIT     (FLEXCOM_FLEX_SPI_CSR1_BITS_11_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 11 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_12_BIT     (FLEXCOM_FLEX_SPI_CSR1_BITS_12_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 12 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_13_BIT     (FLEXCOM_FLEX_SPI_CSR1_BITS_13_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 13 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_14_BIT     (FLEXCOM_FLEX_SPI_CSR1_BITS_14_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 14 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_15_BIT     (FLEXCOM_FLEX_SPI_CSR1_BITS_15_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 15 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_BITS_16_BIT     (FLEXCOM_FLEX_SPI_CSR1_BITS_16_BIT_Val << FLEXCOM_FLEX_SPI_CSR1_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) 16 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR1_SCBR_Pos        _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_CSR1) Serial Clock Bit Rate Position */
#define FLEXCOM_FLEX_SPI_CSR1_SCBR_Msk        (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR1_SCBR_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR1) Serial Clock Bit Rate Mask */
#define FLEXCOM_FLEX_SPI_CSR1_SCBR(value)     (FLEXCOM_FLEX_SPI_CSR1_SCBR_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR1_SCBR_Pos))
#define FLEXCOM_FLEX_SPI_CSR1_DLYBS_Pos       _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_CSR1) Delay Before SPCK Position */
#define FLEXCOM_FLEX_SPI_CSR1_DLYBS_Msk       (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR1_DLYBS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) Delay Before SPCK Mask */
#define FLEXCOM_FLEX_SPI_CSR1_DLYBS(value)    (FLEXCOM_FLEX_SPI_CSR1_DLYBS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR1_DLYBS_Pos))
#define FLEXCOM_FLEX_SPI_CSR1_DLYBCT_Pos      _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_CSR1) Delay Between Consecutive Transfers Position */
#define FLEXCOM_FLEX_SPI_CSR1_DLYBCT_Msk      (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR1_DLYBCT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR1) Delay Between Consecutive Transfers Mask */
#define FLEXCOM_FLEX_SPI_CSR1_DLYBCT(value)   (FLEXCOM_FLEX_SPI_CSR1_DLYBCT_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR1_DLYBCT_Pos))
#define FLEXCOM_FLEX_SPI_CSR1_Msk             _U_(0xFFFFFFFF)                                /**< (FLEXCOM_FLEX_SPI_CSR1) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_CSR2 : (FLEXCOM Offset: 0x438) (R/W 32) SPI Chip Select Register 2 -------- */
#define FLEXCOM_FLEX_SPI_CSR2_CPOL_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_CSR2) Clock Polarity Position */
#define FLEXCOM_FLEX_SPI_CSR2_CPOL_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR2_CPOL_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR2) Clock Polarity Mask */
#define FLEXCOM_FLEX_SPI_CSR2_NCPHA_Pos       _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_CSR2) Clock Phase Position */
#define FLEXCOM_FLEX_SPI_CSR2_NCPHA_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR2_NCPHA_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR2) Clock Phase Mask */
#define FLEXCOM_FLEX_SPI_CSR2_CSNAAT_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_CSR2) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Position */
#define FLEXCOM_FLEX_SPI_CSR2_CSNAAT_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR2_CSNAAT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Mask */
#define FLEXCOM_FLEX_SPI_CSR2_CSAAT_Pos       _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_CSR2) Chip Select Active After Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR2_CSAAT_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR2_CSAAT_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR2) Chip Select Active After Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_SPI_CSR2) Bits Per Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_Msk        (_U_(0xF) << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR2) Bits Per Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR2_BITS(value)     (FLEXCOM_FLEX_SPI_CSR2_BITS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos))
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_8_BIT_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 8 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_9_BIT_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 9 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_10_BIT_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 10 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_11_BIT_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 11 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_12_BIT_Val _U_(0x4)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 12 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_13_BIT_Val _U_(0x5)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 13 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_14_BIT_Val _U_(0x6)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 14 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_15_BIT_Val _U_(0x7)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 15 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR2_BITS_16_BIT_Val _U_(0x8)                                       /**< (FLEXCOM_FLEX_SPI_CSR2) 16 bits for transfer  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_8_BIT      (FLEXCOM_FLEX_SPI_CSR2_BITS_8_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 8 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_9_BIT      (FLEXCOM_FLEX_SPI_CSR2_BITS_9_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 9 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_10_BIT     (FLEXCOM_FLEX_SPI_CSR2_BITS_10_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 10 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_11_BIT     (FLEXCOM_FLEX_SPI_CSR2_BITS_11_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 11 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_12_BIT     (FLEXCOM_FLEX_SPI_CSR2_BITS_12_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 12 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_13_BIT     (FLEXCOM_FLEX_SPI_CSR2_BITS_13_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 13 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_14_BIT     (FLEXCOM_FLEX_SPI_CSR2_BITS_14_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 14 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_15_BIT     (FLEXCOM_FLEX_SPI_CSR2_BITS_15_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 15 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_BITS_16_BIT     (FLEXCOM_FLEX_SPI_CSR2_BITS_16_BIT_Val << FLEXCOM_FLEX_SPI_CSR2_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) 16 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR2_SCBR_Pos        _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_CSR2) Serial Clock Bit Rate Position */
#define FLEXCOM_FLEX_SPI_CSR2_SCBR_Msk        (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR2_SCBR_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR2) Serial Clock Bit Rate Mask */
#define FLEXCOM_FLEX_SPI_CSR2_SCBR(value)     (FLEXCOM_FLEX_SPI_CSR2_SCBR_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR2_SCBR_Pos))
#define FLEXCOM_FLEX_SPI_CSR2_DLYBS_Pos       _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_CSR2) Delay Before SPCK Position */
#define FLEXCOM_FLEX_SPI_CSR2_DLYBS_Msk       (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR2_DLYBS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) Delay Before SPCK Mask */
#define FLEXCOM_FLEX_SPI_CSR2_DLYBS(value)    (FLEXCOM_FLEX_SPI_CSR2_DLYBS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR2_DLYBS_Pos))
#define FLEXCOM_FLEX_SPI_CSR2_DLYBCT_Pos      _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_CSR2) Delay Between Consecutive Transfers Position */
#define FLEXCOM_FLEX_SPI_CSR2_DLYBCT_Msk      (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR2_DLYBCT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR2) Delay Between Consecutive Transfers Mask */
#define FLEXCOM_FLEX_SPI_CSR2_DLYBCT(value)   (FLEXCOM_FLEX_SPI_CSR2_DLYBCT_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR2_DLYBCT_Pos))
#define FLEXCOM_FLEX_SPI_CSR2_Msk             _U_(0xFFFFFFFF)                                /**< (FLEXCOM_FLEX_SPI_CSR2) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_CSR3 : (FLEXCOM Offset: 0x43C) (R/W 32) SPI Chip Select Register 3 -------- */
#define FLEXCOM_FLEX_SPI_CSR3_CPOL_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_CSR3) Clock Polarity Position */
#define FLEXCOM_FLEX_SPI_CSR3_CPOL_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR3_CPOL_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR3) Clock Polarity Mask */
#define FLEXCOM_FLEX_SPI_CSR3_NCPHA_Pos       _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_CSR3) Clock Phase Position */
#define FLEXCOM_FLEX_SPI_CSR3_NCPHA_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR3_NCPHA_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR3) Clock Phase Mask */
#define FLEXCOM_FLEX_SPI_CSR3_CSNAAT_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_CSR3) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Position */
#define FLEXCOM_FLEX_SPI_CSR3_CSNAAT_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR3_CSNAAT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Mask */
#define FLEXCOM_FLEX_SPI_CSR3_CSAAT_Pos       _U_(3)                                         /**< (FLEXCOM_FLEX_SPI_CSR3) Chip Select Active After Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR3_CSAAT_Msk       (_U_(0x1) << FLEXCOM_FLEX_SPI_CSR3_CSAAT_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR3) Chip Select Active After Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_SPI_CSR3) Bits Per Transfer Position */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_Msk        (_U_(0xF) << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos)   /**< (FLEXCOM_FLEX_SPI_CSR3) Bits Per Transfer Mask */
#define FLEXCOM_FLEX_SPI_CSR3_BITS(value)     (FLEXCOM_FLEX_SPI_CSR3_BITS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos))
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_8_BIT_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 8 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_9_BIT_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 9 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_10_BIT_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 10 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_11_BIT_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 11 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_12_BIT_Val _U_(0x4)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 12 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_13_BIT_Val _U_(0x5)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 13 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_14_BIT_Val _U_(0x6)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 14 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_15_BIT_Val _U_(0x7)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 15 bits for transfer  */
#define   FLEXCOM_FLEX_SPI_CSR3_BITS_16_BIT_Val _U_(0x8)                                       /**< (FLEXCOM_FLEX_SPI_CSR3) 16 bits for transfer  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_8_BIT      (FLEXCOM_FLEX_SPI_CSR3_BITS_8_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 8 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_9_BIT      (FLEXCOM_FLEX_SPI_CSR3_BITS_9_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 9 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_10_BIT     (FLEXCOM_FLEX_SPI_CSR3_BITS_10_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 10 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_11_BIT     (FLEXCOM_FLEX_SPI_CSR3_BITS_11_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 11 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_12_BIT     (FLEXCOM_FLEX_SPI_CSR3_BITS_12_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 12 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_13_BIT     (FLEXCOM_FLEX_SPI_CSR3_BITS_13_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 13 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_14_BIT     (FLEXCOM_FLEX_SPI_CSR3_BITS_14_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 14 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_15_BIT     (FLEXCOM_FLEX_SPI_CSR3_BITS_15_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 15 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_BITS_16_BIT     (FLEXCOM_FLEX_SPI_CSR3_BITS_16_BIT_Val << FLEXCOM_FLEX_SPI_CSR3_BITS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) 16 bits for transfer Position  */
#define FLEXCOM_FLEX_SPI_CSR3_SCBR_Pos        _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_CSR3) Serial Clock Bit Rate Position */
#define FLEXCOM_FLEX_SPI_CSR3_SCBR_Msk        (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR3_SCBR_Pos)  /**< (FLEXCOM_FLEX_SPI_CSR3) Serial Clock Bit Rate Mask */
#define FLEXCOM_FLEX_SPI_CSR3_SCBR(value)     (FLEXCOM_FLEX_SPI_CSR3_SCBR_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR3_SCBR_Pos))
#define FLEXCOM_FLEX_SPI_CSR3_DLYBS_Pos       _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_CSR3) Delay Before SPCK Position */
#define FLEXCOM_FLEX_SPI_CSR3_DLYBS_Msk       (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR3_DLYBS_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) Delay Before SPCK Mask */
#define FLEXCOM_FLEX_SPI_CSR3_DLYBS(value)    (FLEXCOM_FLEX_SPI_CSR3_DLYBS_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR3_DLYBS_Pos))
#define FLEXCOM_FLEX_SPI_CSR3_DLYBCT_Pos      _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_CSR3) Delay Between Consecutive Transfers Position */
#define FLEXCOM_FLEX_SPI_CSR3_DLYBCT_Msk      (_U_(0xFF) << FLEXCOM_FLEX_SPI_CSR3_DLYBCT_Pos) /**< (FLEXCOM_FLEX_SPI_CSR3) Delay Between Consecutive Transfers Mask */
#define FLEXCOM_FLEX_SPI_CSR3_DLYBCT(value)   (FLEXCOM_FLEX_SPI_CSR3_DLYBCT_Msk & ((value) << FLEXCOM_FLEX_SPI_CSR3_DLYBCT_Pos))
#define FLEXCOM_FLEX_SPI_CSR3_Msk             _U_(0xFFFFFFFF)                                /**< (FLEXCOM_FLEX_SPI_CSR3) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_FMR : (FLEXCOM Offset: 0x440) (R/W 32) SPI FIFO Mode Register -------- */
#define FLEXCOM_FLEX_SPI_FMR_TXRDYM_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_FMR) Transmit Data Register Empty Mode Position */
#define FLEXCOM_FLEX_SPI_FMR_TXRDYM_Msk       (_U_(0x3) << FLEXCOM_FLEX_SPI_FMR_TXRDYM_Pos)  /**< (FLEXCOM_FLEX_SPI_FMR) Transmit Data Register Empty Mode Mask */
#define FLEXCOM_FLEX_SPI_FMR_TXRDYM(value)    (FLEXCOM_FLEX_SPI_FMR_TXRDYM_Msk & ((value) << FLEXCOM_FLEX_SPI_FMR_TXRDYM_Pos))
#define   FLEXCOM_FLEX_SPI_FMR_TXRDYM_ONE_DATA_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_FMR) TDRE will be at level '1' when at least one data can be written in the Transmit FIFO.  */
#define   FLEXCOM_FLEX_SPI_FMR_TXRDYM_TWO_DATA_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_FMR) TDRE will be at level '1' when at least two data can be written in the Transmit FIFO.Cannot be used if FLEX_SPI_MR.PS =1.  */
#define FLEXCOM_FLEX_SPI_FMR_TXRDYM_ONE_DATA  (FLEXCOM_FLEX_SPI_FMR_TXRDYM_ONE_DATA_Val << FLEXCOM_FLEX_SPI_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_SPI_FMR) TDRE will be at level '1' when at least one data can be written in the Transmit FIFO. Position  */
#define FLEXCOM_FLEX_SPI_FMR_TXRDYM_TWO_DATA  (FLEXCOM_FLEX_SPI_FMR_TXRDYM_TWO_DATA_Val << FLEXCOM_FLEX_SPI_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_SPI_FMR) TDRE will be at level '1' when at least two data can be written in the Transmit FIFO.Cannot be used if FLEX_SPI_MR.PS =1. Position  */
#define FLEXCOM_FLEX_SPI_FMR_RXRDYM_Pos       _U_(4)                                         /**< (FLEXCOM_FLEX_SPI_FMR) Receive Data Register Full Mode Position */
#define FLEXCOM_FLEX_SPI_FMR_RXRDYM_Msk       (_U_(0x3) << FLEXCOM_FLEX_SPI_FMR_RXRDYM_Pos)  /**< (FLEXCOM_FLEX_SPI_FMR) Receive Data Register Full Mode Mask */
#define FLEXCOM_FLEX_SPI_FMR_RXRDYM(value)    (FLEXCOM_FLEX_SPI_FMR_RXRDYM_Msk & ((value) << FLEXCOM_FLEX_SPI_FMR_RXRDYM_Pos))
#define   FLEXCOM_FLEX_SPI_FMR_RXRDYM_ONE_DATA_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_SPI_FMR) RDRF will be at level '1' when at least one unread data is in the Receive FIFO.  */
#define   FLEXCOM_FLEX_SPI_FMR_RXRDYM_TWO_DATA_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_SPI_FMR) RDRF will be at level '1' when at least two unread data are in the Receive FIFO.Cannot be used when FLEX_SPI_MR.MSTR =1, or if FLEX_SPI_MR.PS =1.  */
#define   FLEXCOM_FLEX_SPI_FMR_RXRDYM_FOUR_DATA_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_SPI_FMR) RDRF will be at level '1' when at least four unread data are in the Receive FIFO.Cannot be used when FLEX_SPI_CSRx.BITS is greater than 0, or if FLEX_SPI_MR.MSTR =1, or if FLEX_SPI_MR.PS =1.  */
#define FLEXCOM_FLEX_SPI_FMR_RXRDYM_ONE_DATA  (FLEXCOM_FLEX_SPI_FMR_RXRDYM_ONE_DATA_Val << FLEXCOM_FLEX_SPI_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_SPI_FMR) RDRF will be at level '1' when at least one unread data is in the Receive FIFO. Position  */
#define FLEXCOM_FLEX_SPI_FMR_RXRDYM_TWO_DATA  (FLEXCOM_FLEX_SPI_FMR_RXRDYM_TWO_DATA_Val << FLEXCOM_FLEX_SPI_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_SPI_FMR) RDRF will be at level '1' when at least two unread data are in the Receive FIFO.Cannot be used when FLEX_SPI_MR.MSTR =1, or if FLEX_SPI_MR.PS =1. Position  */
#define FLEXCOM_FLEX_SPI_FMR_RXRDYM_FOUR_DATA (FLEXCOM_FLEX_SPI_FMR_RXRDYM_FOUR_DATA_Val << FLEXCOM_FLEX_SPI_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_SPI_FMR) RDRF will be at level '1' when at least four unread data are in the Receive FIFO.Cannot be used when FLEX_SPI_CSRx.BITS is greater than 0, or if FLEX_SPI_MR.MSTR =1, or if FLEX_SPI_MR.PS =1. Position  */
#define FLEXCOM_FLEX_SPI_FMR_TXFTHRES_Pos     _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_FMR) Transmit FIFO Threshold Position */
#define FLEXCOM_FLEX_SPI_FMR_TXFTHRES_Msk     (_U_(0x3F) << FLEXCOM_FLEX_SPI_FMR_TXFTHRES_Pos) /**< (FLEXCOM_FLEX_SPI_FMR) Transmit FIFO Threshold Mask */
#define FLEXCOM_FLEX_SPI_FMR_TXFTHRES(value)  (FLEXCOM_FLEX_SPI_FMR_TXFTHRES_Msk & ((value) << FLEXCOM_FLEX_SPI_FMR_TXFTHRES_Pos))
#define FLEXCOM_FLEX_SPI_FMR_RXFTHRES_Pos     _U_(24)                                        /**< (FLEXCOM_FLEX_SPI_FMR) Receive FIFO Threshold Position */
#define FLEXCOM_FLEX_SPI_FMR_RXFTHRES_Msk     (_U_(0x3F) << FLEXCOM_FLEX_SPI_FMR_RXFTHRES_Pos) /**< (FLEXCOM_FLEX_SPI_FMR) Receive FIFO Threshold Mask */
#define FLEXCOM_FLEX_SPI_FMR_RXFTHRES(value)  (FLEXCOM_FLEX_SPI_FMR_RXFTHRES_Msk & ((value) << FLEXCOM_FLEX_SPI_FMR_RXFTHRES_Pos))
#define FLEXCOM_FLEX_SPI_FMR_Msk              _U_(0x3F3F0033)                                /**< (FLEXCOM_FLEX_SPI_FMR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_FLR : (FLEXCOM Offset: 0x444) ( R/ 32) SPI FIFO Level Register -------- */
#define FLEXCOM_FLEX_SPI_FLR_TXFL_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_FLR) Transmit FIFO Level Position */
#define FLEXCOM_FLEX_SPI_FLR_TXFL_Msk         (_U_(0x3F) << FLEXCOM_FLEX_SPI_FLR_TXFL_Pos)   /**< (FLEXCOM_FLEX_SPI_FLR) Transmit FIFO Level Mask */
#define FLEXCOM_FLEX_SPI_FLR_TXFL(value)      (FLEXCOM_FLEX_SPI_FLR_TXFL_Msk & ((value) << FLEXCOM_FLEX_SPI_FLR_TXFL_Pos))
#define FLEXCOM_FLEX_SPI_FLR_RXFL_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_FLR) Receive FIFO Level Position */
#define FLEXCOM_FLEX_SPI_FLR_RXFL_Msk         (_U_(0x3F) << FLEXCOM_FLEX_SPI_FLR_RXFL_Pos)   /**< (FLEXCOM_FLEX_SPI_FLR) Receive FIFO Level Mask */
#define FLEXCOM_FLEX_SPI_FLR_RXFL(value)      (FLEXCOM_FLEX_SPI_FLR_RXFL_Msk & ((value) << FLEXCOM_FLEX_SPI_FLR_RXFL_Pos))
#define FLEXCOM_FLEX_SPI_FLR_Msk              _U_(0x003F003F)                                /**< (FLEXCOM_FLEX_SPI_FLR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_CMPR : (FLEXCOM Offset: 0x448) (R/W 32) SPI Comparison Register -------- */
#define FLEXCOM_FLEX_SPI_CMPR_VAL1_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_CMPR) First Comparison Value for Received Character Position */
#define FLEXCOM_FLEX_SPI_CMPR_VAL1_Msk        (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_CMPR_VAL1_Pos) /**< (FLEXCOM_FLEX_SPI_CMPR) First Comparison Value for Received Character Mask */
#define FLEXCOM_FLEX_SPI_CMPR_VAL1(value)     (FLEXCOM_FLEX_SPI_CMPR_VAL1_Msk & ((value) << FLEXCOM_FLEX_SPI_CMPR_VAL1_Pos))
#define FLEXCOM_FLEX_SPI_CMPR_VAL2_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_SPI_CMPR) Second Comparison Value for Received Character Position */
#define FLEXCOM_FLEX_SPI_CMPR_VAL2_Msk        (_U_(0xFFFF) << FLEXCOM_FLEX_SPI_CMPR_VAL2_Pos) /**< (FLEXCOM_FLEX_SPI_CMPR) Second Comparison Value for Received Character Mask */
#define FLEXCOM_FLEX_SPI_CMPR_VAL2(value)     (FLEXCOM_FLEX_SPI_CMPR_VAL2_Msk & ((value) << FLEXCOM_FLEX_SPI_CMPR_VAL2_Pos))
#define FLEXCOM_FLEX_SPI_CMPR_Msk             _U_(0xFFFFFFFF)                                /**< (FLEXCOM_FLEX_SPI_CMPR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_WPMR : (FLEXCOM Offset: 0x4E4) (R/W 32) SPI Write Protection Mode Register -------- */
#define FLEXCOM_FLEX_SPI_WPMR_WPEN_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Enable Position */
#define FLEXCOM_FLEX_SPI_WPMR_WPEN_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_WPMR_WPEN_Pos)   /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Enable Mask */
#define FLEXCOM_FLEX_SPI_WPMR_WPITEN_Pos      _U_(1)                                         /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Interrupt Enable Position */
#define FLEXCOM_FLEX_SPI_WPMR_WPITEN_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_WPMR_WPITEN_Pos) /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Interrupt Enable Mask */
#define FLEXCOM_FLEX_SPI_WPMR_WPCREN_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Control Enable Position */
#define FLEXCOM_FLEX_SPI_WPMR_WPCREN_Msk      (_U_(0x1) << FLEXCOM_FLEX_SPI_WPMR_WPCREN_Pos) /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Control Enable Mask */
#define FLEXCOM_FLEX_SPI_WPMR_WPKEY_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Key Position */
#define FLEXCOM_FLEX_SPI_WPMR_WPKEY_Msk       (_U_(0xFFFFFF) << FLEXCOM_FLEX_SPI_WPMR_WPKEY_Pos) /**< (FLEXCOM_FLEX_SPI_WPMR) Write Protection Key Mask */
#define FLEXCOM_FLEX_SPI_WPMR_WPKEY(value)    (FLEXCOM_FLEX_SPI_WPMR_WPKEY_Msk & ((value) << FLEXCOM_FLEX_SPI_WPMR_WPKEY_Pos))
#define   FLEXCOM_FLEX_SPI_WPMR_WPKEY_PASSWD_Val _U_(0x535049)                                  /**< (FLEXCOM_FLEX_SPI_WPMR) Writing any other value in this field aborts the write operation of bits WPEN, WPITEN and WPCREN.Always reads as 0  */
#define FLEXCOM_FLEX_SPI_WPMR_WPKEY_PASSWD    (FLEXCOM_FLEX_SPI_WPMR_WPKEY_PASSWD_Val << FLEXCOM_FLEX_SPI_WPMR_WPKEY_Pos) /**< (FLEXCOM_FLEX_SPI_WPMR) Writing any other value in this field aborts the write operation of bits WPEN, WPITEN and WPCREN.Always reads as 0 Position  */
#define FLEXCOM_FLEX_SPI_WPMR_Msk             _U_(0xFFFFFF07)                                /**< (FLEXCOM_FLEX_SPI_WPMR) Register Mask  */


/* -------- FLEXCOM_FLEX_SPI_WPSR : (FLEXCOM Offset: 0x4E8) ( R/ 32) SPI Write Protection Status Register -------- */
#define FLEXCOM_FLEX_SPI_WPSR_WPVS_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_SPI_WPSR) Write Protection Violation Status Position */
#define FLEXCOM_FLEX_SPI_WPSR_WPVS_Msk        (_U_(0x1) << FLEXCOM_FLEX_SPI_WPSR_WPVS_Pos)   /**< (FLEXCOM_FLEX_SPI_WPSR) Write Protection Violation Status Mask */
#define FLEXCOM_FLEX_SPI_WPSR_WPVSRC_Pos      _U_(8)                                         /**< (FLEXCOM_FLEX_SPI_WPSR) Write Protection Violation Source Position */
#define FLEXCOM_FLEX_SPI_WPSR_WPVSRC_Msk      (_U_(0xFF) << FLEXCOM_FLEX_SPI_WPSR_WPVSRC_Pos) /**< (FLEXCOM_FLEX_SPI_WPSR) Write Protection Violation Source Mask */
#define FLEXCOM_FLEX_SPI_WPSR_WPVSRC(value)   (FLEXCOM_FLEX_SPI_WPSR_WPVSRC_Msk & ((value) << FLEXCOM_FLEX_SPI_WPSR_WPVSRC_Pos))
#define FLEXCOM_FLEX_SPI_WPSR_Msk             _U_(0x0000FF01)                                /**< (FLEXCOM_FLEX_SPI_WPSR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_CR : (FLEXCOM Offset: 0x600) ( /W 32) TWI Control Register -------- */
#define FLEXCOM_FLEX_TWI_CR_START_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_CR) Send a START Condition Position */
#define FLEXCOM_FLEX_TWI_CR_START_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_START_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) Send a START Condition Mask */
#define FLEXCOM_FLEX_TWI_CR_STOP_Pos          _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_CR) Send a STOP Condition Position */
#define FLEXCOM_FLEX_TWI_CR_STOP_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_STOP_Pos)     /**< (FLEXCOM_FLEX_TWI_CR) Send a STOP Condition Mask */
#define FLEXCOM_FLEX_TWI_CR_MSEN_Pos          _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_MSEN_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_MSEN_Pos)     /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_MSDIS_Pos         _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_MSDIS_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_MSDIS_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_SVEN_Pos          _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_SVEN_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_SVEN_Pos)     /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_SVDIS_Pos         _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_SVDIS_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_SVDIS_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_QUICK_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_CR) SMBus Quick Command Position */
#define FLEXCOM_FLEX_TWI_CR_QUICK_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_QUICK_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) SMBus Quick Command Mask */
#define FLEXCOM_FLEX_TWI_CR_SWRST_Pos         _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_CR) Software Reset Position */
#define FLEXCOM_FLEX_TWI_CR_SWRST_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_SWRST_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) Software Reset Mask */
#define FLEXCOM_FLEX_TWI_CR_HSEN_Pos          _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_HSEN_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_HSEN_Pos)     /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_HSDIS_Pos         _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_HSDIS_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_HSDIS_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_SMBEN_Pos         _U_(10)                                        /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_SMBEN_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_SMBEN_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_SMBDIS_Pos        _U_(11)                                        /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_SMBDIS_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_SMBDIS_Pos)   /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_PECEN_Pos         _U_(12)                                        /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Enable Position */
#define FLEXCOM_FLEX_TWI_CR_PECEN_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_PECEN_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Enable Mask */
#define FLEXCOM_FLEX_TWI_CR_PECDIS_Pos        _U_(13)                                        /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Disable Position */
#define FLEXCOM_FLEX_TWI_CR_PECDIS_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_PECDIS_Pos)   /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Disable Mask */
#define FLEXCOM_FLEX_TWI_CR_PECRQ_Pos         _U_(14)                                        /**< (FLEXCOM_FLEX_TWI_CR) PEC Request Position */
#define FLEXCOM_FLEX_TWI_CR_PECRQ_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_PECRQ_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) PEC Request Mask */
#define FLEXCOM_FLEX_TWI_CR_CLEAR_Pos         _U_(15)                                        /**< (FLEXCOM_FLEX_TWI_CR) Bus CLEAR Command Position */
#define FLEXCOM_FLEX_TWI_CR_CLEAR_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_CLEAR_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) Bus CLEAR Command Mask */
#define FLEXCOM_FLEX_TWI_CR_ACMEN_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Enable Position */
#define FLEXCOM_FLEX_TWI_CR_ACMEN_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_ACMEN_Pos)    /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Enable Mask */
#define FLEXCOM_FLEX_TWI_CR_ACMDIS_Pos        _U_(17)                                        /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Disable Position */
#define FLEXCOM_FLEX_TWI_CR_ACMDIS_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_ACMDIS_Pos)   /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Disable Mask */
#define FLEXCOM_FLEX_TWI_CR_THRCLR_Pos        _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_CR) Transmit Holding Register Clear Position */
#define FLEXCOM_FLEX_TWI_CR_THRCLR_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_THRCLR_Pos)   /**< (FLEXCOM_FLEX_TWI_CR) Transmit Holding Register Clear Mask */
#define FLEXCOM_FLEX_TWI_CR_LOCKCLR_Pos       _U_(26)                                        /**< (FLEXCOM_FLEX_TWI_CR) Lock Clear Position */
#define FLEXCOM_FLEX_TWI_CR_LOCKCLR_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_LOCKCLR_Pos)  /**< (FLEXCOM_FLEX_TWI_CR) Lock Clear Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFOEN_Pos        _U_(28)                                        /**< (FLEXCOM_FLEX_TWI_CR) FIFO Enable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFOEN_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFOEN_Pos)   /**< (FLEXCOM_FLEX_TWI_CR) FIFO Enable Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFODIS_Pos       _U_(29)                                        /**< (FLEXCOM_FLEX_TWI_CR) FIFO Disable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFODIS_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFODIS_Pos)  /**< (FLEXCOM_FLEX_TWI_CR) FIFO Disable Mask */
#define FLEXCOM_FLEX_TWI_CR_Msk               _U_(0x3503FFFF)                                /**< (FLEXCOM_FLEX_TWI_CR) Register Mask  */

/* FIFO_ENABLED mode */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_START_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_CR) Send a START Condition Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_START_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_START_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Send a START Condition Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_STOP_Pos _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_CR) Send a STOP Condition Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_STOP_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_STOP_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Send a STOP Condition Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_MSEN_Pos _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_MSEN_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_MSEN_Pos) /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_MSDIS_Pos _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_MSDIS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_MSDIS_Pos) /**< (FLEXCOM_FLEX_TWI_CR) TWI Master Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SVEN_Pos _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SVEN_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SVEN_Pos) /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SVDIS_Pos _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SVDIS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SVDIS_Pos) /**< (FLEXCOM_FLEX_TWI_CR) TWI Slave Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_QUICK_Pos _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_CR) SMBus Quick Command Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_QUICK_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_QUICK_Pos) /**< (FLEXCOM_FLEX_TWI_CR) SMBus Quick Command Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SWRST_Pos _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_CR) Software Reset Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SWRST_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SWRST_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Software Reset Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_HSEN_Pos _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_HSEN_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_HSEN_Pos) /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_HSDIS_Pos _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_HSDIS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_HSDIS_Pos) /**< (FLEXCOM_FLEX_TWI_CR) TWI High-Speed Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SMBEN_Pos _U_(10)                                        /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Enabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SMBEN_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SMBEN_Pos) /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Enabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SMBDIS_Pos _U_(11)                                        /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Disabled Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SMBDIS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_SMBDIS_Pos) /**< (FLEXCOM_FLEX_TWI_CR) SMBus Mode Disabled Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECEN_Pos _U_(12)                                        /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Enable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECEN_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECEN_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Enable Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECDIS_Pos _U_(13)                                        /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Disable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECDIS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECDIS_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Packet Error Checking Disable Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECRQ_Pos _U_(14)                                        /**< (FLEXCOM_FLEX_TWI_CR) PEC Request Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECRQ_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_PECRQ_Pos) /**< (FLEXCOM_FLEX_TWI_CR) PEC Request Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_CLEAR_Pos _U_(15)                                        /**< (FLEXCOM_FLEX_TWI_CR) Bus CLEAR Command Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_CLEAR_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_CLEAR_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Bus CLEAR Command Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_ACMEN_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Enable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_ACMEN_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_ACMEN_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Enable Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_ACMDIS_Pos _U_(17)                                        /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Disable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_ACMDIS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_ACMDIS_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Alternative Command Mode Disable Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_TXFCLR_Pos _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_CR) Transmit FIFO Clear Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_TXFCLR_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_TXFCLR_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Transmit FIFO Clear Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_RXFCLR_Pos _U_(25)                                        /**< (FLEXCOM_FLEX_TWI_CR) Receive FIFO Clear Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_RXFCLR_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_RXFCLR_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Receive FIFO Clear Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_TXFLCLR_Pos _U_(26)                                        /**< (FLEXCOM_FLEX_TWI_CR) Transmit FIFO Lock CLEAR Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_TXFLCLR_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_TXFLCLR_Pos) /**< (FLEXCOM_FLEX_TWI_CR) Transmit FIFO Lock CLEAR Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_FIFOEN_Pos _U_(28)                                        /**< (FLEXCOM_FLEX_TWI_CR) FIFO Enable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_FIFOEN_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_FIFOEN_Pos) /**< (FLEXCOM_FLEX_TWI_CR) FIFO Enable Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_FIFODIS_Pos _U_(29)                                        /**< (FLEXCOM_FLEX_TWI_CR) FIFO Disable Position */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_FIFODIS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_FIFODIS_Pos) /**< (FLEXCOM_FLEX_TWI_CR) FIFO Disable Mask */
#define FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED_Msk _U_(0x3703FFFF)                                 /**< (FLEXCOM_FLEX_TWI_CR_FIFO_ENABLED) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_MMR : (FLEXCOM Offset: 0x604) (R/W 32) TWI Master Mode Register -------- */
#define FLEXCOM_FLEX_TWI_MMR_IADRSZ_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_MMR) Internal Device Address Size Position */
#define FLEXCOM_FLEX_TWI_MMR_IADRSZ_Msk       (_U_(0x3) << FLEXCOM_FLEX_TWI_MMR_IADRSZ_Pos)  /**< (FLEXCOM_FLEX_TWI_MMR) Internal Device Address Size Mask */
#define FLEXCOM_FLEX_TWI_MMR_IADRSZ(value)    (FLEXCOM_FLEX_TWI_MMR_IADRSZ_Msk & ((value) << FLEXCOM_FLEX_TWI_MMR_IADRSZ_Pos))
#define   FLEXCOM_FLEX_TWI_MMR_IADRSZ_NONE_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_TWI_MMR) No internal device address  */
#define   FLEXCOM_FLEX_TWI_MMR_IADRSZ_1_BYTE_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_TWI_MMR) One-byte internal device address  */
#define   FLEXCOM_FLEX_TWI_MMR_IADRSZ_2_BYTE_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_TWI_MMR) Two-byte internal device address  */
#define   FLEXCOM_FLEX_TWI_MMR_IADRSZ_3_BYTE_Val _U_(0x3)                                       /**< (FLEXCOM_FLEX_TWI_MMR) Three-byte internal device address  */
#define FLEXCOM_FLEX_TWI_MMR_IADRSZ_NONE      (FLEXCOM_FLEX_TWI_MMR_IADRSZ_NONE_Val << FLEXCOM_FLEX_TWI_MMR_IADRSZ_Pos) /**< (FLEXCOM_FLEX_TWI_MMR) No internal device address Position  */
#define FLEXCOM_FLEX_TWI_MMR_IADRSZ_1_BYTE    (FLEXCOM_FLEX_TWI_MMR_IADRSZ_1_BYTE_Val << FLEXCOM_FLEX_TWI_MMR_IADRSZ_Pos) /**< (FLEXCOM_FLEX_TWI_MMR) One-byte internal device address Position  */
#define FLEXCOM_FLEX_TWI_MMR_IADRSZ_2_BYTE    (FLEXCOM_FLEX_TWI_MMR_IADRSZ_2_BYTE_Val << FLEXCOM_FLEX_TWI_MMR_IADRSZ_Pos) /**< (FLEXCOM_FLEX_TWI_MMR) Two-byte internal device address Position  */
#define FLEXCOM_FLEX_TWI_MMR_IADRSZ_3_BYTE    (FLEXCOM_FLEX_TWI_MMR_IADRSZ_3_BYTE_Val << FLEXCOM_FLEX_TWI_MMR_IADRSZ_Pos) /**< (FLEXCOM_FLEX_TWI_MMR) Three-byte internal device address Position  */
#define FLEXCOM_FLEX_TWI_MMR_MREAD_Pos        _U_(12)                                        /**< (FLEXCOM_FLEX_TWI_MMR) Master Read Direction Position */
#define FLEXCOM_FLEX_TWI_MMR_MREAD_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_MMR_MREAD_Pos)   /**< (FLEXCOM_FLEX_TWI_MMR) Master Read Direction Mask */
#define FLEXCOM_FLEX_TWI_MMR_DADR_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_MMR) Device Address Position */
#define FLEXCOM_FLEX_TWI_MMR_DADR_Msk         (_U_(0x7F) << FLEXCOM_FLEX_TWI_MMR_DADR_Pos)   /**< (FLEXCOM_FLEX_TWI_MMR) Device Address Mask */
#define FLEXCOM_FLEX_TWI_MMR_DADR(value)      (FLEXCOM_FLEX_TWI_MMR_DADR_Msk & ((value) << FLEXCOM_FLEX_TWI_MMR_DADR_Pos))
#define FLEXCOM_FLEX_TWI_MMR_NOAP_Pos         _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_MMR) No Auto-Stop On NACK Error Position */
#define FLEXCOM_FLEX_TWI_MMR_NOAP_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_MMR_NOAP_Pos)    /**< (FLEXCOM_FLEX_TWI_MMR) No Auto-Stop On NACK Error Mask */
#define FLEXCOM_FLEX_TWI_MMR_Msk              _U_(0x017F1300)                                /**< (FLEXCOM_FLEX_TWI_MMR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_SMR : (FLEXCOM Offset: 0x608) (R/W 32) TWI Slave Mode Register -------- */
#define FLEXCOM_FLEX_TWI_SMR_NACKEN_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_SMR) Slave Receiver Data Phase NACK Enable Position */
#define FLEXCOM_FLEX_TWI_SMR_NACKEN_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_SMR_NACKEN_Pos)  /**< (FLEXCOM_FLEX_TWI_SMR) Slave Receiver Data Phase NACK Enable Mask */
#define FLEXCOM_FLEX_TWI_SMR_SMDA_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_SMR) SMBus Default Address Position */
#define FLEXCOM_FLEX_TWI_SMR_SMDA_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_SMR_SMDA_Pos)    /**< (FLEXCOM_FLEX_TWI_SMR) SMBus Default Address Mask */
#define FLEXCOM_FLEX_TWI_SMR_SMHH_Pos         _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_SMR) SMBus Host Header Position */
#define FLEXCOM_FLEX_TWI_SMR_SMHH_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_SMR_SMHH_Pos)    /**< (FLEXCOM_FLEX_TWI_SMR) SMBus Host Header Mask */
#define FLEXCOM_FLEX_TWI_SMR_SADAT_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_SMR) Slave Address Treated as Data Position */
#define FLEXCOM_FLEX_TWI_SMR_SADAT_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SMR_SADAT_Pos)   /**< (FLEXCOM_FLEX_TWI_SMR) Slave Address Treated as Data Mask */
#define FLEXCOM_FLEX_TWI_SMR_SCLWSDIS_Pos     _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_SMR) Clock Wait State Disable Position */
#define FLEXCOM_FLEX_TWI_SMR_SCLWSDIS_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_SMR_SCLWSDIS_Pos) /**< (FLEXCOM_FLEX_TWI_SMR) Clock Wait State Disable Mask */
#define FLEXCOM_FLEX_TWI_SMR_SNIFF_Pos        _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_SMR) Slave Sniffer Mode Position */
#define FLEXCOM_FLEX_TWI_SMR_SNIFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SMR_SNIFF_Pos)   /**< (FLEXCOM_FLEX_TWI_SMR) Slave Sniffer Mode Mask */
#define FLEXCOM_FLEX_TWI_SMR_MASK_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_SMR) Slave Address Mask Position */
#define FLEXCOM_FLEX_TWI_SMR_MASK_Msk         (_U_(0x7F) << FLEXCOM_FLEX_TWI_SMR_MASK_Pos)   /**< (FLEXCOM_FLEX_TWI_SMR) Slave Address Mask Mask */
#define FLEXCOM_FLEX_TWI_SMR_MASK(value)      (FLEXCOM_FLEX_TWI_SMR_MASK_Msk & ((value) << FLEXCOM_FLEX_TWI_SMR_MASK_Pos))
#define FLEXCOM_FLEX_TWI_SMR_SADR_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_SMR) Slave Address Position */
#define FLEXCOM_FLEX_TWI_SMR_SADR_Msk         (_U_(0x7F) << FLEXCOM_FLEX_TWI_SMR_SADR_Pos)   /**< (FLEXCOM_FLEX_TWI_SMR) Slave Address Mask */
#define FLEXCOM_FLEX_TWI_SMR_SADR(value)      (FLEXCOM_FLEX_TWI_SMR_SADR_Msk & ((value) << FLEXCOM_FLEX_TWI_SMR_SADR_Pos))
#define FLEXCOM_FLEX_TWI_SMR_Msk              _U_(0x007F7FDD)                                /**< (FLEXCOM_FLEX_TWI_SMR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_IADR : (FLEXCOM Offset: 0x60C) (R/W 32) TWI Internal Address Register -------- */
#define FLEXCOM_FLEX_TWI_IADR_IADR_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_IADR) Internal Address Position */
#define FLEXCOM_FLEX_TWI_IADR_IADR_Msk        (_U_(0xFFFFFF) << FLEXCOM_FLEX_TWI_IADR_IADR_Pos) /**< (FLEXCOM_FLEX_TWI_IADR) Internal Address Mask */
#define FLEXCOM_FLEX_TWI_IADR_IADR(value)     (FLEXCOM_FLEX_TWI_IADR_IADR_Msk & ((value) << FLEXCOM_FLEX_TWI_IADR_IADR_Pos))
#define FLEXCOM_FLEX_TWI_IADR_Msk             _U_(0x00FFFFFF)                                /**< (FLEXCOM_FLEX_TWI_IADR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_CWGR : (FLEXCOM Offset: 0x610) (R/W 32) TWI Clock Waveform Generator Register -------- */
#define FLEXCOM_FLEX_TWI_CWGR_CLDIV_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_CWGR) Clock Low Divider Position */
#define FLEXCOM_FLEX_TWI_CWGR_CLDIV_Msk       (_U_(0xFF) << FLEXCOM_FLEX_TWI_CWGR_CLDIV_Pos) /**< (FLEXCOM_FLEX_TWI_CWGR) Clock Low Divider Mask */
#define FLEXCOM_FLEX_TWI_CWGR_CLDIV(value)    (FLEXCOM_FLEX_TWI_CWGR_CLDIV_Msk & ((value) << FLEXCOM_FLEX_TWI_CWGR_CLDIV_Pos))
#define FLEXCOM_FLEX_TWI_CWGR_CHDIV_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_CWGR) Clock High Divider Position */
#define FLEXCOM_FLEX_TWI_CWGR_CHDIV_Msk       (_U_(0xFF) << FLEXCOM_FLEX_TWI_CWGR_CHDIV_Pos) /**< (FLEXCOM_FLEX_TWI_CWGR) Clock High Divider Mask */
#define FLEXCOM_FLEX_TWI_CWGR_CHDIV(value)    (FLEXCOM_FLEX_TWI_CWGR_CHDIV_Msk & ((value) << FLEXCOM_FLEX_TWI_CWGR_CHDIV_Pos))
#define FLEXCOM_FLEX_TWI_CWGR_CKDIV_Pos       _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_CWGR) Clock Divider Position */
#define FLEXCOM_FLEX_TWI_CWGR_CKDIV_Msk       (_U_(0x7) << FLEXCOM_FLEX_TWI_CWGR_CKDIV_Pos)  /**< (FLEXCOM_FLEX_TWI_CWGR) Clock Divider Mask */
#define FLEXCOM_FLEX_TWI_CWGR_CKDIV(value)    (FLEXCOM_FLEX_TWI_CWGR_CKDIV_Msk & ((value) << FLEXCOM_FLEX_TWI_CWGR_CKDIV_Pos))
#define FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_Pos    _U_(20)                                        /**< (FLEXCOM_FLEX_TWI_CWGR) Bit Rate Source Clock Position */
#define FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_Msk    (_U_(0x1) << FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_Pos) /**< (FLEXCOM_FLEX_TWI_CWGR) Bit Rate Source Clock Mask */
#define   FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_PERIPH_CLK_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_TWI_CWGR) The peripheral clock is the source clock for the bit rate generation.  */
#define   FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_GCLK_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_TWI_CWGR) GCLK is the source clock for the bit rate generation, thus the bit rate can be independent of the core/peripheral clock.  */
#define FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_PERIPH_CLK (FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_PERIPH_CLK_Val << FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_Pos) /**< (FLEXCOM_FLEX_TWI_CWGR) The peripheral clock is the source clock for the bit rate generation. Position  */
#define FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_GCLK   (FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_GCLK_Val << FLEXCOM_FLEX_TWI_CWGR_BRSRCCLK_Pos) /**< (FLEXCOM_FLEX_TWI_CWGR) GCLK is the source clock for the bit rate generation, thus the bit rate can be independent of the core/peripheral clock. Position  */
#define FLEXCOM_FLEX_TWI_CWGR_HOLD_Pos        _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_CWGR) TWD Hold Time Versus TWCK Falling Position */
#define FLEXCOM_FLEX_TWI_CWGR_HOLD_Msk        (_U_(0x3F) << FLEXCOM_FLEX_TWI_CWGR_HOLD_Pos)  /**< (FLEXCOM_FLEX_TWI_CWGR) TWD Hold Time Versus TWCK Falling Mask */
#define FLEXCOM_FLEX_TWI_CWGR_HOLD(value)     (FLEXCOM_FLEX_TWI_CWGR_HOLD_Msk & ((value) << FLEXCOM_FLEX_TWI_CWGR_HOLD_Pos))
#define FLEXCOM_FLEX_TWI_CWGR_Msk             _U_(0x3F17FFFF)                                /**< (FLEXCOM_FLEX_TWI_CWGR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_SR : (FLEXCOM Offset: 0x620) ( R/ 32) TWI Status Register -------- */
#define FLEXCOM_FLEX_TWI_SR_TXCOMP_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_SR) Transmission Completed (cleared by writing FLEX_TWI_THR) Position */
#define FLEXCOM_FLEX_TWI_SR_TXCOMP_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_TXCOMP_Pos)   /**< (FLEXCOM_FLEX_TWI_SR) Transmission Completed (cleared by writing FLEX_TWI_THR) Mask */
#define FLEXCOM_FLEX_TWI_SR_RXRDY_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_SR) Receive Holding Register Ready (cleared when reading FLEX_TWI_RHR) Position */
#define FLEXCOM_FLEX_TWI_SR_RXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_RXRDY_Pos)    /**< (FLEXCOM_FLEX_TWI_SR) Receive Holding Register Ready (cleared when reading FLEX_TWI_RHR) Mask */
#define FLEXCOM_FLEX_TWI_SR_TXRDY_Pos         _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_SR) Transmit Holding Register Ready (cleared by writing FLEX_TWI_THR) Position */
#define FLEXCOM_FLEX_TWI_SR_TXRDY_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_TXRDY_Pos)    /**< (FLEXCOM_FLEX_TWI_SR) Transmit Holding Register Ready (cleared by writing FLEX_TWI_THR) Mask */
#define FLEXCOM_FLEX_TWI_SR_SVREAD_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_SR) Slave Read Position */
#define FLEXCOM_FLEX_TWI_SR_SVREAD_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_SVREAD_Pos)   /**< (FLEXCOM_FLEX_TWI_SR) Slave Read Mask */
#define FLEXCOM_FLEX_TWI_SR_SVACC_Pos         _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_SR) Slave Access Position */
#define FLEXCOM_FLEX_TWI_SR_SVACC_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_SVACC_Pos)    /**< (FLEXCOM_FLEX_TWI_SR) Slave Access Mask */
#define FLEXCOM_FLEX_TWI_SR_GACC_Pos          _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_SR) General Call Access (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_GACC_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_GACC_Pos)     /**< (FLEXCOM_FLEX_TWI_SR) General Call Access (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_OVRE_Pos          _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_SR) Overrun Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_OVRE_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_OVRE_Pos)     /**< (FLEXCOM_FLEX_TWI_SR) Overrun Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_UNRE_Pos          _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_SR) Underrun Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_UNRE_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_UNRE_Pos)     /**< (FLEXCOM_FLEX_TWI_SR) Underrun Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_NACK_Pos          _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_SR) Not Acknowledged (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_NACK_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_NACK_Pos)     /**< (FLEXCOM_FLEX_TWI_SR) Not Acknowledged (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_ARBLST_Pos        _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_SR) Arbitration Lost (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_ARBLST_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_ARBLST_Pos)   /**< (FLEXCOM_FLEX_TWI_SR) Arbitration Lost (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_SCLWS_Pos         _U_(10)                                        /**< (FLEXCOM_FLEX_TWI_SR) Clock Wait State Position */
#define FLEXCOM_FLEX_TWI_SR_SCLWS_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_SCLWS_Pos)    /**< (FLEXCOM_FLEX_TWI_SR) Clock Wait State Mask */
#define FLEXCOM_FLEX_TWI_SR_EOSACC_Pos        _U_(11)                                        /**< (FLEXCOM_FLEX_TWI_SR) End Of Slave Access (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_EOSACC_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_EOSACC_Pos)   /**< (FLEXCOM_FLEX_TWI_SR) End Of Slave Access (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_MCACK_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_SR) Master Code Acknowledge (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_MCACK_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_MCACK_Pos)    /**< (FLEXCOM_FLEX_TWI_SR) Master Code Acknowledge (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_TOUT_Pos          _U_(18)                                        /**< (FLEXCOM_FLEX_TWI_SR) Timeout Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_TOUT_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_TOUT_Pos)     /**< (FLEXCOM_FLEX_TWI_SR) Timeout Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_PECERR_Pos        _U_(19)                                        /**< (FLEXCOM_FLEX_TWI_SR) PEC Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_PECERR_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_PECERR_Pos)   /**< (FLEXCOM_FLEX_TWI_SR) PEC Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_SMBDAM_Pos        _U_(20)                                        /**< (FLEXCOM_FLEX_TWI_SR) SMBus Default Address Match (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_SMBDAM_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_SMBDAM_Pos)   /**< (FLEXCOM_FLEX_TWI_SR) SMBus Default Address Match (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_SMBHHM_Pos        _U_(21)                                        /**< (FLEXCOM_FLEX_TWI_SR) SMBus Host Header Address Match (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_SMBHHM_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_SMBHHM_Pos)   /**< (FLEXCOM_FLEX_TWI_SR) SMBus Host Header Address Match (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_LOCK_Pos          _U_(23)                                        /**< (FLEXCOM_FLEX_TWI_SR) TWI Lock Due to Frame Errors Position */
#define FLEXCOM_FLEX_TWI_SR_LOCK_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_LOCK_Pos)     /**< (FLEXCOM_FLEX_TWI_SR) TWI Lock Due to Frame Errors Mask */
#define FLEXCOM_FLEX_TWI_SR_SCL_Pos           _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_SR) SCL Line Value Position */
#define FLEXCOM_FLEX_TWI_SR_SCL_Msk           (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_SCL_Pos)      /**< (FLEXCOM_FLEX_TWI_SR) SCL Line Value Mask */
#define FLEXCOM_FLEX_TWI_SR_SDA_Pos           _U_(25)                                        /**< (FLEXCOM_FLEX_TWI_SR) SDA Line Value Position */
#define FLEXCOM_FLEX_TWI_SR_SDA_Msk           (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_SDA_Pos)      /**< (FLEXCOM_FLEX_TWI_SR) SDA Line Value Mask */
#define FLEXCOM_FLEX_TWI_SR_Msk               _U_(0x03BD0FFF)                                /**< (FLEXCOM_FLEX_TWI_SR) Register Mask  */

/* FIFO_ENABLED mode */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXCOMP_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_SR) Transmission Completed (cleared by writing FLEX_TWI_THR) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXCOMP_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXCOMP_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Transmission Completed (cleared by writing FLEX_TWI_THR) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_RXRDY_Pos _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_SR) Receive Holding Register Ready (cleared when reading FLEX_TWI_RHR) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_RXRDY_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_RXRDY_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Receive Holding Register Ready (cleared when reading FLEX_TWI_RHR) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXRDY_Pos _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_SR) Transmit Holding Register Ready (cleared by writing FLEX_TWI_THR) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXRDY_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXRDY_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Transmit Holding Register Ready (cleared by writing FLEX_TWI_THR) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SVREAD_Pos _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_SR) Slave Read Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SVREAD_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SVREAD_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Slave Read Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SVACC_Pos _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_SR) Slave Access Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SVACC_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SVACC_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Slave Access Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_GACC_Pos _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_SR) General Call Access (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_GACC_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_GACC_Pos) /**< (FLEXCOM_FLEX_TWI_SR) General Call Access (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_OVRE_Pos _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_SR) Overrun Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_OVRE_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_OVRE_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Overrun Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_UNRE_Pos _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_SR) Underrun Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_UNRE_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_UNRE_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Underrun Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_NACK_Pos _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_SR) Not Acknowledged (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_NACK_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_NACK_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Not Acknowledged (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_ARBLST_Pos _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_SR) Arbitration Lost (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_ARBLST_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_ARBLST_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Arbitration Lost (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SCLWS_Pos _U_(10)                                        /**< (FLEXCOM_FLEX_TWI_SR) Clock Wait State Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SCLWS_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SCLWS_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Clock Wait State Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_EOSACC_Pos _U_(11)                                        /**< (FLEXCOM_FLEX_TWI_SR) End Of Slave Access (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_EOSACC_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_EOSACC_Pos) /**< (FLEXCOM_FLEX_TWI_SR) End Of Slave Access (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_MCACK_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_SR) Master Code Acknowledge (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_MCACK_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_MCACK_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Master Code Acknowledge (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TOUT_Pos _U_(18)                                        /**< (FLEXCOM_FLEX_TWI_SR) Timeout Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TOUT_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TOUT_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Timeout Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_PECERR_Pos _U_(19)                                        /**< (FLEXCOM_FLEX_TWI_SR) PEC Error (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_PECERR_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_PECERR_Pos) /**< (FLEXCOM_FLEX_TWI_SR) PEC Error (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SMBDAM_Pos _U_(20)                                        /**< (FLEXCOM_FLEX_TWI_SR) SMBus Default Address Match (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SMBDAM_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SMBDAM_Pos) /**< (FLEXCOM_FLEX_TWI_SR) SMBus Default Address Match (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SMBHHM_Pos _U_(21)                                        /**< (FLEXCOM_FLEX_TWI_SR) SMBus Host Header Address Match (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SMBHHM_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SMBHHM_Pos) /**< (FLEXCOM_FLEX_TWI_SR) SMBus Host Header Address Match (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXFLOCK_Pos _U_(23)                                        /**< (FLEXCOM_FLEX_TWI_SR) Transmit FIFO Lock Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXFLOCK_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_TXFLOCK_Pos) /**< (FLEXCOM_FLEX_TWI_SR) Transmit FIFO Lock Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SCL_Pos _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_SR) SCL Line Value Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SCL_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SCL_Pos) /**< (FLEXCOM_FLEX_TWI_SR) SCL Line Value Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SDA_Pos _U_(25)                                        /**< (FLEXCOM_FLEX_TWI_SR) SDA Line Value Position */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SDA_Msk (_U_(0x1) << FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_SDA_Pos) /**< (FLEXCOM_FLEX_TWI_SR) SDA Line Value Mask */
#define FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED_Msk _U_(0x03BD0FFF)                                 /**< (FLEXCOM_FLEX_TWI_SR_FIFO_ENABLED) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_IER : (FLEXCOM Offset: 0x624) ( /W 32) TWI Interrupt Enable Register -------- */
#define FLEXCOM_FLEX_TWI_IER_TXCOMP_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_IER) Transmission Completed Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_TXCOMP_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_TXCOMP_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) Transmission Completed Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_RXRDY_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_IER) Receive Holding Register Ready Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_RXRDY_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_RXRDY_Pos)   /**< (FLEXCOM_FLEX_TWI_IER) Receive Holding Register Ready Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_TXRDY_Pos        _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_IER) Transmit Holding Register Ready Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_TXRDY_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_TXRDY_Pos)   /**< (FLEXCOM_FLEX_TWI_IER) Transmit Holding Register Ready Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_SVACC_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_IER) Slave Access Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_SVACC_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_SVACC_Pos)   /**< (FLEXCOM_FLEX_TWI_IER) Slave Access Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_GACC_Pos         _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_IER) General Call Access Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_GACC_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_GACC_Pos)    /**< (FLEXCOM_FLEX_TWI_IER) General Call Access Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_OVRE_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_IER) Overrun Error Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_OVRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_OVRE_Pos)    /**< (FLEXCOM_FLEX_TWI_IER) Overrun Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_UNRE_Pos         _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_IER) Underrun Error Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_UNRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_UNRE_Pos)    /**< (FLEXCOM_FLEX_TWI_IER) Underrun Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_NACK_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_IER) Not Acknowledge Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_NACK_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_NACK_Pos)    /**< (FLEXCOM_FLEX_TWI_IER) Not Acknowledge Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_ARBLST_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_IER) Arbitration Lost Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_ARBLST_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_ARBLST_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) Arbitration Lost Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_SCL_WS_Pos       _U_(10)                                        /**< (FLEXCOM_FLEX_TWI_IER) Clock Wait State Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_SCL_WS_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_SCL_WS_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) Clock Wait State Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_EOSACC_Pos       _U_(11)                                        /**< (FLEXCOM_FLEX_TWI_IER) End Of Slave Access Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_EOSACC_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_EOSACC_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) End Of Slave Access Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_ENDRX_Pos        _U_(12)                                        /**< (FLEXCOM_FLEX_TWI_IER) End of Receive Buffer Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_ENDRX_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_ENDRX_Pos)   /**< (FLEXCOM_FLEX_TWI_IER) End of Receive Buffer Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_ENDTX_Pos        _U_(13)                                        /**< (FLEXCOM_FLEX_TWI_IER) End of Transmit Buffer Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_ENDTX_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_ENDTX_Pos)   /**< (FLEXCOM_FLEX_TWI_IER) End of Transmit Buffer Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_RXBUFF_Pos       _U_(14)                                        /**< (FLEXCOM_FLEX_TWI_IER) Receive Buffer Full Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_RXBUFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_RXBUFF_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) Receive Buffer Full Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_TXBUFE_Pos       _U_(15)                                        /**< (FLEXCOM_FLEX_TWI_IER) Transmit Buffer Empty Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_TXBUFE_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_TXBUFE_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) Transmit Buffer Empty Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_MCACK_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_IER) Master Code Acknowledge Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_MCACK_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_MCACK_Pos)   /**< (FLEXCOM_FLEX_TWI_IER) Master Code Acknowledge Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_TOUT_Pos         _U_(18)                                        /**< (FLEXCOM_FLEX_TWI_IER) Timeout Error Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_TOUT_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_TOUT_Pos)    /**< (FLEXCOM_FLEX_TWI_IER) Timeout Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_PECERR_Pos       _U_(19)                                        /**< (FLEXCOM_FLEX_TWI_IER) PEC Error Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_PECERR_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_PECERR_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) PEC Error Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_SMBDAM_Pos       _U_(20)                                        /**< (FLEXCOM_FLEX_TWI_IER) SMBus Default Address Match Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_SMBDAM_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_SMBDAM_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) SMBus Default Address Match Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_SMBHHM_Pos       _U_(21)                                        /**< (FLEXCOM_FLEX_TWI_IER) SMBus Host Header Address Match Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_IER_SMBHHM_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IER_SMBHHM_Pos)  /**< (FLEXCOM_FLEX_TWI_IER) SMBus Host Header Address Match Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_IER_Msk              _U_(0x003DFFF7)                                /**< (FLEXCOM_FLEX_TWI_IER) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_IDR : (FLEXCOM Offset: 0x628) ( /W 32) TWI Interrupt Disable Register -------- */
#define FLEXCOM_FLEX_TWI_IDR_TXCOMP_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Transmission Completed Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_TXCOMP_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_TXCOMP_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) Transmission Completed Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_RXRDY_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Receive Holding Register Ready Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_RXRDY_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_RXRDY_Pos)   /**< (FLEXCOM_FLEX_TWI_IDR) Receive Holding Register Ready Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_TXRDY_Pos        _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Transmit Holding Register Ready Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_TXRDY_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_TXRDY_Pos)   /**< (FLEXCOM_FLEX_TWI_IDR) Transmit Holding Register Ready Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_SVACC_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Slave Access Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_SVACC_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_SVACC_Pos)   /**< (FLEXCOM_FLEX_TWI_IDR) Slave Access Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_GACC_Pos         _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_IDR) General Call Access Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_GACC_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_GACC_Pos)    /**< (FLEXCOM_FLEX_TWI_IDR) General Call Access Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_OVRE_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Overrun Error Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_OVRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_OVRE_Pos)    /**< (FLEXCOM_FLEX_TWI_IDR) Overrun Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_UNRE_Pos         _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Underrun Error Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_UNRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_UNRE_Pos)    /**< (FLEXCOM_FLEX_TWI_IDR) Underrun Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_NACK_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Not Acknowledge Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_NACK_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_NACK_Pos)    /**< (FLEXCOM_FLEX_TWI_IDR) Not Acknowledge Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_ARBLST_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_IDR) Arbitration Lost Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_ARBLST_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_ARBLST_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) Arbitration Lost Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_SCL_WS_Pos       _U_(10)                                        /**< (FLEXCOM_FLEX_TWI_IDR) Clock Wait State Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_SCL_WS_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_SCL_WS_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) Clock Wait State Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_EOSACC_Pos       _U_(11)                                        /**< (FLEXCOM_FLEX_TWI_IDR) End Of Slave Access Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_EOSACC_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_EOSACC_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) End Of Slave Access Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_ENDRX_Pos        _U_(12)                                        /**< (FLEXCOM_FLEX_TWI_IDR) End of Receive Buffer Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_ENDRX_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_ENDRX_Pos)   /**< (FLEXCOM_FLEX_TWI_IDR) End of Receive Buffer Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_ENDTX_Pos        _U_(13)                                        /**< (FLEXCOM_FLEX_TWI_IDR) End of Transmit Buffer Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_ENDTX_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_ENDTX_Pos)   /**< (FLEXCOM_FLEX_TWI_IDR) End of Transmit Buffer Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_RXBUFF_Pos       _U_(14)                                        /**< (FLEXCOM_FLEX_TWI_IDR) Receive Buffer Full Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_RXBUFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_RXBUFF_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) Receive Buffer Full Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_TXBUFE_Pos       _U_(15)                                        /**< (FLEXCOM_FLEX_TWI_IDR) Transmit Buffer Empty Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_TXBUFE_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_TXBUFE_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) Transmit Buffer Empty Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_MCACK_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_IDR) Master Code Acknowledge Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_MCACK_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_MCACK_Pos)   /**< (FLEXCOM_FLEX_TWI_IDR) Master Code Acknowledge Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_TOUT_Pos         _U_(18)                                        /**< (FLEXCOM_FLEX_TWI_IDR) Timeout Error Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_TOUT_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_TOUT_Pos)    /**< (FLEXCOM_FLEX_TWI_IDR) Timeout Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_PECERR_Pos       _U_(19)                                        /**< (FLEXCOM_FLEX_TWI_IDR) PEC Error Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_PECERR_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_PECERR_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) PEC Error Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_SMBDAM_Pos       _U_(20)                                        /**< (FLEXCOM_FLEX_TWI_IDR) SMBus Default Address Match Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_SMBDAM_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_SMBDAM_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) SMBus Default Address Match Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_SMBHHM_Pos       _U_(21)                                        /**< (FLEXCOM_FLEX_TWI_IDR) SMBus Host Header Address Match Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_IDR_SMBHHM_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IDR_SMBHHM_Pos)  /**< (FLEXCOM_FLEX_TWI_IDR) SMBus Host Header Address Match Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_IDR_Msk              _U_(0x003DFFF7)                                /**< (FLEXCOM_FLEX_TWI_IDR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_IMR : (FLEXCOM Offset: 0x62C) ( R/ 32) TWI Interrupt Mask Register -------- */
#define FLEXCOM_FLEX_TWI_IMR_TXCOMP_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Transmission Completed Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_TXCOMP_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_TXCOMP_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) Transmission Completed Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_RXRDY_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Receive Holding Register Ready Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_RXRDY_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_RXRDY_Pos)   /**< (FLEXCOM_FLEX_TWI_IMR) Receive Holding Register Ready Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_TXRDY_Pos        _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Transmit Holding Register Ready Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_TXRDY_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_TXRDY_Pos)   /**< (FLEXCOM_FLEX_TWI_IMR) Transmit Holding Register Ready Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_SVACC_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Slave Access Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_SVACC_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_SVACC_Pos)   /**< (FLEXCOM_FLEX_TWI_IMR) Slave Access Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_GACC_Pos         _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_IMR) General Call Access Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_GACC_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_GACC_Pos)    /**< (FLEXCOM_FLEX_TWI_IMR) General Call Access Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_OVRE_Pos         _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Overrun Error Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_OVRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_OVRE_Pos)    /**< (FLEXCOM_FLEX_TWI_IMR) Overrun Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_UNRE_Pos         _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Underrun Error Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_UNRE_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_UNRE_Pos)    /**< (FLEXCOM_FLEX_TWI_IMR) Underrun Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_NACK_Pos         _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Not Acknowledge Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_NACK_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_NACK_Pos)    /**< (FLEXCOM_FLEX_TWI_IMR) Not Acknowledge Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_ARBLST_Pos       _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_IMR) Arbitration Lost Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_ARBLST_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_ARBLST_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) Arbitration Lost Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_SCL_WS_Pos       _U_(10)                                        /**< (FLEXCOM_FLEX_TWI_IMR) Clock Wait State Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_SCL_WS_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_SCL_WS_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) Clock Wait State Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_EOSACC_Pos       _U_(11)                                        /**< (FLEXCOM_FLEX_TWI_IMR) End Of Slave Access Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_EOSACC_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_EOSACC_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) End Of Slave Access Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_ENDRX_Pos        _U_(12)                                        /**< (FLEXCOM_FLEX_TWI_IMR) End of Receive Buffer Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_ENDRX_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_ENDRX_Pos)   /**< (FLEXCOM_FLEX_TWI_IMR) End of Receive Buffer Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_ENDTX_Pos        _U_(13)                                        /**< (FLEXCOM_FLEX_TWI_IMR) End of Transmit Buffer Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_ENDTX_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_ENDTX_Pos)   /**< (FLEXCOM_FLEX_TWI_IMR) End of Transmit Buffer Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_RXBUFF_Pos       _U_(14)                                        /**< (FLEXCOM_FLEX_TWI_IMR) Receive Buffer Full Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_RXBUFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_RXBUFF_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) Receive Buffer Full Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_TXBUFE_Pos       _U_(15)                                        /**< (FLEXCOM_FLEX_TWI_IMR) Transmit Buffer Empty Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_TXBUFE_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_TXBUFE_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) Transmit Buffer Empty Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_MCACK_Pos        _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_IMR) Master Code Acknowledge Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_MCACK_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_MCACK_Pos)   /**< (FLEXCOM_FLEX_TWI_IMR) Master Code Acknowledge Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_TOUT_Pos         _U_(18)                                        /**< (FLEXCOM_FLEX_TWI_IMR) Timeout Error Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_TOUT_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_TOUT_Pos)    /**< (FLEXCOM_FLEX_TWI_IMR) Timeout Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_PECERR_Pos       _U_(19)                                        /**< (FLEXCOM_FLEX_TWI_IMR) PEC Error Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_PECERR_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_PECERR_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) PEC Error Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_SMBDAM_Pos       _U_(20)                                        /**< (FLEXCOM_FLEX_TWI_IMR) SMBus Default Address Match Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_SMBDAM_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_SMBDAM_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) SMBus Default Address Match Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_SMBHHM_Pos       _U_(21)                                        /**< (FLEXCOM_FLEX_TWI_IMR) SMBus Host Header Address Match Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_IMR_SMBHHM_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_IMR_SMBHHM_Pos)  /**< (FLEXCOM_FLEX_TWI_IMR) SMBus Host Header Address Match Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_IMR_Msk              _U_(0x003DFFF7)                                /**< (FLEXCOM_FLEX_TWI_IMR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_RHR : (FLEXCOM Offset: 0x630) ( R/ 32) TWI Receive Holding Register -------- */
#define FLEXCOM_FLEX_TWI_RHR_RXDATA_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data Position */
#define FLEXCOM_FLEX_TWI_RHR_RXDATA_Msk       (_U_(0xFF) << FLEXCOM_FLEX_TWI_RHR_RXDATA_Pos) /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data Mask */
#define FLEXCOM_FLEX_TWI_RHR_RXDATA(value)    (FLEXCOM_FLEX_TWI_RHR_RXDATA_Msk & ((value) << FLEXCOM_FLEX_TWI_RHR_RXDATA_Pos))
#define FLEXCOM_FLEX_TWI_RHR_Msk              _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_TWI_RHR) Register Mask  */

/* FIFO_ENABLED mode */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA0_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 0 Position */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA0_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA0_Pos) /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 0 Mask */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA0(value) (FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA0_Msk & ((value) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA0_Pos))
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA1_Pos _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 1 Position */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA1_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA1_Pos) /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 1 Mask */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA1(value) (FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA1_Msk & ((value) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA1_Pos))
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA2_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 2 Position */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA2_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA2_Pos) /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 2 Mask */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA2(value) (FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA2_Msk & ((value) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA2_Pos))
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA3_Pos _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 3 Position */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA3_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA3_Pos) /**< (FLEXCOM_FLEX_TWI_RHR) Master or Slave Receive Holding Data 3 Mask */
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA3(value) (FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA3_Msk & ((value) << FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_RXDATA3_Pos))
#define FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED_Msk _U_(0xFFFFFFFF)                                 /**< (FLEXCOM_FLEX_TWI_RHR_FIFO_ENABLED) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_THR : (FLEXCOM Offset: 0x634) ( /W 32) TWI Transmit Holding Register -------- */
#define FLEXCOM_FLEX_TWI_THR_TXDATA_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data Position */
#define FLEXCOM_FLEX_TWI_THR_TXDATA_Msk       (_U_(0xFF) << FLEXCOM_FLEX_TWI_THR_TXDATA_Pos) /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data Mask */
#define FLEXCOM_FLEX_TWI_THR_TXDATA(value)    (FLEXCOM_FLEX_TWI_THR_TXDATA_Msk & ((value) << FLEXCOM_FLEX_TWI_THR_TXDATA_Pos))
#define FLEXCOM_FLEX_TWI_THR_Msk              _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_TWI_THR) Register Mask  */

/* FIFO_ENABLED mode */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA0_Pos _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 0 Position */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA0_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA0_Pos) /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 0 Mask */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA0(value) (FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA0_Msk & ((value) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA0_Pos))
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA1_Pos _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 1 Position */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA1_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA1_Pos) /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 1 Mask */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA1(value) (FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA1_Msk & ((value) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA1_Pos))
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA2_Pos _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 2 Position */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA2_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA2_Pos) /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 2 Mask */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA2(value) (FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA2_Msk & ((value) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA2_Pos))
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA3_Pos _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 3 Position */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA3_Msk (_U_(0xFF) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA3_Pos) /**< (FLEXCOM_FLEX_TWI_THR) Master or Slave Transmit Holding Data 3 Mask */
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA3(value) (FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA3_Msk & ((value) << FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_TXDATA3_Pos))
#define FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED_Msk _U_(0xFFFFFFFF)                                 /**< (FLEXCOM_FLEX_TWI_THR_FIFO_ENABLED) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_SMBTR : (FLEXCOM Offset: 0x638) (R/W 32) TWI SMBus Timing Register -------- */
#define FLEXCOM_FLEX_TWI_SMBTR_PRESC_Pos      _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_SMBTR) SMBus Clock Prescaler Position */
#define FLEXCOM_FLEX_TWI_SMBTR_PRESC_Msk      (_U_(0xF) << FLEXCOM_FLEX_TWI_SMBTR_PRESC_Pos) /**< (FLEXCOM_FLEX_TWI_SMBTR) SMBus Clock Prescaler Mask */
#define FLEXCOM_FLEX_TWI_SMBTR_PRESC(value)   (FLEXCOM_FLEX_TWI_SMBTR_PRESC_Msk & ((value) << FLEXCOM_FLEX_TWI_SMBTR_PRESC_Pos))
#define FLEXCOM_FLEX_TWI_SMBTR_TLOWS_Pos      _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_SMBTR) Slave Clock Stretch Maximum Cycles Position */
#define FLEXCOM_FLEX_TWI_SMBTR_TLOWS_Msk      (_U_(0xFF) << FLEXCOM_FLEX_TWI_SMBTR_TLOWS_Pos) /**< (FLEXCOM_FLEX_TWI_SMBTR) Slave Clock Stretch Maximum Cycles Mask */
#define FLEXCOM_FLEX_TWI_SMBTR_TLOWS(value)   (FLEXCOM_FLEX_TWI_SMBTR_TLOWS_Msk & ((value) << FLEXCOM_FLEX_TWI_SMBTR_TLOWS_Pos))
#define FLEXCOM_FLEX_TWI_SMBTR_TLOWM_Pos      _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_SMBTR) Master Clock Stretch Maximum Cycles Position */
#define FLEXCOM_FLEX_TWI_SMBTR_TLOWM_Msk      (_U_(0xFF) << FLEXCOM_FLEX_TWI_SMBTR_TLOWM_Pos) /**< (FLEXCOM_FLEX_TWI_SMBTR) Master Clock Stretch Maximum Cycles Mask */
#define FLEXCOM_FLEX_TWI_SMBTR_TLOWM(value)   (FLEXCOM_FLEX_TWI_SMBTR_TLOWM_Msk & ((value) << FLEXCOM_FLEX_TWI_SMBTR_TLOWM_Pos))
#define FLEXCOM_FLEX_TWI_SMBTR_THMAX_Pos      _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_SMBTR) Clock High Maximum Cycles Position */
#define FLEXCOM_FLEX_TWI_SMBTR_THMAX_Msk      (_U_(0xFF) << FLEXCOM_FLEX_TWI_SMBTR_THMAX_Pos) /**< (FLEXCOM_FLEX_TWI_SMBTR) Clock High Maximum Cycles Mask */
#define FLEXCOM_FLEX_TWI_SMBTR_THMAX(value)   (FLEXCOM_FLEX_TWI_SMBTR_THMAX_Msk & ((value) << FLEXCOM_FLEX_TWI_SMBTR_THMAX_Pos))
#define FLEXCOM_FLEX_TWI_SMBTR_Msk            _U_(0xFFFFFF0F)                                /**< (FLEXCOM_FLEX_TWI_SMBTR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_ACR : (FLEXCOM Offset: 0x640) (R/W 32) TWI Alternative Command Register -------- */
#define FLEXCOM_FLEX_TWI_ACR_DATAL_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_ACR) Data Length Position */
#define FLEXCOM_FLEX_TWI_ACR_DATAL_Msk        (_U_(0xFF) << FLEXCOM_FLEX_TWI_ACR_DATAL_Pos)  /**< (FLEXCOM_FLEX_TWI_ACR) Data Length Mask */
#define FLEXCOM_FLEX_TWI_ACR_DATAL(value)     (FLEXCOM_FLEX_TWI_ACR_DATAL_Msk & ((value) << FLEXCOM_FLEX_TWI_ACR_DATAL_Pos))
#define FLEXCOM_FLEX_TWI_ACR_DIR_Pos          _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_ACR) Transfer Direction Position */
#define FLEXCOM_FLEX_TWI_ACR_DIR_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_ACR_DIR_Pos)     /**< (FLEXCOM_FLEX_TWI_ACR) Transfer Direction Mask */
#define FLEXCOM_FLEX_TWI_ACR_PEC_Pos          _U_(9)                                         /**< (FLEXCOM_FLEX_TWI_ACR) PEC Request (SMBus Mode only) Position */
#define FLEXCOM_FLEX_TWI_ACR_PEC_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_ACR_PEC_Pos)     /**< (FLEXCOM_FLEX_TWI_ACR) PEC Request (SMBus Mode only) Mask */
#define FLEXCOM_FLEX_TWI_ACR_NDATAL_Pos       _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_ACR) Next Data Length Position */
#define FLEXCOM_FLEX_TWI_ACR_NDATAL_Msk       (_U_(0xFF) << FLEXCOM_FLEX_TWI_ACR_NDATAL_Pos) /**< (FLEXCOM_FLEX_TWI_ACR) Next Data Length Mask */
#define FLEXCOM_FLEX_TWI_ACR_NDATAL(value)    (FLEXCOM_FLEX_TWI_ACR_NDATAL_Msk & ((value) << FLEXCOM_FLEX_TWI_ACR_NDATAL_Pos))
#define FLEXCOM_FLEX_TWI_ACR_NDIR_Pos         _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_ACR) Next Transfer Direction Position */
#define FLEXCOM_FLEX_TWI_ACR_NDIR_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_ACR_NDIR_Pos)    /**< (FLEXCOM_FLEX_TWI_ACR) Next Transfer Direction Mask */
#define FLEXCOM_FLEX_TWI_ACR_NPEC_Pos         _U_(25)                                        /**< (FLEXCOM_FLEX_TWI_ACR) Next PEC Request (SMBus Mode only) Position */
#define FLEXCOM_FLEX_TWI_ACR_NPEC_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_ACR_NPEC_Pos)    /**< (FLEXCOM_FLEX_TWI_ACR) Next PEC Request (SMBus Mode only) Mask */
#define FLEXCOM_FLEX_TWI_ACR_Msk              _U_(0x03FF03FF)                                /**< (FLEXCOM_FLEX_TWI_ACR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_FILTR : (FLEXCOM Offset: 0x644) (R/W 32) TWI Filter Register -------- */
#define FLEXCOM_FLEX_TWI_FILTR_FILT_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_FILTR) RX Digital Filter Position */
#define FLEXCOM_FLEX_TWI_FILTR_FILT_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FILTR_FILT_Pos)  /**< (FLEXCOM_FLEX_TWI_FILTR) RX Digital Filter Mask */
#define FLEXCOM_FLEX_TWI_FILTR_PADFEN_Pos     _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_FILTR) PAD Filter Enable Position */
#define FLEXCOM_FLEX_TWI_FILTR_PADFEN_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_FILTR_PADFEN_Pos) /**< (FLEXCOM_FLEX_TWI_FILTR) PAD Filter Enable Mask */
#define FLEXCOM_FLEX_TWI_FILTR_PADFCFG_Pos    _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_FILTR) PAD Filter Config Position */
#define FLEXCOM_FLEX_TWI_FILTR_PADFCFG_Msk    (_U_(0x1) << FLEXCOM_FLEX_TWI_FILTR_PADFCFG_Pos) /**< (FLEXCOM_FLEX_TWI_FILTR) PAD Filter Config Mask */
#define FLEXCOM_FLEX_TWI_FILTR_THRES_Pos      _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_FILTR) Digital Filter Threshold Position */
#define FLEXCOM_FLEX_TWI_FILTR_THRES_Msk      (_U_(0x7) << FLEXCOM_FLEX_TWI_FILTR_THRES_Pos) /**< (FLEXCOM_FLEX_TWI_FILTR) Digital Filter Threshold Mask */
#define FLEXCOM_FLEX_TWI_FILTR_THRES(value)   (FLEXCOM_FLEX_TWI_FILTR_THRES_Msk & ((value) << FLEXCOM_FLEX_TWI_FILTR_THRES_Pos))
#define FLEXCOM_FLEX_TWI_FILTR_Msk            _U_(0x00000707)                                /**< (FLEXCOM_FLEX_TWI_FILTR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_FMR : (FLEXCOM Offset: 0x650) (R/W 32) TWI FIFO Mode Register -------- */
#define FLEXCOM_FLEX_TWI_FMR_TXRDYM_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_FMR) Transmitter Ready Mode Position */
#define FLEXCOM_FLEX_TWI_FMR_TXRDYM_Msk       (_U_(0x3) << FLEXCOM_FLEX_TWI_FMR_TXRDYM_Pos)  /**< (FLEXCOM_FLEX_TWI_FMR) Transmitter Ready Mode Mask */
#define FLEXCOM_FLEX_TWI_FMR_TXRDYM(value)    (FLEXCOM_FLEX_TWI_FMR_TXRDYM_Msk & ((value) << FLEXCOM_FLEX_TWI_FMR_TXRDYM_Pos))
#define   FLEXCOM_FLEX_TWI_FMR_TXRDYM_ONE_DATA_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_TWI_FMR) TXRDY will be at level '1' when at least one data can be written in the Transmit FIFO  */
#define   FLEXCOM_FLEX_TWI_FMR_TXRDYM_TWO_DATA_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_TWI_FMR) TXRDY will be at level '1' when at least two data can be written in the Transmit FIFO  */
#define   FLEXCOM_FLEX_TWI_FMR_TXRDYM_FOUR_DATA_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_TWI_FMR) TXRDY will be at level '1' when at least four data can be written in the Transmit FIFO  */
#define FLEXCOM_FLEX_TWI_FMR_TXRDYM_ONE_DATA  (FLEXCOM_FLEX_TWI_FMR_TXRDYM_ONE_DATA_Val << FLEXCOM_FLEX_TWI_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) TXRDY will be at level '1' when at least one data can be written in the Transmit FIFO Position  */
#define FLEXCOM_FLEX_TWI_FMR_TXRDYM_TWO_DATA  (FLEXCOM_FLEX_TWI_FMR_TXRDYM_TWO_DATA_Val << FLEXCOM_FLEX_TWI_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) TXRDY will be at level '1' when at least two data can be written in the Transmit FIFO Position  */
#define FLEXCOM_FLEX_TWI_FMR_TXRDYM_FOUR_DATA (FLEXCOM_FLEX_TWI_FMR_TXRDYM_FOUR_DATA_Val << FLEXCOM_FLEX_TWI_FMR_TXRDYM_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) TXRDY will be at level '1' when at least four data can be written in the Transmit FIFO Position  */
#define FLEXCOM_FLEX_TWI_FMR_RXRDYM_Pos       _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_FMR) Receiver Ready Mode Position */
#define FLEXCOM_FLEX_TWI_FMR_RXRDYM_Msk       (_U_(0x3) << FLEXCOM_FLEX_TWI_FMR_RXRDYM_Pos)  /**< (FLEXCOM_FLEX_TWI_FMR) Receiver Ready Mode Mask */
#define FLEXCOM_FLEX_TWI_FMR_RXRDYM(value)    (FLEXCOM_FLEX_TWI_FMR_RXRDYM_Msk & ((value) << FLEXCOM_FLEX_TWI_FMR_RXRDYM_Pos))
#define   FLEXCOM_FLEX_TWI_FMR_RXRDYM_ONE_DATA_Val _U_(0x0)                                       /**< (FLEXCOM_FLEX_TWI_FMR) RXRDY will be at level '1' when at least one unread data is in the Receive FIFO  */
#define   FLEXCOM_FLEX_TWI_FMR_RXRDYM_TWO_DATA_Val _U_(0x1)                                       /**< (FLEXCOM_FLEX_TWI_FMR) RXRDY will be at level '1' when at least two unread data are in the Receive FIFO  */
#define   FLEXCOM_FLEX_TWI_FMR_RXRDYM_FOUR_DATA_Val _U_(0x2)                                       /**< (FLEXCOM_FLEX_TWI_FMR) RXRDY will be at level '1' when at least four unread data are in the Receive FIFO  */
#define FLEXCOM_FLEX_TWI_FMR_RXRDYM_ONE_DATA  (FLEXCOM_FLEX_TWI_FMR_RXRDYM_ONE_DATA_Val << FLEXCOM_FLEX_TWI_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) RXRDY will be at level '1' when at least one unread data is in the Receive FIFO Position  */
#define FLEXCOM_FLEX_TWI_FMR_RXRDYM_TWO_DATA  (FLEXCOM_FLEX_TWI_FMR_RXRDYM_TWO_DATA_Val << FLEXCOM_FLEX_TWI_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) RXRDY will be at level '1' when at least two unread data are in the Receive FIFO Position  */
#define FLEXCOM_FLEX_TWI_FMR_RXRDYM_FOUR_DATA (FLEXCOM_FLEX_TWI_FMR_RXRDYM_FOUR_DATA_Val << FLEXCOM_FLEX_TWI_FMR_RXRDYM_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) RXRDY will be at level '1' when at least four unread data are in the Receive FIFO Position  */
#define FLEXCOM_FLEX_TWI_FMR_TXFTHRES_Pos     _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_FMR) Transmit FIFO Threshold Position */
#define FLEXCOM_FLEX_TWI_FMR_TXFTHRES_Msk     (_U_(0x3F) << FLEXCOM_FLEX_TWI_FMR_TXFTHRES_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) Transmit FIFO Threshold Mask */
#define FLEXCOM_FLEX_TWI_FMR_TXFTHRES(value)  (FLEXCOM_FLEX_TWI_FMR_TXFTHRES_Msk & ((value) << FLEXCOM_FLEX_TWI_FMR_TXFTHRES_Pos))
#define FLEXCOM_FLEX_TWI_FMR_RXFTHRES_Pos     _U_(24)                                        /**< (FLEXCOM_FLEX_TWI_FMR) Receive FIFO Threshold Position */
#define FLEXCOM_FLEX_TWI_FMR_RXFTHRES_Msk     (_U_(0x3F) << FLEXCOM_FLEX_TWI_FMR_RXFTHRES_Pos) /**< (FLEXCOM_FLEX_TWI_FMR) Receive FIFO Threshold Mask */
#define FLEXCOM_FLEX_TWI_FMR_RXFTHRES(value)  (FLEXCOM_FLEX_TWI_FMR_RXFTHRES_Msk & ((value) << FLEXCOM_FLEX_TWI_FMR_RXFTHRES_Pos))
#define FLEXCOM_FLEX_TWI_FMR_Msk              _U_(0x3F3F0033)                                /**< (FLEXCOM_FLEX_TWI_FMR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_FLR : (FLEXCOM Offset: 0x654) ( R/ 32) TWI FIFO Level Register -------- */
#define FLEXCOM_FLEX_TWI_FLR_TXFL_Pos         _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_FLR) Transmit FIFO Level Position */
#define FLEXCOM_FLEX_TWI_FLR_TXFL_Msk         (_U_(0x3F) << FLEXCOM_FLEX_TWI_FLR_TXFL_Pos)   /**< (FLEXCOM_FLEX_TWI_FLR) Transmit FIFO Level Mask */
#define FLEXCOM_FLEX_TWI_FLR_TXFL(value)      (FLEXCOM_FLEX_TWI_FLR_TXFL_Msk & ((value) << FLEXCOM_FLEX_TWI_FLR_TXFL_Pos))
#define FLEXCOM_FLEX_TWI_FLR_RXFL_Pos         _U_(16)                                        /**< (FLEXCOM_FLEX_TWI_FLR) Receive FIFO Level Position */
#define FLEXCOM_FLEX_TWI_FLR_RXFL_Msk         (_U_(0x3F) << FLEXCOM_FLEX_TWI_FLR_RXFL_Pos)   /**< (FLEXCOM_FLEX_TWI_FLR) Receive FIFO Level Mask */
#define FLEXCOM_FLEX_TWI_FLR_RXFL(value)      (FLEXCOM_FLEX_TWI_FLR_RXFL_Msk & ((value) << FLEXCOM_FLEX_TWI_FLR_RXFL_Pos))
#define FLEXCOM_FLEX_TWI_FLR_Msk              _U_(0x003F003F)                                /**< (FLEXCOM_FLEX_TWI_FLR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_FSR : (FLEXCOM Offset: 0x660) ( R/ 32) TWI FIFO Status Register -------- */
#define FLEXCOM_FLEX_TWI_FSR_TXFEF_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Empty Flag (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_FSR_TXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_TXFEF_Pos)   /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Empty Flag (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_FSR_TXFFF_Pos        _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Full Flag (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_FSR_TXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_TXFFF_Pos)   /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Full Flag (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_FSR_TXFTHF_Pos       _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Threshold Flag (cleared on read) Position */
#define FLEXCOM_FLEX_TWI_FSR_TXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_TXFTHF_Pos)  /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Threshold Flag (cleared on read) Mask */
#define FLEXCOM_FLEX_TWI_FSR_RXFEF_Pos        _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Empty Flag Position */
#define FLEXCOM_FLEX_TWI_FSR_RXFEF_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_RXFEF_Pos)   /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Empty Flag Mask */
#define FLEXCOM_FLEX_TWI_FSR_RXFFF_Pos        _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Full Flag Position */
#define FLEXCOM_FLEX_TWI_FSR_RXFFF_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_RXFFF_Pos)   /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Full Flag Mask */
#define FLEXCOM_FLEX_TWI_FSR_RXFTHF_Pos       _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Threshold Flag Position */
#define FLEXCOM_FLEX_TWI_FSR_RXFTHF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_RXFTHF_Pos)  /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Threshold Flag Mask */
#define FLEXCOM_FLEX_TWI_FSR_TXFPTEF_Pos      _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Pointer Error Flag Position */
#define FLEXCOM_FLEX_TWI_FSR_TXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FSR) Transmit FIFO Pointer Error Flag Mask */
#define FLEXCOM_FLEX_TWI_FSR_RXFPTEF_Pos      _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Pointer Error Flag Position */
#define FLEXCOM_FLEX_TWI_FSR_RXFPTEF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FSR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FSR) Receive FIFO Pointer Error Flag Mask */
#define FLEXCOM_FLEX_TWI_FSR_Msk              _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_TWI_FSR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_FIER : (FLEXCOM Offset: 0x664) ( /W 32) TWI FIFO Interrupt Enable Register -------- */
#define FLEXCOM_FLEX_TWI_FIER_TXFEF_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_FIER) TXFEF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_TXFEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_TXFEF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIER) TXFEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_TXFFF_Pos       _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_FIER) TXFFF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_TXFFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_TXFFF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIER) TXFFF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_TXFTHF_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_FIER) TXFTHF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_TXFTHF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_TXFTHF_Pos) /**< (FLEXCOM_FLEX_TWI_FIER) TXFTHF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_RXFEF_Pos       _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_FIER) RXFEF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_RXFEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_RXFEF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIER) RXFEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_RXFFF_Pos       _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_FIER) RXFFF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_RXFFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_RXFFF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIER) RXFFF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_RXFTHF_Pos      _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_FIER) RXFTHF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_RXFTHF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_RXFTHF_Pos) /**< (FLEXCOM_FLEX_TWI_FIER) RXFTHF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_TXFPTEF_Pos     _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_FIER) TXFPTEF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_TXFPTEF_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FIER) TXFPTEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_RXFPTEF_Pos     _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_FIER) RXFPTEF Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_FIER_RXFPTEF_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_FIER_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FIER) RXFPTEF Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_FIER_Msk             _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_TWI_FIER) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_FIDR : (FLEXCOM Offset: 0x668) ( /W 32) TWI FIFO Interrupt Disable Register -------- */
#define FLEXCOM_FLEX_TWI_FIDR_TXFEF_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) TXFEF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_TXFEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_TXFEF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIDR) TXFEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_TXFFF_Pos       _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) TXFFF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_TXFFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_TXFFF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIDR) TXFFF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_TXFTHF_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) TXFTHF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_TXFTHF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_TXFTHF_Pos) /**< (FLEXCOM_FLEX_TWI_FIDR) TXFTHF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_RXFEF_Pos       _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) RXFEF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_RXFEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_RXFEF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIDR) RXFEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_RXFFF_Pos       _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) RXFFF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_RXFFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_RXFFF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIDR) RXFFF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_RXFTHF_Pos      _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) RXFTHF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_RXFTHF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_RXFTHF_Pos) /**< (FLEXCOM_FLEX_TWI_FIDR) RXFTHF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_TXFPTEF_Pos     _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) TXFPTEF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_TXFPTEF_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FIDR) TXFPTEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_RXFPTEF_Pos     _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_FIDR) RXFPTEF Interrupt Disable Position */
#define FLEXCOM_FLEX_TWI_FIDR_RXFPTEF_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_FIDR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FIDR) RXFPTEF Interrupt Disable Mask */
#define FLEXCOM_FLEX_TWI_FIDR_Msk             _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_TWI_FIDR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_FIMR : (FLEXCOM Offset: 0x66C) ( R/ 32) TWI FIFO Interrupt Mask Register -------- */
#define FLEXCOM_FLEX_TWI_FIMR_TXFEF_Pos       _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) TXFEF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_TXFEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_TXFEF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIMR) TXFEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_TXFFF_Pos       _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) TXFFF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_TXFFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_TXFFF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIMR) TXFFF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_TXFTHF_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) TXFTHF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_TXFTHF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_TXFTHF_Pos) /**< (FLEXCOM_FLEX_TWI_FIMR) TXFTHF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_RXFEF_Pos       _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) RXFEF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_RXFEF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_RXFEF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIMR) RXFEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_RXFFF_Pos       _U_(4)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) RXFFF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_RXFFF_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_RXFFF_Pos)  /**< (FLEXCOM_FLEX_TWI_FIMR) RXFFF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_RXFTHF_Pos      _U_(5)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) RXFTHF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_RXFTHF_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_RXFTHF_Pos) /**< (FLEXCOM_FLEX_TWI_FIMR) RXFTHF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_TXFPTEF_Pos     _U_(6)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) TXFPTEF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_TXFPTEF_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_TXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FIMR) TXFPTEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_RXFPTEF_Pos     _U_(7)                                         /**< (FLEXCOM_FLEX_TWI_FIMR) RXFPTEF Interrupt Mask Position */
#define FLEXCOM_FLEX_TWI_FIMR_RXFPTEF_Msk     (_U_(0x1) << FLEXCOM_FLEX_TWI_FIMR_RXFPTEF_Pos) /**< (FLEXCOM_FLEX_TWI_FIMR) RXFPTEF Interrupt Mask Mask */
#define FLEXCOM_FLEX_TWI_FIMR_Msk             _U_(0x000000FF)                                /**< (FLEXCOM_FLEX_TWI_FIMR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_DR : (FLEXCOM Offset: 0x6D0) ( R/ 32) TWI Debug Register -------- */
#define FLEXCOM_FLEX_TWI_DR_SWEN_Pos          _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_DR) SleepWalking Enable Position */
#define FLEXCOM_FLEX_TWI_DR_SWEN_Msk          (_U_(0x1) << FLEXCOM_FLEX_TWI_DR_SWEN_Pos)     /**< (FLEXCOM_FLEX_TWI_DR) SleepWalking Enable Mask */
#define FLEXCOM_FLEX_TWI_DR_CLKRQ_Pos         _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_DR) Clock Request Position */
#define FLEXCOM_FLEX_TWI_DR_CLKRQ_Msk         (_U_(0x1) << FLEXCOM_FLEX_TWI_DR_CLKRQ_Pos)    /**< (FLEXCOM_FLEX_TWI_DR) Clock Request Mask */
#define FLEXCOM_FLEX_TWI_DR_SWMATCH_Pos       _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_DR) SleepWalking Match Position */
#define FLEXCOM_FLEX_TWI_DR_SWMATCH_Msk       (_U_(0x1) << FLEXCOM_FLEX_TWI_DR_SWMATCH_Pos)  /**< (FLEXCOM_FLEX_TWI_DR) SleepWalking Match Mask */
#define FLEXCOM_FLEX_TWI_DR_TRP_Pos           _U_(3)                                         /**< (FLEXCOM_FLEX_TWI_DR) Transfer Pending Position */
#define FLEXCOM_FLEX_TWI_DR_TRP_Msk           (_U_(0x1) << FLEXCOM_FLEX_TWI_DR_TRP_Pos)      /**< (FLEXCOM_FLEX_TWI_DR) Transfer Pending Mask */
#define FLEXCOM_FLEX_TWI_DR_Msk               _U_(0x0000000F)                                /**< (FLEXCOM_FLEX_TWI_DR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_WPMR : (FLEXCOM Offset: 0x6E4) (R/W 32) TWI Write Protection Mode Register -------- */
#define FLEXCOM_FLEX_TWI_WPMR_WPEN_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Enable Position */
#define FLEXCOM_FLEX_TWI_WPMR_WPEN_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_WPMR_WPEN_Pos)   /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Enable Mask */
#define FLEXCOM_FLEX_TWI_WPMR_WPITEN_Pos      _U_(1)                                         /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Interrupt Enable Position */
#define FLEXCOM_FLEX_TWI_WPMR_WPITEN_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_WPMR_WPITEN_Pos) /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Interrupt Enable Mask */
#define FLEXCOM_FLEX_TWI_WPMR_WPCREN_Pos      _U_(2)                                         /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Control Enable Position */
#define FLEXCOM_FLEX_TWI_WPMR_WPCREN_Msk      (_U_(0x1) << FLEXCOM_FLEX_TWI_WPMR_WPCREN_Pos) /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Control Enable Mask */
#define FLEXCOM_FLEX_TWI_WPMR_WPKEY_Pos       _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Key Position */
#define FLEXCOM_FLEX_TWI_WPMR_WPKEY_Msk       (_U_(0xFFFFFF) << FLEXCOM_FLEX_TWI_WPMR_WPKEY_Pos) /**< (FLEXCOM_FLEX_TWI_WPMR) Write Protection Key Mask */
#define FLEXCOM_FLEX_TWI_WPMR_WPKEY(value)    (FLEXCOM_FLEX_TWI_WPMR_WPKEY_Msk & ((value) << FLEXCOM_FLEX_TWI_WPMR_WPKEY_Pos))
#define   FLEXCOM_FLEX_TWI_WPMR_WPKEY_PASSWD_Val _U_(0x545749)                                  /**< (FLEXCOM_FLEX_TWI_WPMR) Writing any other value in this field aborts the write operation of bits WPEN, WPITEN and WPCREN.Always reads as 0  */
#define FLEXCOM_FLEX_TWI_WPMR_WPKEY_PASSWD    (FLEXCOM_FLEX_TWI_WPMR_WPKEY_PASSWD_Val << FLEXCOM_FLEX_TWI_WPMR_WPKEY_Pos) /**< (FLEXCOM_FLEX_TWI_WPMR) Writing any other value in this field aborts the write operation of bits WPEN, WPITEN and WPCREN.Always reads as 0 Position  */
#define FLEXCOM_FLEX_TWI_WPMR_Msk             _U_(0xFFFFFF07)                                /**< (FLEXCOM_FLEX_TWI_WPMR) Register Mask  */


/* -------- FLEXCOM_FLEX_TWI_WPSR : (FLEXCOM Offset: 0x6E8) ( R/ 32) TWI Write Protection Status Register -------- */
#define FLEXCOM_FLEX_TWI_WPSR_WPVS_Pos        _U_(0)                                         /**< (FLEXCOM_FLEX_TWI_WPSR) Write Protect Violation Status Position */
#define FLEXCOM_FLEX_TWI_WPSR_WPVS_Msk        (_U_(0x1) << FLEXCOM_FLEX_TWI_WPSR_WPVS_Pos)   /**< (FLEXCOM_FLEX_TWI_WPSR) Write Protect Violation Status Mask */
#define FLEXCOM_FLEX_TWI_WPSR_WPVSRC_Pos      _U_(8)                                         /**< (FLEXCOM_FLEX_TWI_WPSR) Write Protection Violation Source Position */
#define FLEXCOM_FLEX_TWI_WPSR_WPVSRC_Msk      (_U_(0xFFFFFF) << FLEXCOM_FLEX_TWI_WPSR_WPVSRC_Pos) /**< (FLEXCOM_FLEX_TWI_WPSR) Write Protection Violation Source Mask */
#define FLEXCOM_FLEX_TWI_WPSR_WPVSRC(value)   (FLEXCOM_FLEX_TWI_WPSR_WPVSRC_Msk & ((value) << FLEXCOM_FLEX_TWI_WPSR_WPVSRC_Pos))
#define FLEXCOM_FLEX_TWI_WPSR_Msk             _U_(0xFFFFFF01)                                /**< (FLEXCOM_FLEX_TWI_WPSR) Register Mask  */


/** \brief FLEXCOM register offsets definitions */
#define FLEXCOM_FLEX_MR_REG_OFST       (0x00)         /**< (FLEXCOM_FLEX_MR) FLEXCOM Mode Register Offset */
#define FLEXCOM_FLEX_RHR_REG_OFST      (0x10)         /**< (FLEXCOM_FLEX_RHR) FLEXCOM Receive Holding Register Offset */
#define FLEXCOM_FLEX_THR_REG_OFST      (0x20)         /**< (FLEXCOM_FLEX_THR) FLEXCOM Transmit Holding Register Offset */
#define FLEXCOM_FLEX_US_CR_REG_OFST    (0x200)        /**< (FLEXCOM_FLEX_US_CR) USART Control Register Offset */
#define FLEXCOM_FLEX_US_MR_REG_OFST    (0x204)        /**< (FLEXCOM_FLEX_US_MR) USART Mode Register Offset */
#define FLEXCOM_FLEX_US_IER_REG_OFST   (0x208)        /**< (FLEXCOM_FLEX_US_IER) USART Interrupt Enable Register Offset */
#define FLEXCOM_FLEX_US_IDR_REG_OFST   (0x20C)        /**< (FLEXCOM_FLEX_US_IDR) USART Interrupt Disable Register Offset */
#define FLEXCOM_FLEX_US_IMR_REG_OFST   (0x210)        /**< (FLEXCOM_FLEX_US_IMR) USART Interrupt Mask Register Offset */
#define FLEXCOM_FLEX_US_CSR_REG_OFST   (0x214)        /**< (FLEXCOM_FLEX_US_CSR) USART Channel Status Register Offset */
#define FLEXCOM_FLEX_US_RHR_REG_OFST   (0x218)        /**< (FLEXCOM_FLEX_US_RHR) USART Receive Holding Register Offset */
#define FLEXCOM_FLEX_US_THR_REG_OFST   (0x21C)        /**< (FLEXCOM_FLEX_US_THR) USART Transmit Holding Register Offset */
#define FLEXCOM_FLEX_US_BRGR_REG_OFST  (0x220)        /**< (FLEXCOM_FLEX_US_BRGR) USART Baud Rate Generator Register Offset */
#define FLEXCOM_FLEX_US_RTOR_REG_OFST  (0x224)        /**< (FLEXCOM_FLEX_US_RTOR) USART Receiver Timeout Register Offset */
#define FLEXCOM_FLEX_US_TTGR_REG_OFST  (0x228)        /**< (FLEXCOM_FLEX_US_TTGR) USART Transmitter Timeguard Register Offset */
#define FLEXCOM_FLEX_US_FIDI_REG_OFST  (0x240)        /**< (FLEXCOM_FLEX_US_FIDI) USART FI DI Ratio Register Offset */
#define FLEXCOM_FLEX_US_NER_REG_OFST   (0x244)        /**< (FLEXCOM_FLEX_US_NER) USART Number of Errors Register Offset */
#define FLEXCOM_FLEX_US_IF_REG_OFST    (0x24C)        /**< (FLEXCOM_FLEX_US_IF) USART IrDA Filter Register Offset */
#define FLEXCOM_FLEX_US_MAN_REG_OFST   (0x250)        /**< (FLEXCOM_FLEX_US_MAN) USART Manchester Configuration Register Offset */
#define FLEXCOM_FLEX_US_LINMR_REG_OFST (0x254)        /**< (FLEXCOM_FLEX_US_LINMR) USART LIN Mode Register Offset */
#define FLEXCOM_FLEX_US_LINIR_REG_OFST (0x258)        /**< (FLEXCOM_FLEX_US_LINIR) USART LIN Identifier Register Offset */
#define FLEXCOM_FLEX_US_LINBRR_REG_OFST (0x25C)        /**< (FLEXCOM_FLEX_US_LINBRR) USART LIN Baud Rate Register Offset */
#define FLEXCOM_FLEX_US_LONMR_REG_OFST (0x260)        /**< (FLEXCOM_FLEX_US_LONMR) USART LON Mode Register Offset */
#define FLEXCOM_FLEX_US_LONPR_REG_OFST (0x264)        /**< (FLEXCOM_FLEX_US_LONPR) USART LON Preamble Register Offset */
#define FLEXCOM_FLEX_US_LONDL_REG_OFST (0x268)        /**< (FLEXCOM_FLEX_US_LONDL) USART LON Data Length Register Offset */
#define FLEXCOM_FLEX_US_LONL2HDR_REG_OFST (0x26C)        /**< (FLEXCOM_FLEX_US_LONL2HDR) USART LON L2HDR Register Offset */
#define FLEXCOM_FLEX_US_LONBL_REG_OFST (0x270)        /**< (FLEXCOM_FLEX_US_LONBL) USART LON Backlog Register Offset */
#define FLEXCOM_FLEX_US_LONB1TX_REG_OFST (0x274)        /**< (FLEXCOM_FLEX_US_LONB1TX) USART LON Beta1 Tx Register Offset */
#define FLEXCOM_FLEX_US_LONB1RX_REG_OFST (0x278)        /**< (FLEXCOM_FLEX_US_LONB1RX) USART LON Beta1 Rx Register Offset */
#define FLEXCOM_FLEX_US_LONPRIO_REG_OFST (0x27C)        /**< (FLEXCOM_FLEX_US_LONPRIO) USART LON Priority Register Offset */
#define FLEXCOM_FLEX_US_IDTTX_REG_OFST (0x280)        /**< (FLEXCOM_FLEX_US_IDTTX) USART LON IDT Tx Register Offset */
#define FLEXCOM_FLEX_US_IDTRX_REG_OFST (0x284)        /**< (FLEXCOM_FLEX_US_IDTRX) USART LON IDT Rx Register Offset */
#define FLEXCOM_FLEX_US_ICDIFF_REG_OFST (0x288)        /**< (FLEXCOM_FLEX_US_ICDIFF) USART IC DIFF Register Offset */
#define FLEXCOM_FLEX_US_CMPR_REG_OFST  (0x290)        /**< (FLEXCOM_FLEX_US_CMPR) USART Comparison Register Offset */
#define FLEXCOM_FLEX_US_FMR_REG_OFST   (0x2A0)        /**< (FLEXCOM_FLEX_US_FMR) USART FIFO Mode Register Offset */
#define FLEXCOM_FLEX_US_FLR_REG_OFST   (0x2A4)        /**< (FLEXCOM_FLEX_US_FLR) USART FIFO Level Register Offset */
#define FLEXCOM_FLEX_US_FIER_REG_OFST  (0x2A8)        /**< (FLEXCOM_FLEX_US_FIER) USART FIFO Interrupt Enable Register Offset */
#define FLEXCOM_FLEX_US_FIDR_REG_OFST  (0x2AC)        /**< (FLEXCOM_FLEX_US_FIDR) USART FIFO Interrupt Disable Register Offset */
#define FLEXCOM_FLEX_US_FIMR_REG_OFST  (0x2B0)        /**< (FLEXCOM_FLEX_US_FIMR) USART FIFO Interrupt Mask Register Offset */
#define FLEXCOM_FLEX_US_FESR_REG_OFST  (0x2B4)        /**< (FLEXCOM_FLEX_US_FESR) USART FIFO Event Status Register Offset */
#define FLEXCOM_FLEX_US_WPMR_REG_OFST  (0x2E4)        /**< (FLEXCOM_FLEX_US_WPMR) USART Write Protection Mode Register Offset */
#define FLEXCOM_FLEX_US_WPSR_REG_OFST  (0x2E8)        /**< (FLEXCOM_FLEX_US_WPSR) USART Write Protection Status Register Offset */
#define FLEXCOM_FLEX_SPI_CR_REG_OFST   (0x400)        /**< (FLEXCOM_FLEX_SPI_CR) SPI Control Register Offset */
#define FLEXCOM_FLEX_SPI_MR_REG_OFST   (0x404)        /**< (FLEXCOM_FLEX_SPI_MR) SPI Mode Register Offset */
#define FLEXCOM_FLEX_SPI_RDR_REG_OFST  (0x408)        /**< (FLEXCOM_FLEX_SPI_RDR) SPI Receive Data Register Offset */
#define FLEXCOM_FLEX_SPI_TDR_REG_OFST  (0x40C)        /**< (FLEXCOM_FLEX_SPI_TDR) SPI Transmit Data Register Offset */
#define FLEXCOM_FLEX_SPI_SR_REG_OFST   (0x410)        /**< (FLEXCOM_FLEX_SPI_SR) SPI Status Register Offset */
#define FLEXCOM_FLEX_SPI_IER_REG_OFST  (0x414)        /**< (FLEXCOM_FLEX_SPI_IER) SPI Interrupt Enable Register Offset */
#define FLEXCOM_FLEX_SPI_IDR_REG_OFST  (0x418)        /**< (FLEXCOM_FLEX_SPI_IDR) SPI Interrupt Disable Register Offset */
#define FLEXCOM_FLEX_SPI_IMR_REG_OFST  (0x41C)        /**< (FLEXCOM_FLEX_SPI_IMR) SPI Interrupt Mask Register Offset */
#define FLEXCOM_FLEX_SPI_CSR0_REG_OFST (0x430)        /**< (FLEXCOM_FLEX_SPI_CSR0) SPI Chip Select Register 0 Offset */
#define FLEXCOM_FLEX_SPI_CSR1_REG_OFST (0x434)        /**< (FLEXCOM_FLEX_SPI_CSR1) SPI Chip Select Register 1 Offset */
#define FLEXCOM_FLEX_SPI_CSR2_REG_OFST (0x438)        /**< (FLEXCOM_FLEX_SPI_CSR2) SPI Chip Select Register 2 Offset */
#define FLEXCOM_FLEX_SPI_CSR3_REG_OFST (0x43C)        /**< (FLEXCOM_FLEX_SPI_CSR3) SPI Chip Select Register 3 Offset */
#define FLEXCOM_FLEX_SPI_FMR_REG_OFST  (0x440)        /**< (FLEXCOM_FLEX_SPI_FMR) SPI FIFO Mode Register Offset */
#define FLEXCOM_FLEX_SPI_FLR_REG_OFST  (0x444)        /**< (FLEXCOM_FLEX_SPI_FLR) SPI FIFO Level Register Offset */
#define FLEXCOM_FLEX_SPI_CMPR_REG_OFST (0x448)        /**< (FLEXCOM_FLEX_SPI_CMPR) SPI Comparison Register Offset */
#define FLEXCOM_FLEX_SPI_WPMR_REG_OFST (0x4E4)        /**< (FLEXCOM_FLEX_SPI_WPMR) SPI Write Protection Mode Register Offset */
#define FLEXCOM_FLEX_SPI_WPSR_REG_OFST (0x4E8)        /**< (FLEXCOM_FLEX_SPI_WPSR) SPI Write Protection Status Register Offset */
#define FLEXCOM_FLEX_TWI_CR_REG_OFST   (0x600)        /**< (FLEXCOM_FLEX_TWI_CR) TWI Control Register Offset */
#define FLEXCOM_FLEX_TWI_MMR_REG_OFST  (0x604)        /**< (FLEXCOM_FLEX_TWI_MMR) TWI Master Mode Register Offset */
#define FLEXCOM_FLEX_TWI_SMR_REG_OFST  (0x608)        /**< (FLEXCOM_FLEX_TWI_SMR) TWI Slave Mode Register Offset */
#define FLEXCOM_FLEX_TWI_IADR_REG_OFST (0x60C)        /**< (FLEXCOM_FLEX_TWI_IADR) TWI Internal Address Register Offset */
#define FLEXCOM_FLEX_TWI_CWGR_REG_OFST (0x610)        /**< (FLEXCOM_FLEX_TWI_CWGR) TWI Clock Waveform Generator Register Offset */
#define FLEXCOM_FLEX_TWI_SR_REG_OFST   (0x620)        /**< (FLEXCOM_FLEX_TWI_SR) TWI Status Register Offset */
#define FLEXCOM_FLEX_TWI_IER_REG_OFST  (0x624)        /**< (FLEXCOM_FLEX_TWI_IER) TWI Interrupt Enable Register Offset */
#define FLEXCOM_FLEX_TWI_IDR_REG_OFST  (0x628)        /**< (FLEXCOM_FLEX_TWI_IDR) TWI Interrupt Disable Register Offset */
#define FLEXCOM_FLEX_TWI_IMR_REG_OFST  (0x62C)        /**< (FLEXCOM_FLEX_TWI_IMR) TWI Interrupt Mask Register Offset */
#define FLEXCOM_FLEX_TWI_RHR_REG_OFST  (0x630)        /**< (FLEXCOM_FLEX_TWI_RHR) TWI Receive Holding Register Offset */
#define FLEXCOM_FLEX_TWI_THR_REG_OFST  (0x634)        /**< (FLEXCOM_FLEX_TWI_THR) TWI Transmit Holding Register Offset */
#define FLEXCOM_FLEX_TWI_SMBTR_REG_OFST (0x638)        /**< (FLEXCOM_FLEX_TWI_SMBTR) TWI SMBus Timing Register Offset */
#define FLEXCOM_FLEX_TWI_ACR_REG_OFST  (0x640)        /**< (FLEXCOM_FLEX_TWI_ACR) TWI Alternative Command Register Offset */
#define FLEXCOM_FLEX_TWI_FILTR_REG_OFST (0x644)        /**< (FLEXCOM_FLEX_TWI_FILTR) TWI Filter Register Offset */
#define FLEXCOM_FLEX_TWI_FMR_REG_OFST  (0x650)        /**< (FLEXCOM_FLEX_TWI_FMR) TWI FIFO Mode Register Offset */
#define FLEXCOM_FLEX_TWI_FLR_REG_OFST  (0x654)        /**< (FLEXCOM_FLEX_TWI_FLR) TWI FIFO Level Register Offset */
#define FLEXCOM_FLEX_TWI_FSR_REG_OFST  (0x660)        /**< (FLEXCOM_FLEX_TWI_FSR) TWI FIFO Status Register Offset */
#define FLEXCOM_FLEX_TWI_FIER_REG_OFST (0x664)        /**< (FLEXCOM_FLEX_TWI_FIER) TWI FIFO Interrupt Enable Register Offset */
#define FLEXCOM_FLEX_TWI_FIDR_REG_OFST (0x668)        /**< (FLEXCOM_FLEX_TWI_FIDR) TWI FIFO Interrupt Disable Register Offset */
#define FLEXCOM_FLEX_TWI_FIMR_REG_OFST (0x66C)        /**< (FLEXCOM_FLEX_TWI_FIMR) TWI FIFO Interrupt Mask Register Offset */
#define FLEXCOM_FLEX_TWI_DR_REG_OFST   (0x6D0)        /**< (FLEXCOM_FLEX_TWI_DR) TWI Debug Register Offset */
#define FLEXCOM_FLEX_TWI_WPMR_REG_OFST (0x6E4)        /**< (FLEXCOM_FLEX_TWI_WPMR) TWI Write Protection Mode Register Offset */
#define FLEXCOM_FLEX_TWI_WPSR_REG_OFST (0x6E8)        /**< (FLEXCOM_FLEX_TWI_WPSR) TWI Write Protection Status Register Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief FLEXCOM register API structure */
typedef struct
{
  __IO  uint32_t                       FLEXCOM_FLEX_MR; /**< Offset: 0x00 (R/W  32) FLEXCOM Mode Register */
  __I   uint8_t                        Reserved1[0x0C];
  __I   uint32_t                       FLEXCOM_FLEX_RHR; /**< Offset: 0x10 (R/   32) FLEXCOM Receive Holding Register */
  __I   uint8_t                        Reserved2[0x0C];
  __IO  uint32_t                       FLEXCOM_FLEX_THR; /**< Offset: 0x20 (R/W  32) FLEXCOM Transmit Holding Register */
  __I   uint8_t                        Reserved3[0x1DC];
  __O   uint32_t                       FLEXCOM_FLEX_US_CR; /**< Offset: 0x200 ( /W  32) USART Control Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_MR; /**< Offset: 0x204 (R/W  32) USART Mode Register */
  __O   uint32_t                       FLEXCOM_FLEX_US_IER; /**< Offset: 0x208 ( /W  32) USART Interrupt Enable Register */
  __O   uint32_t                       FLEXCOM_FLEX_US_IDR; /**< Offset: 0x20C ( /W  32) USART Interrupt Disable Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_IMR; /**< Offset: 0x210 (R/   32) USART Interrupt Mask Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_CSR; /**< Offset: 0x214 (R/   32) USART Channel Status Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_RHR; /**< Offset: 0x218 (R/   32) USART Receive Holding Register */
  __O   uint32_t                       FLEXCOM_FLEX_US_THR; /**< Offset: 0x21C ( /W  32) USART Transmit Holding Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_BRGR; /**< Offset: 0x220 (R/W  32) USART Baud Rate Generator Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_RTOR; /**< Offset: 0x224 (R/W  32) USART Receiver Timeout Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_TTGR; /**< Offset: 0x228 (R/W  32) USART Transmitter Timeguard Register */
  __I   uint8_t                        Reserved4[0x14];
  __IO  uint32_t                       FLEXCOM_FLEX_US_FIDI; /**< Offset: 0x240 (R/W  32) USART FI DI Ratio Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_NER; /**< Offset: 0x244 (R/   32) USART Number of Errors Register */
  __I   uint8_t                        Reserved5[0x04];
  __IO  uint32_t                       FLEXCOM_FLEX_US_IF; /**< Offset: 0x24C (R/W  32) USART IrDA Filter Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_MAN; /**< Offset: 0x250 (R/W  32) USART Manchester Configuration Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LINMR; /**< Offset: 0x254 (R/W  32) USART LIN Mode Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LINIR; /**< Offset: 0x258 (R/W  32) USART LIN Identifier Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_LINBRR; /**< Offset: 0x25C (R/   32) USART LIN Baud Rate Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LONMR; /**< Offset: 0x260 (R/W  32) USART LON Mode Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LONPR; /**< Offset: 0x264 (R/W  32) USART LON Preamble Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LONDL; /**< Offset: 0x268 (R/W  32) USART LON Data Length Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LONL2HDR; /**< Offset: 0x26C (R/W  32) USART LON L2HDR Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_LONBL; /**< Offset: 0x270 (R/   32) USART LON Backlog Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LONB1TX; /**< Offset: 0x274 (R/W  32) USART LON Beta1 Tx Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LONB1RX; /**< Offset: 0x278 (R/W  32) USART LON Beta1 Rx Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_LONPRIO; /**< Offset: 0x27C (R/W  32) USART LON Priority Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_IDTTX; /**< Offset: 0x280 (R/W  32) USART LON IDT Tx Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_IDTRX; /**< Offset: 0x284 (R/W  32) USART LON IDT Rx Register */
  __IO  uint32_t                       FLEXCOM_FLEX_US_ICDIFF; /**< Offset: 0x288 (R/W  32) USART IC DIFF Register */
  __I   uint8_t                        Reserved6[0x04];
  __IO  uint32_t                       FLEXCOM_FLEX_US_CMPR; /**< Offset: 0x290 (R/W  32) USART Comparison Register */
  __I   uint8_t                        Reserved7[0x0C];
  __IO  uint32_t                       FLEXCOM_FLEX_US_FMR; /**< Offset: 0x2A0 (R/W  32) USART FIFO Mode Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_FLR; /**< Offset: 0x2A4 (R/   32) USART FIFO Level Register */
  __O   uint32_t                       FLEXCOM_FLEX_US_FIER; /**< Offset: 0x2A8 ( /W  32) USART FIFO Interrupt Enable Register */
  __O   uint32_t                       FLEXCOM_FLEX_US_FIDR; /**< Offset: 0x2AC ( /W  32) USART FIFO Interrupt Disable Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_FIMR; /**< Offset: 0x2B0 (R/   32) USART FIFO Interrupt Mask Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_FESR; /**< Offset: 0x2B4 (R/   32) USART FIFO Event Status Register */
  __I   uint8_t                        Reserved8[0x2C];
  __IO  uint32_t                       FLEXCOM_FLEX_US_WPMR; /**< Offset: 0x2E4 (R/W  32) USART Write Protection Mode Register */
  __I   uint32_t                       FLEXCOM_FLEX_US_WPSR; /**< Offset: 0x2E8 (R/   32) USART Write Protection Status Register */
  __I   uint8_t                        Reserved9[0x114];
  __O   uint32_t                       FLEXCOM_FLEX_SPI_CR; /**< Offset: 0x400 ( /W  32) SPI Control Register */
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_MR; /**< Offset: 0x404 (R/W  32) SPI Mode Register */
  __I   uint32_t                       FLEXCOM_FLEX_SPI_RDR; /**< Offset: 0x408 (R/   32) SPI Receive Data Register */
  __O   uint32_t                       FLEXCOM_FLEX_SPI_TDR; /**< Offset: 0x40C ( /W  32) SPI Transmit Data Register */
  __I   uint32_t                       FLEXCOM_FLEX_SPI_SR; /**< Offset: 0x410 (R/   32) SPI Status Register */
  __O   uint32_t                       FLEXCOM_FLEX_SPI_IER; /**< Offset: 0x414 ( /W  32) SPI Interrupt Enable Register */
  __O   uint32_t                       FLEXCOM_FLEX_SPI_IDR; /**< Offset: 0x418 ( /W  32) SPI Interrupt Disable Register */
  __I   uint32_t                       FLEXCOM_FLEX_SPI_IMR; /**< Offset: 0x41C (R/   32) SPI Interrupt Mask Register */
  __I   uint8_t                        Reserved10[0x10];
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_CSR0; /**< Offset: 0x430 (R/W  32) SPI Chip Select Register 0 */
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_CSR1; /**< Offset: 0x434 (R/W  32) SPI Chip Select Register 1 */
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_CSR2; /**< Offset: 0x438 (R/W  32) SPI Chip Select Register 2 */
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_CSR3; /**< Offset: 0x43C (R/W  32) SPI Chip Select Register 3 */
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_FMR; /**< Offset: 0x440 (R/W  32) SPI FIFO Mode Register */
  __I   uint32_t                       FLEXCOM_FLEX_SPI_FLR; /**< Offset: 0x444 (R/   32) SPI FIFO Level Register */
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_CMPR; /**< Offset: 0x448 (R/W  32) SPI Comparison Register */
  __I   uint8_t                        Reserved11[0x98];
  __IO  uint32_t                       FLEXCOM_FLEX_SPI_WPMR; /**< Offset: 0x4E4 (R/W  32) SPI Write Protection Mode Register */
  __I   uint32_t                       FLEXCOM_FLEX_SPI_WPSR; /**< Offset: 0x4E8 (R/   32) SPI Write Protection Status Register */
  __I   uint8_t                        Reserved12[0x114];
  __O   uint32_t                       FLEXCOM_FLEX_TWI_CR; /**< Offset: 0x600 ( /W  32) TWI Control Register */
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_MMR; /**< Offset: 0x604 (R/W  32) TWI Master Mode Register */
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_SMR; /**< Offset: 0x608 (R/W  32) TWI Slave Mode Register */
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_IADR; /**< Offset: 0x60C (R/W  32) TWI Internal Address Register */
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_CWGR; /**< Offset: 0x610 (R/W  32) TWI Clock Waveform Generator Register */
  __I   uint8_t                        Reserved13[0x0C];
  __I   uint32_t                       FLEXCOM_FLEX_TWI_SR; /**< Offset: 0x620 (R/   32) TWI Status Register */
  __O   uint32_t                       FLEXCOM_FLEX_TWI_IER; /**< Offset: 0x624 ( /W  32) TWI Interrupt Enable Register */
  __O   uint32_t                       FLEXCOM_FLEX_TWI_IDR; /**< Offset: 0x628 ( /W  32) TWI Interrupt Disable Register */
  __I   uint32_t                       FLEXCOM_FLEX_TWI_IMR; /**< Offset: 0x62C (R/   32) TWI Interrupt Mask Register */
  __I   uint32_t                       FLEXCOM_FLEX_TWI_RHR; /**< Offset: 0x630 (R/   32) TWI Receive Holding Register */
  __O   uint32_t                       FLEXCOM_FLEX_TWI_THR; /**< Offset: 0x634 ( /W  32) TWI Transmit Holding Register */
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_SMBTR; /**< Offset: 0x638 (R/W  32) TWI SMBus Timing Register */
  __I   uint8_t                        Reserved14[0x04];
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_ACR; /**< Offset: 0x640 (R/W  32) TWI Alternative Command Register */
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_FILTR; /**< Offset: 0x644 (R/W  32) TWI Filter Register */
  __I   uint8_t                        Reserved15[0x08];
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_FMR; /**< Offset: 0x650 (R/W  32) TWI FIFO Mode Register */
  __I   uint32_t                       FLEXCOM_FLEX_TWI_FLR; /**< Offset: 0x654 (R/   32) TWI FIFO Level Register */
  __I   uint8_t                        Reserved16[0x08];
  __I   uint32_t                       FLEXCOM_FLEX_TWI_FSR; /**< Offset: 0x660 (R/   32) TWI FIFO Status Register */
  __O   uint32_t                       FLEXCOM_FLEX_TWI_FIER; /**< Offset: 0x664 ( /W  32) TWI FIFO Interrupt Enable Register */
  __O   uint32_t                       FLEXCOM_FLEX_TWI_FIDR; /**< Offset: 0x668 ( /W  32) TWI FIFO Interrupt Disable Register */
  __I   uint32_t                       FLEXCOM_FLEX_TWI_FIMR; /**< Offset: 0x66C (R/   32) TWI FIFO Interrupt Mask Register */
  __I   uint8_t                        Reserved17[0x60];
  __I   uint32_t                       FLEXCOM_FLEX_TWI_DR; /**< Offset: 0x6D0 (R/   32) TWI Debug Register */
  __I   uint8_t                        Reserved18[0x10];
  __IO  uint32_t                       FLEXCOM_FLEX_TWI_WPMR; /**< Offset: 0x6E4 (R/W  32) TWI Write Protection Mode Register */
  __I   uint32_t                       FLEXCOM_FLEX_TWI_WPSR; /**< Offset: 0x6E8 (R/   32) TWI Write Protection Status Register */
} flexcom_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAMRH71_FLEXCOM_COMPONENT_H_ */
