/**
 * \brief Component description for SPW
 *
 * � 2019 Microchip Technology Inc. and its subsidiaries.
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
#ifndef _SAMRH71_SPW_COMPONENT_H_
#define _SAMRH71_SPW_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR SPW                                          */
/* ************************************************************************** */

/* -------- SPW_ROUTER_STS : (SPW Offset: 0x00) ( R/ 32) SpW Router Status -------- */
#define SPW_ROUTER_STS_DEST_Pos               _U_(0)                                         /**< (SPW_ROUTER_STS) Destination addr Position */
#define SPW_ROUTER_STS_DEST_Msk               (_U_(0x1F) << SPW_ROUTER_STS_DEST_Pos)         /**< (SPW_ROUTER_STS) Destination addr Mask */
#define SPW_ROUTER_STS_DEST(value)            (SPW_ROUTER_STS_DEST_Msk & ((value) << SPW_ROUTER_STS_DEST_Pos))
#define SPW_ROUTER_STS_SOURCE_Pos             _U_(8)                                         /**< (SPW_ROUTER_STS) Source address Position */
#define SPW_ROUTER_STS_SOURCE_Msk             (_U_(0x1F) << SPW_ROUTER_STS_SOURCE_Pos)       /**< (SPW_ROUTER_STS) Source address Mask */
#define SPW_ROUTER_STS_SOURCE(value)          (SPW_ROUTER_STS_SOURCE_Msk & ((value) << SPW_ROUTER_STS_SOURCE_Pos))
#define SPW_ROUTER_STS_BYTE_Pos               _U_(16)                                        /**< (SPW_ROUTER_STS) Router byte Position */
#define SPW_ROUTER_STS_BYTE_Msk               (_U_(0xFF) << SPW_ROUTER_STS_BYTE_Pos)         /**< (SPW_ROUTER_STS) Router byte Mask */
#define SPW_ROUTER_STS_BYTE(value)            (SPW_ROUTER_STS_BYTE_Msk & ((value) << SPW_ROUTER_STS_BYTE_Pos))
#define SPW_ROUTER_STS_COUNT_Pos              _U_(24)                                        /**< (SPW_ROUTER_STS) Packet Count Position */
#define SPW_ROUTER_STS_COUNT_Msk              (_U_(0xFF) << SPW_ROUTER_STS_COUNT_Pos)        /**< (SPW_ROUTER_STS) Packet Count Mask */
#define SPW_ROUTER_STS_COUNT(value)           (SPW_ROUTER_STS_COUNT_Msk & ((value) << SPW_ROUTER_STS_COUNT_Pos))
#define SPW_ROUTER_STS_Msk                    _U_(0xFFFF1F1F)                                /**< (SPW_ROUTER_STS) Register Mask  */


/* -------- SPW_ROUTER_CFG : (SPW Offset: 0x04) ( R/ 32) SpW Router Config -------- */
#define SPW_ROUTER_CFG_LAENA_Pos              _U_(0)                                         /**< (SPW_ROUTER_CFG) LA Routing Enable Position */
#define SPW_ROUTER_CFG_LAENA_Msk              (_U_(0x1) << SPW_ROUTER_CFG_LAENA_Pos)         /**< (SPW_ROUTER_CFG) LA Routing Enable Mask */
#define SPW_ROUTER_CFG_FALLBACK_Pos           _U_(1)                                         /**< (SPW_ROUTER_CFG) Fallback Routing Position */
#define SPW_ROUTER_CFG_FALLBACK_Msk           (_U_(0x1) << SPW_ROUTER_CFG_FALLBACK_Pos)      /**< (SPW_ROUTER_CFG) Fallback Routing Mask */
#define SPW_ROUTER_CFG_DISTIMEOUT_Pos         _U_(2)                                         /**< (SPW_ROUTER_CFG) Disable Timeout Position */
#define SPW_ROUTER_CFG_DISTIMEOUT_Msk         (_U_(0x1) << SPW_ROUTER_CFG_DISTIMEOUT_Pos)    /**< (SPW_ROUTER_CFG) Disable Timeout Mask */
#define SPW_ROUTER_CFG_Msk                    _U_(0x00000007)                                /**< (SPW_ROUTER_CFG) Register Mask  */


/* -------- SPW_ROUTER_TIMEOUT : (SPW Offset: 0x08) ( R/ 32) SpW Router Timeout -------- */
#define SPW_ROUTER_TIMEOUT_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TIMEOUT) Physical Address Position */
#define SPW_ROUTER_TIMEOUT_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TIMEOUT_ADDR_Pos)     /**< (SPW_ROUTER_TIMEOUT) Physical Address Mask */
#define SPW_ROUTER_TIMEOUT_ADDR(value)        (SPW_ROUTER_TIMEOUT_ADDR_Msk & ((value) << SPW_ROUTER_TIMEOUT_ADDR_Pos))
#define SPW_ROUTER_TIMEOUT_LOCKED_Pos         _U_(31)                                        /**< (SPW_ROUTER_TIMEOUT) Locked Position */
#define SPW_ROUTER_TIMEOUT_LOCKED_Msk         (_U_(0x1) << SPW_ROUTER_TIMEOUT_LOCKED_Pos)    /**< (SPW_ROUTER_TIMEOUT) Locked Mask */
#define SPW_ROUTER_TIMEOUT_Msk                _U_(0x8000001F)                                /**< (SPW_ROUTER_TIMEOUT) Register Mask  */


/* -------- SPW_ROUTER_TABLE0 : (SPW Offset: 0x80) (R/W 32) SpW Router Table (router_table_nb = 32) 0 -------- */
#define SPW_ROUTER_TABLE0_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE0) Address Position */
#define SPW_ROUTER_TABLE0_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE0_ADDR_Pos)      /**< (SPW_ROUTER_TABLE0) Address Mask */
#define SPW_ROUTER_TABLE0_ADDR(value)         (SPW_ROUTER_TABLE0_ADDR_Msk & ((value) << SPW_ROUTER_TABLE0_ADDR_Pos))
#define SPW_ROUTER_TABLE0_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE0) Delete Header Byte Position */
#define SPW_ROUTER_TABLE0_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE0_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE0) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE0_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE0) Register Mask  */


/* -------- SPW_ROUTER_TABLE1 : (SPW Offset: 0x84) (R/W 32) SpW Router Table (router_table_nb = 32) 1 -------- */
#define SPW_ROUTER_TABLE1_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE1) Address Position */
#define SPW_ROUTER_TABLE1_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE1_ADDR_Pos)      /**< (SPW_ROUTER_TABLE1) Address Mask */
#define SPW_ROUTER_TABLE1_ADDR(value)         (SPW_ROUTER_TABLE1_ADDR_Msk & ((value) << SPW_ROUTER_TABLE1_ADDR_Pos))
#define SPW_ROUTER_TABLE1_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE1) Delete Header Byte Position */
#define SPW_ROUTER_TABLE1_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE1_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE1) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE1_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE1) Register Mask  */


/* -------- SPW_ROUTER_TABLE2 : (SPW Offset: 0x88) (R/W 32) SpW Router Table (router_table_nb = 32) 2 -------- */
#define SPW_ROUTER_TABLE2_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE2) Address Position */
#define SPW_ROUTER_TABLE2_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE2_ADDR_Pos)      /**< (SPW_ROUTER_TABLE2) Address Mask */
#define SPW_ROUTER_TABLE2_ADDR(value)         (SPW_ROUTER_TABLE2_ADDR_Msk & ((value) << SPW_ROUTER_TABLE2_ADDR_Pos))
#define SPW_ROUTER_TABLE2_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE2) Delete Header Byte Position */
#define SPW_ROUTER_TABLE2_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE2_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE2) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE2_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE2) Register Mask  */


/* -------- SPW_ROUTER_TABLE3 : (SPW Offset: 0x8C) (R/W 32) SpW Router Table (router_table_nb = 32) 3 -------- */
#define SPW_ROUTER_TABLE3_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE3) Address Position */
#define SPW_ROUTER_TABLE3_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE3_ADDR_Pos)      /**< (SPW_ROUTER_TABLE3) Address Mask */
#define SPW_ROUTER_TABLE3_ADDR(value)         (SPW_ROUTER_TABLE3_ADDR_Msk & ((value) << SPW_ROUTER_TABLE3_ADDR_Pos))
#define SPW_ROUTER_TABLE3_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE3) Delete Header Byte Position */
#define SPW_ROUTER_TABLE3_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE3_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE3) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE3_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE3) Register Mask  */


/* -------- SPW_ROUTER_TABLE4 : (SPW Offset: 0x90) (R/W 32) SpW Router Table (router_table_nb = 32) 4 -------- */
#define SPW_ROUTER_TABLE4_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE4) Address Position */
#define SPW_ROUTER_TABLE4_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE4_ADDR_Pos)      /**< (SPW_ROUTER_TABLE4) Address Mask */
#define SPW_ROUTER_TABLE4_ADDR(value)         (SPW_ROUTER_TABLE4_ADDR_Msk & ((value) << SPW_ROUTER_TABLE4_ADDR_Pos))
#define SPW_ROUTER_TABLE4_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE4) Delete Header Byte Position */
#define SPW_ROUTER_TABLE4_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE4_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE4) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE4_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE4) Register Mask  */


/* -------- SPW_ROUTER_TABLE5 : (SPW Offset: 0x94) (R/W 32) SpW Router Table (router_table_nb = 32) 5 -------- */
#define SPW_ROUTER_TABLE5_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE5) Address Position */
#define SPW_ROUTER_TABLE5_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE5_ADDR_Pos)      /**< (SPW_ROUTER_TABLE5) Address Mask */
#define SPW_ROUTER_TABLE5_ADDR(value)         (SPW_ROUTER_TABLE5_ADDR_Msk & ((value) << SPW_ROUTER_TABLE5_ADDR_Pos))
#define SPW_ROUTER_TABLE5_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE5) Delete Header Byte Position */
#define SPW_ROUTER_TABLE5_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE5_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE5) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE5_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE5) Register Mask  */


/* -------- SPW_ROUTER_TABLE6 : (SPW Offset: 0x98) (R/W 32) SpW Router Table (router_table_nb = 32) 6 -------- */
#define SPW_ROUTER_TABLE6_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE6) Address Position */
#define SPW_ROUTER_TABLE6_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE6_ADDR_Pos)      /**< (SPW_ROUTER_TABLE6) Address Mask */
#define SPW_ROUTER_TABLE6_ADDR(value)         (SPW_ROUTER_TABLE6_ADDR_Msk & ((value) << SPW_ROUTER_TABLE6_ADDR_Pos))
#define SPW_ROUTER_TABLE6_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE6) Delete Header Byte Position */
#define SPW_ROUTER_TABLE6_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE6_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE6) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE6_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE6) Register Mask  */


/* -------- SPW_ROUTER_TABLE7 : (SPW Offset: 0x9C) (R/W 32) SpW Router Table (router_table_nb = 32) 7 -------- */
#define SPW_ROUTER_TABLE7_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE7) Address Position */
#define SPW_ROUTER_TABLE7_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE7_ADDR_Pos)      /**< (SPW_ROUTER_TABLE7) Address Mask */
#define SPW_ROUTER_TABLE7_ADDR(value)         (SPW_ROUTER_TABLE7_ADDR_Msk & ((value) << SPW_ROUTER_TABLE7_ADDR_Pos))
#define SPW_ROUTER_TABLE7_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE7) Delete Header Byte Position */
#define SPW_ROUTER_TABLE7_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE7_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE7) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE7_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE7) Register Mask  */


/* -------- SPW_ROUTER_TABLE8 : (SPW Offset: 0xA0) (R/W 32) SpW Router Table (router_table_nb = 32) 8 -------- */
#define SPW_ROUTER_TABLE8_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE8) Address Position */
#define SPW_ROUTER_TABLE8_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE8_ADDR_Pos)      /**< (SPW_ROUTER_TABLE8) Address Mask */
#define SPW_ROUTER_TABLE8_ADDR(value)         (SPW_ROUTER_TABLE8_ADDR_Msk & ((value) << SPW_ROUTER_TABLE8_ADDR_Pos))
#define SPW_ROUTER_TABLE8_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE8) Delete Header Byte Position */
#define SPW_ROUTER_TABLE8_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE8_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE8) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE8_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE8) Register Mask  */


/* -------- SPW_ROUTER_TABLE9 : (SPW Offset: 0xA4) (R/W 32) SpW Router Table (router_table_nb = 32) 9 -------- */
#define SPW_ROUTER_TABLE9_ADDR_Pos            _U_(0)                                         /**< (SPW_ROUTER_TABLE9) Address Position */
#define SPW_ROUTER_TABLE9_ADDR_Msk            (_U_(0x1F) << SPW_ROUTER_TABLE9_ADDR_Pos)      /**< (SPW_ROUTER_TABLE9) Address Mask */
#define SPW_ROUTER_TABLE9_ADDR(value)         (SPW_ROUTER_TABLE9_ADDR_Msk & ((value) << SPW_ROUTER_TABLE9_ADDR_Pos))
#define SPW_ROUTER_TABLE9_DELHEAD_Pos         _U_(8)                                         /**< (SPW_ROUTER_TABLE9) Delete Header Byte Position */
#define SPW_ROUTER_TABLE9_DELHEAD_Msk         (_U_(0x1) << SPW_ROUTER_TABLE9_DELHEAD_Pos)    /**< (SPW_ROUTER_TABLE9) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE9_Msk                 _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE9) Register Mask  */


/* -------- SPW_ROUTER_TABLE10 : (SPW Offset: 0xA8) (R/W 32) SpW Router Table (router_table_nb = 32) 10 -------- */
#define SPW_ROUTER_TABLE10_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE10) Address Position */
#define SPW_ROUTER_TABLE10_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE10_ADDR_Pos)     /**< (SPW_ROUTER_TABLE10) Address Mask */
#define SPW_ROUTER_TABLE10_ADDR(value)        (SPW_ROUTER_TABLE10_ADDR_Msk & ((value) << SPW_ROUTER_TABLE10_ADDR_Pos))
#define SPW_ROUTER_TABLE10_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE10) Delete Header Byte Position */
#define SPW_ROUTER_TABLE10_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE10_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE10) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE10_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE10) Register Mask  */


/* -------- SPW_ROUTER_TABLE11 : (SPW Offset: 0xAC) (R/W 32) SpW Router Table (router_table_nb = 32) 11 -------- */
#define SPW_ROUTER_TABLE11_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE11) Address Position */
#define SPW_ROUTER_TABLE11_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE11_ADDR_Pos)     /**< (SPW_ROUTER_TABLE11) Address Mask */
#define SPW_ROUTER_TABLE11_ADDR(value)        (SPW_ROUTER_TABLE11_ADDR_Msk & ((value) << SPW_ROUTER_TABLE11_ADDR_Pos))
#define SPW_ROUTER_TABLE11_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE11) Delete Header Byte Position */
#define SPW_ROUTER_TABLE11_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE11_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE11) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE11_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE11) Register Mask  */


/* -------- SPW_ROUTER_TABLE12 : (SPW Offset: 0xB0) (R/W 32) SpW Router Table (router_table_nb = 32) 12 -------- */
#define SPW_ROUTER_TABLE12_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE12) Address Position */
#define SPW_ROUTER_TABLE12_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE12_ADDR_Pos)     /**< (SPW_ROUTER_TABLE12) Address Mask */
#define SPW_ROUTER_TABLE12_ADDR(value)        (SPW_ROUTER_TABLE12_ADDR_Msk & ((value) << SPW_ROUTER_TABLE12_ADDR_Pos))
#define SPW_ROUTER_TABLE12_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE12) Delete Header Byte Position */
#define SPW_ROUTER_TABLE12_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE12_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE12) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE12_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE12) Register Mask  */


/* -------- SPW_ROUTER_TABLE13 : (SPW Offset: 0xB4) (R/W 32) SpW Router Table (router_table_nb = 32) 13 -------- */
#define SPW_ROUTER_TABLE13_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE13) Address Position */
#define SPW_ROUTER_TABLE13_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE13_ADDR_Pos)     /**< (SPW_ROUTER_TABLE13) Address Mask */
#define SPW_ROUTER_TABLE13_ADDR(value)        (SPW_ROUTER_TABLE13_ADDR_Msk & ((value) << SPW_ROUTER_TABLE13_ADDR_Pos))
#define SPW_ROUTER_TABLE13_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE13) Delete Header Byte Position */
#define SPW_ROUTER_TABLE13_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE13_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE13) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE13_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE13) Register Mask  */


/* -------- SPW_ROUTER_TABLE14 : (SPW Offset: 0xB8) (R/W 32) SpW Router Table (router_table_nb = 32) 14 -------- */
#define SPW_ROUTER_TABLE14_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE14) Address Position */
#define SPW_ROUTER_TABLE14_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE14_ADDR_Pos)     /**< (SPW_ROUTER_TABLE14) Address Mask */
#define SPW_ROUTER_TABLE14_ADDR(value)        (SPW_ROUTER_TABLE14_ADDR_Msk & ((value) << SPW_ROUTER_TABLE14_ADDR_Pos))
#define SPW_ROUTER_TABLE14_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE14) Delete Header Byte Position */
#define SPW_ROUTER_TABLE14_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE14_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE14) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE14_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE14) Register Mask  */


/* -------- SPW_ROUTER_TABLE15 : (SPW Offset: 0xBC) (R/W 32) SpW Router Table (router_table_nb = 32) 15 -------- */
#define SPW_ROUTER_TABLE15_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE15) Address Position */
#define SPW_ROUTER_TABLE15_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE15_ADDR_Pos)     /**< (SPW_ROUTER_TABLE15) Address Mask */
#define SPW_ROUTER_TABLE15_ADDR(value)        (SPW_ROUTER_TABLE15_ADDR_Msk & ((value) << SPW_ROUTER_TABLE15_ADDR_Pos))
#define SPW_ROUTER_TABLE15_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE15) Delete Header Byte Position */
#define SPW_ROUTER_TABLE15_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE15_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE15) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE15_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE15) Register Mask  */


/* -------- SPW_ROUTER_TABLE16 : (SPW Offset: 0xC0) (R/W 32) SpW Router Table (router_table_nb = 32) 16 -------- */
#define SPW_ROUTER_TABLE16_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE16) Address Position */
#define SPW_ROUTER_TABLE16_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE16_ADDR_Pos)     /**< (SPW_ROUTER_TABLE16) Address Mask */
#define SPW_ROUTER_TABLE16_ADDR(value)        (SPW_ROUTER_TABLE16_ADDR_Msk & ((value) << SPW_ROUTER_TABLE16_ADDR_Pos))
#define SPW_ROUTER_TABLE16_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE16) Delete Header Byte Position */
#define SPW_ROUTER_TABLE16_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE16_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE16) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE16_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE16) Register Mask  */


/* -------- SPW_ROUTER_TABLE17 : (SPW Offset: 0xC4) (R/W 32) SpW Router Table (router_table_nb = 32) 17 -------- */
#define SPW_ROUTER_TABLE17_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE17) Address Position */
#define SPW_ROUTER_TABLE17_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE17_ADDR_Pos)     /**< (SPW_ROUTER_TABLE17) Address Mask */
#define SPW_ROUTER_TABLE17_ADDR(value)        (SPW_ROUTER_TABLE17_ADDR_Msk & ((value) << SPW_ROUTER_TABLE17_ADDR_Pos))
#define SPW_ROUTER_TABLE17_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE17) Delete Header Byte Position */
#define SPW_ROUTER_TABLE17_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE17_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE17) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE17_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE17) Register Mask  */


/* -------- SPW_ROUTER_TABLE18 : (SPW Offset: 0xC8) (R/W 32) SpW Router Table (router_table_nb = 32) 18 -------- */
#define SPW_ROUTER_TABLE18_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE18) Address Position */
#define SPW_ROUTER_TABLE18_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE18_ADDR_Pos)     /**< (SPW_ROUTER_TABLE18) Address Mask */
#define SPW_ROUTER_TABLE18_ADDR(value)        (SPW_ROUTER_TABLE18_ADDR_Msk & ((value) << SPW_ROUTER_TABLE18_ADDR_Pos))
#define SPW_ROUTER_TABLE18_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE18) Delete Header Byte Position */
#define SPW_ROUTER_TABLE18_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE18_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE18) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE18_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE18) Register Mask  */


/* -------- SPW_ROUTER_TABLE19 : (SPW Offset: 0xCC) (R/W 32) SpW Router Table (router_table_nb = 32) 19 -------- */
#define SPW_ROUTER_TABLE19_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE19) Address Position */
#define SPW_ROUTER_TABLE19_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE19_ADDR_Pos)     /**< (SPW_ROUTER_TABLE19) Address Mask */
#define SPW_ROUTER_TABLE19_ADDR(value)        (SPW_ROUTER_TABLE19_ADDR_Msk & ((value) << SPW_ROUTER_TABLE19_ADDR_Pos))
#define SPW_ROUTER_TABLE19_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE19) Delete Header Byte Position */
#define SPW_ROUTER_TABLE19_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE19_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE19) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE19_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE19) Register Mask  */


/* -------- SPW_ROUTER_TABLE20 : (SPW Offset: 0xD0) (R/W 32) SpW Router Table (router_table_nb = 32) 20 -------- */
#define SPW_ROUTER_TABLE20_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE20) Address Position */
#define SPW_ROUTER_TABLE20_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE20_ADDR_Pos)     /**< (SPW_ROUTER_TABLE20) Address Mask */
#define SPW_ROUTER_TABLE20_ADDR(value)        (SPW_ROUTER_TABLE20_ADDR_Msk & ((value) << SPW_ROUTER_TABLE20_ADDR_Pos))
#define SPW_ROUTER_TABLE20_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE20) Delete Header Byte Position */
#define SPW_ROUTER_TABLE20_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE20_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE20) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE20_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE20) Register Mask  */


/* -------- SPW_ROUTER_TABLE21 : (SPW Offset: 0xD4) (R/W 32) SpW Router Table (router_table_nb = 32) 21 -------- */
#define SPW_ROUTER_TABLE21_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE21) Address Position */
#define SPW_ROUTER_TABLE21_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE21_ADDR_Pos)     /**< (SPW_ROUTER_TABLE21) Address Mask */
#define SPW_ROUTER_TABLE21_ADDR(value)        (SPW_ROUTER_TABLE21_ADDR_Msk & ((value) << SPW_ROUTER_TABLE21_ADDR_Pos))
#define SPW_ROUTER_TABLE21_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE21) Delete Header Byte Position */
#define SPW_ROUTER_TABLE21_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE21_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE21) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE21_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE21) Register Mask  */


/* -------- SPW_ROUTER_TABLE22 : (SPW Offset: 0xD8) (R/W 32) SpW Router Table (router_table_nb = 32) 22 -------- */
#define SPW_ROUTER_TABLE22_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE22) Address Position */
#define SPW_ROUTER_TABLE22_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE22_ADDR_Pos)     /**< (SPW_ROUTER_TABLE22) Address Mask */
#define SPW_ROUTER_TABLE22_ADDR(value)        (SPW_ROUTER_TABLE22_ADDR_Msk & ((value) << SPW_ROUTER_TABLE22_ADDR_Pos))
#define SPW_ROUTER_TABLE22_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE22) Delete Header Byte Position */
#define SPW_ROUTER_TABLE22_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE22_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE22) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE22_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE22) Register Mask  */


/* -------- SPW_ROUTER_TABLE23 : (SPW Offset: 0xDC) (R/W 32) SpW Router Table (router_table_nb = 32) 23 -------- */
#define SPW_ROUTER_TABLE23_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE23) Address Position */
#define SPW_ROUTER_TABLE23_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE23_ADDR_Pos)     /**< (SPW_ROUTER_TABLE23) Address Mask */
#define SPW_ROUTER_TABLE23_ADDR(value)        (SPW_ROUTER_TABLE23_ADDR_Msk & ((value) << SPW_ROUTER_TABLE23_ADDR_Pos))
#define SPW_ROUTER_TABLE23_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE23) Delete Header Byte Position */
#define SPW_ROUTER_TABLE23_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE23_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE23) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE23_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE23) Register Mask  */


/* -------- SPW_ROUTER_TABLE24 : (SPW Offset: 0xE0) (R/W 32) SpW Router Table (router_table_nb = 32) 24 -------- */
#define SPW_ROUTER_TABLE24_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE24) Address Position */
#define SPW_ROUTER_TABLE24_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE24_ADDR_Pos)     /**< (SPW_ROUTER_TABLE24) Address Mask */
#define SPW_ROUTER_TABLE24_ADDR(value)        (SPW_ROUTER_TABLE24_ADDR_Msk & ((value) << SPW_ROUTER_TABLE24_ADDR_Pos))
#define SPW_ROUTER_TABLE24_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE24) Delete Header Byte Position */
#define SPW_ROUTER_TABLE24_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE24_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE24) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE24_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE24) Register Mask  */


/* -------- SPW_ROUTER_TABLE25 : (SPW Offset: 0xE4) (R/W 32) SpW Router Table (router_table_nb = 32) 25 -------- */
#define SPW_ROUTER_TABLE25_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE25) Address Position */
#define SPW_ROUTER_TABLE25_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE25_ADDR_Pos)     /**< (SPW_ROUTER_TABLE25) Address Mask */
#define SPW_ROUTER_TABLE25_ADDR(value)        (SPW_ROUTER_TABLE25_ADDR_Msk & ((value) << SPW_ROUTER_TABLE25_ADDR_Pos))
#define SPW_ROUTER_TABLE25_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE25) Delete Header Byte Position */
#define SPW_ROUTER_TABLE25_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE25_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE25) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE25_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE25) Register Mask  */


/* -------- SPW_ROUTER_TABLE26 : (SPW Offset: 0xE8) (R/W 32) SpW Router Table (router_table_nb = 32) 26 -------- */
#define SPW_ROUTER_TABLE26_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE26) Address Position */
#define SPW_ROUTER_TABLE26_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE26_ADDR_Pos)     /**< (SPW_ROUTER_TABLE26) Address Mask */
#define SPW_ROUTER_TABLE26_ADDR(value)        (SPW_ROUTER_TABLE26_ADDR_Msk & ((value) << SPW_ROUTER_TABLE26_ADDR_Pos))
#define SPW_ROUTER_TABLE26_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE26) Delete Header Byte Position */
#define SPW_ROUTER_TABLE26_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE26_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE26) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE26_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE26) Register Mask  */


/* -------- SPW_ROUTER_TABLE27 : (SPW Offset: 0xEC) (R/W 32) SpW Router Table (router_table_nb = 32) 27 -------- */
#define SPW_ROUTER_TABLE27_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE27) Address Position */
#define SPW_ROUTER_TABLE27_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE27_ADDR_Pos)     /**< (SPW_ROUTER_TABLE27) Address Mask */
#define SPW_ROUTER_TABLE27_ADDR(value)        (SPW_ROUTER_TABLE27_ADDR_Msk & ((value) << SPW_ROUTER_TABLE27_ADDR_Pos))
#define SPW_ROUTER_TABLE27_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE27) Delete Header Byte Position */
#define SPW_ROUTER_TABLE27_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE27_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE27) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE27_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE27) Register Mask  */


/* -------- SPW_ROUTER_TABLE28 : (SPW Offset: 0xF0) (R/W 32) SpW Router Table (router_table_nb = 32) 28 -------- */
#define SPW_ROUTER_TABLE28_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE28) Address Position */
#define SPW_ROUTER_TABLE28_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE28_ADDR_Pos)     /**< (SPW_ROUTER_TABLE28) Address Mask */
#define SPW_ROUTER_TABLE28_ADDR(value)        (SPW_ROUTER_TABLE28_ADDR_Msk & ((value) << SPW_ROUTER_TABLE28_ADDR_Pos))
#define SPW_ROUTER_TABLE28_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE28) Delete Header Byte Position */
#define SPW_ROUTER_TABLE28_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE28_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE28) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE28_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE28) Register Mask  */


/* -------- SPW_ROUTER_TABLE29 : (SPW Offset: 0xF4) (R/W 32) SpW Router Table (router_table_nb = 32) 29 -------- */
#define SPW_ROUTER_TABLE29_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE29) Address Position */
#define SPW_ROUTER_TABLE29_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE29_ADDR_Pos)     /**< (SPW_ROUTER_TABLE29) Address Mask */
#define SPW_ROUTER_TABLE29_ADDR(value)        (SPW_ROUTER_TABLE29_ADDR_Msk & ((value) << SPW_ROUTER_TABLE29_ADDR_Pos))
#define SPW_ROUTER_TABLE29_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE29) Delete Header Byte Position */
#define SPW_ROUTER_TABLE29_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE29_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE29) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE29_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE29) Register Mask  */


/* -------- SPW_ROUTER_TABLE30 : (SPW Offset: 0xF8) (R/W 32) SpW Router Table (router_table_nb = 32) 30 -------- */
#define SPW_ROUTER_TABLE30_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE30) Address Position */
#define SPW_ROUTER_TABLE30_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE30_ADDR_Pos)     /**< (SPW_ROUTER_TABLE30) Address Mask */
#define SPW_ROUTER_TABLE30_ADDR(value)        (SPW_ROUTER_TABLE30_ADDR_Msk & ((value) << SPW_ROUTER_TABLE30_ADDR_Pos))
#define SPW_ROUTER_TABLE30_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE30) Delete Header Byte Position */
#define SPW_ROUTER_TABLE30_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE30_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE30) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE30_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE30) Register Mask  */


/* -------- SPW_ROUTER_TABLE31 : (SPW Offset: 0xFC) (R/W 32) SpW Router Table (router_table_nb = 32) 31 -------- */
#define SPW_ROUTER_TABLE31_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE31) Address Position */
#define SPW_ROUTER_TABLE31_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE31_ADDR_Pos)     /**< (SPW_ROUTER_TABLE31) Address Mask */
#define SPW_ROUTER_TABLE31_ADDR(value)        (SPW_ROUTER_TABLE31_ADDR_Msk & ((value) << SPW_ROUTER_TABLE31_ADDR_Pos))
#define SPW_ROUTER_TABLE31_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE31) Delete Header Byte Position */
#define SPW_ROUTER_TABLE31_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE31_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE31) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE31_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE31) Register Mask  */


/* -------- SPW_ROUTER_TABLE32 : (SPW Offset: 0x100) (R/W 32) SpW Router Table (router_table_nb = 32) 32 -------- */
#define SPW_ROUTER_TABLE32_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE32) Address Position */
#define SPW_ROUTER_TABLE32_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE32_ADDR_Pos)     /**< (SPW_ROUTER_TABLE32) Address Mask */
#define SPW_ROUTER_TABLE32_ADDR(value)        (SPW_ROUTER_TABLE32_ADDR_Msk & ((value) << SPW_ROUTER_TABLE32_ADDR_Pos))
#define SPW_ROUTER_TABLE32_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE32) Delete Header Byte Position */
#define SPW_ROUTER_TABLE32_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE32_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE32) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE32_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE32) Register Mask  */


/* -------- SPW_ROUTER_TABLE33 : (SPW Offset: 0x104) (R/W 32) SpW Router Table (router_table_nb = 32) 33 -------- */
#define SPW_ROUTER_TABLE33_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE33) Address Position */
#define SPW_ROUTER_TABLE33_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE33_ADDR_Pos)     /**< (SPW_ROUTER_TABLE33) Address Mask */
#define SPW_ROUTER_TABLE33_ADDR(value)        (SPW_ROUTER_TABLE33_ADDR_Msk & ((value) << SPW_ROUTER_TABLE33_ADDR_Pos))
#define SPW_ROUTER_TABLE33_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE33) Delete Header Byte Position */
#define SPW_ROUTER_TABLE33_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE33_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE33) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE33_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE33) Register Mask  */


/* -------- SPW_ROUTER_TABLE34 : (SPW Offset: 0x108) (R/W 32) SpW Router Table (router_table_nb = 32) 34 -------- */
#define SPW_ROUTER_TABLE34_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE34) Address Position */
#define SPW_ROUTER_TABLE34_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE34_ADDR_Pos)     /**< (SPW_ROUTER_TABLE34) Address Mask */
#define SPW_ROUTER_TABLE34_ADDR(value)        (SPW_ROUTER_TABLE34_ADDR_Msk & ((value) << SPW_ROUTER_TABLE34_ADDR_Pos))
#define SPW_ROUTER_TABLE34_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE34) Delete Header Byte Position */
#define SPW_ROUTER_TABLE34_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE34_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE34) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE34_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE34) Register Mask  */


/* -------- SPW_ROUTER_TABLE35 : (SPW Offset: 0x10C) (R/W 32) SpW Router Table (router_table_nb = 32) 35 -------- */
#define SPW_ROUTER_TABLE35_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE35) Address Position */
#define SPW_ROUTER_TABLE35_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE35_ADDR_Pos)     /**< (SPW_ROUTER_TABLE35) Address Mask */
#define SPW_ROUTER_TABLE35_ADDR(value)        (SPW_ROUTER_TABLE35_ADDR_Msk & ((value) << SPW_ROUTER_TABLE35_ADDR_Pos))
#define SPW_ROUTER_TABLE35_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE35) Delete Header Byte Position */
#define SPW_ROUTER_TABLE35_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE35_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE35) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE35_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE35) Register Mask  */


/* -------- SPW_ROUTER_TABLE36 : (SPW Offset: 0x110) (R/W 32) SpW Router Table (router_table_nb = 32) 36 -------- */
#define SPW_ROUTER_TABLE36_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE36) Address Position */
#define SPW_ROUTER_TABLE36_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE36_ADDR_Pos)     /**< (SPW_ROUTER_TABLE36) Address Mask */
#define SPW_ROUTER_TABLE36_ADDR(value)        (SPW_ROUTER_TABLE36_ADDR_Msk & ((value) << SPW_ROUTER_TABLE36_ADDR_Pos))
#define SPW_ROUTER_TABLE36_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE36) Delete Header Byte Position */
#define SPW_ROUTER_TABLE36_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE36_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE36) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE36_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE36) Register Mask  */


/* -------- SPW_ROUTER_TABLE37 : (SPW Offset: 0x114) (R/W 32) SpW Router Table (router_table_nb = 32) 37 -------- */
#define SPW_ROUTER_TABLE37_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE37) Address Position */
#define SPW_ROUTER_TABLE37_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE37_ADDR_Pos)     /**< (SPW_ROUTER_TABLE37) Address Mask */
#define SPW_ROUTER_TABLE37_ADDR(value)        (SPW_ROUTER_TABLE37_ADDR_Msk & ((value) << SPW_ROUTER_TABLE37_ADDR_Pos))
#define SPW_ROUTER_TABLE37_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE37) Delete Header Byte Position */
#define SPW_ROUTER_TABLE37_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE37_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE37) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE37_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE37) Register Mask  */


/* -------- SPW_ROUTER_TABLE38 : (SPW Offset: 0x118) (R/W 32) SpW Router Table (router_table_nb = 32) 38 -------- */
#define SPW_ROUTER_TABLE38_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE38) Address Position */
#define SPW_ROUTER_TABLE38_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE38_ADDR_Pos)     /**< (SPW_ROUTER_TABLE38) Address Mask */
#define SPW_ROUTER_TABLE38_ADDR(value)        (SPW_ROUTER_TABLE38_ADDR_Msk & ((value) << SPW_ROUTER_TABLE38_ADDR_Pos))
#define SPW_ROUTER_TABLE38_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE38) Delete Header Byte Position */
#define SPW_ROUTER_TABLE38_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE38_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE38) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE38_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE38) Register Mask  */


/* -------- SPW_ROUTER_TABLE39 : (SPW Offset: 0x11C) (R/W 32) SpW Router Table (router_table_nb = 32) 39 -------- */
#define SPW_ROUTER_TABLE39_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE39) Address Position */
#define SPW_ROUTER_TABLE39_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE39_ADDR_Pos)     /**< (SPW_ROUTER_TABLE39) Address Mask */
#define SPW_ROUTER_TABLE39_ADDR(value)        (SPW_ROUTER_TABLE39_ADDR_Msk & ((value) << SPW_ROUTER_TABLE39_ADDR_Pos))
#define SPW_ROUTER_TABLE39_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE39) Delete Header Byte Position */
#define SPW_ROUTER_TABLE39_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE39_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE39) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE39_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE39) Register Mask  */


/* -------- SPW_ROUTER_TABLE40 : (SPW Offset: 0x120) (R/W 32) SpW Router Table (router_table_nb = 32) 40 -------- */
#define SPW_ROUTER_TABLE40_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE40) Address Position */
#define SPW_ROUTER_TABLE40_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE40_ADDR_Pos)     /**< (SPW_ROUTER_TABLE40) Address Mask */
#define SPW_ROUTER_TABLE40_ADDR(value)        (SPW_ROUTER_TABLE40_ADDR_Msk & ((value) << SPW_ROUTER_TABLE40_ADDR_Pos))
#define SPW_ROUTER_TABLE40_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE40) Delete Header Byte Position */
#define SPW_ROUTER_TABLE40_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE40_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE40) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE40_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE40) Register Mask  */


/* -------- SPW_ROUTER_TABLE41 : (SPW Offset: 0x124) (R/W 32) SpW Router Table (router_table_nb = 32) 41 -------- */
#define SPW_ROUTER_TABLE41_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE41) Address Position */
#define SPW_ROUTER_TABLE41_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE41_ADDR_Pos)     /**< (SPW_ROUTER_TABLE41) Address Mask */
#define SPW_ROUTER_TABLE41_ADDR(value)        (SPW_ROUTER_TABLE41_ADDR_Msk & ((value) << SPW_ROUTER_TABLE41_ADDR_Pos))
#define SPW_ROUTER_TABLE41_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE41) Delete Header Byte Position */
#define SPW_ROUTER_TABLE41_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE41_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE41) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE41_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE41) Register Mask  */


/* -------- SPW_ROUTER_TABLE42 : (SPW Offset: 0x128) (R/W 32) SpW Router Table (router_table_nb = 32) 42 -------- */
#define SPW_ROUTER_TABLE42_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE42) Address Position */
#define SPW_ROUTER_TABLE42_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE42_ADDR_Pos)     /**< (SPW_ROUTER_TABLE42) Address Mask */
#define SPW_ROUTER_TABLE42_ADDR(value)        (SPW_ROUTER_TABLE42_ADDR_Msk & ((value) << SPW_ROUTER_TABLE42_ADDR_Pos))
#define SPW_ROUTER_TABLE42_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE42) Delete Header Byte Position */
#define SPW_ROUTER_TABLE42_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE42_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE42) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE42_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE42) Register Mask  */


/* -------- SPW_ROUTER_TABLE43 : (SPW Offset: 0x12C) (R/W 32) SpW Router Table (router_table_nb = 32) 43 -------- */
#define SPW_ROUTER_TABLE43_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE43) Address Position */
#define SPW_ROUTER_TABLE43_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE43_ADDR_Pos)     /**< (SPW_ROUTER_TABLE43) Address Mask */
#define SPW_ROUTER_TABLE43_ADDR(value)        (SPW_ROUTER_TABLE43_ADDR_Msk & ((value) << SPW_ROUTER_TABLE43_ADDR_Pos))
#define SPW_ROUTER_TABLE43_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE43) Delete Header Byte Position */
#define SPW_ROUTER_TABLE43_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE43_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE43) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE43_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE43) Register Mask  */


/* -------- SPW_ROUTER_TABLE44 : (SPW Offset: 0x130) (R/W 32) SpW Router Table (router_table_nb = 32) 44 -------- */
#define SPW_ROUTER_TABLE44_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE44) Address Position */
#define SPW_ROUTER_TABLE44_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE44_ADDR_Pos)     /**< (SPW_ROUTER_TABLE44) Address Mask */
#define SPW_ROUTER_TABLE44_ADDR(value)        (SPW_ROUTER_TABLE44_ADDR_Msk & ((value) << SPW_ROUTER_TABLE44_ADDR_Pos))
#define SPW_ROUTER_TABLE44_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE44) Delete Header Byte Position */
#define SPW_ROUTER_TABLE44_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE44_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE44) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE44_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE44) Register Mask  */


/* -------- SPW_ROUTER_TABLE45 : (SPW Offset: 0x134) (R/W 32) SpW Router Table (router_table_nb = 32) 45 -------- */
#define SPW_ROUTER_TABLE45_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE45) Address Position */
#define SPW_ROUTER_TABLE45_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE45_ADDR_Pos)     /**< (SPW_ROUTER_TABLE45) Address Mask */
#define SPW_ROUTER_TABLE45_ADDR(value)        (SPW_ROUTER_TABLE45_ADDR_Msk & ((value) << SPW_ROUTER_TABLE45_ADDR_Pos))
#define SPW_ROUTER_TABLE45_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE45) Delete Header Byte Position */
#define SPW_ROUTER_TABLE45_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE45_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE45) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE45_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE45) Register Mask  */


/* -------- SPW_ROUTER_TABLE46 : (SPW Offset: 0x138) (R/W 32) SpW Router Table (router_table_nb = 32) 46 -------- */
#define SPW_ROUTER_TABLE46_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE46) Address Position */
#define SPW_ROUTER_TABLE46_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE46_ADDR_Pos)     /**< (SPW_ROUTER_TABLE46) Address Mask */
#define SPW_ROUTER_TABLE46_ADDR(value)        (SPW_ROUTER_TABLE46_ADDR_Msk & ((value) << SPW_ROUTER_TABLE46_ADDR_Pos))
#define SPW_ROUTER_TABLE46_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE46) Delete Header Byte Position */
#define SPW_ROUTER_TABLE46_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE46_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE46) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE46_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE46) Register Mask  */


/* -------- SPW_ROUTER_TABLE47 : (SPW Offset: 0x13C) (R/W 32) SpW Router Table (router_table_nb = 32) 47 -------- */
#define SPW_ROUTER_TABLE47_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE47) Address Position */
#define SPW_ROUTER_TABLE47_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE47_ADDR_Pos)     /**< (SPW_ROUTER_TABLE47) Address Mask */
#define SPW_ROUTER_TABLE47_ADDR(value)        (SPW_ROUTER_TABLE47_ADDR_Msk & ((value) << SPW_ROUTER_TABLE47_ADDR_Pos))
#define SPW_ROUTER_TABLE47_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE47) Delete Header Byte Position */
#define SPW_ROUTER_TABLE47_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE47_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE47) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE47_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE47) Register Mask  */


/* -------- SPW_ROUTER_TABLE48 : (SPW Offset: 0x140) (R/W 32) SpW Router Table (router_table_nb = 32) 48 -------- */
#define SPW_ROUTER_TABLE48_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE48) Address Position */
#define SPW_ROUTER_TABLE48_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE48_ADDR_Pos)     /**< (SPW_ROUTER_TABLE48) Address Mask */
#define SPW_ROUTER_TABLE48_ADDR(value)        (SPW_ROUTER_TABLE48_ADDR_Msk & ((value) << SPW_ROUTER_TABLE48_ADDR_Pos))
#define SPW_ROUTER_TABLE48_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE48) Delete Header Byte Position */
#define SPW_ROUTER_TABLE48_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE48_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE48) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE48_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE48) Register Mask  */


/* -------- SPW_ROUTER_TABLE49 : (SPW Offset: 0x144) (R/W 32) SpW Router Table (router_table_nb = 32) 49 -------- */
#define SPW_ROUTER_TABLE49_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE49) Address Position */
#define SPW_ROUTER_TABLE49_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE49_ADDR_Pos)     /**< (SPW_ROUTER_TABLE49) Address Mask */
#define SPW_ROUTER_TABLE49_ADDR(value)        (SPW_ROUTER_TABLE49_ADDR_Msk & ((value) << SPW_ROUTER_TABLE49_ADDR_Pos))
#define SPW_ROUTER_TABLE49_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE49) Delete Header Byte Position */
#define SPW_ROUTER_TABLE49_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE49_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE49) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE49_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE49) Register Mask  */


/* -------- SPW_ROUTER_TABLE50 : (SPW Offset: 0x148) (R/W 32) SpW Router Table (router_table_nb = 32) 50 -------- */
#define SPW_ROUTER_TABLE50_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE50) Address Position */
#define SPW_ROUTER_TABLE50_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE50_ADDR_Pos)     /**< (SPW_ROUTER_TABLE50) Address Mask */
#define SPW_ROUTER_TABLE50_ADDR(value)        (SPW_ROUTER_TABLE50_ADDR_Msk & ((value) << SPW_ROUTER_TABLE50_ADDR_Pos))
#define SPW_ROUTER_TABLE50_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE50) Delete Header Byte Position */
#define SPW_ROUTER_TABLE50_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE50_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE50) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE50_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE50) Register Mask  */


/* -------- SPW_ROUTER_TABLE51 : (SPW Offset: 0x14C) (R/W 32) SpW Router Table (router_table_nb = 32) 51 -------- */
#define SPW_ROUTER_TABLE51_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE51) Address Position */
#define SPW_ROUTER_TABLE51_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE51_ADDR_Pos)     /**< (SPW_ROUTER_TABLE51) Address Mask */
#define SPW_ROUTER_TABLE51_ADDR(value)        (SPW_ROUTER_TABLE51_ADDR_Msk & ((value) << SPW_ROUTER_TABLE51_ADDR_Pos))
#define SPW_ROUTER_TABLE51_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE51) Delete Header Byte Position */
#define SPW_ROUTER_TABLE51_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE51_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE51) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE51_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE51) Register Mask  */


/* -------- SPW_ROUTER_TABLE52 : (SPW Offset: 0x150) (R/W 32) SpW Router Table (router_table_nb = 32) 52 -------- */
#define SPW_ROUTER_TABLE52_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE52) Address Position */
#define SPW_ROUTER_TABLE52_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE52_ADDR_Pos)     /**< (SPW_ROUTER_TABLE52) Address Mask */
#define SPW_ROUTER_TABLE52_ADDR(value)        (SPW_ROUTER_TABLE52_ADDR_Msk & ((value) << SPW_ROUTER_TABLE52_ADDR_Pos))
#define SPW_ROUTER_TABLE52_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE52) Delete Header Byte Position */
#define SPW_ROUTER_TABLE52_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE52_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE52) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE52_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE52) Register Mask  */


/* -------- SPW_ROUTER_TABLE53 : (SPW Offset: 0x154) (R/W 32) SpW Router Table (router_table_nb = 32) 53 -------- */
#define SPW_ROUTER_TABLE53_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE53) Address Position */
#define SPW_ROUTER_TABLE53_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE53_ADDR_Pos)     /**< (SPW_ROUTER_TABLE53) Address Mask */
#define SPW_ROUTER_TABLE53_ADDR(value)        (SPW_ROUTER_TABLE53_ADDR_Msk & ((value) << SPW_ROUTER_TABLE53_ADDR_Pos))
#define SPW_ROUTER_TABLE53_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE53) Delete Header Byte Position */
#define SPW_ROUTER_TABLE53_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE53_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE53) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE53_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE53) Register Mask  */


/* -------- SPW_ROUTER_TABLE54 : (SPW Offset: 0x158) (R/W 32) SpW Router Table (router_table_nb = 32) 54 -------- */
#define SPW_ROUTER_TABLE54_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE54) Address Position */
#define SPW_ROUTER_TABLE54_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE54_ADDR_Pos)     /**< (SPW_ROUTER_TABLE54) Address Mask */
#define SPW_ROUTER_TABLE54_ADDR(value)        (SPW_ROUTER_TABLE54_ADDR_Msk & ((value) << SPW_ROUTER_TABLE54_ADDR_Pos))
#define SPW_ROUTER_TABLE54_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE54) Delete Header Byte Position */
#define SPW_ROUTER_TABLE54_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE54_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE54) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE54_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE54) Register Mask  */


/* -------- SPW_ROUTER_TABLE55 : (SPW Offset: 0x15C) (R/W 32) SpW Router Table (router_table_nb = 32) 55 -------- */
#define SPW_ROUTER_TABLE55_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE55) Address Position */
#define SPW_ROUTER_TABLE55_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE55_ADDR_Pos)     /**< (SPW_ROUTER_TABLE55) Address Mask */
#define SPW_ROUTER_TABLE55_ADDR(value)        (SPW_ROUTER_TABLE55_ADDR_Msk & ((value) << SPW_ROUTER_TABLE55_ADDR_Pos))
#define SPW_ROUTER_TABLE55_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE55) Delete Header Byte Position */
#define SPW_ROUTER_TABLE55_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE55_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE55) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE55_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE55) Register Mask  */


/* -------- SPW_ROUTER_TABLE56 : (SPW Offset: 0x160) (R/W 32) SpW Router Table (router_table_nb = 32) 56 -------- */
#define SPW_ROUTER_TABLE56_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE56) Address Position */
#define SPW_ROUTER_TABLE56_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE56_ADDR_Pos)     /**< (SPW_ROUTER_TABLE56) Address Mask */
#define SPW_ROUTER_TABLE56_ADDR(value)        (SPW_ROUTER_TABLE56_ADDR_Msk & ((value) << SPW_ROUTER_TABLE56_ADDR_Pos))
#define SPW_ROUTER_TABLE56_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE56) Delete Header Byte Position */
#define SPW_ROUTER_TABLE56_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE56_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE56) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE56_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE56) Register Mask  */


/* -------- SPW_ROUTER_TABLE57 : (SPW Offset: 0x164) (R/W 32) SpW Router Table (router_table_nb = 32) 57 -------- */
#define SPW_ROUTER_TABLE57_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE57) Address Position */
#define SPW_ROUTER_TABLE57_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE57_ADDR_Pos)     /**< (SPW_ROUTER_TABLE57) Address Mask */
#define SPW_ROUTER_TABLE57_ADDR(value)        (SPW_ROUTER_TABLE57_ADDR_Msk & ((value) << SPW_ROUTER_TABLE57_ADDR_Pos))
#define SPW_ROUTER_TABLE57_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE57) Delete Header Byte Position */
#define SPW_ROUTER_TABLE57_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE57_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE57) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE57_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE57) Register Mask  */


/* -------- SPW_ROUTER_TABLE58 : (SPW Offset: 0x168) (R/W 32) SpW Router Table (router_table_nb = 32) 58 -------- */
#define SPW_ROUTER_TABLE58_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE58) Address Position */
#define SPW_ROUTER_TABLE58_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE58_ADDR_Pos)     /**< (SPW_ROUTER_TABLE58) Address Mask */
#define SPW_ROUTER_TABLE58_ADDR(value)        (SPW_ROUTER_TABLE58_ADDR_Msk & ((value) << SPW_ROUTER_TABLE58_ADDR_Pos))
#define SPW_ROUTER_TABLE58_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE58) Delete Header Byte Position */
#define SPW_ROUTER_TABLE58_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE58_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE58) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE58_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE58) Register Mask  */


/* -------- SPW_ROUTER_TABLE59 : (SPW Offset: 0x16C) (R/W 32) SpW Router Table (router_table_nb = 32) 59 -------- */
#define SPW_ROUTER_TABLE59_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE59) Address Position */
#define SPW_ROUTER_TABLE59_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE59_ADDR_Pos)     /**< (SPW_ROUTER_TABLE59) Address Mask */
#define SPW_ROUTER_TABLE59_ADDR(value)        (SPW_ROUTER_TABLE59_ADDR_Msk & ((value) << SPW_ROUTER_TABLE59_ADDR_Pos))
#define SPW_ROUTER_TABLE59_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE59) Delete Header Byte Position */
#define SPW_ROUTER_TABLE59_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE59_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE59) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE59_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE59) Register Mask  */


/* -------- SPW_ROUTER_TABLE60 : (SPW Offset: 0x170) (R/W 32) SpW Router Table (router_table_nb = 32) 60 -------- */
#define SPW_ROUTER_TABLE60_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE60) Address Position */
#define SPW_ROUTER_TABLE60_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE60_ADDR_Pos)     /**< (SPW_ROUTER_TABLE60) Address Mask */
#define SPW_ROUTER_TABLE60_ADDR(value)        (SPW_ROUTER_TABLE60_ADDR_Msk & ((value) << SPW_ROUTER_TABLE60_ADDR_Pos))
#define SPW_ROUTER_TABLE60_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE60) Delete Header Byte Position */
#define SPW_ROUTER_TABLE60_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE60_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE60) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE60_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE60) Register Mask  */


/* -------- SPW_ROUTER_TABLE61 : (SPW Offset: 0x174) (R/W 32) SpW Router Table (router_table_nb = 32) 61 -------- */
#define SPW_ROUTER_TABLE61_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE61) Address Position */
#define SPW_ROUTER_TABLE61_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE61_ADDR_Pos)     /**< (SPW_ROUTER_TABLE61) Address Mask */
#define SPW_ROUTER_TABLE61_ADDR(value)        (SPW_ROUTER_TABLE61_ADDR_Msk & ((value) << SPW_ROUTER_TABLE61_ADDR_Pos))
#define SPW_ROUTER_TABLE61_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE61) Delete Header Byte Position */
#define SPW_ROUTER_TABLE61_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE61_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE61) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE61_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE61) Register Mask  */


/* -------- SPW_ROUTER_TABLE62 : (SPW Offset: 0x178) (R/W 32) SpW Router Table (router_table_nb = 32) 62 -------- */
#define SPW_ROUTER_TABLE62_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE62) Address Position */
#define SPW_ROUTER_TABLE62_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE62_ADDR_Pos)     /**< (SPW_ROUTER_TABLE62) Address Mask */
#define SPW_ROUTER_TABLE62_ADDR(value)        (SPW_ROUTER_TABLE62_ADDR_Msk & ((value) << SPW_ROUTER_TABLE62_ADDR_Pos))
#define SPW_ROUTER_TABLE62_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE62) Delete Header Byte Position */
#define SPW_ROUTER_TABLE62_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE62_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE62) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE62_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE62) Register Mask  */


/* -------- SPW_ROUTER_TABLE63 : (SPW Offset: 0x17C) (R/W 32) SpW Router Table (router_table_nb = 32) 63 -------- */
#define SPW_ROUTER_TABLE63_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE63) Address Position */
#define SPW_ROUTER_TABLE63_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE63_ADDR_Pos)     /**< (SPW_ROUTER_TABLE63) Address Mask */
#define SPW_ROUTER_TABLE63_ADDR(value)        (SPW_ROUTER_TABLE63_ADDR_Msk & ((value) << SPW_ROUTER_TABLE63_ADDR_Pos))
#define SPW_ROUTER_TABLE63_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE63) Delete Header Byte Position */
#define SPW_ROUTER_TABLE63_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE63_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE63) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE63_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE63) Register Mask  */


/* -------- SPW_ROUTER_TABLE64 : (SPW Offset: 0x180) (R/W 32) SpW Router Table (router_table_nb = 32) 64 -------- */
#define SPW_ROUTER_TABLE64_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE64) Address Position */
#define SPW_ROUTER_TABLE64_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE64_ADDR_Pos)     /**< (SPW_ROUTER_TABLE64) Address Mask */
#define SPW_ROUTER_TABLE64_ADDR(value)        (SPW_ROUTER_TABLE64_ADDR_Msk & ((value) << SPW_ROUTER_TABLE64_ADDR_Pos))
#define SPW_ROUTER_TABLE64_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE64) Delete Header Byte Position */
#define SPW_ROUTER_TABLE64_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE64_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE64) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE64_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE64) Register Mask  */


/* -------- SPW_ROUTER_TABLE65 : (SPW Offset: 0x184) (R/W 32) SpW Router Table (router_table_nb = 32) 65 -------- */
#define SPW_ROUTER_TABLE65_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE65) Address Position */
#define SPW_ROUTER_TABLE65_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE65_ADDR_Pos)     /**< (SPW_ROUTER_TABLE65) Address Mask */
#define SPW_ROUTER_TABLE65_ADDR(value)        (SPW_ROUTER_TABLE65_ADDR_Msk & ((value) << SPW_ROUTER_TABLE65_ADDR_Pos))
#define SPW_ROUTER_TABLE65_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE65) Delete Header Byte Position */
#define SPW_ROUTER_TABLE65_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE65_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE65) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE65_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE65) Register Mask  */


/* -------- SPW_ROUTER_TABLE66 : (SPW Offset: 0x188) (R/W 32) SpW Router Table (router_table_nb = 32) 66 -------- */
#define SPW_ROUTER_TABLE66_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE66) Address Position */
#define SPW_ROUTER_TABLE66_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE66_ADDR_Pos)     /**< (SPW_ROUTER_TABLE66) Address Mask */
#define SPW_ROUTER_TABLE66_ADDR(value)        (SPW_ROUTER_TABLE66_ADDR_Msk & ((value) << SPW_ROUTER_TABLE66_ADDR_Pos))
#define SPW_ROUTER_TABLE66_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE66) Delete Header Byte Position */
#define SPW_ROUTER_TABLE66_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE66_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE66) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE66_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE66) Register Mask  */


/* -------- SPW_ROUTER_TABLE67 : (SPW Offset: 0x18C) (R/W 32) SpW Router Table (router_table_nb = 32) 67 -------- */
#define SPW_ROUTER_TABLE67_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE67) Address Position */
#define SPW_ROUTER_TABLE67_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE67_ADDR_Pos)     /**< (SPW_ROUTER_TABLE67) Address Mask */
#define SPW_ROUTER_TABLE67_ADDR(value)        (SPW_ROUTER_TABLE67_ADDR_Msk & ((value) << SPW_ROUTER_TABLE67_ADDR_Pos))
#define SPW_ROUTER_TABLE67_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE67) Delete Header Byte Position */
#define SPW_ROUTER_TABLE67_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE67_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE67) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE67_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE67) Register Mask  */


/* -------- SPW_ROUTER_TABLE68 : (SPW Offset: 0x190) (R/W 32) SpW Router Table (router_table_nb = 32) 68 -------- */
#define SPW_ROUTER_TABLE68_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE68) Address Position */
#define SPW_ROUTER_TABLE68_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE68_ADDR_Pos)     /**< (SPW_ROUTER_TABLE68) Address Mask */
#define SPW_ROUTER_TABLE68_ADDR(value)        (SPW_ROUTER_TABLE68_ADDR_Msk & ((value) << SPW_ROUTER_TABLE68_ADDR_Pos))
#define SPW_ROUTER_TABLE68_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE68) Delete Header Byte Position */
#define SPW_ROUTER_TABLE68_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE68_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE68) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE68_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE68) Register Mask  */


/* -------- SPW_ROUTER_TABLE69 : (SPW Offset: 0x194) (R/W 32) SpW Router Table (router_table_nb = 32) 69 -------- */
#define SPW_ROUTER_TABLE69_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE69) Address Position */
#define SPW_ROUTER_TABLE69_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE69_ADDR_Pos)     /**< (SPW_ROUTER_TABLE69) Address Mask */
#define SPW_ROUTER_TABLE69_ADDR(value)        (SPW_ROUTER_TABLE69_ADDR_Msk & ((value) << SPW_ROUTER_TABLE69_ADDR_Pos))
#define SPW_ROUTER_TABLE69_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE69) Delete Header Byte Position */
#define SPW_ROUTER_TABLE69_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE69_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE69) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE69_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE69) Register Mask  */


/* -------- SPW_ROUTER_TABLE70 : (SPW Offset: 0x198) (R/W 32) SpW Router Table (router_table_nb = 32) 70 -------- */
#define SPW_ROUTER_TABLE70_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE70) Address Position */
#define SPW_ROUTER_TABLE70_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE70_ADDR_Pos)     /**< (SPW_ROUTER_TABLE70) Address Mask */
#define SPW_ROUTER_TABLE70_ADDR(value)        (SPW_ROUTER_TABLE70_ADDR_Msk & ((value) << SPW_ROUTER_TABLE70_ADDR_Pos))
#define SPW_ROUTER_TABLE70_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE70) Delete Header Byte Position */
#define SPW_ROUTER_TABLE70_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE70_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE70) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE70_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE70) Register Mask  */


/* -------- SPW_ROUTER_TABLE71 : (SPW Offset: 0x19C) (R/W 32) SpW Router Table (router_table_nb = 32) 71 -------- */
#define SPW_ROUTER_TABLE71_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE71) Address Position */
#define SPW_ROUTER_TABLE71_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE71_ADDR_Pos)     /**< (SPW_ROUTER_TABLE71) Address Mask */
#define SPW_ROUTER_TABLE71_ADDR(value)        (SPW_ROUTER_TABLE71_ADDR_Msk & ((value) << SPW_ROUTER_TABLE71_ADDR_Pos))
#define SPW_ROUTER_TABLE71_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE71) Delete Header Byte Position */
#define SPW_ROUTER_TABLE71_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE71_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE71) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE71_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE71) Register Mask  */


/* -------- SPW_ROUTER_TABLE72 : (SPW Offset: 0x1A0) (R/W 32) SpW Router Table (router_table_nb = 32) 72 -------- */
#define SPW_ROUTER_TABLE72_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE72) Address Position */
#define SPW_ROUTER_TABLE72_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE72_ADDR_Pos)     /**< (SPW_ROUTER_TABLE72) Address Mask */
#define SPW_ROUTER_TABLE72_ADDR(value)        (SPW_ROUTER_TABLE72_ADDR_Msk & ((value) << SPW_ROUTER_TABLE72_ADDR_Pos))
#define SPW_ROUTER_TABLE72_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE72) Delete Header Byte Position */
#define SPW_ROUTER_TABLE72_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE72_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE72) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE72_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE72) Register Mask  */


/* -------- SPW_ROUTER_TABLE73 : (SPW Offset: 0x1A4) (R/W 32) SpW Router Table (router_table_nb = 32) 73 -------- */
#define SPW_ROUTER_TABLE73_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE73) Address Position */
#define SPW_ROUTER_TABLE73_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE73_ADDR_Pos)     /**< (SPW_ROUTER_TABLE73) Address Mask */
#define SPW_ROUTER_TABLE73_ADDR(value)        (SPW_ROUTER_TABLE73_ADDR_Msk & ((value) << SPW_ROUTER_TABLE73_ADDR_Pos))
#define SPW_ROUTER_TABLE73_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE73) Delete Header Byte Position */
#define SPW_ROUTER_TABLE73_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE73_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE73) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE73_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE73) Register Mask  */


/* -------- SPW_ROUTER_TABLE74 : (SPW Offset: 0x1A8) (R/W 32) SpW Router Table (router_table_nb = 32) 74 -------- */
#define SPW_ROUTER_TABLE74_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE74) Address Position */
#define SPW_ROUTER_TABLE74_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE74_ADDR_Pos)     /**< (SPW_ROUTER_TABLE74) Address Mask */
#define SPW_ROUTER_TABLE74_ADDR(value)        (SPW_ROUTER_TABLE74_ADDR_Msk & ((value) << SPW_ROUTER_TABLE74_ADDR_Pos))
#define SPW_ROUTER_TABLE74_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE74) Delete Header Byte Position */
#define SPW_ROUTER_TABLE74_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE74_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE74) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE74_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE74) Register Mask  */


/* -------- SPW_ROUTER_TABLE75 : (SPW Offset: 0x1AC) (R/W 32) SpW Router Table (router_table_nb = 32) 75 -------- */
#define SPW_ROUTER_TABLE75_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE75) Address Position */
#define SPW_ROUTER_TABLE75_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE75_ADDR_Pos)     /**< (SPW_ROUTER_TABLE75) Address Mask */
#define SPW_ROUTER_TABLE75_ADDR(value)        (SPW_ROUTER_TABLE75_ADDR_Msk & ((value) << SPW_ROUTER_TABLE75_ADDR_Pos))
#define SPW_ROUTER_TABLE75_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE75) Delete Header Byte Position */
#define SPW_ROUTER_TABLE75_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE75_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE75) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE75_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE75) Register Mask  */


/* -------- SPW_ROUTER_TABLE76 : (SPW Offset: 0x1B0) (R/W 32) SpW Router Table (router_table_nb = 32) 76 -------- */
#define SPW_ROUTER_TABLE76_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE76) Address Position */
#define SPW_ROUTER_TABLE76_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE76_ADDR_Pos)     /**< (SPW_ROUTER_TABLE76) Address Mask */
#define SPW_ROUTER_TABLE76_ADDR(value)        (SPW_ROUTER_TABLE76_ADDR_Msk & ((value) << SPW_ROUTER_TABLE76_ADDR_Pos))
#define SPW_ROUTER_TABLE76_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE76) Delete Header Byte Position */
#define SPW_ROUTER_TABLE76_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE76_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE76) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE76_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE76) Register Mask  */


/* -------- SPW_ROUTER_TABLE77 : (SPW Offset: 0x1B4) (R/W 32) SpW Router Table (router_table_nb = 32) 77 -------- */
#define SPW_ROUTER_TABLE77_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE77) Address Position */
#define SPW_ROUTER_TABLE77_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE77_ADDR_Pos)     /**< (SPW_ROUTER_TABLE77) Address Mask */
#define SPW_ROUTER_TABLE77_ADDR(value)        (SPW_ROUTER_TABLE77_ADDR_Msk & ((value) << SPW_ROUTER_TABLE77_ADDR_Pos))
#define SPW_ROUTER_TABLE77_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE77) Delete Header Byte Position */
#define SPW_ROUTER_TABLE77_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE77_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE77) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE77_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE77) Register Mask  */


/* -------- SPW_ROUTER_TABLE78 : (SPW Offset: 0x1B8) (R/W 32) SpW Router Table (router_table_nb = 32) 78 -------- */
#define SPW_ROUTER_TABLE78_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE78) Address Position */
#define SPW_ROUTER_TABLE78_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE78_ADDR_Pos)     /**< (SPW_ROUTER_TABLE78) Address Mask */
#define SPW_ROUTER_TABLE78_ADDR(value)        (SPW_ROUTER_TABLE78_ADDR_Msk & ((value) << SPW_ROUTER_TABLE78_ADDR_Pos))
#define SPW_ROUTER_TABLE78_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE78) Delete Header Byte Position */
#define SPW_ROUTER_TABLE78_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE78_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE78) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE78_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE78) Register Mask  */


/* -------- SPW_ROUTER_TABLE79 : (SPW Offset: 0x1BC) (R/W 32) SpW Router Table (router_table_nb = 32) 79 -------- */
#define SPW_ROUTER_TABLE79_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE79) Address Position */
#define SPW_ROUTER_TABLE79_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE79_ADDR_Pos)     /**< (SPW_ROUTER_TABLE79) Address Mask */
#define SPW_ROUTER_TABLE79_ADDR(value)        (SPW_ROUTER_TABLE79_ADDR_Msk & ((value) << SPW_ROUTER_TABLE79_ADDR_Pos))
#define SPW_ROUTER_TABLE79_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE79) Delete Header Byte Position */
#define SPW_ROUTER_TABLE79_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE79_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE79) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE79_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE79) Register Mask  */


/* -------- SPW_ROUTER_TABLE80 : (SPW Offset: 0x1C0) (R/W 32) SpW Router Table (router_table_nb = 32) 80 -------- */
#define SPW_ROUTER_TABLE80_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE80) Address Position */
#define SPW_ROUTER_TABLE80_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE80_ADDR_Pos)     /**< (SPW_ROUTER_TABLE80) Address Mask */
#define SPW_ROUTER_TABLE80_ADDR(value)        (SPW_ROUTER_TABLE80_ADDR_Msk & ((value) << SPW_ROUTER_TABLE80_ADDR_Pos))
#define SPW_ROUTER_TABLE80_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE80) Delete Header Byte Position */
#define SPW_ROUTER_TABLE80_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE80_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE80) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE80_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE80) Register Mask  */


/* -------- SPW_ROUTER_TABLE81 : (SPW Offset: 0x1C4) (R/W 32) SpW Router Table (router_table_nb = 32) 81 -------- */
#define SPW_ROUTER_TABLE81_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE81) Address Position */
#define SPW_ROUTER_TABLE81_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE81_ADDR_Pos)     /**< (SPW_ROUTER_TABLE81) Address Mask */
#define SPW_ROUTER_TABLE81_ADDR(value)        (SPW_ROUTER_TABLE81_ADDR_Msk & ((value) << SPW_ROUTER_TABLE81_ADDR_Pos))
#define SPW_ROUTER_TABLE81_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE81) Delete Header Byte Position */
#define SPW_ROUTER_TABLE81_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE81_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE81) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE81_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE81) Register Mask  */


/* -------- SPW_ROUTER_TABLE82 : (SPW Offset: 0x1C8) (R/W 32) SpW Router Table (router_table_nb = 32) 82 -------- */
#define SPW_ROUTER_TABLE82_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE82) Address Position */
#define SPW_ROUTER_TABLE82_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE82_ADDR_Pos)     /**< (SPW_ROUTER_TABLE82) Address Mask */
#define SPW_ROUTER_TABLE82_ADDR(value)        (SPW_ROUTER_TABLE82_ADDR_Msk & ((value) << SPW_ROUTER_TABLE82_ADDR_Pos))
#define SPW_ROUTER_TABLE82_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE82) Delete Header Byte Position */
#define SPW_ROUTER_TABLE82_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE82_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE82) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE82_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE82) Register Mask  */


/* -------- SPW_ROUTER_TABLE83 : (SPW Offset: 0x1CC) (R/W 32) SpW Router Table (router_table_nb = 32) 83 -------- */
#define SPW_ROUTER_TABLE83_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE83) Address Position */
#define SPW_ROUTER_TABLE83_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE83_ADDR_Pos)     /**< (SPW_ROUTER_TABLE83) Address Mask */
#define SPW_ROUTER_TABLE83_ADDR(value)        (SPW_ROUTER_TABLE83_ADDR_Msk & ((value) << SPW_ROUTER_TABLE83_ADDR_Pos))
#define SPW_ROUTER_TABLE83_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE83) Delete Header Byte Position */
#define SPW_ROUTER_TABLE83_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE83_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE83) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE83_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE83) Register Mask  */


/* -------- SPW_ROUTER_TABLE84 : (SPW Offset: 0x1D0) (R/W 32) SpW Router Table (router_table_nb = 32) 84 -------- */
#define SPW_ROUTER_TABLE84_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE84) Address Position */
#define SPW_ROUTER_TABLE84_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE84_ADDR_Pos)     /**< (SPW_ROUTER_TABLE84) Address Mask */
#define SPW_ROUTER_TABLE84_ADDR(value)        (SPW_ROUTER_TABLE84_ADDR_Msk & ((value) << SPW_ROUTER_TABLE84_ADDR_Pos))
#define SPW_ROUTER_TABLE84_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE84) Delete Header Byte Position */
#define SPW_ROUTER_TABLE84_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE84_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE84) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE84_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE84) Register Mask  */


/* -------- SPW_ROUTER_TABLE85 : (SPW Offset: 0x1D4) (R/W 32) SpW Router Table (router_table_nb = 32) 85 -------- */
#define SPW_ROUTER_TABLE85_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE85) Address Position */
#define SPW_ROUTER_TABLE85_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE85_ADDR_Pos)     /**< (SPW_ROUTER_TABLE85) Address Mask */
#define SPW_ROUTER_TABLE85_ADDR(value)        (SPW_ROUTER_TABLE85_ADDR_Msk & ((value) << SPW_ROUTER_TABLE85_ADDR_Pos))
#define SPW_ROUTER_TABLE85_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE85) Delete Header Byte Position */
#define SPW_ROUTER_TABLE85_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE85_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE85) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE85_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE85) Register Mask  */


/* -------- SPW_ROUTER_TABLE86 : (SPW Offset: 0x1D8) (R/W 32) SpW Router Table (router_table_nb = 32) 86 -------- */
#define SPW_ROUTER_TABLE86_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE86) Address Position */
#define SPW_ROUTER_TABLE86_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE86_ADDR_Pos)     /**< (SPW_ROUTER_TABLE86) Address Mask */
#define SPW_ROUTER_TABLE86_ADDR(value)        (SPW_ROUTER_TABLE86_ADDR_Msk & ((value) << SPW_ROUTER_TABLE86_ADDR_Pos))
#define SPW_ROUTER_TABLE86_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE86) Delete Header Byte Position */
#define SPW_ROUTER_TABLE86_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE86_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE86) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE86_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE86) Register Mask  */


/* -------- SPW_ROUTER_TABLE87 : (SPW Offset: 0x1DC) (R/W 32) SpW Router Table (router_table_nb = 32) 87 -------- */
#define SPW_ROUTER_TABLE87_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE87) Address Position */
#define SPW_ROUTER_TABLE87_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE87_ADDR_Pos)     /**< (SPW_ROUTER_TABLE87) Address Mask */
#define SPW_ROUTER_TABLE87_ADDR(value)        (SPW_ROUTER_TABLE87_ADDR_Msk & ((value) << SPW_ROUTER_TABLE87_ADDR_Pos))
#define SPW_ROUTER_TABLE87_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE87) Delete Header Byte Position */
#define SPW_ROUTER_TABLE87_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE87_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE87) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE87_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE87) Register Mask  */


/* -------- SPW_ROUTER_TABLE88 : (SPW Offset: 0x1E0) (R/W 32) SpW Router Table (router_table_nb = 32) 88 -------- */
#define SPW_ROUTER_TABLE88_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE88) Address Position */
#define SPW_ROUTER_TABLE88_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE88_ADDR_Pos)     /**< (SPW_ROUTER_TABLE88) Address Mask */
#define SPW_ROUTER_TABLE88_ADDR(value)        (SPW_ROUTER_TABLE88_ADDR_Msk & ((value) << SPW_ROUTER_TABLE88_ADDR_Pos))
#define SPW_ROUTER_TABLE88_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE88) Delete Header Byte Position */
#define SPW_ROUTER_TABLE88_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE88_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE88) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE88_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE88) Register Mask  */


/* -------- SPW_ROUTER_TABLE89 : (SPW Offset: 0x1E4) (R/W 32) SpW Router Table (router_table_nb = 32) 89 -------- */
#define SPW_ROUTER_TABLE89_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE89) Address Position */
#define SPW_ROUTER_TABLE89_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE89_ADDR_Pos)     /**< (SPW_ROUTER_TABLE89) Address Mask */
#define SPW_ROUTER_TABLE89_ADDR(value)        (SPW_ROUTER_TABLE89_ADDR_Msk & ((value) << SPW_ROUTER_TABLE89_ADDR_Pos))
#define SPW_ROUTER_TABLE89_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE89) Delete Header Byte Position */
#define SPW_ROUTER_TABLE89_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE89_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE89) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE89_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE89) Register Mask  */


/* -------- SPW_ROUTER_TABLE90 : (SPW Offset: 0x1E8) (R/W 32) SpW Router Table (router_table_nb = 32) 90 -------- */
#define SPW_ROUTER_TABLE90_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE90) Address Position */
#define SPW_ROUTER_TABLE90_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE90_ADDR_Pos)     /**< (SPW_ROUTER_TABLE90) Address Mask */
#define SPW_ROUTER_TABLE90_ADDR(value)        (SPW_ROUTER_TABLE90_ADDR_Msk & ((value) << SPW_ROUTER_TABLE90_ADDR_Pos))
#define SPW_ROUTER_TABLE90_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE90) Delete Header Byte Position */
#define SPW_ROUTER_TABLE90_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE90_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE90) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE90_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE90) Register Mask  */


/* -------- SPW_ROUTER_TABLE91 : (SPW Offset: 0x1EC) (R/W 32) SpW Router Table (router_table_nb = 32) 91 -------- */
#define SPW_ROUTER_TABLE91_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE91) Address Position */
#define SPW_ROUTER_TABLE91_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE91_ADDR_Pos)     /**< (SPW_ROUTER_TABLE91) Address Mask */
#define SPW_ROUTER_TABLE91_ADDR(value)        (SPW_ROUTER_TABLE91_ADDR_Msk & ((value) << SPW_ROUTER_TABLE91_ADDR_Pos))
#define SPW_ROUTER_TABLE91_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE91) Delete Header Byte Position */
#define SPW_ROUTER_TABLE91_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE91_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE91) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE91_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE91) Register Mask  */


/* -------- SPW_ROUTER_TABLE92 : (SPW Offset: 0x1F0) (R/W 32) SpW Router Table (router_table_nb = 32) 92 -------- */
#define SPW_ROUTER_TABLE92_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE92) Address Position */
#define SPW_ROUTER_TABLE92_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE92_ADDR_Pos)     /**< (SPW_ROUTER_TABLE92) Address Mask */
#define SPW_ROUTER_TABLE92_ADDR(value)        (SPW_ROUTER_TABLE92_ADDR_Msk & ((value) << SPW_ROUTER_TABLE92_ADDR_Pos))
#define SPW_ROUTER_TABLE92_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE92) Delete Header Byte Position */
#define SPW_ROUTER_TABLE92_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE92_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE92) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE92_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE92) Register Mask  */


/* -------- SPW_ROUTER_TABLE93 : (SPW Offset: 0x1F4) (R/W 32) SpW Router Table (router_table_nb = 32) 93 -------- */
#define SPW_ROUTER_TABLE93_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE93) Address Position */
#define SPW_ROUTER_TABLE93_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE93_ADDR_Pos)     /**< (SPW_ROUTER_TABLE93) Address Mask */
#define SPW_ROUTER_TABLE93_ADDR(value)        (SPW_ROUTER_TABLE93_ADDR_Msk & ((value) << SPW_ROUTER_TABLE93_ADDR_Pos))
#define SPW_ROUTER_TABLE93_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE93) Delete Header Byte Position */
#define SPW_ROUTER_TABLE93_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE93_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE93) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE93_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE93) Register Mask  */


/* -------- SPW_ROUTER_TABLE94 : (SPW Offset: 0x1F8) (R/W 32) SpW Router Table (router_table_nb = 32) 94 -------- */
#define SPW_ROUTER_TABLE94_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE94) Address Position */
#define SPW_ROUTER_TABLE94_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE94_ADDR_Pos)     /**< (SPW_ROUTER_TABLE94) Address Mask */
#define SPW_ROUTER_TABLE94_ADDR(value)        (SPW_ROUTER_TABLE94_ADDR_Msk & ((value) << SPW_ROUTER_TABLE94_ADDR_Pos))
#define SPW_ROUTER_TABLE94_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE94) Delete Header Byte Position */
#define SPW_ROUTER_TABLE94_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE94_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE94) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE94_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE94) Register Mask  */


/* -------- SPW_ROUTER_TABLE95 : (SPW Offset: 0x1FC) (R/W 32) SpW Router Table (router_table_nb = 32) 95 -------- */
#define SPW_ROUTER_TABLE95_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE95) Address Position */
#define SPW_ROUTER_TABLE95_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE95_ADDR_Pos)     /**< (SPW_ROUTER_TABLE95) Address Mask */
#define SPW_ROUTER_TABLE95_ADDR(value)        (SPW_ROUTER_TABLE95_ADDR_Msk & ((value) << SPW_ROUTER_TABLE95_ADDR_Pos))
#define SPW_ROUTER_TABLE95_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE95) Delete Header Byte Position */
#define SPW_ROUTER_TABLE95_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE95_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE95) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE95_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE95) Register Mask  */


/* -------- SPW_ROUTER_TABLE96 : (SPW Offset: 0x200) (R/W 32) SpW Router Table (router_table_nb = 32) 96 -------- */
#define SPW_ROUTER_TABLE96_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE96) Address Position */
#define SPW_ROUTER_TABLE96_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE96_ADDR_Pos)     /**< (SPW_ROUTER_TABLE96) Address Mask */
#define SPW_ROUTER_TABLE96_ADDR(value)        (SPW_ROUTER_TABLE96_ADDR_Msk & ((value) << SPW_ROUTER_TABLE96_ADDR_Pos))
#define SPW_ROUTER_TABLE96_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE96) Delete Header Byte Position */
#define SPW_ROUTER_TABLE96_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE96_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE96) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE96_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE96) Register Mask  */


/* -------- SPW_ROUTER_TABLE97 : (SPW Offset: 0x204) (R/W 32) SpW Router Table (router_table_nb = 32) 97 -------- */
#define SPW_ROUTER_TABLE97_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE97) Address Position */
#define SPW_ROUTER_TABLE97_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE97_ADDR_Pos)     /**< (SPW_ROUTER_TABLE97) Address Mask */
#define SPW_ROUTER_TABLE97_ADDR(value)        (SPW_ROUTER_TABLE97_ADDR_Msk & ((value) << SPW_ROUTER_TABLE97_ADDR_Pos))
#define SPW_ROUTER_TABLE97_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE97) Delete Header Byte Position */
#define SPW_ROUTER_TABLE97_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE97_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE97) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE97_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE97) Register Mask  */


/* -------- SPW_ROUTER_TABLE98 : (SPW Offset: 0x208) (R/W 32) SpW Router Table (router_table_nb = 32) 98 -------- */
#define SPW_ROUTER_TABLE98_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE98) Address Position */
#define SPW_ROUTER_TABLE98_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE98_ADDR_Pos)     /**< (SPW_ROUTER_TABLE98) Address Mask */
#define SPW_ROUTER_TABLE98_ADDR(value)        (SPW_ROUTER_TABLE98_ADDR_Msk & ((value) << SPW_ROUTER_TABLE98_ADDR_Pos))
#define SPW_ROUTER_TABLE98_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE98) Delete Header Byte Position */
#define SPW_ROUTER_TABLE98_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE98_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE98) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE98_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE98) Register Mask  */


/* -------- SPW_ROUTER_TABLE99 : (SPW Offset: 0x20C) (R/W 32) SpW Router Table (router_table_nb = 32) 99 -------- */
#define SPW_ROUTER_TABLE99_ADDR_Pos           _U_(0)                                         /**< (SPW_ROUTER_TABLE99) Address Position */
#define SPW_ROUTER_TABLE99_ADDR_Msk           (_U_(0x1F) << SPW_ROUTER_TABLE99_ADDR_Pos)     /**< (SPW_ROUTER_TABLE99) Address Mask */
#define SPW_ROUTER_TABLE99_ADDR(value)        (SPW_ROUTER_TABLE99_ADDR_Msk & ((value) << SPW_ROUTER_TABLE99_ADDR_Pos))
#define SPW_ROUTER_TABLE99_DELHEAD_Pos        _U_(8)                                         /**< (SPW_ROUTER_TABLE99) Delete Header Byte Position */
#define SPW_ROUTER_TABLE99_DELHEAD_Msk        (_U_(0x1) << SPW_ROUTER_TABLE99_DELHEAD_Pos)   /**< (SPW_ROUTER_TABLE99) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE99_Msk                _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE99) Register Mask  */


/* -------- SPW_ROUTER_TABLE100 : (SPW Offset: 0x210) (R/W 32) SpW Router Table (router_table_nb = 32) 100 -------- */
#define SPW_ROUTER_TABLE100_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE100) Address Position */
#define SPW_ROUTER_TABLE100_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE100_ADDR_Pos)    /**< (SPW_ROUTER_TABLE100) Address Mask */
#define SPW_ROUTER_TABLE100_ADDR(value)       (SPW_ROUTER_TABLE100_ADDR_Msk & ((value) << SPW_ROUTER_TABLE100_ADDR_Pos))
#define SPW_ROUTER_TABLE100_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE100) Delete Header Byte Position */
#define SPW_ROUTER_TABLE100_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE100_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE100) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE100_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE100) Register Mask  */


/* -------- SPW_ROUTER_TABLE101 : (SPW Offset: 0x214) (R/W 32) SpW Router Table (router_table_nb = 32) 101 -------- */
#define SPW_ROUTER_TABLE101_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE101) Address Position */
#define SPW_ROUTER_TABLE101_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE101_ADDR_Pos)    /**< (SPW_ROUTER_TABLE101) Address Mask */
#define SPW_ROUTER_TABLE101_ADDR(value)       (SPW_ROUTER_TABLE101_ADDR_Msk & ((value) << SPW_ROUTER_TABLE101_ADDR_Pos))
#define SPW_ROUTER_TABLE101_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE101) Delete Header Byte Position */
#define SPW_ROUTER_TABLE101_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE101_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE101) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE101_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE101) Register Mask  */


/* -------- SPW_ROUTER_TABLE102 : (SPW Offset: 0x218) (R/W 32) SpW Router Table (router_table_nb = 32) 102 -------- */
#define SPW_ROUTER_TABLE102_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE102) Address Position */
#define SPW_ROUTER_TABLE102_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE102_ADDR_Pos)    /**< (SPW_ROUTER_TABLE102) Address Mask */
#define SPW_ROUTER_TABLE102_ADDR(value)       (SPW_ROUTER_TABLE102_ADDR_Msk & ((value) << SPW_ROUTER_TABLE102_ADDR_Pos))
#define SPW_ROUTER_TABLE102_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE102) Delete Header Byte Position */
#define SPW_ROUTER_TABLE102_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE102_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE102) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE102_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE102) Register Mask  */


/* -------- SPW_ROUTER_TABLE103 : (SPW Offset: 0x21C) (R/W 32) SpW Router Table (router_table_nb = 32) 103 -------- */
#define SPW_ROUTER_TABLE103_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE103) Address Position */
#define SPW_ROUTER_TABLE103_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE103_ADDR_Pos)    /**< (SPW_ROUTER_TABLE103) Address Mask */
#define SPW_ROUTER_TABLE103_ADDR(value)       (SPW_ROUTER_TABLE103_ADDR_Msk & ((value) << SPW_ROUTER_TABLE103_ADDR_Pos))
#define SPW_ROUTER_TABLE103_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE103) Delete Header Byte Position */
#define SPW_ROUTER_TABLE103_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE103_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE103) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE103_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE103) Register Mask  */


/* -------- SPW_ROUTER_TABLE104 : (SPW Offset: 0x220) (R/W 32) SpW Router Table (router_table_nb = 32) 104 -------- */
#define SPW_ROUTER_TABLE104_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE104) Address Position */
#define SPW_ROUTER_TABLE104_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE104_ADDR_Pos)    /**< (SPW_ROUTER_TABLE104) Address Mask */
#define SPW_ROUTER_TABLE104_ADDR(value)       (SPW_ROUTER_TABLE104_ADDR_Msk & ((value) << SPW_ROUTER_TABLE104_ADDR_Pos))
#define SPW_ROUTER_TABLE104_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE104) Delete Header Byte Position */
#define SPW_ROUTER_TABLE104_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE104_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE104) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE104_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE104) Register Mask  */


/* -------- SPW_ROUTER_TABLE105 : (SPW Offset: 0x224) (R/W 32) SpW Router Table (router_table_nb = 32) 105 -------- */
#define SPW_ROUTER_TABLE105_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE105) Address Position */
#define SPW_ROUTER_TABLE105_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE105_ADDR_Pos)    /**< (SPW_ROUTER_TABLE105) Address Mask */
#define SPW_ROUTER_TABLE105_ADDR(value)       (SPW_ROUTER_TABLE105_ADDR_Msk & ((value) << SPW_ROUTER_TABLE105_ADDR_Pos))
#define SPW_ROUTER_TABLE105_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE105) Delete Header Byte Position */
#define SPW_ROUTER_TABLE105_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE105_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE105) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE105_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE105) Register Mask  */


/* -------- SPW_ROUTER_TABLE106 : (SPW Offset: 0x228) (R/W 32) SpW Router Table (router_table_nb = 32) 106 -------- */
#define SPW_ROUTER_TABLE106_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE106) Address Position */
#define SPW_ROUTER_TABLE106_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE106_ADDR_Pos)    /**< (SPW_ROUTER_TABLE106) Address Mask */
#define SPW_ROUTER_TABLE106_ADDR(value)       (SPW_ROUTER_TABLE106_ADDR_Msk & ((value) << SPW_ROUTER_TABLE106_ADDR_Pos))
#define SPW_ROUTER_TABLE106_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE106) Delete Header Byte Position */
#define SPW_ROUTER_TABLE106_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE106_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE106) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE106_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE106) Register Mask  */


/* -------- SPW_ROUTER_TABLE107 : (SPW Offset: 0x22C) (R/W 32) SpW Router Table (router_table_nb = 32) 107 -------- */
#define SPW_ROUTER_TABLE107_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE107) Address Position */
#define SPW_ROUTER_TABLE107_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE107_ADDR_Pos)    /**< (SPW_ROUTER_TABLE107) Address Mask */
#define SPW_ROUTER_TABLE107_ADDR(value)       (SPW_ROUTER_TABLE107_ADDR_Msk & ((value) << SPW_ROUTER_TABLE107_ADDR_Pos))
#define SPW_ROUTER_TABLE107_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE107) Delete Header Byte Position */
#define SPW_ROUTER_TABLE107_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE107_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE107) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE107_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE107) Register Mask  */


/* -------- SPW_ROUTER_TABLE108 : (SPW Offset: 0x230) (R/W 32) SpW Router Table (router_table_nb = 32) 108 -------- */
#define SPW_ROUTER_TABLE108_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE108) Address Position */
#define SPW_ROUTER_TABLE108_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE108_ADDR_Pos)    /**< (SPW_ROUTER_TABLE108) Address Mask */
#define SPW_ROUTER_TABLE108_ADDR(value)       (SPW_ROUTER_TABLE108_ADDR_Msk & ((value) << SPW_ROUTER_TABLE108_ADDR_Pos))
#define SPW_ROUTER_TABLE108_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE108) Delete Header Byte Position */
#define SPW_ROUTER_TABLE108_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE108_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE108) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE108_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE108) Register Mask  */


/* -------- SPW_ROUTER_TABLE109 : (SPW Offset: 0x234) (R/W 32) SpW Router Table (router_table_nb = 32) 109 -------- */
#define SPW_ROUTER_TABLE109_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE109) Address Position */
#define SPW_ROUTER_TABLE109_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE109_ADDR_Pos)    /**< (SPW_ROUTER_TABLE109) Address Mask */
#define SPW_ROUTER_TABLE109_ADDR(value)       (SPW_ROUTER_TABLE109_ADDR_Msk & ((value) << SPW_ROUTER_TABLE109_ADDR_Pos))
#define SPW_ROUTER_TABLE109_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE109) Delete Header Byte Position */
#define SPW_ROUTER_TABLE109_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE109_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE109) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE109_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE109) Register Mask  */


/* -------- SPW_ROUTER_TABLE110 : (SPW Offset: 0x238) (R/W 32) SpW Router Table (router_table_nb = 32) 110 -------- */
#define SPW_ROUTER_TABLE110_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE110) Address Position */
#define SPW_ROUTER_TABLE110_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE110_ADDR_Pos)    /**< (SPW_ROUTER_TABLE110) Address Mask */
#define SPW_ROUTER_TABLE110_ADDR(value)       (SPW_ROUTER_TABLE110_ADDR_Msk & ((value) << SPW_ROUTER_TABLE110_ADDR_Pos))
#define SPW_ROUTER_TABLE110_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE110) Delete Header Byte Position */
#define SPW_ROUTER_TABLE110_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE110_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE110) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE110_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE110) Register Mask  */


/* -------- SPW_ROUTER_TABLE111 : (SPW Offset: 0x23C) (R/W 32) SpW Router Table (router_table_nb = 32) 111 -------- */
#define SPW_ROUTER_TABLE111_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE111) Address Position */
#define SPW_ROUTER_TABLE111_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE111_ADDR_Pos)    /**< (SPW_ROUTER_TABLE111) Address Mask */
#define SPW_ROUTER_TABLE111_ADDR(value)       (SPW_ROUTER_TABLE111_ADDR_Msk & ((value) << SPW_ROUTER_TABLE111_ADDR_Pos))
#define SPW_ROUTER_TABLE111_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE111) Delete Header Byte Position */
#define SPW_ROUTER_TABLE111_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE111_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE111) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE111_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE111) Register Mask  */


/* -------- SPW_ROUTER_TABLE112 : (SPW Offset: 0x240) (R/W 32) SpW Router Table (router_table_nb = 32) 112 -------- */
#define SPW_ROUTER_TABLE112_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE112) Address Position */
#define SPW_ROUTER_TABLE112_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE112_ADDR_Pos)    /**< (SPW_ROUTER_TABLE112) Address Mask */
#define SPW_ROUTER_TABLE112_ADDR(value)       (SPW_ROUTER_TABLE112_ADDR_Msk & ((value) << SPW_ROUTER_TABLE112_ADDR_Pos))
#define SPW_ROUTER_TABLE112_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE112) Delete Header Byte Position */
#define SPW_ROUTER_TABLE112_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE112_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE112) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE112_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE112) Register Mask  */


/* -------- SPW_ROUTER_TABLE113 : (SPW Offset: 0x244) (R/W 32) SpW Router Table (router_table_nb = 32) 113 -------- */
#define SPW_ROUTER_TABLE113_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE113) Address Position */
#define SPW_ROUTER_TABLE113_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE113_ADDR_Pos)    /**< (SPW_ROUTER_TABLE113) Address Mask */
#define SPW_ROUTER_TABLE113_ADDR(value)       (SPW_ROUTER_TABLE113_ADDR_Msk & ((value) << SPW_ROUTER_TABLE113_ADDR_Pos))
#define SPW_ROUTER_TABLE113_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE113) Delete Header Byte Position */
#define SPW_ROUTER_TABLE113_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE113_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE113) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE113_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE113) Register Mask  */


/* -------- SPW_ROUTER_TABLE114 : (SPW Offset: 0x248) (R/W 32) SpW Router Table (router_table_nb = 32) 114 -------- */
#define SPW_ROUTER_TABLE114_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE114) Address Position */
#define SPW_ROUTER_TABLE114_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE114_ADDR_Pos)    /**< (SPW_ROUTER_TABLE114) Address Mask */
#define SPW_ROUTER_TABLE114_ADDR(value)       (SPW_ROUTER_TABLE114_ADDR_Msk & ((value) << SPW_ROUTER_TABLE114_ADDR_Pos))
#define SPW_ROUTER_TABLE114_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE114) Delete Header Byte Position */
#define SPW_ROUTER_TABLE114_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE114_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE114) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE114_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE114) Register Mask  */


/* -------- SPW_ROUTER_TABLE115 : (SPW Offset: 0x24C) (R/W 32) SpW Router Table (router_table_nb = 32) 115 -------- */
#define SPW_ROUTER_TABLE115_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE115) Address Position */
#define SPW_ROUTER_TABLE115_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE115_ADDR_Pos)    /**< (SPW_ROUTER_TABLE115) Address Mask */
#define SPW_ROUTER_TABLE115_ADDR(value)       (SPW_ROUTER_TABLE115_ADDR_Msk & ((value) << SPW_ROUTER_TABLE115_ADDR_Pos))
#define SPW_ROUTER_TABLE115_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE115) Delete Header Byte Position */
#define SPW_ROUTER_TABLE115_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE115_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE115) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE115_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE115) Register Mask  */


/* -------- SPW_ROUTER_TABLE116 : (SPW Offset: 0x250) (R/W 32) SpW Router Table (router_table_nb = 32) 116 -------- */
#define SPW_ROUTER_TABLE116_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE116) Address Position */
#define SPW_ROUTER_TABLE116_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE116_ADDR_Pos)    /**< (SPW_ROUTER_TABLE116) Address Mask */
#define SPW_ROUTER_TABLE116_ADDR(value)       (SPW_ROUTER_TABLE116_ADDR_Msk & ((value) << SPW_ROUTER_TABLE116_ADDR_Pos))
#define SPW_ROUTER_TABLE116_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE116) Delete Header Byte Position */
#define SPW_ROUTER_TABLE116_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE116_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE116) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE116_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE116) Register Mask  */


/* -------- SPW_ROUTER_TABLE117 : (SPW Offset: 0x254) (R/W 32) SpW Router Table (router_table_nb = 32) 117 -------- */
#define SPW_ROUTER_TABLE117_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE117) Address Position */
#define SPW_ROUTER_TABLE117_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE117_ADDR_Pos)    /**< (SPW_ROUTER_TABLE117) Address Mask */
#define SPW_ROUTER_TABLE117_ADDR(value)       (SPW_ROUTER_TABLE117_ADDR_Msk & ((value) << SPW_ROUTER_TABLE117_ADDR_Pos))
#define SPW_ROUTER_TABLE117_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE117) Delete Header Byte Position */
#define SPW_ROUTER_TABLE117_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE117_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE117) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE117_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE117) Register Mask  */


/* -------- SPW_ROUTER_TABLE118 : (SPW Offset: 0x258) (R/W 32) SpW Router Table (router_table_nb = 32) 118 -------- */
#define SPW_ROUTER_TABLE118_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE118) Address Position */
#define SPW_ROUTER_TABLE118_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE118_ADDR_Pos)    /**< (SPW_ROUTER_TABLE118) Address Mask */
#define SPW_ROUTER_TABLE118_ADDR(value)       (SPW_ROUTER_TABLE118_ADDR_Msk & ((value) << SPW_ROUTER_TABLE118_ADDR_Pos))
#define SPW_ROUTER_TABLE118_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE118) Delete Header Byte Position */
#define SPW_ROUTER_TABLE118_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE118_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE118) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE118_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE118) Register Mask  */


/* -------- SPW_ROUTER_TABLE119 : (SPW Offset: 0x25C) (R/W 32) SpW Router Table (router_table_nb = 32) 119 -------- */
#define SPW_ROUTER_TABLE119_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE119) Address Position */
#define SPW_ROUTER_TABLE119_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE119_ADDR_Pos)    /**< (SPW_ROUTER_TABLE119) Address Mask */
#define SPW_ROUTER_TABLE119_ADDR(value)       (SPW_ROUTER_TABLE119_ADDR_Msk & ((value) << SPW_ROUTER_TABLE119_ADDR_Pos))
#define SPW_ROUTER_TABLE119_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE119) Delete Header Byte Position */
#define SPW_ROUTER_TABLE119_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE119_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE119) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE119_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE119) Register Mask  */


/* -------- SPW_ROUTER_TABLE120 : (SPW Offset: 0x260) (R/W 32) SpW Router Table (router_table_nb = 32) 120 -------- */
#define SPW_ROUTER_TABLE120_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE120) Address Position */
#define SPW_ROUTER_TABLE120_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE120_ADDR_Pos)    /**< (SPW_ROUTER_TABLE120) Address Mask */
#define SPW_ROUTER_TABLE120_ADDR(value)       (SPW_ROUTER_TABLE120_ADDR_Msk & ((value) << SPW_ROUTER_TABLE120_ADDR_Pos))
#define SPW_ROUTER_TABLE120_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE120) Delete Header Byte Position */
#define SPW_ROUTER_TABLE120_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE120_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE120) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE120_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE120) Register Mask  */


/* -------- SPW_ROUTER_TABLE121 : (SPW Offset: 0x264) (R/W 32) SpW Router Table (router_table_nb = 32) 121 -------- */
#define SPW_ROUTER_TABLE121_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE121) Address Position */
#define SPW_ROUTER_TABLE121_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE121_ADDR_Pos)    /**< (SPW_ROUTER_TABLE121) Address Mask */
#define SPW_ROUTER_TABLE121_ADDR(value)       (SPW_ROUTER_TABLE121_ADDR_Msk & ((value) << SPW_ROUTER_TABLE121_ADDR_Pos))
#define SPW_ROUTER_TABLE121_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE121) Delete Header Byte Position */
#define SPW_ROUTER_TABLE121_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE121_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE121) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE121_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE121) Register Mask  */


/* -------- SPW_ROUTER_TABLE122 : (SPW Offset: 0x268) (R/W 32) SpW Router Table (router_table_nb = 32) 122 -------- */
#define SPW_ROUTER_TABLE122_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE122) Address Position */
#define SPW_ROUTER_TABLE122_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE122_ADDR_Pos)    /**< (SPW_ROUTER_TABLE122) Address Mask */
#define SPW_ROUTER_TABLE122_ADDR(value)       (SPW_ROUTER_TABLE122_ADDR_Msk & ((value) << SPW_ROUTER_TABLE122_ADDR_Pos))
#define SPW_ROUTER_TABLE122_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE122) Delete Header Byte Position */
#define SPW_ROUTER_TABLE122_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE122_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE122) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE122_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE122) Register Mask  */


/* -------- SPW_ROUTER_TABLE123 : (SPW Offset: 0x26C) (R/W 32) SpW Router Table (router_table_nb = 32) 123 -------- */
#define SPW_ROUTER_TABLE123_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE123) Address Position */
#define SPW_ROUTER_TABLE123_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE123_ADDR_Pos)    /**< (SPW_ROUTER_TABLE123) Address Mask */
#define SPW_ROUTER_TABLE123_ADDR(value)       (SPW_ROUTER_TABLE123_ADDR_Msk & ((value) << SPW_ROUTER_TABLE123_ADDR_Pos))
#define SPW_ROUTER_TABLE123_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE123) Delete Header Byte Position */
#define SPW_ROUTER_TABLE123_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE123_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE123) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE123_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE123) Register Mask  */


/* -------- SPW_ROUTER_TABLE124 : (SPW Offset: 0x270) (R/W 32) SpW Router Table (router_table_nb = 32) 124 -------- */
#define SPW_ROUTER_TABLE124_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE124) Address Position */
#define SPW_ROUTER_TABLE124_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE124_ADDR_Pos)    /**< (SPW_ROUTER_TABLE124) Address Mask */
#define SPW_ROUTER_TABLE124_ADDR(value)       (SPW_ROUTER_TABLE124_ADDR_Msk & ((value) << SPW_ROUTER_TABLE124_ADDR_Pos))
#define SPW_ROUTER_TABLE124_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE124) Delete Header Byte Position */
#define SPW_ROUTER_TABLE124_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE124_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE124) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE124_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE124) Register Mask  */


/* -------- SPW_ROUTER_TABLE125 : (SPW Offset: 0x274) (R/W 32) SpW Router Table (router_table_nb = 32) 125 -------- */
#define SPW_ROUTER_TABLE125_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE125) Address Position */
#define SPW_ROUTER_TABLE125_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE125_ADDR_Pos)    /**< (SPW_ROUTER_TABLE125) Address Mask */
#define SPW_ROUTER_TABLE125_ADDR(value)       (SPW_ROUTER_TABLE125_ADDR_Msk & ((value) << SPW_ROUTER_TABLE125_ADDR_Pos))
#define SPW_ROUTER_TABLE125_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE125) Delete Header Byte Position */
#define SPW_ROUTER_TABLE125_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE125_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE125) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE125_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE125) Register Mask  */


/* -------- SPW_ROUTER_TABLE126 : (SPW Offset: 0x278) (R/W 32) SpW Router Table (router_table_nb = 32) 126 -------- */
#define SPW_ROUTER_TABLE126_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE126) Address Position */
#define SPW_ROUTER_TABLE126_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE126_ADDR_Pos)    /**< (SPW_ROUTER_TABLE126) Address Mask */
#define SPW_ROUTER_TABLE126_ADDR(value)       (SPW_ROUTER_TABLE126_ADDR_Msk & ((value) << SPW_ROUTER_TABLE126_ADDR_Pos))
#define SPW_ROUTER_TABLE126_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE126) Delete Header Byte Position */
#define SPW_ROUTER_TABLE126_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE126_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE126) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE126_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE126) Register Mask  */


/* -------- SPW_ROUTER_TABLE127 : (SPW Offset: 0x27C) (R/W 32) SpW Router Table (router_table_nb = 32) 127 -------- */
#define SPW_ROUTER_TABLE127_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE127) Address Position */
#define SPW_ROUTER_TABLE127_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE127_ADDR_Pos)    /**< (SPW_ROUTER_TABLE127) Address Mask */
#define SPW_ROUTER_TABLE127_ADDR(value)       (SPW_ROUTER_TABLE127_ADDR_Msk & ((value) << SPW_ROUTER_TABLE127_ADDR_Pos))
#define SPW_ROUTER_TABLE127_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE127) Delete Header Byte Position */
#define SPW_ROUTER_TABLE127_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE127_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE127) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE127_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE127) Register Mask  */


/* -------- SPW_ROUTER_TABLE128 : (SPW Offset: 0x280) (R/W 32) SpW Router Table (router_table_nb = 32) 128 -------- */
#define SPW_ROUTER_TABLE128_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE128) Address Position */
#define SPW_ROUTER_TABLE128_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE128_ADDR_Pos)    /**< (SPW_ROUTER_TABLE128) Address Mask */
#define SPW_ROUTER_TABLE128_ADDR(value)       (SPW_ROUTER_TABLE128_ADDR_Msk & ((value) << SPW_ROUTER_TABLE128_ADDR_Pos))
#define SPW_ROUTER_TABLE128_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE128) Delete Header Byte Position */
#define SPW_ROUTER_TABLE128_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE128_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE128) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE128_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE128) Register Mask  */


/* -------- SPW_ROUTER_TABLE129 : (SPW Offset: 0x284) (R/W 32) SpW Router Table (router_table_nb = 32) 129 -------- */
#define SPW_ROUTER_TABLE129_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE129) Address Position */
#define SPW_ROUTER_TABLE129_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE129_ADDR_Pos)    /**< (SPW_ROUTER_TABLE129) Address Mask */
#define SPW_ROUTER_TABLE129_ADDR(value)       (SPW_ROUTER_TABLE129_ADDR_Msk & ((value) << SPW_ROUTER_TABLE129_ADDR_Pos))
#define SPW_ROUTER_TABLE129_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE129) Delete Header Byte Position */
#define SPW_ROUTER_TABLE129_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE129_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE129) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE129_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE129) Register Mask  */


/* -------- SPW_ROUTER_TABLE130 : (SPW Offset: 0x288) (R/W 32) SpW Router Table (router_table_nb = 32) 130 -------- */
#define SPW_ROUTER_TABLE130_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE130) Address Position */
#define SPW_ROUTER_TABLE130_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE130_ADDR_Pos)    /**< (SPW_ROUTER_TABLE130) Address Mask */
#define SPW_ROUTER_TABLE130_ADDR(value)       (SPW_ROUTER_TABLE130_ADDR_Msk & ((value) << SPW_ROUTER_TABLE130_ADDR_Pos))
#define SPW_ROUTER_TABLE130_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE130) Delete Header Byte Position */
#define SPW_ROUTER_TABLE130_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE130_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE130) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE130_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE130) Register Mask  */


/* -------- SPW_ROUTER_TABLE131 : (SPW Offset: 0x28C) (R/W 32) SpW Router Table (router_table_nb = 32) 131 -------- */
#define SPW_ROUTER_TABLE131_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE131) Address Position */
#define SPW_ROUTER_TABLE131_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE131_ADDR_Pos)    /**< (SPW_ROUTER_TABLE131) Address Mask */
#define SPW_ROUTER_TABLE131_ADDR(value)       (SPW_ROUTER_TABLE131_ADDR_Msk & ((value) << SPW_ROUTER_TABLE131_ADDR_Pos))
#define SPW_ROUTER_TABLE131_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE131) Delete Header Byte Position */
#define SPW_ROUTER_TABLE131_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE131_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE131) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE131_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE131) Register Mask  */


/* -------- SPW_ROUTER_TABLE132 : (SPW Offset: 0x290) (R/W 32) SpW Router Table (router_table_nb = 32) 132 -------- */
#define SPW_ROUTER_TABLE132_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE132) Address Position */
#define SPW_ROUTER_TABLE132_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE132_ADDR_Pos)    /**< (SPW_ROUTER_TABLE132) Address Mask */
#define SPW_ROUTER_TABLE132_ADDR(value)       (SPW_ROUTER_TABLE132_ADDR_Msk & ((value) << SPW_ROUTER_TABLE132_ADDR_Pos))
#define SPW_ROUTER_TABLE132_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE132) Delete Header Byte Position */
#define SPW_ROUTER_TABLE132_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE132_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE132) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE132_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE132) Register Mask  */


/* -------- SPW_ROUTER_TABLE133 : (SPW Offset: 0x294) (R/W 32) SpW Router Table (router_table_nb = 32) 133 -------- */
#define SPW_ROUTER_TABLE133_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE133) Address Position */
#define SPW_ROUTER_TABLE133_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE133_ADDR_Pos)    /**< (SPW_ROUTER_TABLE133) Address Mask */
#define SPW_ROUTER_TABLE133_ADDR(value)       (SPW_ROUTER_TABLE133_ADDR_Msk & ((value) << SPW_ROUTER_TABLE133_ADDR_Pos))
#define SPW_ROUTER_TABLE133_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE133) Delete Header Byte Position */
#define SPW_ROUTER_TABLE133_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE133_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE133) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE133_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE133) Register Mask  */


/* -------- SPW_ROUTER_TABLE134 : (SPW Offset: 0x298) (R/W 32) SpW Router Table (router_table_nb = 32) 134 -------- */
#define SPW_ROUTER_TABLE134_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE134) Address Position */
#define SPW_ROUTER_TABLE134_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE134_ADDR_Pos)    /**< (SPW_ROUTER_TABLE134) Address Mask */
#define SPW_ROUTER_TABLE134_ADDR(value)       (SPW_ROUTER_TABLE134_ADDR_Msk & ((value) << SPW_ROUTER_TABLE134_ADDR_Pos))
#define SPW_ROUTER_TABLE134_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE134) Delete Header Byte Position */
#define SPW_ROUTER_TABLE134_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE134_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE134) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE134_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE134) Register Mask  */


/* -------- SPW_ROUTER_TABLE135 : (SPW Offset: 0x29C) (R/W 32) SpW Router Table (router_table_nb = 32) 135 -------- */
#define SPW_ROUTER_TABLE135_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE135) Address Position */
#define SPW_ROUTER_TABLE135_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE135_ADDR_Pos)    /**< (SPW_ROUTER_TABLE135) Address Mask */
#define SPW_ROUTER_TABLE135_ADDR(value)       (SPW_ROUTER_TABLE135_ADDR_Msk & ((value) << SPW_ROUTER_TABLE135_ADDR_Pos))
#define SPW_ROUTER_TABLE135_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE135) Delete Header Byte Position */
#define SPW_ROUTER_TABLE135_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE135_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE135) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE135_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE135) Register Mask  */


/* -------- SPW_ROUTER_TABLE136 : (SPW Offset: 0x2A0) (R/W 32) SpW Router Table (router_table_nb = 32) 136 -------- */
#define SPW_ROUTER_TABLE136_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE136) Address Position */
#define SPW_ROUTER_TABLE136_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE136_ADDR_Pos)    /**< (SPW_ROUTER_TABLE136) Address Mask */
#define SPW_ROUTER_TABLE136_ADDR(value)       (SPW_ROUTER_TABLE136_ADDR_Msk & ((value) << SPW_ROUTER_TABLE136_ADDR_Pos))
#define SPW_ROUTER_TABLE136_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE136) Delete Header Byte Position */
#define SPW_ROUTER_TABLE136_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE136_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE136) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE136_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE136) Register Mask  */


/* -------- SPW_ROUTER_TABLE137 : (SPW Offset: 0x2A4) (R/W 32) SpW Router Table (router_table_nb = 32) 137 -------- */
#define SPW_ROUTER_TABLE137_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE137) Address Position */
#define SPW_ROUTER_TABLE137_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE137_ADDR_Pos)    /**< (SPW_ROUTER_TABLE137) Address Mask */
#define SPW_ROUTER_TABLE137_ADDR(value)       (SPW_ROUTER_TABLE137_ADDR_Msk & ((value) << SPW_ROUTER_TABLE137_ADDR_Pos))
#define SPW_ROUTER_TABLE137_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE137) Delete Header Byte Position */
#define SPW_ROUTER_TABLE137_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE137_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE137) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE137_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE137) Register Mask  */


/* -------- SPW_ROUTER_TABLE138 : (SPW Offset: 0x2A8) (R/W 32) SpW Router Table (router_table_nb = 32) 138 -------- */
#define SPW_ROUTER_TABLE138_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE138) Address Position */
#define SPW_ROUTER_TABLE138_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE138_ADDR_Pos)    /**< (SPW_ROUTER_TABLE138) Address Mask */
#define SPW_ROUTER_TABLE138_ADDR(value)       (SPW_ROUTER_TABLE138_ADDR_Msk & ((value) << SPW_ROUTER_TABLE138_ADDR_Pos))
#define SPW_ROUTER_TABLE138_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE138) Delete Header Byte Position */
#define SPW_ROUTER_TABLE138_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE138_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE138) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE138_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE138) Register Mask  */


/* -------- SPW_ROUTER_TABLE139 : (SPW Offset: 0x2AC) (R/W 32) SpW Router Table (router_table_nb = 32) 139 -------- */
#define SPW_ROUTER_TABLE139_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE139) Address Position */
#define SPW_ROUTER_TABLE139_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE139_ADDR_Pos)    /**< (SPW_ROUTER_TABLE139) Address Mask */
#define SPW_ROUTER_TABLE139_ADDR(value)       (SPW_ROUTER_TABLE139_ADDR_Msk & ((value) << SPW_ROUTER_TABLE139_ADDR_Pos))
#define SPW_ROUTER_TABLE139_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE139) Delete Header Byte Position */
#define SPW_ROUTER_TABLE139_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE139_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE139) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE139_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE139) Register Mask  */


/* -------- SPW_ROUTER_TABLE140 : (SPW Offset: 0x2B0) (R/W 32) SpW Router Table (router_table_nb = 32) 140 -------- */
#define SPW_ROUTER_TABLE140_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE140) Address Position */
#define SPW_ROUTER_TABLE140_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE140_ADDR_Pos)    /**< (SPW_ROUTER_TABLE140) Address Mask */
#define SPW_ROUTER_TABLE140_ADDR(value)       (SPW_ROUTER_TABLE140_ADDR_Msk & ((value) << SPW_ROUTER_TABLE140_ADDR_Pos))
#define SPW_ROUTER_TABLE140_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE140) Delete Header Byte Position */
#define SPW_ROUTER_TABLE140_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE140_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE140) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE140_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE140) Register Mask  */


/* -------- SPW_ROUTER_TABLE141 : (SPW Offset: 0x2B4) (R/W 32) SpW Router Table (router_table_nb = 32) 141 -------- */
#define SPW_ROUTER_TABLE141_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE141) Address Position */
#define SPW_ROUTER_TABLE141_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE141_ADDR_Pos)    /**< (SPW_ROUTER_TABLE141) Address Mask */
#define SPW_ROUTER_TABLE141_ADDR(value)       (SPW_ROUTER_TABLE141_ADDR_Msk & ((value) << SPW_ROUTER_TABLE141_ADDR_Pos))
#define SPW_ROUTER_TABLE141_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE141) Delete Header Byte Position */
#define SPW_ROUTER_TABLE141_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE141_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE141) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE141_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE141) Register Mask  */


/* -------- SPW_ROUTER_TABLE142 : (SPW Offset: 0x2B8) (R/W 32) SpW Router Table (router_table_nb = 32) 142 -------- */
#define SPW_ROUTER_TABLE142_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE142) Address Position */
#define SPW_ROUTER_TABLE142_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE142_ADDR_Pos)    /**< (SPW_ROUTER_TABLE142) Address Mask */
#define SPW_ROUTER_TABLE142_ADDR(value)       (SPW_ROUTER_TABLE142_ADDR_Msk & ((value) << SPW_ROUTER_TABLE142_ADDR_Pos))
#define SPW_ROUTER_TABLE142_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE142) Delete Header Byte Position */
#define SPW_ROUTER_TABLE142_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE142_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE142) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE142_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE142) Register Mask  */


/* -------- SPW_ROUTER_TABLE143 : (SPW Offset: 0x2BC) (R/W 32) SpW Router Table (router_table_nb = 32) 143 -------- */
#define SPW_ROUTER_TABLE143_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE143) Address Position */
#define SPW_ROUTER_TABLE143_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE143_ADDR_Pos)    /**< (SPW_ROUTER_TABLE143) Address Mask */
#define SPW_ROUTER_TABLE143_ADDR(value)       (SPW_ROUTER_TABLE143_ADDR_Msk & ((value) << SPW_ROUTER_TABLE143_ADDR_Pos))
#define SPW_ROUTER_TABLE143_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE143) Delete Header Byte Position */
#define SPW_ROUTER_TABLE143_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE143_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE143) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE143_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE143) Register Mask  */


/* -------- SPW_ROUTER_TABLE144 : (SPW Offset: 0x2C0) (R/W 32) SpW Router Table (router_table_nb = 32) 144 -------- */
#define SPW_ROUTER_TABLE144_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE144) Address Position */
#define SPW_ROUTER_TABLE144_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE144_ADDR_Pos)    /**< (SPW_ROUTER_TABLE144) Address Mask */
#define SPW_ROUTER_TABLE144_ADDR(value)       (SPW_ROUTER_TABLE144_ADDR_Msk & ((value) << SPW_ROUTER_TABLE144_ADDR_Pos))
#define SPW_ROUTER_TABLE144_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE144) Delete Header Byte Position */
#define SPW_ROUTER_TABLE144_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE144_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE144) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE144_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE144) Register Mask  */


/* -------- SPW_ROUTER_TABLE145 : (SPW Offset: 0x2C4) (R/W 32) SpW Router Table (router_table_nb = 32) 145 -------- */
#define SPW_ROUTER_TABLE145_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE145) Address Position */
#define SPW_ROUTER_TABLE145_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE145_ADDR_Pos)    /**< (SPW_ROUTER_TABLE145) Address Mask */
#define SPW_ROUTER_TABLE145_ADDR(value)       (SPW_ROUTER_TABLE145_ADDR_Msk & ((value) << SPW_ROUTER_TABLE145_ADDR_Pos))
#define SPW_ROUTER_TABLE145_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE145) Delete Header Byte Position */
#define SPW_ROUTER_TABLE145_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE145_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE145) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE145_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE145) Register Mask  */


/* -------- SPW_ROUTER_TABLE146 : (SPW Offset: 0x2C8) (R/W 32) SpW Router Table (router_table_nb = 32) 146 -------- */
#define SPW_ROUTER_TABLE146_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE146) Address Position */
#define SPW_ROUTER_TABLE146_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE146_ADDR_Pos)    /**< (SPW_ROUTER_TABLE146) Address Mask */
#define SPW_ROUTER_TABLE146_ADDR(value)       (SPW_ROUTER_TABLE146_ADDR_Msk & ((value) << SPW_ROUTER_TABLE146_ADDR_Pos))
#define SPW_ROUTER_TABLE146_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE146) Delete Header Byte Position */
#define SPW_ROUTER_TABLE146_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE146_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE146) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE146_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE146) Register Mask  */


/* -------- SPW_ROUTER_TABLE147 : (SPW Offset: 0x2CC) (R/W 32) SpW Router Table (router_table_nb = 32) 147 -------- */
#define SPW_ROUTER_TABLE147_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE147) Address Position */
#define SPW_ROUTER_TABLE147_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE147_ADDR_Pos)    /**< (SPW_ROUTER_TABLE147) Address Mask */
#define SPW_ROUTER_TABLE147_ADDR(value)       (SPW_ROUTER_TABLE147_ADDR_Msk & ((value) << SPW_ROUTER_TABLE147_ADDR_Pos))
#define SPW_ROUTER_TABLE147_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE147) Delete Header Byte Position */
#define SPW_ROUTER_TABLE147_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE147_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE147) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE147_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE147) Register Mask  */


/* -------- SPW_ROUTER_TABLE148 : (SPW Offset: 0x2D0) (R/W 32) SpW Router Table (router_table_nb = 32) 148 -------- */
#define SPW_ROUTER_TABLE148_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE148) Address Position */
#define SPW_ROUTER_TABLE148_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE148_ADDR_Pos)    /**< (SPW_ROUTER_TABLE148) Address Mask */
#define SPW_ROUTER_TABLE148_ADDR(value)       (SPW_ROUTER_TABLE148_ADDR_Msk & ((value) << SPW_ROUTER_TABLE148_ADDR_Pos))
#define SPW_ROUTER_TABLE148_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE148) Delete Header Byte Position */
#define SPW_ROUTER_TABLE148_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE148_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE148) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE148_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE148) Register Mask  */


/* -------- SPW_ROUTER_TABLE149 : (SPW Offset: 0x2D4) (R/W 32) SpW Router Table (router_table_nb = 32) 149 -------- */
#define SPW_ROUTER_TABLE149_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE149) Address Position */
#define SPW_ROUTER_TABLE149_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE149_ADDR_Pos)    /**< (SPW_ROUTER_TABLE149) Address Mask */
#define SPW_ROUTER_TABLE149_ADDR(value)       (SPW_ROUTER_TABLE149_ADDR_Msk & ((value) << SPW_ROUTER_TABLE149_ADDR_Pos))
#define SPW_ROUTER_TABLE149_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE149) Delete Header Byte Position */
#define SPW_ROUTER_TABLE149_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE149_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE149) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE149_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE149) Register Mask  */


/* -------- SPW_ROUTER_TABLE150 : (SPW Offset: 0x2D8) (R/W 32) SpW Router Table (router_table_nb = 32) 150 -------- */
#define SPW_ROUTER_TABLE150_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE150) Address Position */
#define SPW_ROUTER_TABLE150_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE150_ADDR_Pos)    /**< (SPW_ROUTER_TABLE150) Address Mask */
#define SPW_ROUTER_TABLE150_ADDR(value)       (SPW_ROUTER_TABLE150_ADDR_Msk & ((value) << SPW_ROUTER_TABLE150_ADDR_Pos))
#define SPW_ROUTER_TABLE150_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE150) Delete Header Byte Position */
#define SPW_ROUTER_TABLE150_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE150_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE150) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE150_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE150) Register Mask  */


/* -------- SPW_ROUTER_TABLE151 : (SPW Offset: 0x2DC) (R/W 32) SpW Router Table (router_table_nb = 32) 151 -------- */
#define SPW_ROUTER_TABLE151_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE151) Address Position */
#define SPW_ROUTER_TABLE151_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE151_ADDR_Pos)    /**< (SPW_ROUTER_TABLE151) Address Mask */
#define SPW_ROUTER_TABLE151_ADDR(value)       (SPW_ROUTER_TABLE151_ADDR_Msk & ((value) << SPW_ROUTER_TABLE151_ADDR_Pos))
#define SPW_ROUTER_TABLE151_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE151) Delete Header Byte Position */
#define SPW_ROUTER_TABLE151_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE151_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE151) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE151_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE151) Register Mask  */


/* -------- SPW_ROUTER_TABLE152 : (SPW Offset: 0x2E0) (R/W 32) SpW Router Table (router_table_nb = 32) 152 -------- */
#define SPW_ROUTER_TABLE152_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE152) Address Position */
#define SPW_ROUTER_TABLE152_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE152_ADDR_Pos)    /**< (SPW_ROUTER_TABLE152) Address Mask */
#define SPW_ROUTER_TABLE152_ADDR(value)       (SPW_ROUTER_TABLE152_ADDR_Msk & ((value) << SPW_ROUTER_TABLE152_ADDR_Pos))
#define SPW_ROUTER_TABLE152_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE152) Delete Header Byte Position */
#define SPW_ROUTER_TABLE152_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE152_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE152) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE152_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE152) Register Mask  */


/* -------- SPW_ROUTER_TABLE153 : (SPW Offset: 0x2E4) (R/W 32) SpW Router Table (router_table_nb = 32) 153 -------- */
#define SPW_ROUTER_TABLE153_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE153) Address Position */
#define SPW_ROUTER_TABLE153_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE153_ADDR_Pos)    /**< (SPW_ROUTER_TABLE153) Address Mask */
#define SPW_ROUTER_TABLE153_ADDR(value)       (SPW_ROUTER_TABLE153_ADDR_Msk & ((value) << SPW_ROUTER_TABLE153_ADDR_Pos))
#define SPW_ROUTER_TABLE153_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE153) Delete Header Byte Position */
#define SPW_ROUTER_TABLE153_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE153_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE153) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE153_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE153) Register Mask  */


/* -------- SPW_ROUTER_TABLE154 : (SPW Offset: 0x2E8) (R/W 32) SpW Router Table (router_table_nb = 32) 154 -------- */
#define SPW_ROUTER_TABLE154_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE154) Address Position */
#define SPW_ROUTER_TABLE154_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE154_ADDR_Pos)    /**< (SPW_ROUTER_TABLE154) Address Mask */
#define SPW_ROUTER_TABLE154_ADDR(value)       (SPW_ROUTER_TABLE154_ADDR_Msk & ((value) << SPW_ROUTER_TABLE154_ADDR_Pos))
#define SPW_ROUTER_TABLE154_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE154) Delete Header Byte Position */
#define SPW_ROUTER_TABLE154_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE154_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE154) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE154_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE154) Register Mask  */


/* -------- SPW_ROUTER_TABLE155 : (SPW Offset: 0x2EC) (R/W 32) SpW Router Table (router_table_nb = 32) 155 -------- */
#define SPW_ROUTER_TABLE155_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE155) Address Position */
#define SPW_ROUTER_TABLE155_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE155_ADDR_Pos)    /**< (SPW_ROUTER_TABLE155) Address Mask */
#define SPW_ROUTER_TABLE155_ADDR(value)       (SPW_ROUTER_TABLE155_ADDR_Msk & ((value) << SPW_ROUTER_TABLE155_ADDR_Pos))
#define SPW_ROUTER_TABLE155_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE155) Delete Header Byte Position */
#define SPW_ROUTER_TABLE155_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE155_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE155) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE155_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE155) Register Mask  */


/* -------- SPW_ROUTER_TABLE156 : (SPW Offset: 0x2F0) (R/W 32) SpW Router Table (router_table_nb = 32) 156 -------- */
#define SPW_ROUTER_TABLE156_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE156) Address Position */
#define SPW_ROUTER_TABLE156_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE156_ADDR_Pos)    /**< (SPW_ROUTER_TABLE156) Address Mask */
#define SPW_ROUTER_TABLE156_ADDR(value)       (SPW_ROUTER_TABLE156_ADDR_Msk & ((value) << SPW_ROUTER_TABLE156_ADDR_Pos))
#define SPW_ROUTER_TABLE156_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE156) Delete Header Byte Position */
#define SPW_ROUTER_TABLE156_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE156_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE156) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE156_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE156) Register Mask  */


/* -------- SPW_ROUTER_TABLE157 : (SPW Offset: 0x2F4) (R/W 32) SpW Router Table (router_table_nb = 32) 157 -------- */
#define SPW_ROUTER_TABLE157_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE157) Address Position */
#define SPW_ROUTER_TABLE157_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE157_ADDR_Pos)    /**< (SPW_ROUTER_TABLE157) Address Mask */
#define SPW_ROUTER_TABLE157_ADDR(value)       (SPW_ROUTER_TABLE157_ADDR_Msk & ((value) << SPW_ROUTER_TABLE157_ADDR_Pos))
#define SPW_ROUTER_TABLE157_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE157) Delete Header Byte Position */
#define SPW_ROUTER_TABLE157_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE157_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE157) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE157_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE157) Register Mask  */


/* -------- SPW_ROUTER_TABLE158 : (SPW Offset: 0x2F8) (R/W 32) SpW Router Table (router_table_nb = 32) 158 -------- */
#define SPW_ROUTER_TABLE158_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE158) Address Position */
#define SPW_ROUTER_TABLE158_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE158_ADDR_Pos)    /**< (SPW_ROUTER_TABLE158) Address Mask */
#define SPW_ROUTER_TABLE158_ADDR(value)       (SPW_ROUTER_TABLE158_ADDR_Msk & ((value) << SPW_ROUTER_TABLE158_ADDR_Pos))
#define SPW_ROUTER_TABLE158_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE158) Delete Header Byte Position */
#define SPW_ROUTER_TABLE158_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE158_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE158) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE158_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE158) Register Mask  */


/* -------- SPW_ROUTER_TABLE159 : (SPW Offset: 0x2FC) (R/W 32) SpW Router Table (router_table_nb = 32) 159 -------- */
#define SPW_ROUTER_TABLE159_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE159) Address Position */
#define SPW_ROUTER_TABLE159_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE159_ADDR_Pos)    /**< (SPW_ROUTER_TABLE159) Address Mask */
#define SPW_ROUTER_TABLE159_ADDR(value)       (SPW_ROUTER_TABLE159_ADDR_Msk & ((value) << SPW_ROUTER_TABLE159_ADDR_Pos))
#define SPW_ROUTER_TABLE159_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE159) Delete Header Byte Position */
#define SPW_ROUTER_TABLE159_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE159_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE159) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE159_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE159) Register Mask  */


/* -------- SPW_ROUTER_TABLE160 : (SPW Offset: 0x300) (R/W 32) SpW Router Table (router_table_nb = 32) 160 -------- */
#define SPW_ROUTER_TABLE160_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE160) Address Position */
#define SPW_ROUTER_TABLE160_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE160_ADDR_Pos)    /**< (SPW_ROUTER_TABLE160) Address Mask */
#define SPW_ROUTER_TABLE160_ADDR(value)       (SPW_ROUTER_TABLE160_ADDR_Msk & ((value) << SPW_ROUTER_TABLE160_ADDR_Pos))
#define SPW_ROUTER_TABLE160_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE160) Delete Header Byte Position */
#define SPW_ROUTER_TABLE160_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE160_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE160) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE160_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE160) Register Mask  */


/* -------- SPW_ROUTER_TABLE161 : (SPW Offset: 0x304) (R/W 32) SpW Router Table (router_table_nb = 32) 161 -------- */
#define SPW_ROUTER_TABLE161_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE161) Address Position */
#define SPW_ROUTER_TABLE161_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE161_ADDR_Pos)    /**< (SPW_ROUTER_TABLE161) Address Mask */
#define SPW_ROUTER_TABLE161_ADDR(value)       (SPW_ROUTER_TABLE161_ADDR_Msk & ((value) << SPW_ROUTER_TABLE161_ADDR_Pos))
#define SPW_ROUTER_TABLE161_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE161) Delete Header Byte Position */
#define SPW_ROUTER_TABLE161_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE161_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE161) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE161_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE161) Register Mask  */


/* -------- SPW_ROUTER_TABLE162 : (SPW Offset: 0x308) (R/W 32) SpW Router Table (router_table_nb = 32) 162 -------- */
#define SPW_ROUTER_TABLE162_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE162) Address Position */
#define SPW_ROUTER_TABLE162_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE162_ADDR_Pos)    /**< (SPW_ROUTER_TABLE162) Address Mask */
#define SPW_ROUTER_TABLE162_ADDR(value)       (SPW_ROUTER_TABLE162_ADDR_Msk & ((value) << SPW_ROUTER_TABLE162_ADDR_Pos))
#define SPW_ROUTER_TABLE162_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE162) Delete Header Byte Position */
#define SPW_ROUTER_TABLE162_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE162_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE162) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE162_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE162) Register Mask  */


/* -------- SPW_ROUTER_TABLE163 : (SPW Offset: 0x30C) (R/W 32) SpW Router Table (router_table_nb = 32) 163 -------- */
#define SPW_ROUTER_TABLE163_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE163) Address Position */
#define SPW_ROUTER_TABLE163_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE163_ADDR_Pos)    /**< (SPW_ROUTER_TABLE163) Address Mask */
#define SPW_ROUTER_TABLE163_ADDR(value)       (SPW_ROUTER_TABLE163_ADDR_Msk & ((value) << SPW_ROUTER_TABLE163_ADDR_Pos))
#define SPW_ROUTER_TABLE163_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE163) Delete Header Byte Position */
#define SPW_ROUTER_TABLE163_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE163_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE163) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE163_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE163) Register Mask  */


/* -------- SPW_ROUTER_TABLE164 : (SPW Offset: 0x310) (R/W 32) SpW Router Table (router_table_nb = 32) 164 -------- */
#define SPW_ROUTER_TABLE164_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE164) Address Position */
#define SPW_ROUTER_TABLE164_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE164_ADDR_Pos)    /**< (SPW_ROUTER_TABLE164) Address Mask */
#define SPW_ROUTER_TABLE164_ADDR(value)       (SPW_ROUTER_TABLE164_ADDR_Msk & ((value) << SPW_ROUTER_TABLE164_ADDR_Pos))
#define SPW_ROUTER_TABLE164_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE164) Delete Header Byte Position */
#define SPW_ROUTER_TABLE164_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE164_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE164) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE164_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE164) Register Mask  */


/* -------- SPW_ROUTER_TABLE165 : (SPW Offset: 0x314) (R/W 32) SpW Router Table (router_table_nb = 32) 165 -------- */
#define SPW_ROUTER_TABLE165_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE165) Address Position */
#define SPW_ROUTER_TABLE165_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE165_ADDR_Pos)    /**< (SPW_ROUTER_TABLE165) Address Mask */
#define SPW_ROUTER_TABLE165_ADDR(value)       (SPW_ROUTER_TABLE165_ADDR_Msk & ((value) << SPW_ROUTER_TABLE165_ADDR_Pos))
#define SPW_ROUTER_TABLE165_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE165) Delete Header Byte Position */
#define SPW_ROUTER_TABLE165_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE165_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE165) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE165_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE165) Register Mask  */


/* -------- SPW_ROUTER_TABLE166 : (SPW Offset: 0x318) (R/W 32) SpW Router Table (router_table_nb = 32) 166 -------- */
#define SPW_ROUTER_TABLE166_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE166) Address Position */
#define SPW_ROUTER_TABLE166_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE166_ADDR_Pos)    /**< (SPW_ROUTER_TABLE166) Address Mask */
#define SPW_ROUTER_TABLE166_ADDR(value)       (SPW_ROUTER_TABLE166_ADDR_Msk & ((value) << SPW_ROUTER_TABLE166_ADDR_Pos))
#define SPW_ROUTER_TABLE166_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE166) Delete Header Byte Position */
#define SPW_ROUTER_TABLE166_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE166_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE166) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE166_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE166) Register Mask  */


/* -------- SPW_ROUTER_TABLE167 : (SPW Offset: 0x31C) (R/W 32) SpW Router Table (router_table_nb = 32) 167 -------- */
#define SPW_ROUTER_TABLE167_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE167) Address Position */
#define SPW_ROUTER_TABLE167_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE167_ADDR_Pos)    /**< (SPW_ROUTER_TABLE167) Address Mask */
#define SPW_ROUTER_TABLE167_ADDR(value)       (SPW_ROUTER_TABLE167_ADDR_Msk & ((value) << SPW_ROUTER_TABLE167_ADDR_Pos))
#define SPW_ROUTER_TABLE167_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE167) Delete Header Byte Position */
#define SPW_ROUTER_TABLE167_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE167_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE167) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE167_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE167) Register Mask  */


/* -------- SPW_ROUTER_TABLE168 : (SPW Offset: 0x320) (R/W 32) SpW Router Table (router_table_nb = 32) 168 -------- */
#define SPW_ROUTER_TABLE168_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE168) Address Position */
#define SPW_ROUTER_TABLE168_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE168_ADDR_Pos)    /**< (SPW_ROUTER_TABLE168) Address Mask */
#define SPW_ROUTER_TABLE168_ADDR(value)       (SPW_ROUTER_TABLE168_ADDR_Msk & ((value) << SPW_ROUTER_TABLE168_ADDR_Pos))
#define SPW_ROUTER_TABLE168_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE168) Delete Header Byte Position */
#define SPW_ROUTER_TABLE168_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE168_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE168) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE168_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE168) Register Mask  */


/* -------- SPW_ROUTER_TABLE169 : (SPW Offset: 0x324) (R/W 32) SpW Router Table (router_table_nb = 32) 169 -------- */
#define SPW_ROUTER_TABLE169_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE169) Address Position */
#define SPW_ROUTER_TABLE169_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE169_ADDR_Pos)    /**< (SPW_ROUTER_TABLE169) Address Mask */
#define SPW_ROUTER_TABLE169_ADDR(value)       (SPW_ROUTER_TABLE169_ADDR_Msk & ((value) << SPW_ROUTER_TABLE169_ADDR_Pos))
#define SPW_ROUTER_TABLE169_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE169) Delete Header Byte Position */
#define SPW_ROUTER_TABLE169_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE169_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE169) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE169_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE169) Register Mask  */


/* -------- SPW_ROUTER_TABLE170 : (SPW Offset: 0x328) (R/W 32) SpW Router Table (router_table_nb = 32) 170 -------- */
#define SPW_ROUTER_TABLE170_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE170) Address Position */
#define SPW_ROUTER_TABLE170_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE170_ADDR_Pos)    /**< (SPW_ROUTER_TABLE170) Address Mask */
#define SPW_ROUTER_TABLE170_ADDR(value)       (SPW_ROUTER_TABLE170_ADDR_Msk & ((value) << SPW_ROUTER_TABLE170_ADDR_Pos))
#define SPW_ROUTER_TABLE170_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE170) Delete Header Byte Position */
#define SPW_ROUTER_TABLE170_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE170_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE170) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE170_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE170) Register Mask  */


/* -------- SPW_ROUTER_TABLE171 : (SPW Offset: 0x32C) (R/W 32) SpW Router Table (router_table_nb = 32) 171 -------- */
#define SPW_ROUTER_TABLE171_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE171) Address Position */
#define SPW_ROUTER_TABLE171_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE171_ADDR_Pos)    /**< (SPW_ROUTER_TABLE171) Address Mask */
#define SPW_ROUTER_TABLE171_ADDR(value)       (SPW_ROUTER_TABLE171_ADDR_Msk & ((value) << SPW_ROUTER_TABLE171_ADDR_Pos))
#define SPW_ROUTER_TABLE171_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE171) Delete Header Byte Position */
#define SPW_ROUTER_TABLE171_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE171_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE171) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE171_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE171) Register Mask  */


/* -------- SPW_ROUTER_TABLE172 : (SPW Offset: 0x330) (R/W 32) SpW Router Table (router_table_nb = 32) 172 -------- */
#define SPW_ROUTER_TABLE172_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE172) Address Position */
#define SPW_ROUTER_TABLE172_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE172_ADDR_Pos)    /**< (SPW_ROUTER_TABLE172) Address Mask */
#define SPW_ROUTER_TABLE172_ADDR(value)       (SPW_ROUTER_TABLE172_ADDR_Msk & ((value) << SPW_ROUTER_TABLE172_ADDR_Pos))
#define SPW_ROUTER_TABLE172_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE172) Delete Header Byte Position */
#define SPW_ROUTER_TABLE172_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE172_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE172) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE172_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE172) Register Mask  */


/* -------- SPW_ROUTER_TABLE173 : (SPW Offset: 0x334) (R/W 32) SpW Router Table (router_table_nb = 32) 173 -------- */
#define SPW_ROUTER_TABLE173_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE173) Address Position */
#define SPW_ROUTER_TABLE173_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE173_ADDR_Pos)    /**< (SPW_ROUTER_TABLE173) Address Mask */
#define SPW_ROUTER_TABLE173_ADDR(value)       (SPW_ROUTER_TABLE173_ADDR_Msk & ((value) << SPW_ROUTER_TABLE173_ADDR_Pos))
#define SPW_ROUTER_TABLE173_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE173) Delete Header Byte Position */
#define SPW_ROUTER_TABLE173_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE173_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE173) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE173_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE173) Register Mask  */


/* -------- SPW_ROUTER_TABLE174 : (SPW Offset: 0x338) (R/W 32) SpW Router Table (router_table_nb = 32) 174 -------- */
#define SPW_ROUTER_TABLE174_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE174) Address Position */
#define SPW_ROUTER_TABLE174_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE174_ADDR_Pos)    /**< (SPW_ROUTER_TABLE174) Address Mask */
#define SPW_ROUTER_TABLE174_ADDR(value)       (SPW_ROUTER_TABLE174_ADDR_Msk & ((value) << SPW_ROUTER_TABLE174_ADDR_Pos))
#define SPW_ROUTER_TABLE174_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE174) Delete Header Byte Position */
#define SPW_ROUTER_TABLE174_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE174_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE174) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE174_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE174) Register Mask  */


/* -------- SPW_ROUTER_TABLE175 : (SPW Offset: 0x33C) (R/W 32) SpW Router Table (router_table_nb = 32) 175 -------- */
#define SPW_ROUTER_TABLE175_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE175) Address Position */
#define SPW_ROUTER_TABLE175_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE175_ADDR_Pos)    /**< (SPW_ROUTER_TABLE175) Address Mask */
#define SPW_ROUTER_TABLE175_ADDR(value)       (SPW_ROUTER_TABLE175_ADDR_Msk & ((value) << SPW_ROUTER_TABLE175_ADDR_Pos))
#define SPW_ROUTER_TABLE175_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE175) Delete Header Byte Position */
#define SPW_ROUTER_TABLE175_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE175_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE175) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE175_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE175) Register Mask  */


/* -------- SPW_ROUTER_TABLE176 : (SPW Offset: 0x340) (R/W 32) SpW Router Table (router_table_nb = 32) 176 -------- */
#define SPW_ROUTER_TABLE176_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE176) Address Position */
#define SPW_ROUTER_TABLE176_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE176_ADDR_Pos)    /**< (SPW_ROUTER_TABLE176) Address Mask */
#define SPW_ROUTER_TABLE176_ADDR(value)       (SPW_ROUTER_TABLE176_ADDR_Msk & ((value) << SPW_ROUTER_TABLE176_ADDR_Pos))
#define SPW_ROUTER_TABLE176_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE176) Delete Header Byte Position */
#define SPW_ROUTER_TABLE176_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE176_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE176) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE176_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE176) Register Mask  */


/* -------- SPW_ROUTER_TABLE177 : (SPW Offset: 0x344) (R/W 32) SpW Router Table (router_table_nb = 32) 177 -------- */
#define SPW_ROUTER_TABLE177_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE177) Address Position */
#define SPW_ROUTER_TABLE177_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE177_ADDR_Pos)    /**< (SPW_ROUTER_TABLE177) Address Mask */
#define SPW_ROUTER_TABLE177_ADDR(value)       (SPW_ROUTER_TABLE177_ADDR_Msk & ((value) << SPW_ROUTER_TABLE177_ADDR_Pos))
#define SPW_ROUTER_TABLE177_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE177) Delete Header Byte Position */
#define SPW_ROUTER_TABLE177_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE177_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE177) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE177_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE177) Register Mask  */


/* -------- SPW_ROUTER_TABLE178 : (SPW Offset: 0x348) (R/W 32) SpW Router Table (router_table_nb = 32) 178 -------- */
#define SPW_ROUTER_TABLE178_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE178) Address Position */
#define SPW_ROUTER_TABLE178_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE178_ADDR_Pos)    /**< (SPW_ROUTER_TABLE178) Address Mask */
#define SPW_ROUTER_TABLE178_ADDR(value)       (SPW_ROUTER_TABLE178_ADDR_Msk & ((value) << SPW_ROUTER_TABLE178_ADDR_Pos))
#define SPW_ROUTER_TABLE178_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE178) Delete Header Byte Position */
#define SPW_ROUTER_TABLE178_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE178_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE178) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE178_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE178) Register Mask  */


/* -------- SPW_ROUTER_TABLE179 : (SPW Offset: 0x34C) (R/W 32) SpW Router Table (router_table_nb = 32) 179 -------- */
#define SPW_ROUTER_TABLE179_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE179) Address Position */
#define SPW_ROUTER_TABLE179_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE179_ADDR_Pos)    /**< (SPW_ROUTER_TABLE179) Address Mask */
#define SPW_ROUTER_TABLE179_ADDR(value)       (SPW_ROUTER_TABLE179_ADDR_Msk & ((value) << SPW_ROUTER_TABLE179_ADDR_Pos))
#define SPW_ROUTER_TABLE179_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE179) Delete Header Byte Position */
#define SPW_ROUTER_TABLE179_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE179_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE179) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE179_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE179) Register Mask  */


/* -------- SPW_ROUTER_TABLE180 : (SPW Offset: 0x350) (R/W 32) SpW Router Table (router_table_nb = 32) 180 -------- */
#define SPW_ROUTER_TABLE180_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE180) Address Position */
#define SPW_ROUTER_TABLE180_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE180_ADDR_Pos)    /**< (SPW_ROUTER_TABLE180) Address Mask */
#define SPW_ROUTER_TABLE180_ADDR(value)       (SPW_ROUTER_TABLE180_ADDR_Msk & ((value) << SPW_ROUTER_TABLE180_ADDR_Pos))
#define SPW_ROUTER_TABLE180_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE180) Delete Header Byte Position */
#define SPW_ROUTER_TABLE180_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE180_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE180) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE180_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE180) Register Mask  */


/* -------- SPW_ROUTER_TABLE181 : (SPW Offset: 0x354) (R/W 32) SpW Router Table (router_table_nb = 32) 181 -------- */
#define SPW_ROUTER_TABLE181_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE181) Address Position */
#define SPW_ROUTER_TABLE181_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE181_ADDR_Pos)    /**< (SPW_ROUTER_TABLE181) Address Mask */
#define SPW_ROUTER_TABLE181_ADDR(value)       (SPW_ROUTER_TABLE181_ADDR_Msk & ((value) << SPW_ROUTER_TABLE181_ADDR_Pos))
#define SPW_ROUTER_TABLE181_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE181) Delete Header Byte Position */
#define SPW_ROUTER_TABLE181_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE181_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE181) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE181_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE181) Register Mask  */


/* -------- SPW_ROUTER_TABLE182 : (SPW Offset: 0x358) (R/W 32) SpW Router Table (router_table_nb = 32) 182 -------- */
#define SPW_ROUTER_TABLE182_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE182) Address Position */
#define SPW_ROUTER_TABLE182_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE182_ADDR_Pos)    /**< (SPW_ROUTER_TABLE182) Address Mask */
#define SPW_ROUTER_TABLE182_ADDR(value)       (SPW_ROUTER_TABLE182_ADDR_Msk & ((value) << SPW_ROUTER_TABLE182_ADDR_Pos))
#define SPW_ROUTER_TABLE182_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE182) Delete Header Byte Position */
#define SPW_ROUTER_TABLE182_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE182_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE182) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE182_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE182) Register Mask  */


/* -------- SPW_ROUTER_TABLE183 : (SPW Offset: 0x35C) (R/W 32) SpW Router Table (router_table_nb = 32) 183 -------- */
#define SPW_ROUTER_TABLE183_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE183) Address Position */
#define SPW_ROUTER_TABLE183_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE183_ADDR_Pos)    /**< (SPW_ROUTER_TABLE183) Address Mask */
#define SPW_ROUTER_TABLE183_ADDR(value)       (SPW_ROUTER_TABLE183_ADDR_Msk & ((value) << SPW_ROUTER_TABLE183_ADDR_Pos))
#define SPW_ROUTER_TABLE183_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE183) Delete Header Byte Position */
#define SPW_ROUTER_TABLE183_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE183_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE183) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE183_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE183) Register Mask  */


/* -------- SPW_ROUTER_TABLE184 : (SPW Offset: 0x360) (R/W 32) SpW Router Table (router_table_nb = 32) 184 -------- */
#define SPW_ROUTER_TABLE184_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE184) Address Position */
#define SPW_ROUTER_TABLE184_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE184_ADDR_Pos)    /**< (SPW_ROUTER_TABLE184) Address Mask */
#define SPW_ROUTER_TABLE184_ADDR(value)       (SPW_ROUTER_TABLE184_ADDR_Msk & ((value) << SPW_ROUTER_TABLE184_ADDR_Pos))
#define SPW_ROUTER_TABLE184_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE184) Delete Header Byte Position */
#define SPW_ROUTER_TABLE184_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE184_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE184) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE184_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE184) Register Mask  */


/* -------- SPW_ROUTER_TABLE185 : (SPW Offset: 0x364) (R/W 32) SpW Router Table (router_table_nb = 32) 185 -------- */
#define SPW_ROUTER_TABLE185_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE185) Address Position */
#define SPW_ROUTER_TABLE185_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE185_ADDR_Pos)    /**< (SPW_ROUTER_TABLE185) Address Mask */
#define SPW_ROUTER_TABLE185_ADDR(value)       (SPW_ROUTER_TABLE185_ADDR_Msk & ((value) << SPW_ROUTER_TABLE185_ADDR_Pos))
#define SPW_ROUTER_TABLE185_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE185) Delete Header Byte Position */
#define SPW_ROUTER_TABLE185_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE185_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE185) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE185_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE185) Register Mask  */


/* -------- SPW_ROUTER_TABLE186 : (SPW Offset: 0x368) (R/W 32) SpW Router Table (router_table_nb = 32) 186 -------- */
#define SPW_ROUTER_TABLE186_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE186) Address Position */
#define SPW_ROUTER_TABLE186_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE186_ADDR_Pos)    /**< (SPW_ROUTER_TABLE186) Address Mask */
#define SPW_ROUTER_TABLE186_ADDR(value)       (SPW_ROUTER_TABLE186_ADDR_Msk & ((value) << SPW_ROUTER_TABLE186_ADDR_Pos))
#define SPW_ROUTER_TABLE186_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE186) Delete Header Byte Position */
#define SPW_ROUTER_TABLE186_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE186_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE186) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE186_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE186) Register Mask  */


/* -------- SPW_ROUTER_TABLE187 : (SPW Offset: 0x36C) (R/W 32) SpW Router Table (router_table_nb = 32) 187 -------- */
#define SPW_ROUTER_TABLE187_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE187) Address Position */
#define SPW_ROUTER_TABLE187_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE187_ADDR_Pos)    /**< (SPW_ROUTER_TABLE187) Address Mask */
#define SPW_ROUTER_TABLE187_ADDR(value)       (SPW_ROUTER_TABLE187_ADDR_Msk & ((value) << SPW_ROUTER_TABLE187_ADDR_Pos))
#define SPW_ROUTER_TABLE187_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE187) Delete Header Byte Position */
#define SPW_ROUTER_TABLE187_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE187_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE187) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE187_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE187) Register Mask  */


/* -------- SPW_ROUTER_TABLE188 : (SPW Offset: 0x370) (R/W 32) SpW Router Table (router_table_nb = 32) 188 -------- */
#define SPW_ROUTER_TABLE188_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE188) Address Position */
#define SPW_ROUTER_TABLE188_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE188_ADDR_Pos)    /**< (SPW_ROUTER_TABLE188) Address Mask */
#define SPW_ROUTER_TABLE188_ADDR(value)       (SPW_ROUTER_TABLE188_ADDR_Msk & ((value) << SPW_ROUTER_TABLE188_ADDR_Pos))
#define SPW_ROUTER_TABLE188_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE188) Delete Header Byte Position */
#define SPW_ROUTER_TABLE188_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE188_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE188) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE188_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE188) Register Mask  */


/* -------- SPW_ROUTER_TABLE189 : (SPW Offset: 0x374) (R/W 32) SpW Router Table (router_table_nb = 32) 189 -------- */
#define SPW_ROUTER_TABLE189_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE189) Address Position */
#define SPW_ROUTER_TABLE189_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE189_ADDR_Pos)    /**< (SPW_ROUTER_TABLE189) Address Mask */
#define SPW_ROUTER_TABLE189_ADDR(value)       (SPW_ROUTER_TABLE189_ADDR_Msk & ((value) << SPW_ROUTER_TABLE189_ADDR_Pos))
#define SPW_ROUTER_TABLE189_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE189) Delete Header Byte Position */
#define SPW_ROUTER_TABLE189_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE189_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE189) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE189_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE189) Register Mask  */


/* -------- SPW_ROUTER_TABLE190 : (SPW Offset: 0x378) (R/W 32) SpW Router Table (router_table_nb = 32) 190 -------- */
#define SPW_ROUTER_TABLE190_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE190) Address Position */
#define SPW_ROUTER_TABLE190_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE190_ADDR_Pos)    /**< (SPW_ROUTER_TABLE190) Address Mask */
#define SPW_ROUTER_TABLE190_ADDR(value)       (SPW_ROUTER_TABLE190_ADDR_Msk & ((value) << SPW_ROUTER_TABLE190_ADDR_Pos))
#define SPW_ROUTER_TABLE190_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE190) Delete Header Byte Position */
#define SPW_ROUTER_TABLE190_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE190_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE190) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE190_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE190) Register Mask  */


/* -------- SPW_ROUTER_TABLE191 : (SPW Offset: 0x37C) (R/W 32) SpW Router Table (router_table_nb = 32) 191 -------- */
#define SPW_ROUTER_TABLE191_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE191) Address Position */
#define SPW_ROUTER_TABLE191_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE191_ADDR_Pos)    /**< (SPW_ROUTER_TABLE191) Address Mask */
#define SPW_ROUTER_TABLE191_ADDR(value)       (SPW_ROUTER_TABLE191_ADDR_Msk & ((value) << SPW_ROUTER_TABLE191_ADDR_Pos))
#define SPW_ROUTER_TABLE191_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE191) Delete Header Byte Position */
#define SPW_ROUTER_TABLE191_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE191_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE191) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE191_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE191) Register Mask  */


/* -------- SPW_ROUTER_TABLE192 : (SPW Offset: 0x380) (R/W 32) SpW Router Table (router_table_nb = 32) 192 -------- */
#define SPW_ROUTER_TABLE192_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE192) Address Position */
#define SPW_ROUTER_TABLE192_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE192_ADDR_Pos)    /**< (SPW_ROUTER_TABLE192) Address Mask */
#define SPW_ROUTER_TABLE192_ADDR(value)       (SPW_ROUTER_TABLE192_ADDR_Msk & ((value) << SPW_ROUTER_TABLE192_ADDR_Pos))
#define SPW_ROUTER_TABLE192_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE192) Delete Header Byte Position */
#define SPW_ROUTER_TABLE192_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE192_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE192) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE192_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE192) Register Mask  */


/* -------- SPW_ROUTER_TABLE193 : (SPW Offset: 0x384) (R/W 32) SpW Router Table (router_table_nb = 32) 193 -------- */
#define SPW_ROUTER_TABLE193_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE193) Address Position */
#define SPW_ROUTER_TABLE193_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE193_ADDR_Pos)    /**< (SPW_ROUTER_TABLE193) Address Mask */
#define SPW_ROUTER_TABLE193_ADDR(value)       (SPW_ROUTER_TABLE193_ADDR_Msk & ((value) << SPW_ROUTER_TABLE193_ADDR_Pos))
#define SPW_ROUTER_TABLE193_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE193) Delete Header Byte Position */
#define SPW_ROUTER_TABLE193_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE193_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE193) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE193_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE193) Register Mask  */


/* -------- SPW_ROUTER_TABLE194 : (SPW Offset: 0x388) (R/W 32) SpW Router Table (router_table_nb = 32) 194 -------- */
#define SPW_ROUTER_TABLE194_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE194) Address Position */
#define SPW_ROUTER_TABLE194_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE194_ADDR_Pos)    /**< (SPW_ROUTER_TABLE194) Address Mask */
#define SPW_ROUTER_TABLE194_ADDR(value)       (SPW_ROUTER_TABLE194_ADDR_Msk & ((value) << SPW_ROUTER_TABLE194_ADDR_Pos))
#define SPW_ROUTER_TABLE194_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE194) Delete Header Byte Position */
#define SPW_ROUTER_TABLE194_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE194_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE194) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE194_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE194) Register Mask  */


/* -------- SPW_ROUTER_TABLE195 : (SPW Offset: 0x38C) (R/W 32) SpW Router Table (router_table_nb = 32) 195 -------- */
#define SPW_ROUTER_TABLE195_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE195) Address Position */
#define SPW_ROUTER_TABLE195_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE195_ADDR_Pos)    /**< (SPW_ROUTER_TABLE195) Address Mask */
#define SPW_ROUTER_TABLE195_ADDR(value)       (SPW_ROUTER_TABLE195_ADDR_Msk & ((value) << SPW_ROUTER_TABLE195_ADDR_Pos))
#define SPW_ROUTER_TABLE195_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE195) Delete Header Byte Position */
#define SPW_ROUTER_TABLE195_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE195_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE195) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE195_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE195) Register Mask  */


/* -------- SPW_ROUTER_TABLE196 : (SPW Offset: 0x390) (R/W 32) SpW Router Table (router_table_nb = 32) 196 -------- */
#define SPW_ROUTER_TABLE196_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE196) Address Position */
#define SPW_ROUTER_TABLE196_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE196_ADDR_Pos)    /**< (SPW_ROUTER_TABLE196) Address Mask */
#define SPW_ROUTER_TABLE196_ADDR(value)       (SPW_ROUTER_TABLE196_ADDR_Msk & ((value) << SPW_ROUTER_TABLE196_ADDR_Pos))
#define SPW_ROUTER_TABLE196_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE196) Delete Header Byte Position */
#define SPW_ROUTER_TABLE196_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE196_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE196) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE196_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE196) Register Mask  */


/* -------- SPW_ROUTER_TABLE197 : (SPW Offset: 0x394) (R/W 32) SpW Router Table (router_table_nb = 32) 197 -------- */
#define SPW_ROUTER_TABLE197_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE197) Address Position */
#define SPW_ROUTER_TABLE197_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE197_ADDR_Pos)    /**< (SPW_ROUTER_TABLE197) Address Mask */
#define SPW_ROUTER_TABLE197_ADDR(value)       (SPW_ROUTER_TABLE197_ADDR_Msk & ((value) << SPW_ROUTER_TABLE197_ADDR_Pos))
#define SPW_ROUTER_TABLE197_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE197) Delete Header Byte Position */
#define SPW_ROUTER_TABLE197_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE197_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE197) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE197_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE197) Register Mask  */


/* -------- SPW_ROUTER_TABLE198 : (SPW Offset: 0x398) (R/W 32) SpW Router Table (router_table_nb = 32) 198 -------- */
#define SPW_ROUTER_TABLE198_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE198) Address Position */
#define SPW_ROUTER_TABLE198_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE198_ADDR_Pos)    /**< (SPW_ROUTER_TABLE198) Address Mask */
#define SPW_ROUTER_TABLE198_ADDR(value)       (SPW_ROUTER_TABLE198_ADDR_Msk & ((value) << SPW_ROUTER_TABLE198_ADDR_Pos))
#define SPW_ROUTER_TABLE198_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE198) Delete Header Byte Position */
#define SPW_ROUTER_TABLE198_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE198_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE198) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE198_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE198) Register Mask  */


/* -------- SPW_ROUTER_TABLE199 : (SPW Offset: 0x39C) (R/W 32) SpW Router Table (router_table_nb = 32) 199 -------- */
#define SPW_ROUTER_TABLE199_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE199) Address Position */
#define SPW_ROUTER_TABLE199_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE199_ADDR_Pos)    /**< (SPW_ROUTER_TABLE199) Address Mask */
#define SPW_ROUTER_TABLE199_ADDR(value)       (SPW_ROUTER_TABLE199_ADDR_Msk & ((value) << SPW_ROUTER_TABLE199_ADDR_Pos))
#define SPW_ROUTER_TABLE199_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE199) Delete Header Byte Position */
#define SPW_ROUTER_TABLE199_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE199_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE199) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE199_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE199) Register Mask  */


/* -------- SPW_ROUTER_TABLE200 : (SPW Offset: 0x3A0) (R/W 32) SpW Router Table (router_table_nb = 32) 200 -------- */
#define SPW_ROUTER_TABLE200_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE200) Address Position */
#define SPW_ROUTER_TABLE200_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE200_ADDR_Pos)    /**< (SPW_ROUTER_TABLE200) Address Mask */
#define SPW_ROUTER_TABLE200_ADDR(value)       (SPW_ROUTER_TABLE200_ADDR_Msk & ((value) << SPW_ROUTER_TABLE200_ADDR_Pos))
#define SPW_ROUTER_TABLE200_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE200) Delete Header Byte Position */
#define SPW_ROUTER_TABLE200_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE200_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE200) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE200_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE200) Register Mask  */


/* -------- SPW_ROUTER_TABLE201 : (SPW Offset: 0x3A4) (R/W 32) SpW Router Table (router_table_nb = 32) 201 -------- */
#define SPW_ROUTER_TABLE201_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE201) Address Position */
#define SPW_ROUTER_TABLE201_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE201_ADDR_Pos)    /**< (SPW_ROUTER_TABLE201) Address Mask */
#define SPW_ROUTER_TABLE201_ADDR(value)       (SPW_ROUTER_TABLE201_ADDR_Msk & ((value) << SPW_ROUTER_TABLE201_ADDR_Pos))
#define SPW_ROUTER_TABLE201_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE201) Delete Header Byte Position */
#define SPW_ROUTER_TABLE201_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE201_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE201) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE201_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE201) Register Mask  */


/* -------- SPW_ROUTER_TABLE202 : (SPW Offset: 0x3A8) (R/W 32) SpW Router Table (router_table_nb = 32) 202 -------- */
#define SPW_ROUTER_TABLE202_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE202) Address Position */
#define SPW_ROUTER_TABLE202_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE202_ADDR_Pos)    /**< (SPW_ROUTER_TABLE202) Address Mask */
#define SPW_ROUTER_TABLE202_ADDR(value)       (SPW_ROUTER_TABLE202_ADDR_Msk & ((value) << SPW_ROUTER_TABLE202_ADDR_Pos))
#define SPW_ROUTER_TABLE202_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE202) Delete Header Byte Position */
#define SPW_ROUTER_TABLE202_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE202_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE202) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE202_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE202) Register Mask  */


/* -------- SPW_ROUTER_TABLE203 : (SPW Offset: 0x3AC) (R/W 32) SpW Router Table (router_table_nb = 32) 203 -------- */
#define SPW_ROUTER_TABLE203_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE203) Address Position */
#define SPW_ROUTER_TABLE203_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE203_ADDR_Pos)    /**< (SPW_ROUTER_TABLE203) Address Mask */
#define SPW_ROUTER_TABLE203_ADDR(value)       (SPW_ROUTER_TABLE203_ADDR_Msk & ((value) << SPW_ROUTER_TABLE203_ADDR_Pos))
#define SPW_ROUTER_TABLE203_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE203) Delete Header Byte Position */
#define SPW_ROUTER_TABLE203_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE203_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE203) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE203_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE203) Register Mask  */


/* -------- SPW_ROUTER_TABLE204 : (SPW Offset: 0x3B0) (R/W 32) SpW Router Table (router_table_nb = 32) 204 -------- */
#define SPW_ROUTER_TABLE204_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE204) Address Position */
#define SPW_ROUTER_TABLE204_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE204_ADDR_Pos)    /**< (SPW_ROUTER_TABLE204) Address Mask */
#define SPW_ROUTER_TABLE204_ADDR(value)       (SPW_ROUTER_TABLE204_ADDR_Msk & ((value) << SPW_ROUTER_TABLE204_ADDR_Pos))
#define SPW_ROUTER_TABLE204_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE204) Delete Header Byte Position */
#define SPW_ROUTER_TABLE204_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE204_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE204) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE204_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE204) Register Mask  */


/* -------- SPW_ROUTER_TABLE205 : (SPW Offset: 0x3B4) (R/W 32) SpW Router Table (router_table_nb = 32) 205 -------- */
#define SPW_ROUTER_TABLE205_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE205) Address Position */
#define SPW_ROUTER_TABLE205_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE205_ADDR_Pos)    /**< (SPW_ROUTER_TABLE205) Address Mask */
#define SPW_ROUTER_TABLE205_ADDR(value)       (SPW_ROUTER_TABLE205_ADDR_Msk & ((value) << SPW_ROUTER_TABLE205_ADDR_Pos))
#define SPW_ROUTER_TABLE205_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE205) Delete Header Byte Position */
#define SPW_ROUTER_TABLE205_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE205_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE205) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE205_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE205) Register Mask  */


/* -------- SPW_ROUTER_TABLE206 : (SPW Offset: 0x3B8) (R/W 32) SpW Router Table (router_table_nb = 32) 206 -------- */
#define SPW_ROUTER_TABLE206_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE206) Address Position */
#define SPW_ROUTER_TABLE206_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE206_ADDR_Pos)    /**< (SPW_ROUTER_TABLE206) Address Mask */
#define SPW_ROUTER_TABLE206_ADDR(value)       (SPW_ROUTER_TABLE206_ADDR_Msk & ((value) << SPW_ROUTER_TABLE206_ADDR_Pos))
#define SPW_ROUTER_TABLE206_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE206) Delete Header Byte Position */
#define SPW_ROUTER_TABLE206_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE206_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE206) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE206_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE206) Register Mask  */


/* -------- SPW_ROUTER_TABLE207 : (SPW Offset: 0x3BC) (R/W 32) SpW Router Table (router_table_nb = 32) 207 -------- */
#define SPW_ROUTER_TABLE207_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE207) Address Position */
#define SPW_ROUTER_TABLE207_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE207_ADDR_Pos)    /**< (SPW_ROUTER_TABLE207) Address Mask */
#define SPW_ROUTER_TABLE207_ADDR(value)       (SPW_ROUTER_TABLE207_ADDR_Msk & ((value) << SPW_ROUTER_TABLE207_ADDR_Pos))
#define SPW_ROUTER_TABLE207_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE207) Delete Header Byte Position */
#define SPW_ROUTER_TABLE207_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE207_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE207) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE207_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE207) Register Mask  */


/* -------- SPW_ROUTER_TABLE208 : (SPW Offset: 0x3C0) (R/W 32) SpW Router Table (router_table_nb = 32) 208 -------- */
#define SPW_ROUTER_TABLE208_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE208) Address Position */
#define SPW_ROUTER_TABLE208_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE208_ADDR_Pos)    /**< (SPW_ROUTER_TABLE208) Address Mask */
#define SPW_ROUTER_TABLE208_ADDR(value)       (SPW_ROUTER_TABLE208_ADDR_Msk & ((value) << SPW_ROUTER_TABLE208_ADDR_Pos))
#define SPW_ROUTER_TABLE208_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE208) Delete Header Byte Position */
#define SPW_ROUTER_TABLE208_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE208_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE208) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE208_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE208) Register Mask  */


/* -------- SPW_ROUTER_TABLE209 : (SPW Offset: 0x3C4) (R/W 32) SpW Router Table (router_table_nb = 32) 209 -------- */
#define SPW_ROUTER_TABLE209_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE209) Address Position */
#define SPW_ROUTER_TABLE209_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE209_ADDR_Pos)    /**< (SPW_ROUTER_TABLE209) Address Mask */
#define SPW_ROUTER_TABLE209_ADDR(value)       (SPW_ROUTER_TABLE209_ADDR_Msk & ((value) << SPW_ROUTER_TABLE209_ADDR_Pos))
#define SPW_ROUTER_TABLE209_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE209) Delete Header Byte Position */
#define SPW_ROUTER_TABLE209_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE209_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE209) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE209_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE209) Register Mask  */


/* -------- SPW_ROUTER_TABLE210 : (SPW Offset: 0x3C8) (R/W 32) SpW Router Table (router_table_nb = 32) 210 -------- */
#define SPW_ROUTER_TABLE210_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE210) Address Position */
#define SPW_ROUTER_TABLE210_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE210_ADDR_Pos)    /**< (SPW_ROUTER_TABLE210) Address Mask */
#define SPW_ROUTER_TABLE210_ADDR(value)       (SPW_ROUTER_TABLE210_ADDR_Msk & ((value) << SPW_ROUTER_TABLE210_ADDR_Pos))
#define SPW_ROUTER_TABLE210_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE210) Delete Header Byte Position */
#define SPW_ROUTER_TABLE210_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE210_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE210) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE210_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE210) Register Mask  */


/* -------- SPW_ROUTER_TABLE211 : (SPW Offset: 0x3CC) (R/W 32) SpW Router Table (router_table_nb = 32) 211 -------- */
#define SPW_ROUTER_TABLE211_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE211) Address Position */
#define SPW_ROUTER_TABLE211_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE211_ADDR_Pos)    /**< (SPW_ROUTER_TABLE211) Address Mask */
#define SPW_ROUTER_TABLE211_ADDR(value)       (SPW_ROUTER_TABLE211_ADDR_Msk & ((value) << SPW_ROUTER_TABLE211_ADDR_Pos))
#define SPW_ROUTER_TABLE211_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE211) Delete Header Byte Position */
#define SPW_ROUTER_TABLE211_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE211_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE211) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE211_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE211) Register Mask  */


/* -------- SPW_ROUTER_TABLE212 : (SPW Offset: 0x3D0) (R/W 32) SpW Router Table (router_table_nb = 32) 212 -------- */
#define SPW_ROUTER_TABLE212_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE212) Address Position */
#define SPW_ROUTER_TABLE212_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE212_ADDR_Pos)    /**< (SPW_ROUTER_TABLE212) Address Mask */
#define SPW_ROUTER_TABLE212_ADDR(value)       (SPW_ROUTER_TABLE212_ADDR_Msk & ((value) << SPW_ROUTER_TABLE212_ADDR_Pos))
#define SPW_ROUTER_TABLE212_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE212) Delete Header Byte Position */
#define SPW_ROUTER_TABLE212_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE212_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE212) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE212_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE212) Register Mask  */


/* -------- SPW_ROUTER_TABLE213 : (SPW Offset: 0x3D4) (R/W 32) SpW Router Table (router_table_nb = 32) 213 -------- */
#define SPW_ROUTER_TABLE213_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE213) Address Position */
#define SPW_ROUTER_TABLE213_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE213_ADDR_Pos)    /**< (SPW_ROUTER_TABLE213) Address Mask */
#define SPW_ROUTER_TABLE213_ADDR(value)       (SPW_ROUTER_TABLE213_ADDR_Msk & ((value) << SPW_ROUTER_TABLE213_ADDR_Pos))
#define SPW_ROUTER_TABLE213_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE213) Delete Header Byte Position */
#define SPW_ROUTER_TABLE213_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE213_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE213) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE213_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE213) Register Mask  */


/* -------- SPW_ROUTER_TABLE214 : (SPW Offset: 0x3D8) (R/W 32) SpW Router Table (router_table_nb = 32) 214 -------- */
#define SPW_ROUTER_TABLE214_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE214) Address Position */
#define SPW_ROUTER_TABLE214_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE214_ADDR_Pos)    /**< (SPW_ROUTER_TABLE214) Address Mask */
#define SPW_ROUTER_TABLE214_ADDR(value)       (SPW_ROUTER_TABLE214_ADDR_Msk & ((value) << SPW_ROUTER_TABLE214_ADDR_Pos))
#define SPW_ROUTER_TABLE214_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE214) Delete Header Byte Position */
#define SPW_ROUTER_TABLE214_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE214_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE214) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE214_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE214) Register Mask  */


/* -------- SPW_ROUTER_TABLE215 : (SPW Offset: 0x3DC) (R/W 32) SpW Router Table (router_table_nb = 32) 215 -------- */
#define SPW_ROUTER_TABLE215_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE215) Address Position */
#define SPW_ROUTER_TABLE215_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE215_ADDR_Pos)    /**< (SPW_ROUTER_TABLE215) Address Mask */
#define SPW_ROUTER_TABLE215_ADDR(value)       (SPW_ROUTER_TABLE215_ADDR_Msk & ((value) << SPW_ROUTER_TABLE215_ADDR_Pos))
#define SPW_ROUTER_TABLE215_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE215) Delete Header Byte Position */
#define SPW_ROUTER_TABLE215_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE215_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE215) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE215_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE215) Register Mask  */


/* -------- SPW_ROUTER_TABLE216 : (SPW Offset: 0x3E0) (R/W 32) SpW Router Table (router_table_nb = 32) 216 -------- */
#define SPW_ROUTER_TABLE216_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE216) Address Position */
#define SPW_ROUTER_TABLE216_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE216_ADDR_Pos)    /**< (SPW_ROUTER_TABLE216) Address Mask */
#define SPW_ROUTER_TABLE216_ADDR(value)       (SPW_ROUTER_TABLE216_ADDR_Msk & ((value) << SPW_ROUTER_TABLE216_ADDR_Pos))
#define SPW_ROUTER_TABLE216_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE216) Delete Header Byte Position */
#define SPW_ROUTER_TABLE216_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE216_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE216) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE216_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE216) Register Mask  */


/* -------- SPW_ROUTER_TABLE217 : (SPW Offset: 0x3E4) (R/W 32) SpW Router Table (router_table_nb = 32) 217 -------- */
#define SPW_ROUTER_TABLE217_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE217) Address Position */
#define SPW_ROUTER_TABLE217_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE217_ADDR_Pos)    /**< (SPW_ROUTER_TABLE217) Address Mask */
#define SPW_ROUTER_TABLE217_ADDR(value)       (SPW_ROUTER_TABLE217_ADDR_Msk & ((value) << SPW_ROUTER_TABLE217_ADDR_Pos))
#define SPW_ROUTER_TABLE217_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE217) Delete Header Byte Position */
#define SPW_ROUTER_TABLE217_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE217_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE217) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE217_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE217) Register Mask  */


/* -------- SPW_ROUTER_TABLE218 : (SPW Offset: 0x3E8) (R/W 32) SpW Router Table (router_table_nb = 32) 218 -------- */
#define SPW_ROUTER_TABLE218_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE218) Address Position */
#define SPW_ROUTER_TABLE218_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE218_ADDR_Pos)    /**< (SPW_ROUTER_TABLE218) Address Mask */
#define SPW_ROUTER_TABLE218_ADDR(value)       (SPW_ROUTER_TABLE218_ADDR_Msk & ((value) << SPW_ROUTER_TABLE218_ADDR_Pos))
#define SPW_ROUTER_TABLE218_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE218) Delete Header Byte Position */
#define SPW_ROUTER_TABLE218_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE218_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE218) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE218_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE218) Register Mask  */


/* -------- SPW_ROUTER_TABLE219 : (SPW Offset: 0x3EC) (R/W 32) SpW Router Table (router_table_nb = 32) 219 -------- */
#define SPW_ROUTER_TABLE219_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE219) Address Position */
#define SPW_ROUTER_TABLE219_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE219_ADDR_Pos)    /**< (SPW_ROUTER_TABLE219) Address Mask */
#define SPW_ROUTER_TABLE219_ADDR(value)       (SPW_ROUTER_TABLE219_ADDR_Msk & ((value) << SPW_ROUTER_TABLE219_ADDR_Pos))
#define SPW_ROUTER_TABLE219_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE219) Delete Header Byte Position */
#define SPW_ROUTER_TABLE219_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE219_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE219) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE219_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE219) Register Mask  */


/* -------- SPW_ROUTER_TABLE220 : (SPW Offset: 0x3F0) (R/W 32) SpW Router Table (router_table_nb = 32) 220 -------- */
#define SPW_ROUTER_TABLE220_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE220) Address Position */
#define SPW_ROUTER_TABLE220_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE220_ADDR_Pos)    /**< (SPW_ROUTER_TABLE220) Address Mask */
#define SPW_ROUTER_TABLE220_ADDR(value)       (SPW_ROUTER_TABLE220_ADDR_Msk & ((value) << SPW_ROUTER_TABLE220_ADDR_Pos))
#define SPW_ROUTER_TABLE220_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE220) Delete Header Byte Position */
#define SPW_ROUTER_TABLE220_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE220_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE220) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE220_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE220) Register Mask  */


/* -------- SPW_ROUTER_TABLE221 : (SPW Offset: 0x3F4) (R/W 32) SpW Router Table (router_table_nb = 32) 221 -------- */
#define SPW_ROUTER_TABLE221_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE221) Address Position */
#define SPW_ROUTER_TABLE221_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE221_ADDR_Pos)    /**< (SPW_ROUTER_TABLE221) Address Mask */
#define SPW_ROUTER_TABLE221_ADDR(value)       (SPW_ROUTER_TABLE221_ADDR_Msk & ((value) << SPW_ROUTER_TABLE221_ADDR_Pos))
#define SPW_ROUTER_TABLE221_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE221) Delete Header Byte Position */
#define SPW_ROUTER_TABLE221_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE221_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE221) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE221_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE221) Register Mask  */


/* -------- SPW_ROUTER_TABLE222 : (SPW Offset: 0x3F8) (R/W 32) SpW Router Table (router_table_nb = 32) 222 -------- */
#define SPW_ROUTER_TABLE222_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE222) Address Position */
#define SPW_ROUTER_TABLE222_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE222_ADDR_Pos)    /**< (SPW_ROUTER_TABLE222) Address Mask */
#define SPW_ROUTER_TABLE222_ADDR(value)       (SPW_ROUTER_TABLE222_ADDR_Msk & ((value) << SPW_ROUTER_TABLE222_ADDR_Pos))
#define SPW_ROUTER_TABLE222_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE222) Delete Header Byte Position */
#define SPW_ROUTER_TABLE222_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE222_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE222) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE222_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE222) Register Mask  */


/* -------- SPW_ROUTER_TABLE223 : (SPW Offset: 0x3FC) (R/W 32) SpW Router Table (router_table_nb = 32) 223 -------- */
#define SPW_ROUTER_TABLE223_ADDR_Pos          _U_(0)                                         /**< (SPW_ROUTER_TABLE223) Address Position */
#define SPW_ROUTER_TABLE223_ADDR_Msk          (_U_(0x1F) << SPW_ROUTER_TABLE223_ADDR_Pos)    /**< (SPW_ROUTER_TABLE223) Address Mask */
#define SPW_ROUTER_TABLE223_ADDR(value)       (SPW_ROUTER_TABLE223_ADDR_Msk & ((value) << SPW_ROUTER_TABLE223_ADDR_Pos))
#define SPW_ROUTER_TABLE223_DELHEAD_Pos       _U_(8)                                         /**< (SPW_ROUTER_TABLE223) Delete Header Byte Position */
#define SPW_ROUTER_TABLE223_DELHEAD_Msk       (_U_(0x1) << SPW_ROUTER_TABLE223_DELHEAD_Pos)  /**< (SPW_ROUTER_TABLE223) Delete Header Byte Mask */
#define SPW_ROUTER_TABLE223_Msk               _U_(0x0000011F)                                /**< (SPW_ROUTER_TABLE223) Register Mask  */


/* -------- SPW_LINK1_PI_RM : (SPW Offset: 0x400) ( R/ 32) SpW Link 1 Pending Read Masked Interrupt -------- */
#define SPW_LINK1_PI_RM_DISERR_Pos            _U_(0)                                         /**< (SPW_LINK1_PI_RM) DisErr Position */
#define SPW_LINK1_PI_RM_DISERR_Msk            (_U_(0x1) << SPW_LINK1_PI_RM_DISERR_Pos)       /**< (SPW_LINK1_PI_RM) DisErr Mask */
#define SPW_LINK1_PI_RM_PARERR_Pos            _U_(1)                                         /**< (SPW_LINK1_PI_RM) ParErr Position */
#define SPW_LINK1_PI_RM_PARERR_Msk            (_U_(0x1) << SPW_LINK1_PI_RM_PARERR_Pos)       /**< (SPW_LINK1_PI_RM) ParErr Mask */
#define SPW_LINK1_PI_RM_ESCERR_Pos            _U_(2)                                         /**< (SPW_LINK1_PI_RM) ESCErr Position */
#define SPW_LINK1_PI_RM_ESCERR_Msk            (_U_(0x1) << SPW_LINK1_PI_RM_ESCERR_Pos)       /**< (SPW_LINK1_PI_RM) ESCErr Mask */
#define SPW_LINK1_PI_RM_CRERR_Pos             _U_(3)                                         /**< (SPW_LINK1_PI_RM) CrErr Position */
#define SPW_LINK1_PI_RM_CRERR_Msk             (_U_(0x1) << SPW_LINK1_PI_RM_CRERR_Pos)        /**< (SPW_LINK1_PI_RM) CrErr Mask */
#define SPW_LINK1_PI_RM_LINKABORT_Pos         _U_(4)                                         /**< (SPW_LINK1_PI_RM) LinkAbort Position */
#define SPW_LINK1_PI_RM_LINKABORT_Msk         (_U_(0x1) << SPW_LINK1_PI_RM_LINKABORT_Pos)    /**< (SPW_LINK1_PI_RM) LinkAbort Mask */
#define SPW_LINK1_PI_RM_EEPTRANS_Pos          _U_(5)                                         /**< (SPW_LINK1_PI_RM) EEP transmitted Position */
#define SPW_LINK1_PI_RM_EEPTRANS_Msk          (_U_(0x1) << SPW_LINK1_PI_RM_EEPTRANS_Pos)     /**< (SPW_LINK1_PI_RM) EEP transmitted Mask */
#define SPW_LINK1_PI_RM_EEPREC_Pos            _U_(6)                                         /**< (SPW_LINK1_PI_RM) EEP received Position */
#define SPW_LINK1_PI_RM_EEPREC_Msk            (_U_(0x1) << SPW_LINK1_PI_RM_EEPREC_Pos)       /**< (SPW_LINK1_PI_RM) EEP received Mask */
#define SPW_LINK1_PI_RM_DISCARD_Pos           _U_(7)                                         /**< (SPW_LINK1_PI_RM) Discard Position */
#define SPW_LINK1_PI_RM_DISCARD_Msk           (_U_(0x1) << SPW_LINK1_PI_RM_DISCARD_Pos)      /**< (SPW_LINK1_PI_RM) Discard Mask */
#define SPW_LINK1_PI_RM_ESCEVENT2_Pos         _U_(8)                                         /**< (SPW_LINK1_PI_RM) Escape Event 2 Position */
#define SPW_LINK1_PI_RM_ESCEVENT2_Msk         (_U_(0x1) << SPW_LINK1_PI_RM_ESCEVENT2_Pos)    /**< (SPW_LINK1_PI_RM) Escape Event 2 Mask */
#define SPW_LINK1_PI_RM_ESCEVENT1_Pos         _U_(9)                                         /**< (SPW_LINK1_PI_RM) Escape Event 1 Position */
#define SPW_LINK1_PI_RM_ESCEVENT1_Msk         (_U_(0x1) << SPW_LINK1_PI_RM_ESCEVENT1_Pos)    /**< (SPW_LINK1_PI_RM) Escape Event 1 Mask */
#define SPW_LINK1_PI_RM_Msk                   _U_(0x000003FF)                                /**< (SPW_LINK1_PI_RM) Register Mask  */

#define SPW_LINK1_PI_RM_ESCEVENT_Pos          _U_(8)                                         /**< (SPW_LINK1_PI_RM Position) Escape Event x */
#define SPW_LINK1_PI_RM_ESCEVENT_Msk          (_U_(0x3) << SPW_LINK1_PI_RM_ESCEVENT_Pos)     /**< (SPW_LINK1_PI_RM Mask) ESCEVENT */
#define SPW_LINK1_PI_RM_ESCEVENT(value)       (SPW_LINK1_PI_RM_ESCEVENT_Msk & ((value) << SPW_LINK1_PI_RM_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_PI_RCM : (SPW Offset: 0x404) ( R/ 32) SpW Link 1 Pending Read and Clear Masked Interrupt -------- */
#define SPW_LINK1_PI_RCM_DISERR_Pos           _U_(0)                                         /**< (SPW_LINK1_PI_RCM) DisErr Position */
#define SPW_LINK1_PI_RCM_DISERR_Msk           (_U_(0x1) << SPW_LINK1_PI_RCM_DISERR_Pos)      /**< (SPW_LINK1_PI_RCM) DisErr Mask */
#define SPW_LINK1_PI_RCM_PARERR_Pos           _U_(1)                                         /**< (SPW_LINK1_PI_RCM) ParErr Position */
#define SPW_LINK1_PI_RCM_PARERR_Msk           (_U_(0x1) << SPW_LINK1_PI_RCM_PARERR_Pos)      /**< (SPW_LINK1_PI_RCM) ParErr Mask */
#define SPW_LINK1_PI_RCM_ESCERR_Pos           _U_(2)                                         /**< (SPW_LINK1_PI_RCM) ESCErr Position */
#define SPW_LINK1_PI_RCM_ESCERR_Msk           (_U_(0x1) << SPW_LINK1_PI_RCM_ESCERR_Pos)      /**< (SPW_LINK1_PI_RCM) ESCErr Mask */
#define SPW_LINK1_PI_RCM_CRERR_Pos            _U_(3)                                         /**< (SPW_LINK1_PI_RCM) CrErr Position */
#define SPW_LINK1_PI_RCM_CRERR_Msk            (_U_(0x1) << SPW_LINK1_PI_RCM_CRERR_Pos)       /**< (SPW_LINK1_PI_RCM) CrErr Mask */
#define SPW_LINK1_PI_RCM_LINKABORT_Pos        _U_(4)                                         /**< (SPW_LINK1_PI_RCM) LinkAbort Position */
#define SPW_LINK1_PI_RCM_LINKABORT_Msk        (_U_(0x1) << SPW_LINK1_PI_RCM_LINKABORT_Pos)   /**< (SPW_LINK1_PI_RCM) LinkAbort Mask */
#define SPW_LINK1_PI_RCM_EEPTRANS_Pos         _U_(5)                                         /**< (SPW_LINK1_PI_RCM) EEP transmitted Position */
#define SPW_LINK1_PI_RCM_EEPTRANS_Msk         (_U_(0x1) << SPW_LINK1_PI_RCM_EEPTRANS_Pos)    /**< (SPW_LINK1_PI_RCM) EEP transmitted Mask */
#define SPW_LINK1_PI_RCM_EEPREC_Pos           _U_(6)                                         /**< (SPW_LINK1_PI_RCM) EEP received Position */
#define SPW_LINK1_PI_RCM_EEPREC_Msk           (_U_(0x1) << SPW_LINK1_PI_RCM_EEPREC_Pos)      /**< (SPW_LINK1_PI_RCM) EEP received Mask */
#define SPW_LINK1_PI_RCM_DISCARD_Pos          _U_(7)                                         /**< (SPW_LINK1_PI_RCM) Discard Position */
#define SPW_LINK1_PI_RCM_DISCARD_Msk          (_U_(0x1) << SPW_LINK1_PI_RCM_DISCARD_Pos)     /**< (SPW_LINK1_PI_RCM) Discard Mask */
#define SPW_LINK1_PI_RCM_ESCEVENT2_Pos        _U_(8)                                         /**< (SPW_LINK1_PI_RCM) Escape Event 2 Position */
#define SPW_LINK1_PI_RCM_ESCEVENT2_Msk        (_U_(0x1) << SPW_LINK1_PI_RCM_ESCEVENT2_Pos)   /**< (SPW_LINK1_PI_RCM) Escape Event 2 Mask */
#define SPW_LINK1_PI_RCM_ESCEVENT1_Pos        _U_(9)                                         /**< (SPW_LINK1_PI_RCM) Escape Event 1 Position */
#define SPW_LINK1_PI_RCM_ESCEVENT1_Msk        (_U_(0x1) << SPW_LINK1_PI_RCM_ESCEVENT1_Pos)   /**< (SPW_LINK1_PI_RCM) Escape Event 1 Mask */
#define SPW_LINK1_PI_RCM_Msk                  _U_(0x000003FF)                                /**< (SPW_LINK1_PI_RCM) Register Mask  */

#define SPW_LINK1_PI_RCM_ESCEVENT_Pos         _U_(8)                                         /**< (SPW_LINK1_PI_RCM Position) Escape Event x */
#define SPW_LINK1_PI_RCM_ESCEVENT_Msk         (_U_(0x3) << SPW_LINK1_PI_RCM_ESCEVENT_Pos)    /**< (SPW_LINK1_PI_RCM Mask) ESCEVENT */
#define SPW_LINK1_PI_RCM_ESCEVENT(value)      (SPW_LINK1_PI_RCM_ESCEVENT_Msk & ((value) << SPW_LINK1_PI_RCM_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_PI_R : (SPW Offset: 0x408) ( R/ 32) SpW Link 1 Pending Read Interrupt -------- */
#define SPW_LINK1_PI_R_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK1_PI_R) DisErr Position */
#define SPW_LINK1_PI_R_DISERR_Msk             (_U_(0x1) << SPW_LINK1_PI_R_DISERR_Pos)        /**< (SPW_LINK1_PI_R) DisErr Mask */
#define SPW_LINK1_PI_R_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK1_PI_R) ParErr Position */
#define SPW_LINK1_PI_R_PARERR_Msk             (_U_(0x1) << SPW_LINK1_PI_R_PARERR_Pos)        /**< (SPW_LINK1_PI_R) ParErr Mask */
#define SPW_LINK1_PI_R_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK1_PI_R) ESCErr Position */
#define SPW_LINK1_PI_R_ESCERR_Msk             (_U_(0x1) << SPW_LINK1_PI_R_ESCERR_Pos)        /**< (SPW_LINK1_PI_R) ESCErr Mask */
#define SPW_LINK1_PI_R_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK1_PI_R) CrErr Position */
#define SPW_LINK1_PI_R_CRERR_Msk              (_U_(0x1) << SPW_LINK1_PI_R_CRERR_Pos)         /**< (SPW_LINK1_PI_R) CrErr Mask */
#define SPW_LINK1_PI_R_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK1_PI_R) LinkAbort Position */
#define SPW_LINK1_PI_R_LINKABORT_Msk          (_U_(0x1) << SPW_LINK1_PI_R_LINKABORT_Pos)     /**< (SPW_LINK1_PI_R) LinkAbort Mask */
#define SPW_LINK1_PI_R_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK1_PI_R) EEP transmitted Position */
#define SPW_LINK1_PI_R_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK1_PI_R_EEPTRANS_Pos)      /**< (SPW_LINK1_PI_R) EEP transmitted Mask */
#define SPW_LINK1_PI_R_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK1_PI_R) EEP received Position */
#define SPW_LINK1_PI_R_EEPREC_Msk             (_U_(0x1) << SPW_LINK1_PI_R_EEPREC_Pos)        /**< (SPW_LINK1_PI_R) EEP received Mask */
#define SPW_LINK1_PI_R_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK1_PI_R) Discard Position */
#define SPW_LINK1_PI_R_DISCARD_Msk            (_U_(0x1) << SPW_LINK1_PI_R_DISCARD_Pos)       /**< (SPW_LINK1_PI_R) Discard Mask */
#define SPW_LINK1_PI_R_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK1_PI_R) Escape Event 2 Position */
#define SPW_LINK1_PI_R_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK1_PI_R_ESCEVENT2_Pos)     /**< (SPW_LINK1_PI_R) Escape Event 2 Mask */
#define SPW_LINK1_PI_R_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK1_PI_R) Escape Event 1 Position */
#define SPW_LINK1_PI_R_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK1_PI_R_ESCEVENT1_Pos)     /**< (SPW_LINK1_PI_R) Escape Event 1 Mask */
#define SPW_LINK1_PI_R_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK1_PI_R) Register Mask  */

#define SPW_LINK1_PI_R_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK1_PI_R Position) Escape Event x */
#define SPW_LINK1_PI_R_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK1_PI_R_ESCEVENT_Pos)      /**< (SPW_LINK1_PI_R Mask) ESCEVENT */
#define SPW_LINK1_PI_R_ESCEVENT(value)        (SPW_LINK1_PI_R_ESCEVENT_Msk & ((value) << SPW_LINK1_PI_R_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_PI_RCS : (SPW Offset: 0x40C) (R/W 32) SpW Link 1 Pending Read, Clear and Enabed Interrupt -------- */
#define SPW_LINK1_PI_RCS_DISERR_Pos           _U_(0)                                         /**< (SPW_LINK1_PI_RCS) DisErr Position */
#define SPW_LINK1_PI_RCS_DISERR_Msk           (_U_(0x1) << SPW_LINK1_PI_RCS_DISERR_Pos)      /**< (SPW_LINK1_PI_RCS) DisErr Mask */
#define SPW_LINK1_PI_RCS_PARERR_Pos           _U_(1)                                         /**< (SPW_LINK1_PI_RCS) ParErr Position */
#define SPW_LINK1_PI_RCS_PARERR_Msk           (_U_(0x1) << SPW_LINK1_PI_RCS_PARERR_Pos)      /**< (SPW_LINK1_PI_RCS) ParErr Mask */
#define SPW_LINK1_PI_RCS_ESCERR_Pos           _U_(2)                                         /**< (SPW_LINK1_PI_RCS) ESCErr Position */
#define SPW_LINK1_PI_RCS_ESCERR_Msk           (_U_(0x1) << SPW_LINK1_PI_RCS_ESCERR_Pos)      /**< (SPW_LINK1_PI_RCS) ESCErr Mask */
#define SPW_LINK1_PI_RCS_CRERR_Pos            _U_(3)                                         /**< (SPW_LINK1_PI_RCS) CrErr Position */
#define SPW_LINK1_PI_RCS_CRERR_Msk            (_U_(0x1) << SPW_LINK1_PI_RCS_CRERR_Pos)       /**< (SPW_LINK1_PI_RCS) CrErr Mask */
#define SPW_LINK1_PI_RCS_LINKABORT_Pos        _U_(4)                                         /**< (SPW_LINK1_PI_RCS) LinkAbort Position */
#define SPW_LINK1_PI_RCS_LINKABORT_Msk        (_U_(0x1) << SPW_LINK1_PI_RCS_LINKABORT_Pos)   /**< (SPW_LINK1_PI_RCS) LinkAbort Mask */
#define SPW_LINK1_PI_RCS_EEPTRANS_Pos         _U_(5)                                         /**< (SPW_LINK1_PI_RCS) EEP transmitted Position */
#define SPW_LINK1_PI_RCS_EEPTRANS_Msk         (_U_(0x1) << SPW_LINK1_PI_RCS_EEPTRANS_Pos)    /**< (SPW_LINK1_PI_RCS) EEP transmitted Mask */
#define SPW_LINK1_PI_RCS_EEPREC_Pos           _U_(6)                                         /**< (SPW_LINK1_PI_RCS) EEP received Position */
#define SPW_LINK1_PI_RCS_EEPREC_Msk           (_U_(0x1) << SPW_LINK1_PI_RCS_EEPREC_Pos)      /**< (SPW_LINK1_PI_RCS) EEP received Mask */
#define SPW_LINK1_PI_RCS_DISCARD_Pos          _U_(7)                                         /**< (SPW_LINK1_PI_RCS) Discard Position */
#define SPW_LINK1_PI_RCS_DISCARD_Msk          (_U_(0x1) << SPW_LINK1_PI_RCS_DISCARD_Pos)     /**< (SPW_LINK1_PI_RCS) Discard Mask */
#define SPW_LINK1_PI_RCS_ESCEVENT2_Pos        _U_(8)                                         /**< (SPW_LINK1_PI_RCS) Escape Event 2 Position */
#define SPW_LINK1_PI_RCS_ESCEVENT2_Msk        (_U_(0x1) << SPW_LINK1_PI_RCS_ESCEVENT2_Pos)   /**< (SPW_LINK1_PI_RCS) Escape Event 2 Mask */
#define SPW_LINK1_PI_RCS_ESCEVENT1_Pos        _U_(9)                                         /**< (SPW_LINK1_PI_RCS) Escape Event 1 Position */
#define SPW_LINK1_PI_RCS_ESCEVENT1_Msk        (_U_(0x1) << SPW_LINK1_PI_RCS_ESCEVENT1_Pos)   /**< (SPW_LINK1_PI_RCS) Escape Event 1 Mask */
#define SPW_LINK1_PI_RCS_Msk                  _U_(0x000003FF)                                /**< (SPW_LINK1_PI_RCS) Register Mask  */

#define SPW_LINK1_PI_RCS_ESCEVENT_Pos         _U_(8)                                         /**< (SPW_LINK1_PI_RCS Position) Escape Event x */
#define SPW_LINK1_PI_RCS_ESCEVENT_Msk         (_U_(0x3) << SPW_LINK1_PI_RCS_ESCEVENT_Pos)    /**< (SPW_LINK1_PI_RCS Mask) ESCEVENT */
#define SPW_LINK1_PI_RCS_ESCEVENT(value)      (SPW_LINK1_PI_RCS_ESCEVENT_Msk & ((value) << SPW_LINK1_PI_RCS_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_IM : (SPW Offset: 0x410) (R/W 32) SpW Link 1 Interrupt Mask -------- */
#define SPW_LINK1_IM_DISERR_Pos               _U_(0)                                         /**< (SPW_LINK1_IM) DisErr Position */
#define SPW_LINK1_IM_DISERR_Msk               (_U_(0x1) << SPW_LINK1_IM_DISERR_Pos)          /**< (SPW_LINK1_IM) DisErr Mask */
#define SPW_LINK1_IM_PARERR_Pos               _U_(1)                                         /**< (SPW_LINK1_IM) ParErr Position */
#define SPW_LINK1_IM_PARERR_Msk               (_U_(0x1) << SPW_LINK1_IM_PARERR_Pos)          /**< (SPW_LINK1_IM) ParErr Mask */
#define SPW_LINK1_IM_ESCERR_Pos               _U_(2)                                         /**< (SPW_LINK1_IM) ESCErr Position */
#define SPW_LINK1_IM_ESCERR_Msk               (_U_(0x1) << SPW_LINK1_IM_ESCERR_Pos)          /**< (SPW_LINK1_IM) ESCErr Mask */
#define SPW_LINK1_IM_CRERR_Pos                _U_(3)                                         /**< (SPW_LINK1_IM) CrErr Position */
#define SPW_LINK1_IM_CRERR_Msk                (_U_(0x1) << SPW_LINK1_IM_CRERR_Pos)           /**< (SPW_LINK1_IM) CrErr Mask */
#define SPW_LINK1_IM_LINKABORT_Pos            _U_(4)                                         /**< (SPW_LINK1_IM) LinkAbort Position */
#define SPW_LINK1_IM_LINKABORT_Msk            (_U_(0x1) << SPW_LINK1_IM_LINKABORT_Pos)       /**< (SPW_LINK1_IM) LinkAbort Mask */
#define SPW_LINK1_IM_EEPTRANS_Pos             _U_(5)                                         /**< (SPW_LINK1_IM) EEP transmitted Position */
#define SPW_LINK1_IM_EEPTRANS_Msk             (_U_(0x1) << SPW_LINK1_IM_EEPTRANS_Pos)        /**< (SPW_LINK1_IM) EEP transmitted Mask */
#define SPW_LINK1_IM_EEPREC_Pos               _U_(6)                                         /**< (SPW_LINK1_IM) EEP received Position */
#define SPW_LINK1_IM_EEPREC_Msk               (_U_(0x1) << SPW_LINK1_IM_EEPREC_Pos)          /**< (SPW_LINK1_IM) EEP received Mask */
#define SPW_LINK1_IM_DISCARD_Pos              _U_(7)                                         /**< (SPW_LINK1_IM) Discard Position */
#define SPW_LINK1_IM_DISCARD_Msk              (_U_(0x1) << SPW_LINK1_IM_DISCARD_Pos)         /**< (SPW_LINK1_IM) Discard Mask */
#define SPW_LINK1_IM_ESCEVENT2_Pos            _U_(8)                                         /**< (SPW_LINK1_IM) Escape Event 2 Position */
#define SPW_LINK1_IM_ESCEVENT2_Msk            (_U_(0x1) << SPW_LINK1_IM_ESCEVENT2_Pos)       /**< (SPW_LINK1_IM) Escape Event 2 Mask */
#define SPW_LINK1_IM_ESCEVENT1_Pos            _U_(9)                                         /**< (SPW_LINK1_IM) Escape Event 1 Position */
#define SPW_LINK1_IM_ESCEVENT1_Msk            (_U_(0x1) << SPW_LINK1_IM_ESCEVENT1_Pos)       /**< (SPW_LINK1_IM) Escape Event 1 Mask */
#define SPW_LINK1_IM_Msk                      _U_(0x000003FF)                                /**< (SPW_LINK1_IM) Register Mask  */

#define SPW_LINK1_IM_ESCEVENT_Pos             _U_(8)                                         /**< (SPW_LINK1_IM Position) Escape Event x */
#define SPW_LINK1_IM_ESCEVENT_Msk             (_U_(0x3) << SPW_LINK1_IM_ESCEVENT_Pos)        /**< (SPW_LINK1_IM Mask) ESCEVENT */
#define SPW_LINK1_IM_ESCEVENT(value)          (SPW_LINK1_IM_ESCEVENT_Msk & ((value) << SPW_LINK1_IM_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_PI_C : (SPW Offset: 0x414) ( /W 32) SpW Link 1 Clear Pending Interrupt -------- */
#define SPW_LINK1_PI_C_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK1_PI_C) DisErr Position */
#define SPW_LINK1_PI_C_DISERR_Msk             (_U_(0x1) << SPW_LINK1_PI_C_DISERR_Pos)        /**< (SPW_LINK1_PI_C) DisErr Mask */
#define SPW_LINK1_PI_C_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK1_PI_C) ParErr Position */
#define SPW_LINK1_PI_C_PARERR_Msk             (_U_(0x1) << SPW_LINK1_PI_C_PARERR_Pos)        /**< (SPW_LINK1_PI_C) ParErr Mask */
#define SPW_LINK1_PI_C_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK1_PI_C) ESCErr Position */
#define SPW_LINK1_PI_C_ESCERR_Msk             (_U_(0x1) << SPW_LINK1_PI_C_ESCERR_Pos)        /**< (SPW_LINK1_PI_C) ESCErr Mask */
#define SPW_LINK1_PI_C_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK1_PI_C) CrErr Position */
#define SPW_LINK1_PI_C_CRERR_Msk              (_U_(0x1) << SPW_LINK1_PI_C_CRERR_Pos)         /**< (SPW_LINK1_PI_C) CrErr Mask */
#define SPW_LINK1_PI_C_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK1_PI_C) LinkAbort Position */
#define SPW_LINK1_PI_C_LINKABORT_Msk          (_U_(0x1) << SPW_LINK1_PI_C_LINKABORT_Pos)     /**< (SPW_LINK1_PI_C) LinkAbort Mask */
#define SPW_LINK1_PI_C_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK1_PI_C) EEP transmitted Position */
#define SPW_LINK1_PI_C_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK1_PI_C_EEPTRANS_Pos)      /**< (SPW_LINK1_PI_C) EEP transmitted Mask */
#define SPW_LINK1_PI_C_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK1_PI_C) EEP received Position */
#define SPW_LINK1_PI_C_EEPREC_Msk             (_U_(0x1) << SPW_LINK1_PI_C_EEPREC_Pos)        /**< (SPW_LINK1_PI_C) EEP received Mask */
#define SPW_LINK1_PI_C_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK1_PI_C) Discard Position */
#define SPW_LINK1_PI_C_DISCARD_Msk            (_U_(0x1) << SPW_LINK1_PI_C_DISCARD_Pos)       /**< (SPW_LINK1_PI_C) Discard Mask */
#define SPW_LINK1_PI_C_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK1_PI_C) Escape Event 2 Position */
#define SPW_LINK1_PI_C_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK1_PI_C_ESCEVENT2_Pos)     /**< (SPW_LINK1_PI_C) Escape Event 2 Mask */
#define SPW_LINK1_PI_C_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK1_PI_C) Escape Event 1 Position */
#define SPW_LINK1_PI_C_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK1_PI_C_ESCEVENT1_Pos)     /**< (SPW_LINK1_PI_C) Escape Event 1 Mask */
#define SPW_LINK1_PI_C_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK1_PI_C) Register Mask  */

#define SPW_LINK1_PI_C_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK1_PI_C Position) Escape Event x */
#define SPW_LINK1_PI_C_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK1_PI_C_ESCEVENT_Pos)      /**< (SPW_LINK1_PI_C Mask) ESCEVENT */
#define SPW_LINK1_PI_C_ESCEVENT(value)        (SPW_LINK1_PI_C_ESCEVENT_Msk & ((value) << SPW_LINK1_PI_C_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_IM_S : (SPW Offset: 0x418) ( /W 32) SpW Link 1 Interrupt Set Mask -------- */
#define SPW_LINK1_IM_S_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK1_IM_S) DisErr Position */
#define SPW_LINK1_IM_S_DISERR_Msk             (_U_(0x1) << SPW_LINK1_IM_S_DISERR_Pos)        /**< (SPW_LINK1_IM_S) DisErr Mask */
#define SPW_LINK1_IM_S_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK1_IM_S) ParErr Position */
#define SPW_LINK1_IM_S_PARERR_Msk             (_U_(0x1) << SPW_LINK1_IM_S_PARERR_Pos)        /**< (SPW_LINK1_IM_S) ParErr Mask */
#define SPW_LINK1_IM_S_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK1_IM_S) ESCErr Position */
#define SPW_LINK1_IM_S_ESCERR_Msk             (_U_(0x1) << SPW_LINK1_IM_S_ESCERR_Pos)        /**< (SPW_LINK1_IM_S) ESCErr Mask */
#define SPW_LINK1_IM_S_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK1_IM_S) CrErr Position */
#define SPW_LINK1_IM_S_CRERR_Msk              (_U_(0x1) << SPW_LINK1_IM_S_CRERR_Pos)         /**< (SPW_LINK1_IM_S) CrErr Mask */
#define SPW_LINK1_IM_S_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK1_IM_S) LinkAbort Position */
#define SPW_LINK1_IM_S_LINKABORT_Msk          (_U_(0x1) << SPW_LINK1_IM_S_LINKABORT_Pos)     /**< (SPW_LINK1_IM_S) LinkAbort Mask */
#define SPW_LINK1_IM_S_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK1_IM_S) EEP transmitted Position */
#define SPW_LINK1_IM_S_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK1_IM_S_EEPTRANS_Pos)      /**< (SPW_LINK1_IM_S) EEP transmitted Mask */
#define SPW_LINK1_IM_S_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK1_IM_S) EEP received Position */
#define SPW_LINK1_IM_S_EEPREC_Msk             (_U_(0x1) << SPW_LINK1_IM_S_EEPREC_Pos)        /**< (SPW_LINK1_IM_S) EEP received Mask */
#define SPW_LINK1_IM_S_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK1_IM_S) Discard Position */
#define SPW_LINK1_IM_S_DISCARD_Msk            (_U_(0x1) << SPW_LINK1_IM_S_DISCARD_Pos)       /**< (SPW_LINK1_IM_S) Discard Mask */
#define SPW_LINK1_IM_S_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK1_IM_S) Escape Event 2 Position */
#define SPW_LINK1_IM_S_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK1_IM_S_ESCEVENT2_Pos)     /**< (SPW_LINK1_IM_S) Escape Event 2 Mask */
#define SPW_LINK1_IM_S_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK1_IM_S) Escape Event 1 Position */
#define SPW_LINK1_IM_S_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK1_IM_S_ESCEVENT1_Pos)     /**< (SPW_LINK1_IM_S) Escape Event 1 Mask */
#define SPW_LINK1_IM_S_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK1_IM_S) Register Mask  */

#define SPW_LINK1_IM_S_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK1_IM_S Position) Escape Event x */
#define SPW_LINK1_IM_S_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK1_IM_S_ESCEVENT_Pos)      /**< (SPW_LINK1_IM_S Mask) ESCEVENT */
#define SPW_LINK1_IM_S_ESCEVENT(value)        (SPW_LINK1_IM_S_ESCEVENT_Msk & ((value) << SPW_LINK1_IM_S_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_IM_C : (SPW Offset: 0x41C) ( /W 32) SpW Link 1 Interrupt Clear Mask -------- */
#define SPW_LINK1_IM_C_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK1_IM_C) DisErr Position */
#define SPW_LINK1_IM_C_DISERR_Msk             (_U_(0x1) << SPW_LINK1_IM_C_DISERR_Pos)        /**< (SPW_LINK1_IM_C) DisErr Mask */
#define SPW_LINK1_IM_C_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK1_IM_C) ParErr Position */
#define SPW_LINK1_IM_C_PARERR_Msk             (_U_(0x1) << SPW_LINK1_IM_C_PARERR_Pos)        /**< (SPW_LINK1_IM_C) ParErr Mask */
#define SPW_LINK1_IM_C_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK1_IM_C) ESCErr Position */
#define SPW_LINK1_IM_C_ESCERR_Msk             (_U_(0x1) << SPW_LINK1_IM_C_ESCERR_Pos)        /**< (SPW_LINK1_IM_C) ESCErr Mask */
#define SPW_LINK1_IM_C_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK1_IM_C) CrErr Position */
#define SPW_LINK1_IM_C_CRERR_Msk              (_U_(0x1) << SPW_LINK1_IM_C_CRERR_Pos)         /**< (SPW_LINK1_IM_C) CrErr Mask */
#define SPW_LINK1_IM_C_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK1_IM_C) LinkAbort Position */
#define SPW_LINK1_IM_C_LINKABORT_Msk          (_U_(0x1) << SPW_LINK1_IM_C_LINKABORT_Pos)     /**< (SPW_LINK1_IM_C) LinkAbort Mask */
#define SPW_LINK1_IM_C_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK1_IM_C) EEP transmitted Position */
#define SPW_LINK1_IM_C_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK1_IM_C_EEPTRANS_Pos)      /**< (SPW_LINK1_IM_C) EEP transmitted Mask */
#define SPW_LINK1_IM_C_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK1_IM_C) EEP received Position */
#define SPW_LINK1_IM_C_EEPREC_Msk             (_U_(0x1) << SPW_LINK1_IM_C_EEPREC_Pos)        /**< (SPW_LINK1_IM_C) EEP received Mask */
#define SPW_LINK1_IM_C_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK1_IM_C) Discard Position */
#define SPW_LINK1_IM_C_DISCARD_Msk            (_U_(0x1) << SPW_LINK1_IM_C_DISCARD_Pos)       /**< (SPW_LINK1_IM_C) Discard Mask */
#define SPW_LINK1_IM_C_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK1_IM_C) Escape Event 2 Position */
#define SPW_LINK1_IM_C_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK1_IM_C_ESCEVENT2_Pos)     /**< (SPW_LINK1_IM_C) Escape Event 2 Mask */
#define SPW_LINK1_IM_C_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK1_IM_C) Escape Event 1 Position */
#define SPW_LINK1_IM_C_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK1_IM_C_ESCEVENT1_Pos)     /**< (SPW_LINK1_IM_C) Escape Event 1 Mask */
#define SPW_LINK1_IM_C_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK1_IM_C) Register Mask  */

#define SPW_LINK1_IM_C_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK1_IM_C Position) Escape Event x */
#define SPW_LINK1_IM_C_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK1_IM_C_ESCEVENT_Pos)      /**< (SPW_LINK1_IM_C Mask) ESCEVENT */
#define SPW_LINK1_IM_C_ESCEVENT(value)        (SPW_LINK1_IM_C_ESCEVENT_Msk & ((value) << SPW_LINK1_IM_C_ESCEVENT_Pos)) 

/* -------- SPW_LINK1_CFG : (SPW Offset: 0x420) (R/W 32) SpW Link 1 Config -------- */
#define SPW_LINK1_CFG_COMMAND_Pos             _U_(0)                                         /**< (SPW_LINK1_CFG) Command Position */
#define SPW_LINK1_CFG_COMMAND_Msk             (_U_(0x3) << SPW_LINK1_CFG_COMMAND_Pos)        /**< (SPW_LINK1_CFG) Command Mask */
#define SPW_LINK1_CFG_COMMAND(value)          (SPW_LINK1_CFG_COMMAND_Msk & ((value) << SPW_LINK1_CFG_COMMAND_Pos))
#define   SPW_LINK1_CFG_COMMAND_LINK_DISABLE_Val _U_(0x0)                                       /**< (SPW_LINK1_CFG) The link proceeds directly to the ErrorReset state when reaching the Run state.  */
#define   SPW_LINK1_CFG_COMMAND_NO_COMMAND_Val _U_(0x1)                                       /**< (SPW_LINK1_CFG) State is not actively changed.  */
#define   SPW_LINK1_CFG_COMMAND_AUTO_START_Val _U_(0x2)                                       /**< (SPW_LINK1_CFG) The Codec will wait in state Ready until the first NULL character is received.  */
#define   SPW_LINK1_CFG_COMMAND_LINK_START_Val _U_(0x3)                                       /**< (SPW_LINK1_CFG) SpaceWire link can proceed to Started state.  */
#define SPW_LINK1_CFG_COMMAND_LINK_DISABLE    (SPW_LINK1_CFG_COMMAND_LINK_DISABLE_Val << SPW_LINK1_CFG_COMMAND_Pos) /**< (SPW_LINK1_CFG) The link proceeds directly to the ErrorReset state when reaching the Run state. Position  */
#define SPW_LINK1_CFG_COMMAND_NO_COMMAND      (SPW_LINK1_CFG_COMMAND_NO_COMMAND_Val << SPW_LINK1_CFG_COMMAND_Pos) /**< (SPW_LINK1_CFG) State is not actively changed. Position  */
#define SPW_LINK1_CFG_COMMAND_AUTO_START      (SPW_LINK1_CFG_COMMAND_AUTO_START_Val << SPW_LINK1_CFG_COMMAND_Pos) /**< (SPW_LINK1_CFG) The Codec will wait in state Ready until the first NULL character is received. Position  */
#define SPW_LINK1_CFG_COMMAND_LINK_START      (SPW_LINK1_CFG_COMMAND_LINK_START_Val << SPW_LINK1_CFG_COMMAND_Pos) /**< (SPW_LINK1_CFG) SpaceWire link can proceed to Started state. Position  */
#define SPW_LINK1_CFG_Msk                     _U_(0x00000003)                                /**< (SPW_LINK1_CFG) Register Mask  */


/* -------- SPW_LINK1_CLKDIV : (SPW Offset: 0x424) (R/W 32) SpW Link 1 Clock Division -------- */
#define SPW_LINK1_CLKDIV_TXOPERDIV_Pos        _U_(0)                                         /**< (SPW_LINK1_CLKDIV) TxOperDiv Position */
#define SPW_LINK1_CLKDIV_TXOPERDIV_Msk        (_U_(0x1F) << SPW_LINK1_CLKDIV_TXOPERDIV_Pos)  /**< (SPW_LINK1_CLKDIV) TxOperDiv Mask */
#define SPW_LINK1_CLKDIV_TXOPERDIV(value)     (SPW_LINK1_CLKDIV_TXOPERDIV_Msk & ((value) << SPW_LINK1_CLKDIV_TXOPERDIV_Pos))
#define SPW_LINK1_CLKDIV_TXINITDIV_Pos        _U_(16)                                        /**< (SPW_LINK1_CLKDIV) TxInitDiv Position */
#define SPW_LINK1_CLKDIV_TXINITDIV_Msk        (_U_(0x1F) << SPW_LINK1_CLKDIV_TXINITDIV_Pos)  /**< (SPW_LINK1_CLKDIV) TxInitDiv Mask */
#define SPW_LINK1_CLKDIV_TXINITDIV(value)     (SPW_LINK1_CLKDIV_TXINITDIV_Msk & ((value) << SPW_LINK1_CLKDIV_TXINITDIV_Pos))
#define SPW_LINK1_CLKDIV_Msk                  _U_(0x001F001F)                                /**< (SPW_LINK1_CLKDIV) Register Mask  */


/* -------- SPW_LINK1_STATUS : (SPW Offset: 0x428) ( R/ 32) SpW Link 1 Status -------- */
#define SPW_LINK1_STATUS_LINKSTATE_Pos        _U_(0)                                         /**< (SPW_LINK1_STATUS) LinkState Position */
#define SPW_LINK1_STATUS_LINKSTATE_Msk        (_U_(0x7) << SPW_LINK1_STATUS_LINKSTATE_Pos)   /**< (SPW_LINK1_STATUS) LinkState Mask */
#define SPW_LINK1_STATUS_LINKSTATE(value)     (SPW_LINK1_STATUS_LINKSTATE_Msk & ((value) << SPW_LINK1_STATUS_LINKSTATE_Pos))
#define   SPW_LINK1_STATUS_LINKSTATE_ERRORRESET_Val _U_(0x0)                                       /**< (SPW_LINK1_STATUS) CODEC link state machine in ErrorReset state  */
#define   SPW_LINK1_STATUS_LINKSTATE_ERRORWAIT_Val _U_(0x1)                                       /**< (SPW_LINK1_STATUS) CODEC link state machine in ErrorWait state  */
#define   SPW_LINK1_STATUS_LINKSTATE_READY_Val _U_(0x2)                                       /**< (SPW_LINK1_STATUS) CODEC link state machine in Ready state  */
#define   SPW_LINK1_STATUS_LINKSTATE_STARTED_Val _U_(0x3)                                       /**< (SPW_LINK1_STATUS) CODEC link state machine in Started state  */
#define   SPW_LINK1_STATUS_LINKSTATE_CONNECTING_Val _U_(0x4)                                       /**< (SPW_LINK1_STATUS) CODEC link state machine in Connecting state  */
#define   SPW_LINK1_STATUS_LINKSTATE_RUN_Val  _U_(0x5)                                       /**< (SPW_LINK1_STATUS) CODEC link state machine in Run state  */
#define SPW_LINK1_STATUS_LINKSTATE_ERRORRESET (SPW_LINK1_STATUS_LINKSTATE_ERRORRESET_Val << SPW_LINK1_STATUS_LINKSTATE_Pos) /**< (SPW_LINK1_STATUS) CODEC link state machine in ErrorReset state Position  */
#define SPW_LINK1_STATUS_LINKSTATE_ERRORWAIT  (SPW_LINK1_STATUS_LINKSTATE_ERRORWAIT_Val << SPW_LINK1_STATUS_LINKSTATE_Pos) /**< (SPW_LINK1_STATUS) CODEC link state machine in ErrorWait state Position  */
#define SPW_LINK1_STATUS_LINKSTATE_READY      (SPW_LINK1_STATUS_LINKSTATE_READY_Val << SPW_LINK1_STATUS_LINKSTATE_Pos) /**< (SPW_LINK1_STATUS) CODEC link state machine in Ready state Position  */
#define SPW_LINK1_STATUS_LINKSTATE_STARTED    (SPW_LINK1_STATUS_LINKSTATE_STARTED_Val << SPW_LINK1_STATUS_LINKSTATE_Pos) /**< (SPW_LINK1_STATUS) CODEC link state machine in Started state Position  */
#define SPW_LINK1_STATUS_LINKSTATE_CONNECTING (SPW_LINK1_STATUS_LINKSTATE_CONNECTING_Val << SPW_LINK1_STATUS_LINKSTATE_Pos) /**< (SPW_LINK1_STATUS) CODEC link state machine in Connecting state Position  */
#define SPW_LINK1_STATUS_LINKSTATE_RUN        (SPW_LINK1_STATUS_LINKSTATE_RUN_Val << SPW_LINK1_STATUS_LINKSTATE_Pos) /**< (SPW_LINK1_STATUS) CODEC link state machine in Run state Position  */
#define SPW_LINK1_STATUS_TXDEFDIV_Pos         _U_(4)                                         /**< (SPW_LINK1_STATUS) TxDefDiv Position */
#define SPW_LINK1_STATUS_TXDEFDIV_Msk         (_U_(0x1F) << SPW_LINK1_STATUS_TXDEFDIV_Pos)   /**< (SPW_LINK1_STATUS) TxDefDiv Mask */
#define SPW_LINK1_STATUS_TXDEFDIV(value)      (SPW_LINK1_STATUS_TXDEFDIV_Msk & ((value) << SPW_LINK1_STATUS_TXDEFDIV_Pos))
#define SPW_LINK1_STATUS_TXEMPTY_Pos          _U_(16)                                        /**< (SPW_LINK1_STATUS) TxEmpty Position */
#define SPW_LINK1_STATUS_TXEMPTY_Msk          (_U_(0x1) << SPW_LINK1_STATUS_TXEMPTY_Pos)     /**< (SPW_LINK1_STATUS) TxEmpty Mask */
#define SPW_LINK1_STATUS_GOTNULL_Pos          _U_(17)                                        /**< (SPW_LINK1_STATUS) GotNull Position */
#define SPW_LINK1_STATUS_GOTNULL_Msk          (_U_(0x1) << SPW_LINK1_STATUS_GOTNULL_Pos)     /**< (SPW_LINK1_STATUS) GotNull Mask */
#define SPW_LINK1_STATUS_GOTFCT_Pos           _U_(18)                                        /**< (SPW_LINK1_STATUS) GotFCT Position */
#define SPW_LINK1_STATUS_GOTFCT_Msk           (_U_(0x1) << SPW_LINK1_STATUS_GOTFCT_Pos)      /**< (SPW_LINK1_STATUS) GotFCT Mask */
#define SPW_LINK1_STATUS_GOTNCHAR_Pos         _U_(19)                                        /**< (SPW_LINK1_STATUS) GotNChar Position */
#define SPW_LINK1_STATUS_GOTNCHAR_Msk         (_U_(0x1) << SPW_LINK1_STATUS_GOTNCHAR_Pos)    /**< (SPW_LINK1_STATUS) GotNChar Mask */
#define SPW_LINK1_STATUS_SEEN0_Pos            _U_(20)                                        /**< (SPW_LINK1_STATUS) SEEN0 Position */
#define SPW_LINK1_STATUS_SEEN0_Msk            (_U_(0x1) << SPW_LINK1_STATUS_SEEN0_Pos)       /**< (SPW_LINK1_STATUS) SEEN0 Mask */
#define SPW_LINK1_STATUS_SEEN1_Pos            _U_(21)                                        /**< (SPW_LINK1_STATUS) SEEN1 Position */
#define SPW_LINK1_STATUS_SEEN1_Msk            (_U_(0x1) << SPW_LINK1_STATUS_SEEN1_Pos)       /**< (SPW_LINK1_STATUS) SEEN1 Mask */
#define SPW_LINK1_STATUS_SEEN2_Pos            _U_(22)                                        /**< (SPW_LINK1_STATUS) SEEN2 Position */
#define SPW_LINK1_STATUS_SEEN2_Msk            (_U_(0x1) << SPW_LINK1_STATUS_SEEN2_Pos)       /**< (SPW_LINK1_STATUS) SEEN2 Mask */
#define SPW_LINK1_STATUS_SEEN3_Pos            _U_(23)                                        /**< (SPW_LINK1_STATUS) SEEN3 Position */
#define SPW_LINK1_STATUS_SEEN3_Msk            (_U_(0x1) << SPW_LINK1_STATUS_SEEN3_Pos)       /**< (SPW_LINK1_STATUS) SEEN3 Mask */
#define SPW_LINK1_STATUS_SEEN4_Pos            _U_(24)                                        /**< (SPW_LINK1_STATUS) SEEN4 Position */
#define SPW_LINK1_STATUS_SEEN4_Msk            (_U_(0x1) << SPW_LINK1_STATUS_SEEN4_Pos)       /**< (SPW_LINK1_STATUS) SEEN4 Mask */
#define SPW_LINK1_STATUS_SEEN5_Pos            _U_(25)                                        /**< (SPW_LINK1_STATUS) SEEN5 Position */
#define SPW_LINK1_STATUS_SEEN5_Msk            (_U_(0x1) << SPW_LINK1_STATUS_SEEN5_Pos)       /**< (SPW_LINK1_STATUS) SEEN5 Mask */
#define SPW_LINK1_STATUS_Msk                  _U_(0x03FF01F7)                                /**< (SPW_LINK1_STATUS) Register Mask  */

#define SPW_LINK1_STATUS_SEEN_Pos             _U_(20)                                        /**< (SPW_LINK1_STATUS Position) SEEN5 */
#define SPW_LINK1_STATUS_SEEN_Msk             (_U_(0x3F) << SPW_LINK1_STATUS_SEEN_Pos)       /**< (SPW_LINK1_STATUS Mask) SEEN */
#define SPW_LINK1_STATUS_SEEN(value)          (SPW_LINK1_STATUS_SEEN_Msk & ((value) << SPW_LINK1_STATUS_SEEN_Pos)) 

/* -------- SPW_LINK1_SWRESET : (SPW Offset: 0x42C) (R/W 32) SpW Link 1 Software Reset -------- */
#define SPW_LINK1_SWRESET_PATTERN_Pos         _U_(0)                                         /**< (SPW_LINK1_SWRESET) Pattern Position */
#define SPW_LINK1_SWRESET_PATTERN_Msk         (_U_(0xFFFFFFFF) << SPW_LINK1_SWRESET_PATTERN_Pos) /**< (SPW_LINK1_SWRESET) Pattern Mask */
#define SPW_LINK1_SWRESET_PATTERN(value)      (SPW_LINK1_SWRESET_PATTERN_Msk & ((value) << SPW_LINK1_SWRESET_PATTERN_Pos))
#define SPW_LINK1_SWRESET_Msk                 _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_SWRESET) Register Mask  */


/* -------- SPW_LINK1_ESCCHAREVENT0 : (SPW Offset: 0x430) (R/W 32) SpW Link 1 Escape Character Event 0 -------- */
#define SPW_LINK1_ESCCHAREVENT0_VALUE_Pos     _U_(0)                                         /**< (SPW_LINK1_ESCCHAREVENT0) Value Position */
#define SPW_LINK1_ESCCHAREVENT0_VALUE_Msk     (_U_(0xFF) << SPW_LINK1_ESCCHAREVENT0_VALUE_Pos) /**< (SPW_LINK1_ESCCHAREVENT0) Value Mask */
#define SPW_LINK1_ESCCHAREVENT0_VALUE(value)  (SPW_LINK1_ESCCHAREVENT0_VALUE_Msk & ((value) << SPW_LINK1_ESCCHAREVENT0_VALUE_Pos))
#define SPW_LINK1_ESCCHAREVENT0_MASK_Pos      _U_(8)                                         /**< (SPW_LINK1_ESCCHAREVENT0) Mask Position */
#define SPW_LINK1_ESCCHAREVENT0_MASK_Msk      (_U_(0xFF) << SPW_LINK1_ESCCHAREVENT0_MASK_Pos) /**< (SPW_LINK1_ESCCHAREVENT0) Mask Mask */
#define SPW_LINK1_ESCCHAREVENT0_MASK(value)   (SPW_LINK1_ESCCHAREVENT0_MASK_Msk & ((value) << SPW_LINK1_ESCCHAREVENT0_MASK_Pos))
#define SPW_LINK1_ESCCHAREVENT0_ACTIVE_Pos    _U_(16)                                        /**< (SPW_LINK1_ESCCHAREVENT0) Active Position */
#define SPW_LINK1_ESCCHAREVENT0_ACTIVE_Msk    (_U_(0x1) << SPW_LINK1_ESCCHAREVENT0_ACTIVE_Pos) /**< (SPW_LINK1_ESCCHAREVENT0) Active Mask */
#define SPW_LINK1_ESCCHAREVENT0_HWEVENT_Pos   _U_(17)                                        /**< (SPW_LINK1_ESCCHAREVENT0) HwEvent Position */
#define SPW_LINK1_ESCCHAREVENT0_HWEVENT_Msk   (_U_(0x1) << SPW_LINK1_ESCCHAREVENT0_HWEVENT_Pos) /**< (SPW_LINK1_ESCCHAREVENT0) HwEvent Mask */
#define SPW_LINK1_ESCCHAREVENT0_Msk           _U_(0x0003FFFF)                                /**< (SPW_LINK1_ESCCHAREVENT0) Register Mask  */


/* -------- SPW_LINK1_ESCCHAREVENT1 : (SPW Offset: 0x434) (R/W 32) SpW Link 1 Escape Character Event 1 -------- */
#define SPW_LINK1_ESCCHAREVENT1_VALUE_Pos     _U_(0)                                         /**< (SPW_LINK1_ESCCHAREVENT1) Value Position */
#define SPW_LINK1_ESCCHAREVENT1_VALUE_Msk     (_U_(0xFF) << SPW_LINK1_ESCCHAREVENT1_VALUE_Pos) /**< (SPW_LINK1_ESCCHAREVENT1) Value Mask */
#define SPW_LINK1_ESCCHAREVENT1_VALUE(value)  (SPW_LINK1_ESCCHAREVENT1_VALUE_Msk & ((value) << SPW_LINK1_ESCCHAREVENT1_VALUE_Pos))
#define SPW_LINK1_ESCCHAREVENT1_MASK_Pos      _U_(8)                                         /**< (SPW_LINK1_ESCCHAREVENT1) Mask Position */
#define SPW_LINK1_ESCCHAREVENT1_MASK_Msk      (_U_(0xFF) << SPW_LINK1_ESCCHAREVENT1_MASK_Pos) /**< (SPW_LINK1_ESCCHAREVENT1) Mask Mask */
#define SPW_LINK1_ESCCHAREVENT1_MASK(value)   (SPW_LINK1_ESCCHAREVENT1_MASK_Msk & ((value) << SPW_LINK1_ESCCHAREVENT1_MASK_Pos))
#define SPW_LINK1_ESCCHAREVENT1_ACTIVE_Pos    _U_(16)                                        /**< (SPW_LINK1_ESCCHAREVENT1) Active Position */
#define SPW_LINK1_ESCCHAREVENT1_ACTIVE_Msk    (_U_(0x1) << SPW_LINK1_ESCCHAREVENT1_ACTIVE_Pos) /**< (SPW_LINK1_ESCCHAREVENT1) Active Mask */
#define SPW_LINK1_ESCCHAREVENT1_HWEVENT_Pos   _U_(17)                                        /**< (SPW_LINK1_ESCCHAREVENT1) HwEvent Position */
#define SPW_LINK1_ESCCHAREVENT1_HWEVENT_Msk   (_U_(0x1) << SPW_LINK1_ESCCHAREVENT1_HWEVENT_Pos) /**< (SPW_LINK1_ESCCHAREVENT1) HwEvent Mask */
#define SPW_LINK1_ESCCHAREVENT1_Msk           _U_(0x0003FFFF)                                /**< (SPW_LINK1_ESCCHAREVENT1) Register Mask  */


/* -------- SPW_LINK1_ESCCHARSTS : (SPW Offset: 0x438) ( R/ 32) SpW Link 1 Escape Character Status -------- */
#define SPW_LINK1_ESCCHARSTS_CHAR1_Pos        _U_(0)                                         /**< (SPW_LINK1_ESCCHARSTS) Esc Char 1 Position */
#define SPW_LINK1_ESCCHARSTS_CHAR1_Msk        (_U_(0xFF) << SPW_LINK1_ESCCHARSTS_CHAR1_Pos)  /**< (SPW_LINK1_ESCCHARSTS) Esc Char 1 Mask */
#define SPW_LINK1_ESCCHARSTS_CHAR1(value)     (SPW_LINK1_ESCCHARSTS_CHAR1_Msk & ((value) << SPW_LINK1_ESCCHARSTS_CHAR1_Pos))
#define SPW_LINK1_ESCCHARSTS_CHAR2_Pos        _U_(8)                                         /**< (SPW_LINK1_ESCCHARSTS) Esc Char 2 Position */
#define SPW_LINK1_ESCCHARSTS_CHAR2_Msk        (_U_(0xFF) << SPW_LINK1_ESCCHARSTS_CHAR2_Pos)  /**< (SPW_LINK1_ESCCHARSTS) Esc Char 2 Mask */
#define SPW_LINK1_ESCCHARSTS_CHAR2(value)     (SPW_LINK1_ESCCHARSTS_CHAR2_Msk & ((value) << SPW_LINK1_ESCCHARSTS_CHAR2_Pos))
#define SPW_LINK1_ESCCHARSTS_Msk              _U_(0x0000FFFF)                                /**< (SPW_LINK1_ESCCHARSTS) Register Mask  */


/* -------- SPW_LINK1_TRANSESC : (SPW Offset: 0x43C) (R/W 32) SpW Link 1 Transmit Escape Character -------- */
#define SPW_LINK1_TRANSESC_CHAR_Pos           _U_(0)                                         /**< (SPW_LINK1_TRANSESC) Character Position */
#define SPW_LINK1_TRANSESC_CHAR_Msk           (_U_(0xFF) << SPW_LINK1_TRANSESC_CHAR_Pos)     /**< (SPW_LINK1_TRANSESC) Character Mask */
#define SPW_LINK1_TRANSESC_CHAR(value)        (SPW_LINK1_TRANSESC_CHAR_Msk & ((value) << SPW_LINK1_TRANSESC_CHAR_Pos))
#define SPW_LINK1_TRANSESC_Msk                _U_(0x000000FF)                                /**< (SPW_LINK1_TRANSESC) Register Mask  */


/* -------- SPW_LINK1_DISTINTPI_RM : (SPW Offset: 0x440) ( R/ 32) SpW Link 1 Distributed Interrupt Pending Read Masked Interrupt -------- */
#define SPW_LINK1_DISTINTPI_RM_DI0_Pos        _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI0_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI0_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI1_Pos        _U_(1)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI1_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI1_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI2_Pos        _U_(2)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI2_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI2_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI3_Pos        _U_(3)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI3_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI3_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI4_Pos        _U_(4)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI4_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI4_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI5_Pos        _U_(5)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI5_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI5_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI6_Pos        _U_(6)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI6_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI6_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI7_Pos        _U_(7)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI7_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI7_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI8_Pos        _U_(8)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI8_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI8_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI9_Pos        _U_(9)                                         /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI9_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI9_Pos)   /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI10_Pos       _U_(10)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI10_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI10_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI11_Pos       _U_(11)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI11_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI11_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI12_Pos       _U_(12)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI12_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI12_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI13_Pos       _U_(13)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI13_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI13_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI14_Pos       _U_(14)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI14_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI14_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI15_Pos       _U_(15)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI15_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI15_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI16_Pos       _U_(16)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI16_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI16_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI17_Pos       _U_(17)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI17_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI17_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI18_Pos       _U_(18)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI18_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI18_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI19_Pos       _U_(19)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI19_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI19_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI20_Pos       _U_(20)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI20_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI20_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI21_Pos       _U_(21)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI21_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI21_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI22_Pos       _U_(22)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI22_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI22_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI23_Pos       _U_(23)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI23_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI23_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI24_Pos       _U_(24)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI24_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI24_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI25_Pos       _U_(25)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI25_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI25_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI26_Pos       _U_(26)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI26_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI26_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI27_Pos       _U_(27)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI27_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI27_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI28_Pos       _U_(28)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI28_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI28_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI29_Pos       _U_(29)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI29_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI29_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI30_Pos       _U_(30)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI30_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI30_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_DI31_Pos       _U_(31)                                        /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RM_DI31_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RM_DI31_Pos)  /**< (SPW_LINK1_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RM_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTPI_RM) Register Mask  */

#define SPW_LINK1_DISTINTPI_RM_DI_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_RM Position) Distributed Interrupt */
#define SPW_LINK1_DISTINTPI_RM_DI_Msk         (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTPI_RM_DI_Pos) /**< (SPW_LINK1_DISTINTPI_RM Mask) DI */
#define SPW_LINK1_DISTINTPI_RM_DI(value)      (SPW_LINK1_DISTINTPI_RM_DI_Msk & ((value) << SPW_LINK1_DISTINTPI_RM_DI_Pos)) 

/* -------- SPW_LINK1_DISTINTPI_RCM : (SPW Offset: 0x444) ( R/ 32) SpW Link 1 Distributed Interrupt Pending Read and Clear Masked Interrupt -------- */
#define SPW_LINK1_DISTINTPI_RCM_DI0_Pos       _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI0_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI0_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI1_Pos       _U_(1)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI1_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI1_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI2_Pos       _U_(2)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI2_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI2_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI3_Pos       _U_(3)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI3_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI3_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI4_Pos       _U_(4)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI4_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI4_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI5_Pos       _U_(5)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI5_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI5_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI6_Pos       _U_(6)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI6_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI6_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI7_Pos       _U_(7)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI7_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI7_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI8_Pos       _U_(8)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI8_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI8_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI9_Pos       _U_(9)                                         /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI9_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI9_Pos)  /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI10_Pos      _U_(10)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI10_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI10_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI11_Pos      _U_(11)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI11_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI11_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI12_Pos      _U_(12)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI12_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI12_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI13_Pos      _U_(13)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI13_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI13_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI14_Pos      _U_(14)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI14_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI14_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI15_Pos      _U_(15)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI15_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI15_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI16_Pos      _U_(16)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI16_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI16_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI17_Pos      _U_(17)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI17_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI17_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI18_Pos      _U_(18)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI18_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI18_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI19_Pos      _U_(19)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI19_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI19_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI20_Pos      _U_(20)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI20_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI20_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI21_Pos      _U_(21)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI21_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI21_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI22_Pos      _U_(22)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI22_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI22_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI23_Pos      _U_(23)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI23_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI23_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI24_Pos      _U_(24)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI24_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI24_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI25_Pos      _U_(25)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI25_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI25_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI26_Pos      _U_(26)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI26_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI26_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI27_Pos      _U_(27)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI27_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI27_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI28_Pos      _U_(28)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI28_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI28_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI29_Pos      _U_(29)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI29_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI29_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI30_Pos      _U_(30)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI30_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI30_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_DI31_Pos      _U_(31)                                        /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCM_DI31_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCM_DI31_Pos) /**< (SPW_LINK1_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCM_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTPI_RCM) Register Mask  */

#define SPW_LINK1_DISTINTPI_RCM_DI_Pos        _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_RCM Position) Distributed Interrupt */
#define SPW_LINK1_DISTINTPI_RCM_DI_Msk        (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTPI_RCM_DI_Pos) /**< (SPW_LINK1_DISTINTPI_RCM Mask) DI */
#define SPW_LINK1_DISTINTPI_RCM_DI(value)     (SPW_LINK1_DISTINTPI_RCM_DI_Msk & ((value) << SPW_LINK1_DISTINTPI_RCM_DI_Pos)) 

/* -------- SPW_LINK1_DISTINTPI_R : (SPW Offset: 0x448) ( R/ 32) SpW Link 1 Distributed Interrupt Pending Read Interrupt -------- */
#define SPW_LINK1_DISTINTPI_R_DI0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI0_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI0_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI1_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI1_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI2_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI2_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI3_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI3_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI4_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI4_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI5_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI5_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI6_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI6_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI7_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI7_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI8_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI8_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI9_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI9_Pos)    /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI10_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI10_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI11_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI11_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI12_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI12_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI13_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI13_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI14_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI14_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI15_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI15_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI16_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI16_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI17_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI17_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI18_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI18_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI19_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI19_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI20_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI20_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI21_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI21_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI22_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI22_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI23_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI23_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI24_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI24_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI25_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI25_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI26_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI26_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI27_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI27_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI28_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI28_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI29_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI29_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI30_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI30_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_DI31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_R_DI31_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_R_DI31_Pos)   /**< (SPW_LINK1_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_R_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTPI_R) Register Mask  */

#define SPW_LINK1_DISTINTPI_R_DI_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_R Position) Distributed Interrupt */
#define SPW_LINK1_DISTINTPI_R_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTPI_R_DI_Pos) /**< (SPW_LINK1_DISTINTPI_R Mask) DI */
#define SPW_LINK1_DISTINTPI_R_DI(value)       (SPW_LINK1_DISTINTPI_R_DI_Msk & ((value) << SPW_LINK1_DISTINTPI_R_DI_Pos)) 

/* -------- SPW_LINK1_DISTINTPI_RCS : (SPW Offset: 0x44C) (R/W 32) SpW Link 1 Distributed Interrupt Pending Read and Clear Interrupt -------- */
#define SPW_LINK1_DISTINTPI_RCS_DI0_Pos       _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI0_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI0_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI1_Pos       _U_(1)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI1_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI1_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI2_Pos       _U_(2)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI2_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI2_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI3_Pos       _U_(3)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI3_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI3_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI4_Pos       _U_(4)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI4_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI4_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI5_Pos       _U_(5)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI5_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI5_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI6_Pos       _U_(6)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI6_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI6_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI7_Pos       _U_(7)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI7_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI7_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI8_Pos       _U_(8)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI8_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI8_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI9_Pos       _U_(9)                                         /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI9_Msk       (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI9_Pos)  /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI10_Pos      _U_(10)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI10_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI10_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI11_Pos      _U_(11)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI11_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI11_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI12_Pos      _U_(12)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI12_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI12_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI13_Pos      _U_(13)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI13_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI13_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI14_Pos      _U_(14)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI14_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI14_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI15_Pos      _U_(15)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI15_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI15_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI16_Pos      _U_(16)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI16_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI16_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI17_Pos      _U_(17)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI17_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI17_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI18_Pos      _U_(18)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI18_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI18_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI19_Pos      _U_(19)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI19_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI19_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI20_Pos      _U_(20)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI20_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI20_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI21_Pos      _U_(21)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI21_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI21_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI22_Pos      _U_(22)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI22_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI22_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI23_Pos      _U_(23)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI23_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI23_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI24_Pos      _U_(24)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI24_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI24_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI25_Pos      _U_(25)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI25_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI25_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI26_Pos      _U_(26)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI26_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI26_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI27_Pos      _U_(27)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI27_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI27_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI28_Pos      _U_(28)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI28_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI28_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI29_Pos      _U_(29)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI29_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI29_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI30_Pos      _U_(30)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI30_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI30_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_DI31_Pos      _U_(31)                                        /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_RCS_DI31_Msk      (_U_(0x1) << SPW_LINK1_DISTINTPI_RCS_DI31_Pos) /**< (SPW_LINK1_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_RCS_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTPI_RCS) Register Mask  */

#define SPW_LINK1_DISTINTPI_RCS_DI_Pos        _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_RCS Position) Distributed Interrupt */
#define SPW_LINK1_DISTINTPI_RCS_DI_Msk        (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTPI_RCS_DI_Pos) /**< (SPW_LINK1_DISTINTPI_RCS Mask) DI */
#define SPW_LINK1_DISTINTPI_RCS_DI(value)     (SPW_LINK1_DISTINTPI_RCS_DI_Msk & ((value) << SPW_LINK1_DISTINTPI_RCS_DI_Pos)) 

/* -------- SPW_LINK1_DISTINTIM : (SPW Offset: 0x450) (R/W 32) SpW Link 1 Distributed Interrupt Mask -------- */
#define SPW_LINK1_DISTINTIM_DI0_Pos           _U_(0)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI0_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI0_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI1_Pos           _U_(1)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI1_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI1_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI2_Pos           _U_(2)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI2_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI2_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI3_Pos           _U_(3)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI3_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI3_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI4_Pos           _U_(4)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI4_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI4_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI5_Pos           _U_(5)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI5_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI5_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI6_Pos           _U_(6)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI6_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI6_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI7_Pos           _U_(7)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI7_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI7_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI8_Pos           _U_(8)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI8_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI8_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI9_Pos           _U_(9)                                         /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI9_Msk           (_U_(0x1) << SPW_LINK1_DISTINTIM_DI9_Pos)      /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI10_Pos          _U_(10)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI10_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI10_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI11_Pos          _U_(11)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI11_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI11_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI12_Pos          _U_(12)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI12_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI12_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI13_Pos          _U_(13)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI13_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI13_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI14_Pos          _U_(14)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI14_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI14_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI15_Pos          _U_(15)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI15_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI15_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI16_Pos          _U_(16)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI16_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI16_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI17_Pos          _U_(17)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI17_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI17_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI18_Pos          _U_(18)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI18_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI18_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI19_Pos          _U_(19)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI19_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI19_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI20_Pos          _U_(20)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI20_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI20_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI21_Pos          _U_(21)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI21_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI21_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI22_Pos          _U_(22)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI22_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI22_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI23_Pos          _U_(23)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI23_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI23_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI24_Pos          _U_(24)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI24_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI24_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI25_Pos          _U_(25)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI25_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI25_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI26_Pos          _U_(26)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI26_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI26_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI27_Pos          _U_(27)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI27_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI27_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI28_Pos          _U_(28)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI28_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI28_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI29_Pos          _U_(29)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI29_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI29_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI30_Pos          _U_(30)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI30_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI30_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_DI31_Pos          _U_(31)                                        /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_DI31_Msk          (_U_(0x1) << SPW_LINK1_DISTINTIM_DI31_Pos)     /**< (SPW_LINK1_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_Msk               _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTIM) Register Mask  */

#define SPW_LINK1_DISTINTIM_DI_Pos            _U_(0)                                         /**< (SPW_LINK1_DISTINTIM Position) Distributed Interrupt mask */
#define SPW_LINK1_DISTINTIM_DI_Msk            (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTIM_DI_Pos) /**< (SPW_LINK1_DISTINTIM Mask) DI */
#define SPW_LINK1_DISTINTIM_DI(value)         (SPW_LINK1_DISTINTIM_DI_Msk & ((value) << SPW_LINK1_DISTINTIM_DI_Pos)) 

/* -------- SPW_LINK1_DISTINTPI_C : (SPW Offset: 0x454) ( /W 32) SpW Link 1 Distributed Interrupt Clear Pending Interrupt -------- */
#define SPW_LINK1_DISTINTPI_C_DI0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI0_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI0_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI1_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI1_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI2_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI2_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI3_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI3_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI4_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI4_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI5_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI5_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI6_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI6_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI7_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI7_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI8_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI8_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI9_Msk         (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI9_Pos)    /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI10_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI10_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI11_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI11_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI12_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI12_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI13_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI13_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI14_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI14_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI15_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI15_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI16_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI16_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI17_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI17_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI18_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI18_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI19_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI19_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI20_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI20_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI21_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI21_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI22_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI22_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI23_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI23_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI24_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI24_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI25_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI25_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI26_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI26_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI27_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI27_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI28_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI28_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI29_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI29_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI30_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI30_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_DI31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK1_DISTINTPI_C_DI31_Msk        (_U_(0x1) << SPW_LINK1_DISTINTPI_C_DI31_Pos)   /**< (SPW_LINK1_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK1_DISTINTPI_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTPI_C) Register Mask  */

#define SPW_LINK1_DISTINTPI_C_DI_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTINTPI_C Position) Distributed Interrupt */
#define SPW_LINK1_DISTINTPI_C_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTPI_C_DI_Pos) /**< (SPW_LINK1_DISTINTPI_C Mask) DI */
#define SPW_LINK1_DISTINTPI_C_DI(value)       (SPW_LINK1_DISTINTPI_C_DI_Msk & ((value) << SPW_LINK1_DISTINTPI_C_DI_Pos)) 

/* -------- SPW_LINK1_DISTINTIM_S : (SPW Offset: 0x458) ( /W 32) SpW Link 1 Distributed Interrupt Set Mask -------- */
#define SPW_LINK1_DISTINTIM_S_DI0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI0_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI0_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI1_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI1_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI2_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI2_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI3_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI3_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI4_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI4_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI5_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI5_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI6_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI6_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI7_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI7_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI8_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI8_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI9_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI9_Pos)    /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI10_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI10_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI11_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI11_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI12_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI12_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI13_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI13_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI14_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI14_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI15_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI15_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI16_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI16_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI17_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI17_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI18_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI18_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI19_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI19_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI20_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI20_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI21_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI21_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI22_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI22_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI23_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI23_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI24_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI24_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI25_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI25_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI26_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI26_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI27_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI27_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI28_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI28_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI29_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI29_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI30_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI30_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_DI31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_S_DI31_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_S_DI31_Pos)   /**< (SPW_LINK1_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_S_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTIM_S) Register Mask  */

#define SPW_LINK1_DISTINTIM_S_DI_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTINTIM_S Position) Distributed Interrupt mask */
#define SPW_LINK1_DISTINTIM_S_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTIM_S_DI_Pos) /**< (SPW_LINK1_DISTINTIM_S Mask) DI */
#define SPW_LINK1_DISTINTIM_S_DI(value)       (SPW_LINK1_DISTINTIM_S_DI_Msk & ((value) << SPW_LINK1_DISTINTIM_S_DI_Pos)) 

/* -------- SPW_LINK1_DISTINTIM_C : (SPW Offset: 0x45C) ( /W 32) SpW Link 1 Distributed Interrupt Clear Mask -------- */
#define SPW_LINK1_DISTINTIM_C_DI0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI0_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI0_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI1_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI1_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI2_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI2_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI3_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI3_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI4_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI4_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI5_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI5_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI6_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI6_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI7_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI7_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI8_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI8_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI9_Msk         (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI9_Pos)    /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI10_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI10_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI11_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI11_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI12_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI12_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI13_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI13_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI14_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI14_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI15_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI15_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI16_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI16_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI17_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI17_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI18_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI18_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI19_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI19_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI20_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI20_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI21_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI21_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI22_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI22_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI23_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI23_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI24_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI24_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI25_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI25_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI26_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI26_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI27_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI27_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI28_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI28_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI29_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI29_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI30_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI30_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_DI31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK1_DISTINTIM_C_DI31_Msk        (_U_(0x1) << SPW_LINK1_DISTINTIM_C_DI31_Pos)   /**< (SPW_LINK1_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK1_DISTINTIM_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTINTIM_C) Register Mask  */

#define SPW_LINK1_DISTINTIM_C_DI_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTINTIM_C Position) Distributed Interrupt mask */
#define SPW_LINK1_DISTINTIM_C_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTINTIM_C_DI_Pos) /**< (SPW_LINK1_DISTINTIM_C Mask) DI */
#define SPW_LINK1_DISTINTIM_C_DI(value)       (SPW_LINK1_DISTINTIM_C_DI_Msk & ((value) << SPW_LINK1_DISTINTIM_C_DI_Pos)) 

/* -------- SPW_LINK1_DISTACKPI_RM : (SPW Offset: 0x460) ( R/ 32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read Masked Interrupt -------- */
#define SPW_LINK1_DISTACKPI_RM_DA0_Pos        _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA0_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA0_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA1_Pos        _U_(1)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA1_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA1_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA2_Pos        _U_(2)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA2_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA2_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA3_Pos        _U_(3)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA3_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA3_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA4_Pos        _U_(4)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA4_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA4_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA5_Pos        _U_(5)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA5_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA5_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA6_Pos        _U_(6)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA6_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA6_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA7_Pos        _U_(7)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA7_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA7_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA8_Pos        _U_(8)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA8_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA8_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA9_Pos        _U_(9)                                         /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA9_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA9_Pos)   /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA10_Pos       _U_(10)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA10_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA10_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA11_Pos       _U_(11)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA11_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA11_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA12_Pos       _U_(12)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA12_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA12_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA13_Pos       _U_(13)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA13_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA13_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA14_Pos       _U_(14)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA14_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA14_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA15_Pos       _U_(15)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA15_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA15_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA16_Pos       _U_(16)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA16_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA16_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA17_Pos       _U_(17)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA17_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA17_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA18_Pos       _U_(18)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA18_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA18_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA19_Pos       _U_(19)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA19_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA19_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA20_Pos       _U_(20)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA20_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA20_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA21_Pos       _U_(21)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA21_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA21_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA22_Pos       _U_(22)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA22_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA22_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA23_Pos       _U_(23)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA23_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA23_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA24_Pos       _U_(24)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA24_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA24_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA25_Pos       _U_(25)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA25_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA25_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA26_Pos       _U_(26)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA26_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA26_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA27_Pos       _U_(27)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA27_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA27_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA28_Pos       _U_(28)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA28_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA28_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA29_Pos       _U_(29)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA29_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA29_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA30_Pos       _U_(30)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA30_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA30_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_DA31_Pos       _U_(31)                                        /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RM_DA31_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RM_DA31_Pos)  /**< (SPW_LINK1_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RM_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKPI_RM) Register Mask  */

#define SPW_LINK1_DISTACKPI_RM_DA_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_RM Position) Distributed Acknowledge */
#define SPW_LINK1_DISTACKPI_RM_DA_Msk         (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKPI_RM_DA_Pos) /**< (SPW_LINK1_DISTACKPI_RM Mask) DA */
#define SPW_LINK1_DISTACKPI_RM_DA(value)      (SPW_LINK1_DISTACKPI_RM_DA_Msk & ((value) << SPW_LINK1_DISTACKPI_RM_DA_Pos)) 

/* -------- SPW_LINK1_DISTACKPI_RCM : (SPW Offset: 0x464) ( R/ 32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read and Clear Masked Interrupt -------- */
#define SPW_LINK1_DISTACKPI_RCM_DA0_Pos       _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA0_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA0_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA1_Pos       _U_(1)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA1_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA1_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA2_Pos       _U_(2)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA2_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA2_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA3_Pos       _U_(3)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA3_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA3_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA4_Pos       _U_(4)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA4_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA4_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA5_Pos       _U_(5)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA5_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA5_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA6_Pos       _U_(6)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA6_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA6_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA7_Pos       _U_(7)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA7_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA7_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA8_Pos       _U_(8)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA8_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA8_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA9_Pos       _U_(9)                                         /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA9_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA9_Pos)  /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA10_Pos      _U_(10)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA10_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA10_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA11_Pos      _U_(11)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA11_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA11_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA12_Pos      _U_(12)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA12_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA12_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA13_Pos      _U_(13)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA13_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA13_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA14_Pos      _U_(14)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA14_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA14_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA15_Pos      _U_(15)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA15_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA15_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA16_Pos      _U_(16)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA16_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA16_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA17_Pos      _U_(17)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA17_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA17_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA18_Pos      _U_(18)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA18_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA18_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA19_Pos      _U_(19)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA19_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA19_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA20_Pos      _U_(20)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA20_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA20_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA21_Pos      _U_(21)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA21_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA21_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA22_Pos      _U_(22)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA22_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA22_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA23_Pos      _U_(23)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA23_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA23_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA24_Pos      _U_(24)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA24_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA24_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA25_Pos      _U_(25)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA25_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA25_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA26_Pos      _U_(26)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA26_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA26_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA27_Pos      _U_(27)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA27_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA27_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA28_Pos      _U_(28)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA28_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA28_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA29_Pos      _U_(29)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA29_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA29_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA30_Pos      _U_(30)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA30_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA30_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_DA31_Pos      _U_(31)                                        /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCM_DA31_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCM_DA31_Pos) /**< (SPW_LINK1_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCM_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKPI_RCM) Register Mask  */

#define SPW_LINK1_DISTACKPI_RCM_DA_Pos        _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_RCM Position) Distributed Acknowledge */
#define SPW_LINK1_DISTACKPI_RCM_DA_Msk        (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKPI_RCM_DA_Pos) /**< (SPW_LINK1_DISTACKPI_RCM Mask) DA */
#define SPW_LINK1_DISTACKPI_RCM_DA(value)     (SPW_LINK1_DISTACKPI_RCM_DA_Msk & ((value) << SPW_LINK1_DISTACKPI_RCM_DA_Pos)) 

/* -------- SPW_LINK1_DISTACKPI_R : (SPW Offset: 0x468) ( R/ 32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read Interrupt -------- */
#define SPW_LINK1_DISTACKPI_R_DA0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA0_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA0_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA1_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA1_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA2_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA2_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA3_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA3_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA4_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA4_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA5_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA5_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA6_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA6_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA7_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA7_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA8_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA8_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA9_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA9_Pos)    /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA10_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA10_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA11_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA11_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA12_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA12_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA13_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA13_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA14_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA14_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA15_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA15_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA16_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA16_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA17_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA17_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA18_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA18_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA19_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA19_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA20_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA20_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA21_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA21_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA22_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA22_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA23_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA23_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA24_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA24_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA25_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA25_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA26_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA26_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA27_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA27_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA28_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA28_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA29_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA29_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA30_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA30_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_DA31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_R_DA31_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_R_DA31_Pos)   /**< (SPW_LINK1_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_R_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKPI_R) Register Mask  */

#define SPW_LINK1_DISTACKPI_R_DA_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_R Position) Distributed Acknowledge */
#define SPW_LINK1_DISTACKPI_R_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKPI_R_DA_Pos) /**< (SPW_LINK1_DISTACKPI_R Mask) DA */
#define SPW_LINK1_DISTACKPI_R_DA(value)       (SPW_LINK1_DISTACKPI_R_DA_Msk & ((value) << SPW_LINK1_DISTACKPI_R_DA_Pos)) 

/* -------- SPW_LINK1_DISTACKPI_RCS : (SPW Offset: 0x46C) (R/W 32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read and Clear Interrupt -------- */
#define SPW_LINK1_DISTACKPI_RCS_DA0_Pos       _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA0_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA0_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA1_Pos       _U_(1)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA1_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA1_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA2_Pos       _U_(2)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA2_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA2_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA3_Pos       _U_(3)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA3_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA3_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA4_Pos       _U_(4)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA4_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA4_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA5_Pos       _U_(5)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA5_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA5_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA6_Pos       _U_(6)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA6_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA6_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA7_Pos       _U_(7)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA7_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA7_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA8_Pos       _U_(8)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA8_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA8_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA9_Pos       _U_(9)                                         /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA9_Msk       (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA9_Pos)  /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA10_Pos      _U_(10)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA10_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA10_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA11_Pos      _U_(11)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA11_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA11_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA12_Pos      _U_(12)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA12_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA12_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA13_Pos      _U_(13)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA13_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA13_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA14_Pos      _U_(14)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA14_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA14_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA15_Pos      _U_(15)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA15_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA15_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA16_Pos      _U_(16)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA16_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA16_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA17_Pos      _U_(17)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA17_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA17_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA18_Pos      _U_(18)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA18_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA18_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA19_Pos      _U_(19)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA19_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA19_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA20_Pos      _U_(20)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA20_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA20_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA21_Pos      _U_(21)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA21_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA21_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA22_Pos      _U_(22)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA22_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA22_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA23_Pos      _U_(23)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA23_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA23_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA24_Pos      _U_(24)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA24_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA24_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA25_Pos      _U_(25)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA25_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA25_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA26_Pos      _U_(26)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA26_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA26_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA27_Pos      _U_(27)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA27_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA27_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA28_Pos      _U_(28)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA28_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA28_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA29_Pos      _U_(29)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA29_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA29_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA30_Pos      _U_(30)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA30_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA30_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_DA31_Pos      _U_(31)                                        /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_RCS_DA31_Msk      (_U_(0x1) << SPW_LINK1_DISTACKPI_RCS_DA31_Pos) /**< (SPW_LINK1_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_RCS_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKPI_RCS) Register Mask  */

#define SPW_LINK1_DISTACKPI_RCS_DA_Pos        _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_RCS Position) Distributed Acknowledge */
#define SPW_LINK1_DISTACKPI_RCS_DA_Msk        (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKPI_RCS_DA_Pos) /**< (SPW_LINK1_DISTACKPI_RCS Mask) DA */
#define SPW_LINK1_DISTACKPI_RCS_DA(value)     (SPW_LINK1_DISTACKPI_RCS_DA_Msk & ((value) << SPW_LINK1_DISTACKPI_RCS_DA_Pos)) 

/* -------- SPW_LINK1_DISTACKIM : (SPW Offset: 0x470) (R/W 32) SpW Link 1 Distributed Interrupt Acknowledge Mask -------- */
#define SPW_LINK1_DISTACKIM_DA0_Pos           _U_(0)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA0_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA0_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA1_Pos           _U_(1)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA1_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA1_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA2_Pos           _U_(2)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA2_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA2_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA3_Pos           _U_(3)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA3_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA3_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA4_Pos           _U_(4)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA4_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA4_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA5_Pos           _U_(5)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA5_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA5_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA6_Pos           _U_(6)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA6_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA6_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA7_Pos           _U_(7)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA7_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA7_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA8_Pos           _U_(8)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA8_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA8_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA9_Pos           _U_(9)                                         /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA9_Msk           (_U_(0x1) << SPW_LINK1_DISTACKIM_DA9_Pos)      /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA10_Pos          _U_(10)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA10_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA10_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA11_Pos          _U_(11)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA11_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA11_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA12_Pos          _U_(12)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA12_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA12_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA13_Pos          _U_(13)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA13_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA13_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA14_Pos          _U_(14)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA14_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA14_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA15_Pos          _U_(15)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA15_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA15_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA16_Pos          _U_(16)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA16_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA16_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA17_Pos          _U_(17)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA17_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA17_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA18_Pos          _U_(18)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA18_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA18_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA19_Pos          _U_(19)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA19_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA19_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA20_Pos          _U_(20)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA20_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA20_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA21_Pos          _U_(21)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA21_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA21_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA22_Pos          _U_(22)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA22_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA22_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA23_Pos          _U_(23)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA23_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA23_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA24_Pos          _U_(24)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA24_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA24_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA25_Pos          _U_(25)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA25_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA25_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA26_Pos          _U_(26)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA26_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA26_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA27_Pos          _U_(27)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA27_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA27_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA28_Pos          _U_(28)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA28_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA28_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA29_Pos          _U_(29)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA29_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA29_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA30_Pos          _U_(30)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA30_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA30_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_DA31_Pos          _U_(31)                                        /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_DA31_Msk          (_U_(0x1) << SPW_LINK1_DISTACKIM_DA31_Pos)     /**< (SPW_LINK1_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_Msk               _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKIM) Register Mask  */

#define SPW_LINK1_DISTACKIM_DA_Pos            _U_(0)                                         /**< (SPW_LINK1_DISTACKIM Position) Distributed Acknowledge mask */
#define SPW_LINK1_DISTACKIM_DA_Msk            (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKIM_DA_Pos) /**< (SPW_LINK1_DISTACKIM Mask) DA */
#define SPW_LINK1_DISTACKIM_DA(value)         (SPW_LINK1_DISTACKIM_DA_Msk & ((value) << SPW_LINK1_DISTACKIM_DA_Pos)) 

/* -------- SPW_LINK1_DISTACKPI_C : (SPW Offset: 0x474) ( /W 32) SpW Link 1 Distributed Interrupt Acknowledge Clear Pending Interrupt -------- */
#define SPW_LINK1_DISTACKPI_C_DA0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA0_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA0_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA1_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA1_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA2_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA2_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA3_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA3_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA4_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA4_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA5_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA5_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA6_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA6_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA7_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA7_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA8_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA8_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA9_Msk         (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA9_Pos)    /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA10_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA10_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA11_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA11_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA12_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA12_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA13_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA13_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA14_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA14_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA15_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA15_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA16_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA16_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA17_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA17_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA18_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA18_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA19_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA19_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA20_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA20_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA21_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA21_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA22_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA22_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA23_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA23_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA24_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA24_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA25_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA25_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA26_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA26_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA27_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA27_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA28_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA28_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA29_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA29_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA30_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA30_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_DA31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK1_DISTACKPI_C_DA31_Msk        (_U_(0x1) << SPW_LINK1_DISTACKPI_C_DA31_Pos)   /**< (SPW_LINK1_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK1_DISTACKPI_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKPI_C) Register Mask  */

#define SPW_LINK1_DISTACKPI_C_DA_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTACKPI_C Position) Distributed Acknowledge */
#define SPW_LINK1_DISTACKPI_C_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKPI_C_DA_Pos) /**< (SPW_LINK1_DISTACKPI_C Mask) DA */
#define SPW_LINK1_DISTACKPI_C_DA(value)       (SPW_LINK1_DISTACKPI_C_DA_Msk & ((value) << SPW_LINK1_DISTACKPI_C_DA_Pos)) 

/* -------- SPW_LINK1_DISTACKIM_S : (SPW Offset: 0x478) ( /W 32) SpW Link 1 Distributed Interrupt Acknowledge Set Mask -------- */
#define SPW_LINK1_DISTACKIM_S_DA0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA0_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA0_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA1_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA1_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA2_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA2_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA3_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA3_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA4_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA4_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA5_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA5_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA6_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA6_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA7_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA7_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA8_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA8_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA9_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA9_Pos)    /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA10_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA10_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA11_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA11_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA12_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA12_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA13_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA13_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA14_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA14_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA15_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA15_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA16_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA16_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA17_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA17_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA18_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA18_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA19_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA19_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA20_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA20_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA21_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA21_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA22_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA22_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA23_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA23_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA24_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA24_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA25_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA25_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA26_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA26_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA27_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA27_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA28_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA28_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA29_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA29_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA30_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA30_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_DA31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_S_DA31_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_S_DA31_Pos)   /**< (SPW_LINK1_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_S_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKIM_S) Register Mask  */

#define SPW_LINK1_DISTACKIM_S_DA_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTACKIM_S Position) Distributed Acknowledge mask */
#define SPW_LINK1_DISTACKIM_S_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKIM_S_DA_Pos) /**< (SPW_LINK1_DISTACKIM_S Mask) DA */
#define SPW_LINK1_DISTACKIM_S_DA(value)       (SPW_LINK1_DISTACKIM_S_DA_Msk & ((value) << SPW_LINK1_DISTACKIM_S_DA_Pos)) 

/* -------- SPW_LINK1_DISTACKIM_C : (SPW Offset: 0x47C) ( /W 32) SpW Link 1 Distributed Interrupt Acknowledge Clear Mask -------- */
#define SPW_LINK1_DISTACKIM_C_DA0_Pos         _U_(0)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA0_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA0_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA1_Pos         _U_(1)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA1_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA1_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA2_Pos         _U_(2)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA2_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA2_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA3_Pos         _U_(3)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA3_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA3_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA4_Pos         _U_(4)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA4_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA4_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA5_Pos         _U_(5)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA5_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA5_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA6_Pos         _U_(6)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA6_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA6_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA7_Pos         _U_(7)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA7_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA7_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA8_Pos         _U_(8)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA8_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA8_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA9_Pos         _U_(9)                                         /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA9_Msk         (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA9_Pos)    /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA10_Pos        _U_(10)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA10_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA10_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA11_Pos        _U_(11)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA11_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA11_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA12_Pos        _U_(12)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA12_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA12_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA13_Pos        _U_(13)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA13_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA13_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA14_Pos        _U_(14)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA14_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA14_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA15_Pos        _U_(15)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA15_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA15_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA16_Pos        _U_(16)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA16_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA16_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA17_Pos        _U_(17)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA17_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA17_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA18_Pos        _U_(18)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA18_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA18_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA19_Pos        _U_(19)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA19_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA19_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA20_Pos        _U_(20)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA20_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA20_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA21_Pos        _U_(21)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA21_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA21_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA22_Pos        _U_(22)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA22_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA22_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA23_Pos        _U_(23)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA23_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA23_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA24_Pos        _U_(24)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA24_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA24_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA25_Pos        _U_(25)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA25_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA25_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA26_Pos        _U_(26)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA26_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA26_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA27_Pos        _U_(27)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA27_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA27_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA28_Pos        _U_(28)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA28_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA28_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA29_Pos        _U_(29)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA29_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA29_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA30_Pos        _U_(30)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA30_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA30_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_DA31_Pos        _U_(31)                                        /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK1_DISTACKIM_C_DA31_Msk        (_U_(0x1) << SPW_LINK1_DISTACKIM_C_DA31_Pos)   /**< (SPW_LINK1_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK1_DISTACKIM_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK1_DISTACKIM_C) Register Mask  */

#define SPW_LINK1_DISTACKIM_C_DA_Pos          _U_(0)                                         /**< (SPW_LINK1_DISTACKIM_C Position) Distributed Acknowledge mask */
#define SPW_LINK1_DISTACKIM_C_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK1_DISTACKIM_C_DA_Pos) /**< (SPW_LINK1_DISTACKIM_C Mask) DA */
#define SPW_LINK1_DISTACKIM_C_DA(value)       (SPW_LINK1_DISTACKIM_C_DA_Msk & ((value) << SPW_LINK1_DISTACKIM_C_DA_Pos)) 

/* -------- SPW_LINK2_PI_RM : (SPW Offset: 0x480) ( R/ 32) SpW Link 2 Pending Read Masked Interrupt -------- */
#define SPW_LINK2_PI_RM_DISERR_Pos            _U_(0)                                         /**< (SPW_LINK2_PI_RM) DisErr Position */
#define SPW_LINK2_PI_RM_DISERR_Msk            (_U_(0x1) << SPW_LINK2_PI_RM_DISERR_Pos)       /**< (SPW_LINK2_PI_RM) DisErr Mask */
#define SPW_LINK2_PI_RM_PARERR_Pos            _U_(1)                                         /**< (SPW_LINK2_PI_RM) ParErr Position */
#define SPW_LINK2_PI_RM_PARERR_Msk            (_U_(0x1) << SPW_LINK2_PI_RM_PARERR_Pos)       /**< (SPW_LINK2_PI_RM) ParErr Mask */
#define SPW_LINK2_PI_RM_ESCERR_Pos            _U_(2)                                         /**< (SPW_LINK2_PI_RM) ESCErr Position */
#define SPW_LINK2_PI_RM_ESCERR_Msk            (_U_(0x1) << SPW_LINK2_PI_RM_ESCERR_Pos)       /**< (SPW_LINK2_PI_RM) ESCErr Mask */
#define SPW_LINK2_PI_RM_CRERR_Pos             _U_(3)                                         /**< (SPW_LINK2_PI_RM) CrErr Position */
#define SPW_LINK2_PI_RM_CRERR_Msk             (_U_(0x1) << SPW_LINK2_PI_RM_CRERR_Pos)        /**< (SPW_LINK2_PI_RM) CrErr Mask */
#define SPW_LINK2_PI_RM_LINKABORT_Pos         _U_(4)                                         /**< (SPW_LINK2_PI_RM) LinkAbort Position */
#define SPW_LINK2_PI_RM_LINKABORT_Msk         (_U_(0x1) << SPW_LINK2_PI_RM_LINKABORT_Pos)    /**< (SPW_LINK2_PI_RM) LinkAbort Mask */
#define SPW_LINK2_PI_RM_EEPTRANS_Pos          _U_(5)                                         /**< (SPW_LINK2_PI_RM) EEP transmitted Position */
#define SPW_LINK2_PI_RM_EEPTRANS_Msk          (_U_(0x1) << SPW_LINK2_PI_RM_EEPTRANS_Pos)     /**< (SPW_LINK2_PI_RM) EEP transmitted Mask */
#define SPW_LINK2_PI_RM_EEPREC_Pos            _U_(6)                                         /**< (SPW_LINK2_PI_RM) EEP received Position */
#define SPW_LINK2_PI_RM_EEPREC_Msk            (_U_(0x1) << SPW_LINK2_PI_RM_EEPREC_Pos)       /**< (SPW_LINK2_PI_RM) EEP received Mask */
#define SPW_LINK2_PI_RM_DISCARD_Pos           _U_(7)                                         /**< (SPW_LINK2_PI_RM) Discard Position */
#define SPW_LINK2_PI_RM_DISCARD_Msk           (_U_(0x1) << SPW_LINK2_PI_RM_DISCARD_Pos)      /**< (SPW_LINK2_PI_RM) Discard Mask */
#define SPW_LINK2_PI_RM_ESCEVENT2_Pos         _U_(8)                                         /**< (SPW_LINK2_PI_RM) Escape Event 2 Position */
#define SPW_LINK2_PI_RM_ESCEVENT2_Msk         (_U_(0x1) << SPW_LINK2_PI_RM_ESCEVENT2_Pos)    /**< (SPW_LINK2_PI_RM) Escape Event 2 Mask */
#define SPW_LINK2_PI_RM_ESCEVENT1_Pos         _U_(9)                                         /**< (SPW_LINK2_PI_RM) Escape Event 1 Position */
#define SPW_LINK2_PI_RM_ESCEVENT1_Msk         (_U_(0x1) << SPW_LINK2_PI_RM_ESCEVENT1_Pos)    /**< (SPW_LINK2_PI_RM) Escape Event 1 Mask */
#define SPW_LINK2_PI_RM_Msk                   _U_(0x000003FF)                                /**< (SPW_LINK2_PI_RM) Register Mask  */

#define SPW_LINK2_PI_RM_ESCEVENT_Pos          _U_(8)                                         /**< (SPW_LINK2_PI_RM Position) Escape Event x */
#define SPW_LINK2_PI_RM_ESCEVENT_Msk          (_U_(0x3) << SPW_LINK2_PI_RM_ESCEVENT_Pos)     /**< (SPW_LINK2_PI_RM Mask) ESCEVENT */
#define SPW_LINK2_PI_RM_ESCEVENT(value)       (SPW_LINK2_PI_RM_ESCEVENT_Msk & ((value) << SPW_LINK2_PI_RM_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_PI_RCM : (SPW Offset: 0x484) ( R/ 32) SpW Link 2 Pending Read and Clear Masked Interrupt -------- */
#define SPW_LINK2_PI_RCM_DISERR_Pos           _U_(0)                                         /**< (SPW_LINK2_PI_RCM) DisErr Position */
#define SPW_LINK2_PI_RCM_DISERR_Msk           (_U_(0x1) << SPW_LINK2_PI_RCM_DISERR_Pos)      /**< (SPW_LINK2_PI_RCM) DisErr Mask */
#define SPW_LINK2_PI_RCM_PARERR_Pos           _U_(1)                                         /**< (SPW_LINK2_PI_RCM) ParErr Position */
#define SPW_LINK2_PI_RCM_PARERR_Msk           (_U_(0x1) << SPW_LINK2_PI_RCM_PARERR_Pos)      /**< (SPW_LINK2_PI_RCM) ParErr Mask */
#define SPW_LINK2_PI_RCM_ESCERR_Pos           _U_(2)                                         /**< (SPW_LINK2_PI_RCM) ESCErr Position */
#define SPW_LINK2_PI_RCM_ESCERR_Msk           (_U_(0x1) << SPW_LINK2_PI_RCM_ESCERR_Pos)      /**< (SPW_LINK2_PI_RCM) ESCErr Mask */
#define SPW_LINK2_PI_RCM_CRERR_Pos            _U_(3)                                         /**< (SPW_LINK2_PI_RCM) CrErr Position */
#define SPW_LINK2_PI_RCM_CRERR_Msk            (_U_(0x1) << SPW_LINK2_PI_RCM_CRERR_Pos)       /**< (SPW_LINK2_PI_RCM) CrErr Mask */
#define SPW_LINK2_PI_RCM_LINKABORT_Pos        _U_(4)                                         /**< (SPW_LINK2_PI_RCM) LinkAbort Position */
#define SPW_LINK2_PI_RCM_LINKABORT_Msk        (_U_(0x1) << SPW_LINK2_PI_RCM_LINKABORT_Pos)   /**< (SPW_LINK2_PI_RCM) LinkAbort Mask */
#define SPW_LINK2_PI_RCM_EEPTRANS_Pos         _U_(5)                                         /**< (SPW_LINK2_PI_RCM) EEP transmitted Position */
#define SPW_LINK2_PI_RCM_EEPTRANS_Msk         (_U_(0x1) << SPW_LINK2_PI_RCM_EEPTRANS_Pos)    /**< (SPW_LINK2_PI_RCM) EEP transmitted Mask */
#define SPW_LINK2_PI_RCM_EEPREC_Pos           _U_(6)                                         /**< (SPW_LINK2_PI_RCM) EEP received Position */
#define SPW_LINK2_PI_RCM_EEPREC_Msk           (_U_(0x1) << SPW_LINK2_PI_RCM_EEPREC_Pos)      /**< (SPW_LINK2_PI_RCM) EEP received Mask */
#define SPW_LINK2_PI_RCM_DISCARD_Pos          _U_(7)                                         /**< (SPW_LINK2_PI_RCM) Discard Position */
#define SPW_LINK2_PI_RCM_DISCARD_Msk          (_U_(0x1) << SPW_LINK2_PI_RCM_DISCARD_Pos)     /**< (SPW_LINK2_PI_RCM) Discard Mask */
#define SPW_LINK2_PI_RCM_ESCEVENT2_Pos        _U_(8)                                         /**< (SPW_LINK2_PI_RCM) Escape Event 2 Position */
#define SPW_LINK2_PI_RCM_ESCEVENT2_Msk        (_U_(0x1) << SPW_LINK2_PI_RCM_ESCEVENT2_Pos)   /**< (SPW_LINK2_PI_RCM) Escape Event 2 Mask */
#define SPW_LINK2_PI_RCM_ESCEVENT1_Pos        _U_(9)                                         /**< (SPW_LINK2_PI_RCM) Escape Event 1 Position */
#define SPW_LINK2_PI_RCM_ESCEVENT1_Msk        (_U_(0x1) << SPW_LINK2_PI_RCM_ESCEVENT1_Pos)   /**< (SPW_LINK2_PI_RCM) Escape Event 1 Mask */
#define SPW_LINK2_PI_RCM_Msk                  _U_(0x000003FF)                                /**< (SPW_LINK2_PI_RCM) Register Mask  */

#define SPW_LINK2_PI_RCM_ESCEVENT_Pos         _U_(8)                                         /**< (SPW_LINK2_PI_RCM Position) Escape Event x */
#define SPW_LINK2_PI_RCM_ESCEVENT_Msk         (_U_(0x3) << SPW_LINK2_PI_RCM_ESCEVENT_Pos)    /**< (SPW_LINK2_PI_RCM Mask) ESCEVENT */
#define SPW_LINK2_PI_RCM_ESCEVENT(value)      (SPW_LINK2_PI_RCM_ESCEVENT_Msk & ((value) << SPW_LINK2_PI_RCM_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_PI_R : (SPW Offset: 0x488) ( R/ 32) SpW Link 2 Pending Read Interrupt -------- */
#define SPW_LINK2_PI_R_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK2_PI_R) DisErr Position */
#define SPW_LINK2_PI_R_DISERR_Msk             (_U_(0x1) << SPW_LINK2_PI_R_DISERR_Pos)        /**< (SPW_LINK2_PI_R) DisErr Mask */
#define SPW_LINK2_PI_R_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK2_PI_R) ParErr Position */
#define SPW_LINK2_PI_R_PARERR_Msk             (_U_(0x1) << SPW_LINK2_PI_R_PARERR_Pos)        /**< (SPW_LINK2_PI_R) ParErr Mask */
#define SPW_LINK2_PI_R_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK2_PI_R) ESCErr Position */
#define SPW_LINK2_PI_R_ESCERR_Msk             (_U_(0x1) << SPW_LINK2_PI_R_ESCERR_Pos)        /**< (SPW_LINK2_PI_R) ESCErr Mask */
#define SPW_LINK2_PI_R_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK2_PI_R) CrErr Position */
#define SPW_LINK2_PI_R_CRERR_Msk              (_U_(0x1) << SPW_LINK2_PI_R_CRERR_Pos)         /**< (SPW_LINK2_PI_R) CrErr Mask */
#define SPW_LINK2_PI_R_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK2_PI_R) LinkAbort Position */
#define SPW_LINK2_PI_R_LINKABORT_Msk          (_U_(0x1) << SPW_LINK2_PI_R_LINKABORT_Pos)     /**< (SPW_LINK2_PI_R) LinkAbort Mask */
#define SPW_LINK2_PI_R_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK2_PI_R) EEP transmitted Position */
#define SPW_LINK2_PI_R_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK2_PI_R_EEPTRANS_Pos)      /**< (SPW_LINK2_PI_R) EEP transmitted Mask */
#define SPW_LINK2_PI_R_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK2_PI_R) EEP received Position */
#define SPW_LINK2_PI_R_EEPREC_Msk             (_U_(0x1) << SPW_LINK2_PI_R_EEPREC_Pos)        /**< (SPW_LINK2_PI_R) EEP received Mask */
#define SPW_LINK2_PI_R_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK2_PI_R) Discard Position */
#define SPW_LINK2_PI_R_DISCARD_Msk            (_U_(0x1) << SPW_LINK2_PI_R_DISCARD_Pos)       /**< (SPW_LINK2_PI_R) Discard Mask */
#define SPW_LINK2_PI_R_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK2_PI_R) Escape Event 2 Position */
#define SPW_LINK2_PI_R_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK2_PI_R_ESCEVENT2_Pos)     /**< (SPW_LINK2_PI_R) Escape Event 2 Mask */
#define SPW_LINK2_PI_R_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK2_PI_R) Escape Event 1 Position */
#define SPW_LINK2_PI_R_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK2_PI_R_ESCEVENT1_Pos)     /**< (SPW_LINK2_PI_R) Escape Event 1 Mask */
#define SPW_LINK2_PI_R_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK2_PI_R) Register Mask  */

#define SPW_LINK2_PI_R_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK2_PI_R Position) Escape Event x */
#define SPW_LINK2_PI_R_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK2_PI_R_ESCEVENT_Pos)      /**< (SPW_LINK2_PI_R Mask) ESCEVENT */
#define SPW_LINK2_PI_R_ESCEVENT(value)        (SPW_LINK2_PI_R_ESCEVENT_Msk & ((value) << SPW_LINK2_PI_R_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_PI_RCS : (SPW Offset: 0x48C) (R/W 32) SpW Link 2 Pending Read, Clear and Enabled Interrupt -------- */
#define SPW_LINK2_PI_RCS_DISERR_Pos           _U_(0)                                         /**< (SPW_LINK2_PI_RCS) DisErr Position */
#define SPW_LINK2_PI_RCS_DISERR_Msk           (_U_(0x1) << SPW_LINK2_PI_RCS_DISERR_Pos)      /**< (SPW_LINK2_PI_RCS) DisErr Mask */
#define SPW_LINK2_PI_RCS_PARERR_Pos           _U_(1)                                         /**< (SPW_LINK2_PI_RCS) ParErr Position */
#define SPW_LINK2_PI_RCS_PARERR_Msk           (_U_(0x1) << SPW_LINK2_PI_RCS_PARERR_Pos)      /**< (SPW_LINK2_PI_RCS) ParErr Mask */
#define SPW_LINK2_PI_RCS_ESCERR_Pos           _U_(2)                                         /**< (SPW_LINK2_PI_RCS) ESCErr Position */
#define SPW_LINK2_PI_RCS_ESCERR_Msk           (_U_(0x1) << SPW_LINK2_PI_RCS_ESCERR_Pos)      /**< (SPW_LINK2_PI_RCS) ESCErr Mask */
#define SPW_LINK2_PI_RCS_CRERR_Pos            _U_(3)                                         /**< (SPW_LINK2_PI_RCS) CrErr Position */
#define SPW_LINK2_PI_RCS_CRERR_Msk            (_U_(0x1) << SPW_LINK2_PI_RCS_CRERR_Pos)       /**< (SPW_LINK2_PI_RCS) CrErr Mask */
#define SPW_LINK2_PI_RCS_LINKABORT_Pos        _U_(4)                                         /**< (SPW_LINK2_PI_RCS) LinkAbort Position */
#define SPW_LINK2_PI_RCS_LINKABORT_Msk        (_U_(0x1) << SPW_LINK2_PI_RCS_LINKABORT_Pos)   /**< (SPW_LINK2_PI_RCS) LinkAbort Mask */
#define SPW_LINK2_PI_RCS_EEPTRANS_Pos         _U_(5)                                         /**< (SPW_LINK2_PI_RCS) EEP transmitted Position */
#define SPW_LINK2_PI_RCS_EEPTRANS_Msk         (_U_(0x1) << SPW_LINK2_PI_RCS_EEPTRANS_Pos)    /**< (SPW_LINK2_PI_RCS) EEP transmitted Mask */
#define SPW_LINK2_PI_RCS_EEPREC_Pos           _U_(6)                                         /**< (SPW_LINK2_PI_RCS) EEP received Position */
#define SPW_LINK2_PI_RCS_EEPREC_Msk           (_U_(0x1) << SPW_LINK2_PI_RCS_EEPREC_Pos)      /**< (SPW_LINK2_PI_RCS) EEP received Mask */
#define SPW_LINK2_PI_RCS_DISCARD_Pos          _U_(7)                                         /**< (SPW_LINK2_PI_RCS) Discard Position */
#define SPW_LINK2_PI_RCS_DISCARD_Msk          (_U_(0x1) << SPW_LINK2_PI_RCS_DISCARD_Pos)     /**< (SPW_LINK2_PI_RCS) Discard Mask */
#define SPW_LINK2_PI_RCS_ESCEVENT2_Pos        _U_(8)                                         /**< (SPW_LINK2_PI_RCS) Escape Event 2 Position */
#define SPW_LINK2_PI_RCS_ESCEVENT2_Msk        (_U_(0x1) << SPW_LINK2_PI_RCS_ESCEVENT2_Pos)   /**< (SPW_LINK2_PI_RCS) Escape Event 2 Mask */
#define SPW_LINK2_PI_RCS_ESCEVENT1_Pos        _U_(9)                                         /**< (SPW_LINK2_PI_RCS) Escape Event 1 Position */
#define SPW_LINK2_PI_RCS_ESCEVENT1_Msk        (_U_(0x1) << SPW_LINK2_PI_RCS_ESCEVENT1_Pos)   /**< (SPW_LINK2_PI_RCS) Escape Event 1 Mask */
#define SPW_LINK2_PI_RCS_Msk                  _U_(0x000003FF)                                /**< (SPW_LINK2_PI_RCS) Register Mask  */

#define SPW_LINK2_PI_RCS_ESCEVENT_Pos         _U_(8)                                         /**< (SPW_LINK2_PI_RCS Position) Escape Event x */
#define SPW_LINK2_PI_RCS_ESCEVENT_Msk         (_U_(0x3) << SPW_LINK2_PI_RCS_ESCEVENT_Pos)    /**< (SPW_LINK2_PI_RCS Mask) ESCEVENT */
#define SPW_LINK2_PI_RCS_ESCEVENT(value)      (SPW_LINK2_PI_RCS_ESCEVENT_Msk & ((value) << SPW_LINK2_PI_RCS_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_IM : (SPW Offset: 0x490) (R/W 32) SpW Link 2 Interrupt Mask -------- */
#define SPW_LINK2_IM_DISERR_Pos               _U_(0)                                         /**< (SPW_LINK2_IM) DisErr Position */
#define SPW_LINK2_IM_DISERR_Msk               (_U_(0x1) << SPW_LINK2_IM_DISERR_Pos)          /**< (SPW_LINK2_IM) DisErr Mask */
#define SPW_LINK2_IM_PARERR_Pos               _U_(1)                                         /**< (SPW_LINK2_IM) ParErr Position */
#define SPW_LINK2_IM_PARERR_Msk               (_U_(0x1) << SPW_LINK2_IM_PARERR_Pos)          /**< (SPW_LINK2_IM) ParErr Mask */
#define SPW_LINK2_IM_ESCERR_Pos               _U_(2)                                         /**< (SPW_LINK2_IM) ESCErr Position */
#define SPW_LINK2_IM_ESCERR_Msk               (_U_(0x1) << SPW_LINK2_IM_ESCERR_Pos)          /**< (SPW_LINK2_IM) ESCErr Mask */
#define SPW_LINK2_IM_CRERR_Pos                _U_(3)                                         /**< (SPW_LINK2_IM) CrErr Position */
#define SPW_LINK2_IM_CRERR_Msk                (_U_(0x1) << SPW_LINK2_IM_CRERR_Pos)           /**< (SPW_LINK2_IM) CrErr Mask */
#define SPW_LINK2_IM_LINKABORT_Pos            _U_(4)                                         /**< (SPW_LINK2_IM) LinkAbort Position */
#define SPW_LINK2_IM_LINKABORT_Msk            (_U_(0x1) << SPW_LINK2_IM_LINKABORT_Pos)       /**< (SPW_LINK2_IM) LinkAbort Mask */
#define SPW_LINK2_IM_EEPTRANS_Pos             _U_(5)                                         /**< (SPW_LINK2_IM) EEP transmitted Position */
#define SPW_LINK2_IM_EEPTRANS_Msk             (_U_(0x1) << SPW_LINK2_IM_EEPTRANS_Pos)        /**< (SPW_LINK2_IM) EEP transmitted Mask */
#define SPW_LINK2_IM_EEPREC_Pos               _U_(6)                                         /**< (SPW_LINK2_IM) EEP received Position */
#define SPW_LINK2_IM_EEPREC_Msk               (_U_(0x1) << SPW_LINK2_IM_EEPREC_Pos)          /**< (SPW_LINK2_IM) EEP received Mask */
#define SPW_LINK2_IM_DISCARD_Pos              _U_(7)                                         /**< (SPW_LINK2_IM) Discard Position */
#define SPW_LINK2_IM_DISCARD_Msk              (_U_(0x1) << SPW_LINK2_IM_DISCARD_Pos)         /**< (SPW_LINK2_IM) Discard Mask */
#define SPW_LINK2_IM_ESCEVENT2_Pos            _U_(8)                                         /**< (SPW_LINK2_IM) Escape Event 2 Position */
#define SPW_LINK2_IM_ESCEVENT2_Msk            (_U_(0x1) << SPW_LINK2_IM_ESCEVENT2_Pos)       /**< (SPW_LINK2_IM) Escape Event 2 Mask */
#define SPW_LINK2_IM_ESCEVENT1_Pos            _U_(9)                                         /**< (SPW_LINK2_IM) Escape Event 1 Position */
#define SPW_LINK2_IM_ESCEVENT1_Msk            (_U_(0x1) << SPW_LINK2_IM_ESCEVENT1_Pos)       /**< (SPW_LINK2_IM) Escape Event 1 Mask */
#define SPW_LINK2_IM_Msk                      _U_(0x000003FF)                                /**< (SPW_LINK2_IM) Register Mask  */

#define SPW_LINK2_IM_ESCEVENT_Pos             _U_(8)                                         /**< (SPW_LINK2_IM Position) Escape Event x */
#define SPW_LINK2_IM_ESCEVENT_Msk             (_U_(0x3) << SPW_LINK2_IM_ESCEVENT_Pos)        /**< (SPW_LINK2_IM Mask) ESCEVENT */
#define SPW_LINK2_IM_ESCEVENT(value)          (SPW_LINK2_IM_ESCEVENT_Msk & ((value) << SPW_LINK2_IM_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_PI_C : (SPW Offset: 0x494) ( /W 32) SpW Link 2 Clear Pending Interrupt -------- */
#define SPW_LINK2_PI_C_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK2_PI_C) DisErr Position */
#define SPW_LINK2_PI_C_DISERR_Msk             (_U_(0x1) << SPW_LINK2_PI_C_DISERR_Pos)        /**< (SPW_LINK2_PI_C) DisErr Mask */
#define SPW_LINK2_PI_C_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK2_PI_C) ParErr Position */
#define SPW_LINK2_PI_C_PARERR_Msk             (_U_(0x1) << SPW_LINK2_PI_C_PARERR_Pos)        /**< (SPW_LINK2_PI_C) ParErr Mask */
#define SPW_LINK2_PI_C_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK2_PI_C) ESCErr Position */
#define SPW_LINK2_PI_C_ESCERR_Msk             (_U_(0x1) << SPW_LINK2_PI_C_ESCERR_Pos)        /**< (SPW_LINK2_PI_C) ESCErr Mask */
#define SPW_LINK2_PI_C_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK2_PI_C) CrErr Position */
#define SPW_LINK2_PI_C_CRERR_Msk              (_U_(0x1) << SPW_LINK2_PI_C_CRERR_Pos)         /**< (SPW_LINK2_PI_C) CrErr Mask */
#define SPW_LINK2_PI_C_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK2_PI_C) LinkAbort Position */
#define SPW_LINK2_PI_C_LINKABORT_Msk          (_U_(0x1) << SPW_LINK2_PI_C_LINKABORT_Pos)     /**< (SPW_LINK2_PI_C) LinkAbort Mask */
#define SPW_LINK2_PI_C_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK2_PI_C) EEP transmitted Position */
#define SPW_LINK2_PI_C_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK2_PI_C_EEPTRANS_Pos)      /**< (SPW_LINK2_PI_C) EEP transmitted Mask */
#define SPW_LINK2_PI_C_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK2_PI_C) EEP received Position */
#define SPW_LINK2_PI_C_EEPREC_Msk             (_U_(0x1) << SPW_LINK2_PI_C_EEPREC_Pos)        /**< (SPW_LINK2_PI_C) EEP received Mask */
#define SPW_LINK2_PI_C_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK2_PI_C) Discard Position */
#define SPW_LINK2_PI_C_DISCARD_Msk            (_U_(0x1) << SPW_LINK2_PI_C_DISCARD_Pos)       /**< (SPW_LINK2_PI_C) Discard Mask */
#define SPW_LINK2_PI_C_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK2_PI_C) Escape Event 2 Position */
#define SPW_LINK2_PI_C_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK2_PI_C_ESCEVENT2_Pos)     /**< (SPW_LINK2_PI_C) Escape Event 2 Mask */
#define SPW_LINK2_PI_C_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK2_PI_C) Escape Event 1 Position */
#define SPW_LINK2_PI_C_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK2_PI_C_ESCEVENT1_Pos)     /**< (SPW_LINK2_PI_C) Escape Event 1 Mask */
#define SPW_LINK2_PI_C_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK2_PI_C) Register Mask  */

#define SPW_LINK2_PI_C_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK2_PI_C Position) Escape Event x */
#define SPW_LINK2_PI_C_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK2_PI_C_ESCEVENT_Pos)      /**< (SPW_LINK2_PI_C Mask) ESCEVENT */
#define SPW_LINK2_PI_C_ESCEVENT(value)        (SPW_LINK2_PI_C_ESCEVENT_Msk & ((value) << SPW_LINK2_PI_C_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_IM_S : (SPW Offset: 0x498) ( /W 32) SpW Link 2 Interrupt Set Mask -------- */
#define SPW_LINK2_IM_S_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK2_IM_S) DisErr Position */
#define SPW_LINK2_IM_S_DISERR_Msk             (_U_(0x1) << SPW_LINK2_IM_S_DISERR_Pos)        /**< (SPW_LINK2_IM_S) DisErr Mask */
#define SPW_LINK2_IM_S_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK2_IM_S) ParErr Position */
#define SPW_LINK2_IM_S_PARERR_Msk             (_U_(0x1) << SPW_LINK2_IM_S_PARERR_Pos)        /**< (SPW_LINK2_IM_S) ParErr Mask */
#define SPW_LINK2_IM_S_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK2_IM_S) ESCErr Position */
#define SPW_LINK2_IM_S_ESCERR_Msk             (_U_(0x1) << SPW_LINK2_IM_S_ESCERR_Pos)        /**< (SPW_LINK2_IM_S) ESCErr Mask */
#define SPW_LINK2_IM_S_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK2_IM_S) CrErr Position */
#define SPW_LINK2_IM_S_CRERR_Msk              (_U_(0x1) << SPW_LINK2_IM_S_CRERR_Pos)         /**< (SPW_LINK2_IM_S) CrErr Mask */
#define SPW_LINK2_IM_S_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK2_IM_S) LinkAbort Position */
#define SPW_LINK2_IM_S_LINKABORT_Msk          (_U_(0x1) << SPW_LINK2_IM_S_LINKABORT_Pos)     /**< (SPW_LINK2_IM_S) LinkAbort Mask */
#define SPW_LINK2_IM_S_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK2_IM_S) EEP transmitted Position */
#define SPW_LINK2_IM_S_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK2_IM_S_EEPTRANS_Pos)      /**< (SPW_LINK2_IM_S) EEP transmitted Mask */
#define SPW_LINK2_IM_S_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK2_IM_S) EEP received Position */
#define SPW_LINK2_IM_S_EEPREC_Msk             (_U_(0x1) << SPW_LINK2_IM_S_EEPREC_Pos)        /**< (SPW_LINK2_IM_S) EEP received Mask */
#define SPW_LINK2_IM_S_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK2_IM_S) Discard Position */
#define SPW_LINK2_IM_S_DISCARD_Msk            (_U_(0x1) << SPW_LINK2_IM_S_DISCARD_Pos)       /**< (SPW_LINK2_IM_S) Discard Mask */
#define SPW_LINK2_IM_S_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK2_IM_S) Escape Event 2 Position */
#define SPW_LINK2_IM_S_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK2_IM_S_ESCEVENT2_Pos)     /**< (SPW_LINK2_IM_S) Escape Event 2 Mask */
#define SPW_LINK2_IM_S_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK2_IM_S) Escape Event 1 Position */
#define SPW_LINK2_IM_S_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK2_IM_S_ESCEVENT1_Pos)     /**< (SPW_LINK2_IM_S) Escape Event 1 Mask */
#define SPW_LINK2_IM_S_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK2_IM_S) Register Mask  */

#define SPW_LINK2_IM_S_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK2_IM_S Position) Escape Event x */
#define SPW_LINK2_IM_S_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK2_IM_S_ESCEVENT_Pos)      /**< (SPW_LINK2_IM_S Mask) ESCEVENT */
#define SPW_LINK2_IM_S_ESCEVENT(value)        (SPW_LINK2_IM_S_ESCEVENT_Msk & ((value) << SPW_LINK2_IM_S_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_IM_C : (SPW Offset: 0x49C) ( /W 32) SpW Link 2 Interrupt Clear Mask -------- */
#define SPW_LINK2_IM_C_DISERR_Pos             _U_(0)                                         /**< (SPW_LINK2_IM_C) DisErr Position */
#define SPW_LINK2_IM_C_DISERR_Msk             (_U_(0x1) << SPW_LINK2_IM_C_DISERR_Pos)        /**< (SPW_LINK2_IM_C) DisErr Mask */
#define SPW_LINK2_IM_C_PARERR_Pos             _U_(1)                                         /**< (SPW_LINK2_IM_C) ParErr Position */
#define SPW_LINK2_IM_C_PARERR_Msk             (_U_(0x1) << SPW_LINK2_IM_C_PARERR_Pos)        /**< (SPW_LINK2_IM_C) ParErr Mask */
#define SPW_LINK2_IM_C_ESCERR_Pos             _U_(2)                                         /**< (SPW_LINK2_IM_C) ESCErr Position */
#define SPW_LINK2_IM_C_ESCERR_Msk             (_U_(0x1) << SPW_LINK2_IM_C_ESCERR_Pos)        /**< (SPW_LINK2_IM_C) ESCErr Mask */
#define SPW_LINK2_IM_C_CRERR_Pos              _U_(3)                                         /**< (SPW_LINK2_IM_C) CrErr Position */
#define SPW_LINK2_IM_C_CRERR_Msk              (_U_(0x1) << SPW_LINK2_IM_C_CRERR_Pos)         /**< (SPW_LINK2_IM_C) CrErr Mask */
#define SPW_LINK2_IM_C_LINKABORT_Pos          _U_(4)                                         /**< (SPW_LINK2_IM_C) LinkAbort Position */
#define SPW_LINK2_IM_C_LINKABORT_Msk          (_U_(0x1) << SPW_LINK2_IM_C_LINKABORT_Pos)     /**< (SPW_LINK2_IM_C) LinkAbort Mask */
#define SPW_LINK2_IM_C_EEPTRANS_Pos           _U_(5)                                         /**< (SPW_LINK2_IM_C) EEP transmitted Position */
#define SPW_LINK2_IM_C_EEPTRANS_Msk           (_U_(0x1) << SPW_LINK2_IM_C_EEPTRANS_Pos)      /**< (SPW_LINK2_IM_C) EEP transmitted Mask */
#define SPW_LINK2_IM_C_EEPREC_Pos             _U_(6)                                         /**< (SPW_LINK2_IM_C) EEP received Position */
#define SPW_LINK2_IM_C_EEPREC_Msk             (_U_(0x1) << SPW_LINK2_IM_C_EEPREC_Pos)        /**< (SPW_LINK2_IM_C) EEP received Mask */
#define SPW_LINK2_IM_C_DISCARD_Pos            _U_(7)                                         /**< (SPW_LINK2_IM_C) Discard Position */
#define SPW_LINK2_IM_C_DISCARD_Msk            (_U_(0x1) << SPW_LINK2_IM_C_DISCARD_Pos)       /**< (SPW_LINK2_IM_C) Discard Mask */
#define SPW_LINK2_IM_C_ESCEVENT2_Pos          _U_(8)                                         /**< (SPW_LINK2_IM_C) Escape Event 2 Position */
#define SPW_LINK2_IM_C_ESCEVENT2_Msk          (_U_(0x1) << SPW_LINK2_IM_C_ESCEVENT2_Pos)     /**< (SPW_LINK2_IM_C) Escape Event 2 Mask */
#define SPW_LINK2_IM_C_ESCEVENT1_Pos          _U_(9)                                         /**< (SPW_LINK2_IM_C) Escape Event 1 Position */
#define SPW_LINK2_IM_C_ESCEVENT1_Msk          (_U_(0x1) << SPW_LINK2_IM_C_ESCEVENT1_Pos)     /**< (SPW_LINK2_IM_C) Escape Event 1 Mask */
#define SPW_LINK2_IM_C_Msk                    _U_(0x000003FF)                                /**< (SPW_LINK2_IM_C) Register Mask  */

#define SPW_LINK2_IM_C_ESCEVENT_Pos           _U_(8)                                         /**< (SPW_LINK2_IM_C Position) Escape Event x */
#define SPW_LINK2_IM_C_ESCEVENT_Msk           (_U_(0x3) << SPW_LINK2_IM_C_ESCEVENT_Pos)      /**< (SPW_LINK2_IM_C Mask) ESCEVENT */
#define SPW_LINK2_IM_C_ESCEVENT(value)        (SPW_LINK2_IM_C_ESCEVENT_Msk & ((value) << SPW_LINK2_IM_C_ESCEVENT_Pos)) 

/* -------- SPW_LINK2_CFG : (SPW Offset: 0x4A0) (R/W 32) SpW Link 2 Config -------- */
#define SPW_LINK2_CFG_COMMAND_Pos             _U_(0)                                         /**< (SPW_LINK2_CFG) Command Position */
#define SPW_LINK2_CFG_COMMAND_Msk             (_U_(0x3) << SPW_LINK2_CFG_COMMAND_Pos)        /**< (SPW_LINK2_CFG) Command Mask */
#define SPW_LINK2_CFG_COMMAND(value)          (SPW_LINK2_CFG_COMMAND_Msk & ((value) << SPW_LINK2_CFG_COMMAND_Pos))
#define   SPW_LINK2_CFG_COMMAND_LINK_DISABLE_Val _U_(0x0)                                       /**< (SPW_LINK2_CFG) The link proceeds directly to the ErrorReset state when reaching the Run state.  */
#define   SPW_LINK2_CFG_COMMAND_NO_COMMAND_Val _U_(0x1)                                       /**< (SPW_LINK2_CFG) State is not actively changed.  */
#define   SPW_LINK2_CFG_COMMAND_AUTO_START_Val _U_(0x2)                                       /**< (SPW_LINK2_CFG) The Codec will wait in state Ready until the first NULL character is received.  */
#define   SPW_LINK2_CFG_COMMAND_LINK_START_Val _U_(0x3)                                       /**< (SPW_LINK2_CFG) SpaceWire link can proceed to Started state.  */
#define SPW_LINK2_CFG_COMMAND_LINK_DISABLE    (SPW_LINK2_CFG_COMMAND_LINK_DISABLE_Val << SPW_LINK2_CFG_COMMAND_Pos) /**< (SPW_LINK2_CFG) The link proceeds directly to the ErrorReset state when reaching the Run state. Position  */
#define SPW_LINK2_CFG_COMMAND_NO_COMMAND      (SPW_LINK2_CFG_COMMAND_NO_COMMAND_Val << SPW_LINK2_CFG_COMMAND_Pos) /**< (SPW_LINK2_CFG) State is not actively changed. Position  */
#define SPW_LINK2_CFG_COMMAND_AUTO_START      (SPW_LINK2_CFG_COMMAND_AUTO_START_Val << SPW_LINK2_CFG_COMMAND_Pos) /**< (SPW_LINK2_CFG) The Codec will wait in state Ready until the first NULL character is received. Position  */
#define SPW_LINK2_CFG_COMMAND_LINK_START      (SPW_LINK2_CFG_COMMAND_LINK_START_Val << SPW_LINK2_CFG_COMMAND_Pos) /**< (SPW_LINK2_CFG) SpaceWire link can proceed to Started state. Position  */
#define SPW_LINK2_CFG_Msk                     _U_(0x00000003)                                /**< (SPW_LINK2_CFG) Register Mask  */


/* -------- SPW_LINK2_CLKDIV : (SPW Offset: 0x4A4) (R/W 32) SpW Link 2 Clock Division -------- */
#define SPW_LINK2_CLKDIV_TXOPERDIV_Pos        _U_(0)                                         /**< (SPW_LINK2_CLKDIV) TxOperDiv Position */
#define SPW_LINK2_CLKDIV_TXOPERDIV_Msk        (_U_(0x1F) << SPW_LINK2_CLKDIV_TXOPERDIV_Pos)  /**< (SPW_LINK2_CLKDIV) TxOperDiv Mask */
#define SPW_LINK2_CLKDIV_TXOPERDIV(value)     (SPW_LINK2_CLKDIV_TXOPERDIV_Msk & ((value) << SPW_LINK2_CLKDIV_TXOPERDIV_Pos))
#define SPW_LINK2_CLKDIV_TXINITDIV_Pos        _U_(16)                                        /**< (SPW_LINK2_CLKDIV) TxInitDiv Position */
#define SPW_LINK2_CLKDIV_TXINITDIV_Msk        (_U_(0x1F) << SPW_LINK2_CLKDIV_TXINITDIV_Pos)  /**< (SPW_LINK2_CLKDIV) TxInitDiv Mask */
#define SPW_LINK2_CLKDIV_TXINITDIV(value)     (SPW_LINK2_CLKDIV_TXINITDIV_Msk & ((value) << SPW_LINK2_CLKDIV_TXINITDIV_Pos))
#define SPW_LINK2_CLKDIV_Msk                  _U_(0x001F001F)                                /**< (SPW_LINK2_CLKDIV) Register Mask  */


/* -------- SPW_LINK2_STATUS : (SPW Offset: 0x4A8) ( R/ 32) SpW Link 2 Status -------- */
#define SPW_LINK2_STATUS_LINKSTATE_Pos        _U_(0)                                         /**< (SPW_LINK2_STATUS) LinkState Position */
#define SPW_LINK2_STATUS_LINKSTATE_Msk        (_U_(0x7) << SPW_LINK2_STATUS_LINKSTATE_Pos)   /**< (SPW_LINK2_STATUS) LinkState Mask */
#define SPW_LINK2_STATUS_LINKSTATE(value)     (SPW_LINK2_STATUS_LINKSTATE_Msk & ((value) << SPW_LINK2_STATUS_LINKSTATE_Pos))
#define   SPW_LINK2_STATUS_LINKSTATE_ERRORRESET_Val _U_(0x0)                                       /**< (SPW_LINK2_STATUS) CODEC link state machine in ErrorReset state  */
#define   SPW_LINK2_STATUS_LINKSTATE_ERRORWAIT_Val _U_(0x1)                                       /**< (SPW_LINK2_STATUS) CODEC link state machine in ErrorWait state  */
#define   SPW_LINK2_STATUS_LINKSTATE_READY_Val _U_(0x2)                                       /**< (SPW_LINK2_STATUS) CODEC link state machine in Ready state  */
#define   SPW_LINK2_STATUS_LINKSTATE_STARTED_Val _U_(0x3)                                       /**< (SPW_LINK2_STATUS) CODEC link state machine in Started state  */
#define   SPW_LINK2_STATUS_LINKSTATE_CONNECTING_Val _U_(0x4)                                       /**< (SPW_LINK2_STATUS) CODEC link state machine in Connecting state  */
#define   SPW_LINK2_STATUS_LINKSTATE_RUN_Val  _U_(0x5)                                       /**< (SPW_LINK2_STATUS) CODEC link state machine in Run state  */
#define SPW_LINK2_STATUS_LINKSTATE_ERRORRESET (SPW_LINK2_STATUS_LINKSTATE_ERRORRESET_Val << SPW_LINK2_STATUS_LINKSTATE_Pos) /**< (SPW_LINK2_STATUS) CODEC link state machine in ErrorReset state Position  */
#define SPW_LINK2_STATUS_LINKSTATE_ERRORWAIT  (SPW_LINK2_STATUS_LINKSTATE_ERRORWAIT_Val << SPW_LINK2_STATUS_LINKSTATE_Pos) /**< (SPW_LINK2_STATUS) CODEC link state machine in ErrorWait state Position  */
#define SPW_LINK2_STATUS_LINKSTATE_READY      (SPW_LINK2_STATUS_LINKSTATE_READY_Val << SPW_LINK2_STATUS_LINKSTATE_Pos) /**< (SPW_LINK2_STATUS) CODEC link state machine in Ready state Position  */
#define SPW_LINK2_STATUS_LINKSTATE_STARTED    (SPW_LINK2_STATUS_LINKSTATE_STARTED_Val << SPW_LINK2_STATUS_LINKSTATE_Pos) /**< (SPW_LINK2_STATUS) CODEC link state machine in Started state Position  */
#define SPW_LINK2_STATUS_LINKSTATE_CONNECTING (SPW_LINK2_STATUS_LINKSTATE_CONNECTING_Val << SPW_LINK2_STATUS_LINKSTATE_Pos) /**< (SPW_LINK2_STATUS) CODEC link state machine in Connecting state Position  */
#define SPW_LINK2_STATUS_LINKSTATE_RUN        (SPW_LINK2_STATUS_LINKSTATE_RUN_Val << SPW_LINK2_STATUS_LINKSTATE_Pos) /**< (SPW_LINK2_STATUS) CODEC link state machine in Run state Position  */
#define SPW_LINK2_STATUS_TXDEFDIV_Pos         _U_(4)                                         /**< (SPW_LINK2_STATUS) TxDefDiv Position */
#define SPW_LINK2_STATUS_TXDEFDIV_Msk         (_U_(0x1F) << SPW_LINK2_STATUS_TXDEFDIV_Pos)   /**< (SPW_LINK2_STATUS) TxDefDiv Mask */
#define SPW_LINK2_STATUS_TXDEFDIV(value)      (SPW_LINK2_STATUS_TXDEFDIV_Msk & ((value) << SPW_LINK2_STATUS_TXDEFDIV_Pos))
#define SPW_LINK2_STATUS_TXEMPTY_Pos          _U_(16)                                        /**< (SPW_LINK2_STATUS) TxEmpty Position */
#define SPW_LINK2_STATUS_TXEMPTY_Msk          (_U_(0x1) << SPW_LINK2_STATUS_TXEMPTY_Pos)     /**< (SPW_LINK2_STATUS) TxEmpty Mask */
#define SPW_LINK2_STATUS_GOTNULL_Pos          _U_(17)                                        /**< (SPW_LINK2_STATUS) GotNull Position */
#define SPW_LINK2_STATUS_GOTNULL_Msk          (_U_(0x1) << SPW_LINK2_STATUS_GOTNULL_Pos)     /**< (SPW_LINK2_STATUS) GotNull Mask */
#define SPW_LINK2_STATUS_GOTFCT_Pos           _U_(18)                                        /**< (SPW_LINK2_STATUS) GotFCT Position */
#define SPW_LINK2_STATUS_GOTFCT_Msk           (_U_(0x1) << SPW_LINK2_STATUS_GOTFCT_Pos)      /**< (SPW_LINK2_STATUS) GotFCT Mask */
#define SPW_LINK2_STATUS_GOTNCHAR_Pos         _U_(19)                                        /**< (SPW_LINK2_STATUS) GotNChar Position */
#define SPW_LINK2_STATUS_GOTNCHAR_Msk         (_U_(0x1) << SPW_LINK2_STATUS_GOTNCHAR_Pos)    /**< (SPW_LINK2_STATUS) GotNChar Mask */
#define SPW_LINK2_STATUS_SEEN0_Pos            _U_(20)                                        /**< (SPW_LINK2_STATUS) SEEN0 Position */
#define SPW_LINK2_STATUS_SEEN0_Msk            (_U_(0x1) << SPW_LINK2_STATUS_SEEN0_Pos)       /**< (SPW_LINK2_STATUS) SEEN0 Mask */
#define SPW_LINK2_STATUS_SEEN1_Pos            _U_(21)                                        /**< (SPW_LINK2_STATUS) SEEN1 Position */
#define SPW_LINK2_STATUS_SEEN1_Msk            (_U_(0x1) << SPW_LINK2_STATUS_SEEN1_Pos)       /**< (SPW_LINK2_STATUS) SEEN1 Mask */
#define SPW_LINK2_STATUS_SEEN2_Pos            _U_(22)                                        /**< (SPW_LINK2_STATUS) SEEN2 Position */
#define SPW_LINK2_STATUS_SEEN2_Msk            (_U_(0x1) << SPW_LINK2_STATUS_SEEN2_Pos)       /**< (SPW_LINK2_STATUS) SEEN2 Mask */
#define SPW_LINK2_STATUS_SEEN3_Pos            _U_(23)                                        /**< (SPW_LINK2_STATUS) SEEN3 Position */
#define SPW_LINK2_STATUS_SEEN3_Msk            (_U_(0x1) << SPW_LINK2_STATUS_SEEN3_Pos)       /**< (SPW_LINK2_STATUS) SEEN3 Mask */
#define SPW_LINK2_STATUS_SEEN4_Pos            _U_(24)                                        /**< (SPW_LINK2_STATUS) SEEN4 Position */
#define SPW_LINK2_STATUS_SEEN4_Msk            (_U_(0x1) << SPW_LINK2_STATUS_SEEN4_Pos)       /**< (SPW_LINK2_STATUS) SEEN4 Mask */
#define SPW_LINK2_STATUS_SEEN5_Pos            _U_(25)                                        /**< (SPW_LINK2_STATUS) SEEN5 Position */
#define SPW_LINK2_STATUS_SEEN5_Msk            (_U_(0x1) << SPW_LINK2_STATUS_SEEN5_Pos)       /**< (SPW_LINK2_STATUS) SEEN5 Mask */
#define SPW_LINK2_STATUS_Msk                  _U_(0x03FF01F7)                                /**< (SPW_LINK2_STATUS) Register Mask  */

#define SPW_LINK2_STATUS_SEEN_Pos             _U_(20)                                        /**< (SPW_LINK2_STATUS Position) SEEN5 */
#define SPW_LINK2_STATUS_SEEN_Msk             (_U_(0x3F) << SPW_LINK2_STATUS_SEEN_Pos)       /**< (SPW_LINK2_STATUS Mask) SEEN */
#define SPW_LINK2_STATUS_SEEN(value)          (SPW_LINK2_STATUS_SEEN_Msk & ((value) << SPW_LINK2_STATUS_SEEN_Pos)) 

/* -------- SPW_LINK2_SWRESET : (SPW Offset: 0x4AC) (R/W 32) SpW Link 2 Software Reset -------- */
#define SPW_LINK2_SWRESET_PATTERN_Pos         _U_(0)                                         /**< (SPW_LINK2_SWRESET) Pattern Position */
#define SPW_LINK2_SWRESET_PATTERN_Msk         (_U_(0xFFFFFFFF) << SPW_LINK2_SWRESET_PATTERN_Pos) /**< (SPW_LINK2_SWRESET) Pattern Mask */
#define SPW_LINK2_SWRESET_PATTERN(value)      (SPW_LINK2_SWRESET_PATTERN_Msk & ((value) << SPW_LINK2_SWRESET_PATTERN_Pos))
#define SPW_LINK2_SWRESET_Msk                 _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_SWRESET) Register Mask  */


/* -------- SPW_LINK2_ESCCHAREVENT0 : (SPW Offset: 0x4B0) (R/W 32) SpW Link 2 Escape Character Event 0 -------- */
#define SPW_LINK2_ESCCHAREVENT0_VALUE_Pos     _U_(0)                                         /**< (SPW_LINK2_ESCCHAREVENT0) Value Position */
#define SPW_LINK2_ESCCHAREVENT0_VALUE_Msk     (_U_(0xFF) << SPW_LINK2_ESCCHAREVENT0_VALUE_Pos) /**< (SPW_LINK2_ESCCHAREVENT0) Value Mask */
#define SPW_LINK2_ESCCHAREVENT0_VALUE(value)  (SPW_LINK2_ESCCHAREVENT0_VALUE_Msk & ((value) << SPW_LINK2_ESCCHAREVENT0_VALUE_Pos))
#define SPW_LINK2_ESCCHAREVENT0_MASK_Pos      _U_(8)                                         /**< (SPW_LINK2_ESCCHAREVENT0) Mask Position */
#define SPW_LINK2_ESCCHAREVENT0_MASK_Msk      (_U_(0xFF) << SPW_LINK2_ESCCHAREVENT0_MASK_Pos) /**< (SPW_LINK2_ESCCHAREVENT0) Mask Mask */
#define SPW_LINK2_ESCCHAREVENT0_MASK(value)   (SPW_LINK2_ESCCHAREVENT0_MASK_Msk & ((value) << SPW_LINK2_ESCCHAREVENT0_MASK_Pos))
#define SPW_LINK2_ESCCHAREVENT0_ACTIVE_Pos    _U_(16)                                        /**< (SPW_LINK2_ESCCHAREVENT0) Active Position */
#define SPW_LINK2_ESCCHAREVENT0_ACTIVE_Msk    (_U_(0x1) << SPW_LINK2_ESCCHAREVENT0_ACTIVE_Pos) /**< (SPW_LINK2_ESCCHAREVENT0) Active Mask */
#define SPW_LINK2_ESCCHAREVENT0_HWEVENT_Pos   _U_(17)                                        /**< (SPW_LINK2_ESCCHAREVENT0) HwEvent Position */
#define SPW_LINK2_ESCCHAREVENT0_HWEVENT_Msk   (_U_(0x1) << SPW_LINK2_ESCCHAREVENT0_HWEVENT_Pos) /**< (SPW_LINK2_ESCCHAREVENT0) HwEvent Mask */
#define SPW_LINK2_ESCCHAREVENT0_Msk           _U_(0x0003FFFF)                                /**< (SPW_LINK2_ESCCHAREVENT0) Register Mask  */


/* -------- SPW_LINK2_ESCCHAREVENT1 : (SPW Offset: 0x4B4) (R/W 32) SpW Link 2 Escape Character Event 1 -------- */
#define SPW_LINK2_ESCCHAREVENT1_VALUE_Pos     _U_(0)                                         /**< (SPW_LINK2_ESCCHAREVENT1) Value Position */
#define SPW_LINK2_ESCCHAREVENT1_VALUE_Msk     (_U_(0xFF) << SPW_LINK2_ESCCHAREVENT1_VALUE_Pos) /**< (SPW_LINK2_ESCCHAREVENT1) Value Mask */
#define SPW_LINK2_ESCCHAREVENT1_VALUE(value)  (SPW_LINK2_ESCCHAREVENT1_VALUE_Msk & ((value) << SPW_LINK2_ESCCHAREVENT1_VALUE_Pos))
#define SPW_LINK2_ESCCHAREVENT1_MASK_Pos      _U_(8)                                         /**< (SPW_LINK2_ESCCHAREVENT1) Mask Position */
#define SPW_LINK2_ESCCHAREVENT1_MASK_Msk      (_U_(0xFF) << SPW_LINK2_ESCCHAREVENT1_MASK_Pos) /**< (SPW_LINK2_ESCCHAREVENT1) Mask Mask */
#define SPW_LINK2_ESCCHAREVENT1_MASK(value)   (SPW_LINK2_ESCCHAREVENT1_MASK_Msk & ((value) << SPW_LINK2_ESCCHAREVENT1_MASK_Pos))
#define SPW_LINK2_ESCCHAREVENT1_ACTIVE_Pos    _U_(16)                                        /**< (SPW_LINK2_ESCCHAREVENT1) Active Position */
#define SPW_LINK2_ESCCHAREVENT1_ACTIVE_Msk    (_U_(0x1) << SPW_LINK2_ESCCHAREVENT1_ACTIVE_Pos) /**< (SPW_LINK2_ESCCHAREVENT1) Active Mask */
#define SPW_LINK2_ESCCHAREVENT1_HWEVENT_Pos   _U_(17)                                        /**< (SPW_LINK2_ESCCHAREVENT1) HwEvent Position */
#define SPW_LINK2_ESCCHAREVENT1_HWEVENT_Msk   (_U_(0x1) << SPW_LINK2_ESCCHAREVENT1_HWEVENT_Pos) /**< (SPW_LINK2_ESCCHAREVENT1) HwEvent Mask */
#define SPW_LINK2_ESCCHAREVENT1_Msk           _U_(0x0003FFFF)                                /**< (SPW_LINK2_ESCCHAREVENT1) Register Mask  */


/* -------- SPW_LINK2_ESCCHARSTS : (SPW Offset: 0x4B8) ( R/ 32) SpW Link 2 Escape Character Status -------- */
#define SPW_LINK2_ESCCHARSTS_CHAR1_Pos        _U_(0)                                         /**< (SPW_LINK2_ESCCHARSTS) Esc Char 1 Position */
#define SPW_LINK2_ESCCHARSTS_CHAR1_Msk        (_U_(0xFF) << SPW_LINK2_ESCCHARSTS_CHAR1_Pos)  /**< (SPW_LINK2_ESCCHARSTS) Esc Char 1 Mask */
#define SPW_LINK2_ESCCHARSTS_CHAR1(value)     (SPW_LINK2_ESCCHARSTS_CHAR1_Msk & ((value) << SPW_LINK2_ESCCHARSTS_CHAR1_Pos))
#define SPW_LINK2_ESCCHARSTS_CHAR2_Pos        _U_(8)                                         /**< (SPW_LINK2_ESCCHARSTS) Esc Char 2 Position */
#define SPW_LINK2_ESCCHARSTS_CHAR2_Msk        (_U_(0xFF) << SPW_LINK2_ESCCHARSTS_CHAR2_Pos)  /**< (SPW_LINK2_ESCCHARSTS) Esc Char 2 Mask */
#define SPW_LINK2_ESCCHARSTS_CHAR2(value)     (SPW_LINK2_ESCCHARSTS_CHAR2_Msk & ((value) << SPW_LINK2_ESCCHARSTS_CHAR2_Pos))
#define SPW_LINK2_ESCCHARSTS_Msk              _U_(0x0000FFFF)                                /**< (SPW_LINK2_ESCCHARSTS) Register Mask  */


/* -------- SPW_LINK2_TRANSESC : (SPW Offset: 0x4BC) (R/W 32) SpW Link 2 Transmit Escape Character -------- */
#define SPW_LINK2_TRANSESC_CHAR_Pos           _U_(0)                                         /**< (SPW_LINK2_TRANSESC) Character Position */
#define SPW_LINK2_TRANSESC_CHAR_Msk           (_U_(0xFF) << SPW_LINK2_TRANSESC_CHAR_Pos)     /**< (SPW_LINK2_TRANSESC) Character Mask */
#define SPW_LINK2_TRANSESC_CHAR(value)        (SPW_LINK2_TRANSESC_CHAR_Msk & ((value) << SPW_LINK2_TRANSESC_CHAR_Pos))
#define SPW_LINK2_TRANSESC_Msk                _U_(0x000000FF)                                /**< (SPW_LINK2_TRANSESC) Register Mask  */


/* -------- SPW_LINK2_DISTINTPI_RM : (SPW Offset: 0x4C0) ( R/ 32) SpW Link 2 Distributed Interrupt Pending Read Masked Interrupt -------- */
#define SPW_LINK2_DISTINTPI_RM_DI0_Pos        _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI0_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI0_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI1_Pos        _U_(1)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI1_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI1_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI2_Pos        _U_(2)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI2_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI2_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI3_Pos        _U_(3)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI3_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI3_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI4_Pos        _U_(4)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI4_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI4_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI5_Pos        _U_(5)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI5_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI5_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI6_Pos        _U_(6)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI6_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI6_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI7_Pos        _U_(7)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI7_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI7_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI8_Pos        _U_(8)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI8_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI8_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI9_Pos        _U_(9)                                         /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI9_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI9_Pos)   /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI10_Pos       _U_(10)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI10_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI10_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI11_Pos       _U_(11)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI11_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI11_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI12_Pos       _U_(12)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI12_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI12_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI13_Pos       _U_(13)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI13_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI13_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI14_Pos       _U_(14)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI14_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI14_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI15_Pos       _U_(15)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI15_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI15_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI16_Pos       _U_(16)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI16_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI16_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI17_Pos       _U_(17)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI17_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI17_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI18_Pos       _U_(18)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI18_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI18_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI19_Pos       _U_(19)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI19_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI19_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI20_Pos       _U_(20)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI20_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI20_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI21_Pos       _U_(21)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI21_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI21_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI22_Pos       _U_(22)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI22_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI22_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI23_Pos       _U_(23)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI23_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI23_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI24_Pos       _U_(24)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI24_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI24_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI25_Pos       _U_(25)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI25_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI25_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI26_Pos       _U_(26)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI26_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI26_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI27_Pos       _U_(27)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI27_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI27_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI28_Pos       _U_(28)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI28_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI28_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI29_Pos       _U_(29)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI29_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI29_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI30_Pos       _U_(30)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI30_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI30_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_DI31_Pos       _U_(31)                                        /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RM_DI31_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RM_DI31_Pos)  /**< (SPW_LINK2_DISTINTPI_RM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RM_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTPI_RM) Register Mask  */

#define SPW_LINK2_DISTINTPI_RM_DI_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_RM Position) Distributed Interrupt */
#define SPW_LINK2_DISTINTPI_RM_DI_Msk         (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTPI_RM_DI_Pos) /**< (SPW_LINK2_DISTINTPI_RM Mask) DI */
#define SPW_LINK2_DISTINTPI_RM_DI(value)      (SPW_LINK2_DISTINTPI_RM_DI_Msk & ((value) << SPW_LINK2_DISTINTPI_RM_DI_Pos)) 

/* -------- SPW_LINK2_DISTINTPI_RCM : (SPW Offset: 0x4C4) ( R/ 32) SpW Link 2 Distributed Interrupt Pending Read and Clear Masked Interrupt -------- */
#define SPW_LINK2_DISTINTPI_RCM_DI0_Pos       _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI0_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI0_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI1_Pos       _U_(1)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI1_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI1_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI2_Pos       _U_(2)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI2_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI2_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI3_Pos       _U_(3)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI3_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI3_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI4_Pos       _U_(4)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI4_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI4_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI5_Pos       _U_(5)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI5_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI5_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI6_Pos       _U_(6)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI6_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI6_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI7_Pos       _U_(7)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI7_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI7_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI8_Pos       _U_(8)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI8_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI8_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI9_Pos       _U_(9)                                         /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI9_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI9_Pos)  /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI10_Pos      _U_(10)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI10_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI10_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI11_Pos      _U_(11)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI11_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI11_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI12_Pos      _U_(12)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI12_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI12_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI13_Pos      _U_(13)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI13_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI13_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI14_Pos      _U_(14)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI14_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI14_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI15_Pos      _U_(15)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI15_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI15_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI16_Pos      _U_(16)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI16_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI16_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI17_Pos      _U_(17)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI17_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI17_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI18_Pos      _U_(18)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI18_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI18_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI19_Pos      _U_(19)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI19_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI19_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI20_Pos      _U_(20)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI20_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI20_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI21_Pos      _U_(21)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI21_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI21_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI22_Pos      _U_(22)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI22_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI22_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI23_Pos      _U_(23)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI23_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI23_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI24_Pos      _U_(24)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI24_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI24_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI25_Pos      _U_(25)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI25_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI25_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI26_Pos      _U_(26)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI26_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI26_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI27_Pos      _U_(27)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI27_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI27_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI28_Pos      _U_(28)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI28_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI28_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI29_Pos      _U_(29)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI29_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI29_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI30_Pos      _U_(30)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI30_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI30_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_DI31_Pos      _U_(31)                                        /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCM_DI31_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCM_DI31_Pos) /**< (SPW_LINK2_DISTINTPI_RCM) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCM_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTPI_RCM) Register Mask  */

#define SPW_LINK2_DISTINTPI_RCM_DI_Pos        _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_RCM Position) Distributed Interrupt */
#define SPW_LINK2_DISTINTPI_RCM_DI_Msk        (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTPI_RCM_DI_Pos) /**< (SPW_LINK2_DISTINTPI_RCM Mask) DI */
#define SPW_LINK2_DISTINTPI_RCM_DI(value)     (SPW_LINK2_DISTINTPI_RCM_DI_Msk & ((value) << SPW_LINK2_DISTINTPI_RCM_DI_Pos)) 

/* -------- SPW_LINK2_DISTINTPI_R : (SPW Offset: 0x4C8) ( R/ 32) SpW Link 2 Distributed Interrupt Pending Read Interrupt -------- */
#define SPW_LINK2_DISTINTPI_R_DI0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI0_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI0_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI1_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI1_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI2_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI2_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI3_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI3_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI4_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI4_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI5_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI5_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI6_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI6_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI7_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI7_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI8_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI8_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI9_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI9_Pos)    /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI10_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI10_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI11_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI11_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI12_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI12_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI13_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI13_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI14_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI14_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI15_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI15_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI16_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI16_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI17_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI17_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI18_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI18_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI19_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI19_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI20_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI20_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI21_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI21_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI22_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI22_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI23_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI23_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI24_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI24_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI25_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI25_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI26_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI26_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI27_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI27_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI28_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI28_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI29_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI29_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI30_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI30_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_DI31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_R_DI31_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_R_DI31_Pos)   /**< (SPW_LINK2_DISTINTPI_R) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_R_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTPI_R) Register Mask  */

#define SPW_LINK2_DISTINTPI_R_DI_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_R Position) Distributed Interrupt */
#define SPW_LINK2_DISTINTPI_R_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTPI_R_DI_Pos) /**< (SPW_LINK2_DISTINTPI_R Mask) DI */
#define SPW_LINK2_DISTINTPI_R_DI(value)       (SPW_LINK2_DISTINTPI_R_DI_Msk & ((value) << SPW_LINK2_DISTINTPI_R_DI_Pos)) 

/* -------- SPW_LINK2_DISTINTPI_RCS : (SPW Offset: 0x4CC) (R/W 32) SpW Link 2 Distributed Interrupt Pending Read and Clear Interrupt -------- */
#define SPW_LINK2_DISTINTPI_RCS_DI0_Pos       _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI0_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI0_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI1_Pos       _U_(1)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI1_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI1_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI2_Pos       _U_(2)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI2_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI2_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI3_Pos       _U_(3)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI3_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI3_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI4_Pos       _U_(4)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI4_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI4_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI5_Pos       _U_(5)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI5_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI5_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI6_Pos       _U_(6)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI6_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI6_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI7_Pos       _U_(7)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI7_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI7_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI8_Pos       _U_(8)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI8_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI8_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI9_Pos       _U_(9)                                         /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI9_Msk       (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI9_Pos)  /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI10_Pos      _U_(10)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI10_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI10_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI11_Pos      _U_(11)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI11_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI11_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI12_Pos      _U_(12)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI12_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI12_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI13_Pos      _U_(13)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI13_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI13_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI14_Pos      _U_(14)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI14_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI14_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI15_Pos      _U_(15)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI15_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI15_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI16_Pos      _U_(16)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI16_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI16_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI17_Pos      _U_(17)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI17_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI17_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI18_Pos      _U_(18)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI18_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI18_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI19_Pos      _U_(19)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI19_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI19_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI20_Pos      _U_(20)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI20_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI20_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI21_Pos      _U_(21)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI21_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI21_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI22_Pos      _U_(22)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI22_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI22_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI23_Pos      _U_(23)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI23_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI23_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI24_Pos      _U_(24)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI24_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI24_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI25_Pos      _U_(25)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI25_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI25_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI26_Pos      _U_(26)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI26_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI26_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI27_Pos      _U_(27)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI27_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI27_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI28_Pos      _U_(28)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI28_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI28_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI29_Pos      _U_(29)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI29_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI29_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI30_Pos      _U_(30)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI30_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI30_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_DI31_Pos      _U_(31)                                        /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_RCS_DI31_Msk      (_U_(0x1) << SPW_LINK2_DISTINTPI_RCS_DI31_Pos) /**< (SPW_LINK2_DISTINTPI_RCS) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_RCS_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTPI_RCS) Register Mask  */

#define SPW_LINK2_DISTINTPI_RCS_DI_Pos        _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_RCS Position) Distributed Interrupt */
#define SPW_LINK2_DISTINTPI_RCS_DI_Msk        (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTPI_RCS_DI_Pos) /**< (SPW_LINK2_DISTINTPI_RCS Mask) DI */
#define SPW_LINK2_DISTINTPI_RCS_DI(value)     (SPW_LINK2_DISTINTPI_RCS_DI_Msk & ((value) << SPW_LINK2_DISTINTPI_RCS_DI_Pos)) 

/* -------- SPW_LINK2_DISTINTIM : (SPW Offset: 0x4D0) (R/W 32) SpW Link 2 Distributed Interrupt Mask -------- */
#define SPW_LINK2_DISTINTIM_DI0_Pos           _U_(0)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI0_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI0_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI1_Pos           _U_(1)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI1_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI1_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI2_Pos           _U_(2)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI2_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI2_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI3_Pos           _U_(3)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI3_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI3_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI4_Pos           _U_(4)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI4_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI4_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI5_Pos           _U_(5)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI5_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI5_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI6_Pos           _U_(6)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI6_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI6_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI7_Pos           _U_(7)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI7_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI7_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI8_Pos           _U_(8)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI8_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI8_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI9_Pos           _U_(9)                                         /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI9_Msk           (_U_(0x1) << SPW_LINK2_DISTINTIM_DI9_Pos)      /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI10_Pos          _U_(10)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI10_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI10_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI11_Pos          _U_(11)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI11_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI11_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI12_Pos          _U_(12)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI12_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI12_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI13_Pos          _U_(13)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI13_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI13_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI14_Pos          _U_(14)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI14_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI14_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI15_Pos          _U_(15)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI15_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI15_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI16_Pos          _U_(16)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI16_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI16_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI17_Pos          _U_(17)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI17_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI17_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI18_Pos          _U_(18)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI18_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI18_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI19_Pos          _U_(19)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI19_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI19_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI20_Pos          _U_(20)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI20_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI20_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI21_Pos          _U_(21)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI21_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI21_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI22_Pos          _U_(22)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI22_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI22_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI23_Pos          _U_(23)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI23_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI23_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI24_Pos          _U_(24)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI24_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI24_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI25_Pos          _U_(25)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI25_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI25_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI26_Pos          _U_(26)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI26_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI26_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI27_Pos          _U_(27)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI27_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI27_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI28_Pos          _U_(28)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI28_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI28_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI29_Pos          _U_(29)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI29_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI29_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI30_Pos          _U_(30)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI30_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI30_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_DI31_Pos          _U_(31)                                        /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_DI31_Msk          (_U_(0x1) << SPW_LINK2_DISTINTIM_DI31_Pos)     /**< (SPW_LINK2_DISTINTIM) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_Msk               _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTIM) Register Mask  */

#define SPW_LINK2_DISTINTIM_DI_Pos            _U_(0)                                         /**< (SPW_LINK2_DISTINTIM Position) Distributed Interrupt mask */
#define SPW_LINK2_DISTINTIM_DI_Msk            (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTIM_DI_Pos) /**< (SPW_LINK2_DISTINTIM Mask) DI */
#define SPW_LINK2_DISTINTIM_DI(value)         (SPW_LINK2_DISTINTIM_DI_Msk & ((value) << SPW_LINK2_DISTINTIM_DI_Pos)) 

/* -------- SPW_LINK2_DISTINTPI_C : (SPW Offset: 0x4D4) ( /W 32) SpW Link 2 Distributed Interrupt Clear Pending Interrupt -------- */
#define SPW_LINK2_DISTINTPI_C_DI0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI0_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI0_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI1_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI1_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI2_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI2_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI3_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI3_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI4_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI4_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI5_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI5_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI6_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI6_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI7_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI7_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI8_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI8_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI9_Msk         (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI9_Pos)    /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI10_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI10_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI11_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI11_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI12_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI12_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI13_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI13_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI14_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI14_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI15_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI15_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI16_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI16_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI17_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI17_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI18_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI18_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI19_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI19_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI20_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI20_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI21_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI21_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI22_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI22_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI23_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI23_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI24_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI24_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI25_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI25_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI26_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI26_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI27_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI27_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI28_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI28_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI29_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI29_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI30_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI30_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_DI31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Position */
#define SPW_LINK2_DISTINTPI_C_DI31_Msk        (_U_(0x1) << SPW_LINK2_DISTINTPI_C_DI31_Pos)   /**< (SPW_LINK2_DISTINTPI_C) Distributed Interrupt Mask */
#define SPW_LINK2_DISTINTPI_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTPI_C) Register Mask  */

#define SPW_LINK2_DISTINTPI_C_DI_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTINTPI_C Position) Distributed Interrupt */
#define SPW_LINK2_DISTINTPI_C_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTPI_C_DI_Pos) /**< (SPW_LINK2_DISTINTPI_C Mask) DI */
#define SPW_LINK2_DISTINTPI_C_DI(value)       (SPW_LINK2_DISTINTPI_C_DI_Msk & ((value) << SPW_LINK2_DISTINTPI_C_DI_Pos)) 

/* -------- SPW_LINK2_DISTINTIM_S : (SPW Offset: 0x4D8) ( /W 32) SpW Link 2 Distributed Interrupt Set Mask -------- */
#define SPW_LINK2_DISTINTIM_S_DI0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI0_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI0_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI1_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI1_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI2_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI2_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI3_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI3_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI4_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI4_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI5_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI5_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI6_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI6_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI7_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI7_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI8_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI8_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI9_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI9_Pos)    /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI10_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI10_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI11_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI11_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI12_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI12_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI13_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI13_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI14_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI14_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI15_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI15_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI16_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI16_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI17_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI17_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI18_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI18_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI19_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI19_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI20_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI20_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI21_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI21_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI22_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI22_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI23_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI23_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI24_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI24_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI25_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI25_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI26_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI26_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI27_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI27_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI28_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI28_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI29_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI29_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI30_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI30_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_DI31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_S_DI31_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_S_DI31_Pos)   /**< (SPW_LINK2_DISTINTIM_S) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_S_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTIM_S) Register Mask  */

#define SPW_LINK2_DISTINTIM_S_DI_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTINTIM_S Position) Distributed Interrupt mask */
#define SPW_LINK2_DISTINTIM_S_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTIM_S_DI_Pos) /**< (SPW_LINK2_DISTINTIM_S Mask) DI */
#define SPW_LINK2_DISTINTIM_S_DI(value)       (SPW_LINK2_DISTINTIM_S_DI_Msk & ((value) << SPW_LINK2_DISTINTIM_S_DI_Pos)) 

/* -------- SPW_LINK2_DISTINTIM_C : (SPW Offset: 0x4DC) ( /W 32) SpW Link 2 Distributed Interrupt Clear Mask -------- */
#define SPW_LINK2_DISTINTIM_C_DI0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI0_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI0_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI1_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI1_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI2_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI2_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI3_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI3_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI4_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI4_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI5_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI5_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI6_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI6_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI7_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI7_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI8_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI8_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI9_Msk         (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI9_Pos)    /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI10_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI10_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI11_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI11_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI12_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI12_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI13_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI13_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI14_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI14_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI15_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI15_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI16_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI16_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI17_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI17_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI18_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI18_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI19_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI19_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI20_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI20_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI21_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI21_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI22_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI22_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI23_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI23_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI24_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI24_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI25_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI25_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI26_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI26_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI27_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI27_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI28_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI28_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI29_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI29_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI30_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI30_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_DI31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Position */
#define SPW_LINK2_DISTINTIM_C_DI31_Msk        (_U_(0x1) << SPW_LINK2_DISTINTIM_C_DI31_Pos)   /**< (SPW_LINK2_DISTINTIM_C) Distributed Interrupt mask Mask */
#define SPW_LINK2_DISTINTIM_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTINTIM_C) Register Mask  */

#define SPW_LINK2_DISTINTIM_C_DI_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTINTIM_C Position) Distributed Interrupt mask */
#define SPW_LINK2_DISTINTIM_C_DI_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTINTIM_C_DI_Pos) /**< (SPW_LINK2_DISTINTIM_C Mask) DI */
#define SPW_LINK2_DISTINTIM_C_DI(value)       (SPW_LINK2_DISTINTIM_C_DI_Msk & ((value) << SPW_LINK2_DISTINTIM_C_DI_Pos)) 

/* -------- SPW_LINK2_DISTACKPI_RM : (SPW Offset: 0x4E0) ( R/ 32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read Masked Interrupt -------- */
#define SPW_LINK2_DISTACKPI_RM_DA0_Pos        _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA0_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA0_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA1_Pos        _U_(1)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA1_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA1_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA2_Pos        _U_(2)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA2_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA2_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA3_Pos        _U_(3)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA3_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA3_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA4_Pos        _U_(4)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA4_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA4_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA5_Pos        _U_(5)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA5_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA5_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA6_Pos        _U_(6)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA6_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA6_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA7_Pos        _U_(7)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA7_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA7_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA8_Pos        _U_(8)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA8_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA8_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA9_Pos        _U_(9)                                         /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA9_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA9_Pos)   /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA10_Pos       _U_(10)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA10_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA10_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA11_Pos       _U_(11)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA11_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA11_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA12_Pos       _U_(12)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA12_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA12_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA13_Pos       _U_(13)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA13_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA13_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA14_Pos       _U_(14)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA14_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA14_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA15_Pos       _U_(15)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA15_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA15_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA16_Pos       _U_(16)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA16_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA16_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA17_Pos       _U_(17)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA17_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA17_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA18_Pos       _U_(18)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA18_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA18_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA19_Pos       _U_(19)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA19_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA19_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA20_Pos       _U_(20)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA20_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA20_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA21_Pos       _U_(21)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA21_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA21_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA22_Pos       _U_(22)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA22_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA22_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA23_Pos       _U_(23)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA23_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA23_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA24_Pos       _U_(24)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA24_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA24_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA25_Pos       _U_(25)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA25_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA25_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA26_Pos       _U_(26)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA26_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA26_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA27_Pos       _U_(27)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA27_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA27_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA28_Pos       _U_(28)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA28_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA28_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA29_Pos       _U_(29)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA29_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA29_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA30_Pos       _U_(30)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA30_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA30_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_DA31_Pos       _U_(31)                                        /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RM_DA31_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RM_DA31_Pos)  /**< (SPW_LINK2_DISTACKPI_RM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RM_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKPI_RM) Register Mask  */

#define SPW_LINK2_DISTACKPI_RM_DA_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_RM Position) Distributed Acknowledge */
#define SPW_LINK2_DISTACKPI_RM_DA_Msk         (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKPI_RM_DA_Pos) /**< (SPW_LINK2_DISTACKPI_RM Mask) DA */
#define SPW_LINK2_DISTACKPI_RM_DA(value)      (SPW_LINK2_DISTACKPI_RM_DA_Msk & ((value) << SPW_LINK2_DISTACKPI_RM_DA_Pos)) 

/* -------- SPW_LINK2_DISTACKPI_RCM : (SPW Offset: 0x4E4) ( R/ 32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read and Clear Masked Interrupt -------- */
#define SPW_LINK2_DISTACKPI_RCM_DA0_Pos       _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA0_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA0_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA1_Pos       _U_(1)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA1_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA1_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA2_Pos       _U_(2)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA2_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA2_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA3_Pos       _U_(3)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA3_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA3_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA4_Pos       _U_(4)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA4_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA4_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA5_Pos       _U_(5)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA5_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA5_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA6_Pos       _U_(6)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA6_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA6_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA7_Pos       _U_(7)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA7_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA7_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA8_Pos       _U_(8)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA8_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA8_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA9_Pos       _U_(9)                                         /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA9_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA9_Pos)  /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA10_Pos      _U_(10)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA10_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA10_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA11_Pos      _U_(11)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA11_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA11_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA12_Pos      _U_(12)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA12_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA12_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA13_Pos      _U_(13)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA13_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA13_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA14_Pos      _U_(14)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA14_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA14_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA15_Pos      _U_(15)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA15_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA15_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA16_Pos      _U_(16)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA16_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA16_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA17_Pos      _U_(17)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA17_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA17_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA18_Pos      _U_(18)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA18_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA18_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA19_Pos      _U_(19)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA19_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA19_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA20_Pos      _U_(20)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA20_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA20_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA21_Pos      _U_(21)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA21_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA21_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA22_Pos      _U_(22)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA22_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA22_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA23_Pos      _U_(23)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA23_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA23_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA24_Pos      _U_(24)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA24_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA24_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA25_Pos      _U_(25)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA25_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA25_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA26_Pos      _U_(26)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA26_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA26_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA27_Pos      _U_(27)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA27_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA27_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA28_Pos      _U_(28)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA28_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA28_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA29_Pos      _U_(29)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA29_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA29_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA30_Pos      _U_(30)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA30_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA30_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_DA31_Pos      _U_(31)                                        /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCM_DA31_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCM_DA31_Pos) /**< (SPW_LINK2_DISTACKPI_RCM) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCM_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKPI_RCM) Register Mask  */

#define SPW_LINK2_DISTACKPI_RCM_DA_Pos        _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_RCM Position) Distributed Acknowledge */
#define SPW_LINK2_DISTACKPI_RCM_DA_Msk        (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKPI_RCM_DA_Pos) /**< (SPW_LINK2_DISTACKPI_RCM Mask) DA */
#define SPW_LINK2_DISTACKPI_RCM_DA(value)     (SPW_LINK2_DISTACKPI_RCM_DA_Msk & ((value) << SPW_LINK2_DISTACKPI_RCM_DA_Pos)) 

/* -------- SPW_LINK2_DISTACKPI_R : (SPW Offset: 0x4E8) ( R/ 32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read Interrupt -------- */
#define SPW_LINK2_DISTACKPI_R_DA0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA0_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA0_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA1_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA1_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA2_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA2_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA3_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA3_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA4_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA4_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA5_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA5_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA6_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA6_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA7_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA7_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA8_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA8_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA9_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA9_Pos)    /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA10_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA10_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA11_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA11_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA12_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA12_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA13_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA13_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA14_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA14_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA15_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA15_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA16_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA16_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA17_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA17_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA18_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA18_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA19_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA19_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA20_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA20_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA21_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA21_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA22_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA22_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA23_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA23_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA24_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA24_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA25_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA25_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA26_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA26_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA27_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA27_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA28_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA28_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA29_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA29_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA30_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA30_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_DA31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_R_DA31_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_R_DA31_Pos)   /**< (SPW_LINK2_DISTACKPI_R) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_R_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKPI_R) Register Mask  */

#define SPW_LINK2_DISTACKPI_R_DA_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_R Position) Distributed Acknowledge */
#define SPW_LINK2_DISTACKPI_R_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKPI_R_DA_Pos) /**< (SPW_LINK2_DISTACKPI_R Mask) DA */
#define SPW_LINK2_DISTACKPI_R_DA(value)       (SPW_LINK2_DISTACKPI_R_DA_Msk & ((value) << SPW_LINK2_DISTACKPI_R_DA_Pos)) 

/* -------- SPW_LINK2_DISTACKPI_RCS : (SPW Offset: 0x4EC) (R/W 32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read and Clear Interrupt -------- */
#define SPW_LINK2_DISTACKPI_RCS_DA0_Pos       _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA0_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA0_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA1_Pos       _U_(1)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA1_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA1_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA2_Pos       _U_(2)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA2_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA2_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA3_Pos       _U_(3)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA3_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA3_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA4_Pos       _U_(4)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA4_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA4_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA5_Pos       _U_(5)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA5_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA5_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA6_Pos       _U_(6)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA6_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA6_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA7_Pos       _U_(7)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA7_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA7_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA8_Pos       _U_(8)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA8_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA8_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA9_Pos       _U_(9)                                         /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA9_Msk       (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA9_Pos)  /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA10_Pos      _U_(10)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA10_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA10_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA11_Pos      _U_(11)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA11_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA11_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA12_Pos      _U_(12)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA12_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA12_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA13_Pos      _U_(13)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA13_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA13_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA14_Pos      _U_(14)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA14_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA14_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA15_Pos      _U_(15)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA15_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA15_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA16_Pos      _U_(16)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA16_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA16_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA17_Pos      _U_(17)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA17_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA17_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA18_Pos      _U_(18)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA18_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA18_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA19_Pos      _U_(19)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA19_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA19_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA20_Pos      _U_(20)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA20_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA20_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA21_Pos      _U_(21)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA21_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA21_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA22_Pos      _U_(22)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA22_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA22_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA23_Pos      _U_(23)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA23_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA23_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA24_Pos      _U_(24)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA24_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA24_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA25_Pos      _U_(25)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA25_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA25_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA26_Pos      _U_(26)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA26_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA26_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA27_Pos      _U_(27)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA27_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA27_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA28_Pos      _U_(28)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA28_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA28_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA29_Pos      _U_(29)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA29_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA29_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA30_Pos      _U_(30)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA30_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA30_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_DA31_Pos      _U_(31)                                        /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_RCS_DA31_Msk      (_U_(0x1) << SPW_LINK2_DISTACKPI_RCS_DA31_Pos) /**< (SPW_LINK2_DISTACKPI_RCS) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_RCS_Msk           _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKPI_RCS) Register Mask  */

#define SPW_LINK2_DISTACKPI_RCS_DA_Pos        _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_RCS Position) Distributed Acknowledge */
#define SPW_LINK2_DISTACKPI_RCS_DA_Msk        (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKPI_RCS_DA_Pos) /**< (SPW_LINK2_DISTACKPI_RCS Mask) DA */
#define SPW_LINK2_DISTACKPI_RCS_DA(value)     (SPW_LINK2_DISTACKPI_RCS_DA_Msk & ((value) << SPW_LINK2_DISTACKPI_RCS_DA_Pos)) 

/* -------- SPW_LINK2_DISTACKIM : (SPW Offset: 0x4F0) (R/W 32) SpW Link 2 Distributed Interrupt Acknowledge Mask -------- */
#define SPW_LINK2_DISTACKIM_DA0_Pos           _U_(0)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA0_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA0_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA1_Pos           _U_(1)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA1_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA1_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA2_Pos           _U_(2)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA2_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA2_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA3_Pos           _U_(3)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA3_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA3_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA4_Pos           _U_(4)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA4_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA4_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA5_Pos           _U_(5)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA5_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA5_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA6_Pos           _U_(6)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA6_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA6_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA7_Pos           _U_(7)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA7_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA7_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA8_Pos           _U_(8)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA8_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA8_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA9_Pos           _U_(9)                                         /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA9_Msk           (_U_(0x1) << SPW_LINK2_DISTACKIM_DA9_Pos)      /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA10_Pos          _U_(10)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA10_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA10_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA11_Pos          _U_(11)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA11_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA11_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA12_Pos          _U_(12)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA12_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA12_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA13_Pos          _U_(13)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA13_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA13_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA14_Pos          _U_(14)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA14_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA14_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA15_Pos          _U_(15)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA15_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA15_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA16_Pos          _U_(16)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA16_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA16_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA17_Pos          _U_(17)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA17_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA17_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA18_Pos          _U_(18)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA18_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA18_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA19_Pos          _U_(19)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA19_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA19_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA20_Pos          _U_(20)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA20_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA20_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA21_Pos          _U_(21)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA21_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA21_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA22_Pos          _U_(22)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA22_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA22_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA23_Pos          _U_(23)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA23_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA23_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA24_Pos          _U_(24)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA24_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA24_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA25_Pos          _U_(25)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA25_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA25_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA26_Pos          _U_(26)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA26_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA26_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA27_Pos          _U_(27)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA27_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA27_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA28_Pos          _U_(28)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA28_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA28_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA29_Pos          _U_(29)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA29_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA29_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA30_Pos          _U_(30)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA30_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA30_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_DA31_Pos          _U_(31)                                        /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_DA31_Msk          (_U_(0x1) << SPW_LINK2_DISTACKIM_DA31_Pos)     /**< (SPW_LINK2_DISTACKIM) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_Msk               _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKIM) Register Mask  */

#define SPW_LINK2_DISTACKIM_DA_Pos            _U_(0)                                         /**< (SPW_LINK2_DISTACKIM Position) Distributed Acknowledge mask */
#define SPW_LINK2_DISTACKIM_DA_Msk            (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKIM_DA_Pos) /**< (SPW_LINK2_DISTACKIM Mask) DA */
#define SPW_LINK2_DISTACKIM_DA(value)         (SPW_LINK2_DISTACKIM_DA_Msk & ((value) << SPW_LINK2_DISTACKIM_DA_Pos)) 

/* -------- SPW_LINK2_DISTACKPI_C : (SPW Offset: 0x4F4) ( /W 32) SpW Link 2 Distributed Interrupt Acknowledge Clear Pending Interrupt -------- */
#define SPW_LINK2_DISTACKPI_C_DA0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA0_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA0_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA1_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA1_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA2_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA2_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA3_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA3_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA4_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA4_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA5_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA5_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA6_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA6_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA7_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA7_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA8_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA8_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA9_Msk         (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA9_Pos)    /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA10_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA10_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA11_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA11_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA12_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA12_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA13_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA13_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA14_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA14_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA15_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA15_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA16_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA16_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA17_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA17_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA18_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA18_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA19_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA19_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA20_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA20_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA21_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA21_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA22_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA22_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA23_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA23_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA24_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA24_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA25_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA25_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA26_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA26_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA27_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA27_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA28_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA28_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA29_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA29_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA30_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA30_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_DA31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Position */
#define SPW_LINK2_DISTACKPI_C_DA31_Msk        (_U_(0x1) << SPW_LINK2_DISTACKPI_C_DA31_Pos)   /**< (SPW_LINK2_DISTACKPI_C) Distributed Acknowledge Mask */
#define SPW_LINK2_DISTACKPI_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKPI_C) Register Mask  */

#define SPW_LINK2_DISTACKPI_C_DA_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTACKPI_C Position) Distributed Acknowledge */
#define SPW_LINK2_DISTACKPI_C_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKPI_C_DA_Pos) /**< (SPW_LINK2_DISTACKPI_C Mask) DA */
#define SPW_LINK2_DISTACKPI_C_DA(value)       (SPW_LINK2_DISTACKPI_C_DA_Msk & ((value) << SPW_LINK2_DISTACKPI_C_DA_Pos)) 

/* -------- SPW_LINK2_DISTACKIM_S : (SPW Offset: 0x4F8) ( /W 32) SpW Link 2 Distributed Interrupt Acknowledge Set Mask -------- */
#define SPW_LINK2_DISTACKIM_S_DA0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA0_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA0_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA1_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA1_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA2_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA2_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA3_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA3_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA4_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA4_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA5_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA5_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA6_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA6_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA7_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA7_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA8_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA8_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA9_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA9_Pos)    /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA10_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA10_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA11_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA11_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA12_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA12_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA13_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA13_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA14_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA14_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA15_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA15_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA16_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA16_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA17_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA17_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA18_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA18_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA19_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA19_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA20_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA20_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA21_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA21_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA22_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA22_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA23_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA23_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA24_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA24_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA25_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA25_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA26_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA26_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA27_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA27_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA28_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA28_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA29_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA29_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA30_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA30_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_DA31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_S_DA31_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_S_DA31_Pos)   /**< (SPW_LINK2_DISTACKIM_S) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_S_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKIM_S) Register Mask  */

#define SPW_LINK2_DISTACKIM_S_DA_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTACKIM_S Position) Distributed Acknowledge mask */
#define SPW_LINK2_DISTACKIM_S_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKIM_S_DA_Pos) /**< (SPW_LINK2_DISTACKIM_S Mask) DA */
#define SPW_LINK2_DISTACKIM_S_DA(value)       (SPW_LINK2_DISTACKIM_S_DA_Msk & ((value) << SPW_LINK2_DISTACKIM_S_DA_Pos)) 

/* -------- SPW_LINK2_DISTACKIM_C : (SPW Offset: 0x4FC) ( /W 32) SpW Link 2 Distributed Interrupt Acknowledge Clear Mask -------- */
#define SPW_LINK2_DISTACKIM_C_DA0_Pos         _U_(0)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA0_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA0_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA1_Pos         _U_(1)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA1_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA1_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA2_Pos         _U_(2)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA2_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA2_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA3_Pos         _U_(3)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA3_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA3_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA4_Pos         _U_(4)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA4_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA4_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA5_Pos         _U_(5)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA5_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA5_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA6_Pos         _U_(6)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA6_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA6_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA7_Pos         _U_(7)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA7_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA7_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA8_Pos         _U_(8)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA8_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA8_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA9_Pos         _U_(9)                                         /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA9_Msk         (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA9_Pos)    /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA10_Pos        _U_(10)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA10_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA10_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA11_Pos        _U_(11)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA11_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA11_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA12_Pos        _U_(12)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA12_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA12_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA13_Pos        _U_(13)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA13_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA13_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA14_Pos        _U_(14)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA14_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA14_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA15_Pos        _U_(15)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA15_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA15_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA16_Pos        _U_(16)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA16_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA16_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA17_Pos        _U_(17)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA17_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA17_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA18_Pos        _U_(18)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA18_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA18_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA19_Pos        _U_(19)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA19_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA19_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA20_Pos        _U_(20)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA20_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA20_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA21_Pos        _U_(21)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA21_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA21_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA22_Pos        _U_(22)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA22_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA22_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA23_Pos        _U_(23)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA23_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA23_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA24_Pos        _U_(24)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA24_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA24_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA25_Pos        _U_(25)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA25_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA25_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA26_Pos        _U_(26)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA26_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA26_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA27_Pos        _U_(27)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA27_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA27_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA28_Pos        _U_(28)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA28_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA28_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA29_Pos        _U_(29)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA29_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA29_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA30_Pos        _U_(30)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA30_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA30_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_DA31_Pos        _U_(31)                                        /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Position */
#define SPW_LINK2_DISTACKIM_C_DA31_Msk        (_U_(0x1) << SPW_LINK2_DISTACKIM_C_DA31_Pos)   /**< (SPW_LINK2_DISTACKIM_C) Distributed Acknowledge mask Mask */
#define SPW_LINK2_DISTACKIM_C_Msk             _U_(0xFFFFFFFF)                                /**< (SPW_LINK2_DISTACKIM_C) Register Mask  */

#define SPW_LINK2_DISTACKIM_C_DA_Pos          _U_(0)                                         /**< (SPW_LINK2_DISTACKIM_C Position) Distributed Acknowledge mask */
#define SPW_LINK2_DISTACKIM_C_DA_Msk          (_U_(0xFFFFFFFF) << SPW_LINK2_DISTACKIM_C_DA_Pos) /**< (SPW_LINK2_DISTACKIM_C Mask) DA */
#define SPW_LINK2_DISTACKIM_C_DA(value)       (SPW_LINK2_DISTACKIM_C_DA_Msk & ((value) << SPW_LINK2_DISTACKIM_C_DA_Pos)) 

/* -------- SPW_PKTRX1_PI_RM : (SPW Offset: 0x800) ( R/ 32) PktRx Pending Read Masked Interrupt -------- */
#define SPW_PKTRX1_PI_RM_DEACT_Pos            _U_(0)                                         /**< (SPW_PKTRX1_PI_RM) Deactivated Position */
#define SPW_PKTRX1_PI_RM_DEACT_Msk            (_U_(0x1) << SPW_PKTRX1_PI_RM_DEACT_Pos)       /**< (SPW_PKTRX1_PI_RM) Deactivated Mask */
#define SPW_PKTRX1_PI_RM_EOP_Pos              _U_(1)                                         /**< (SPW_PKTRX1_PI_RM) EOP seen Position */
#define SPW_PKTRX1_PI_RM_EOP_Msk              (_U_(0x1) << SPW_PKTRX1_PI_RM_EOP_Pos)         /**< (SPW_PKTRX1_PI_RM) EOP seen Mask */
#define SPW_PKTRX1_PI_RM_EEP_Pos              _U_(2)                                         /**< (SPW_PKTRX1_PI_RM) EEP seen Position */
#define SPW_PKTRX1_PI_RM_EEP_Msk              (_U_(0x1) << SPW_PKTRX1_PI_RM_EEP_Pos)         /**< (SPW_PKTRX1_PI_RM) EEP seen Mask */
#define SPW_PKTRX1_PI_RM_DISCARD_Pos          _U_(3)                                         /**< (SPW_PKTRX1_PI_RM) Packet Discard Position */
#define SPW_PKTRX1_PI_RM_DISCARD_Msk          (_U_(0x1) << SPW_PKTRX1_PI_RM_DISCARD_Pos)     /**< (SPW_PKTRX1_PI_RM) Packet Discard Mask */
#define SPW_PKTRX1_PI_RM_ACT_Pos              _U_(4)                                         /**< (SPW_PKTRX1_PI_RM) Activated Position */
#define SPW_PKTRX1_PI_RM_ACT_Msk              (_U_(0x1) << SPW_PKTRX1_PI_RM_ACT_Pos)         /**< (SPW_PKTRX1_PI_RM) Activated Mask */
#define SPW_PKTRX1_PI_RM_Msk                  _U_(0x0000001F)                                /**< (SPW_PKTRX1_PI_RM) Register Mask  */


/* -------- SPW_PKTRX1_PI_RCM : (SPW Offset: 0x804) ( R/ 32) PktRx Pending Read and Clear Masked Interrupt -------- */
#define SPW_PKTRX1_PI_RCM_DEACT_Pos           _U_(0)                                         /**< (SPW_PKTRX1_PI_RCM) Deactivated Position */
#define SPW_PKTRX1_PI_RCM_DEACT_Msk           (_U_(0x1) << SPW_PKTRX1_PI_RCM_DEACT_Pos)      /**< (SPW_PKTRX1_PI_RCM) Deactivated Mask */
#define SPW_PKTRX1_PI_RCM_EOP_Pos             _U_(1)                                         /**< (SPW_PKTRX1_PI_RCM) EOP seen Position */
#define SPW_PKTRX1_PI_RCM_EOP_Msk             (_U_(0x1) << SPW_PKTRX1_PI_RCM_EOP_Pos)        /**< (SPW_PKTRX1_PI_RCM) EOP seen Mask */
#define SPW_PKTRX1_PI_RCM_EEP_Pos             _U_(2)                                         /**< (SPW_PKTRX1_PI_RCM) EEP seen Position */
#define SPW_PKTRX1_PI_RCM_EEP_Msk             (_U_(0x1) << SPW_PKTRX1_PI_RCM_EEP_Pos)        /**< (SPW_PKTRX1_PI_RCM) EEP seen Mask */
#define SPW_PKTRX1_PI_RCM_DISCARD_Pos         _U_(3)                                         /**< (SPW_PKTRX1_PI_RCM) Packet Discard Position */
#define SPW_PKTRX1_PI_RCM_DISCARD_Msk         (_U_(0x1) << SPW_PKTRX1_PI_RCM_DISCARD_Pos)    /**< (SPW_PKTRX1_PI_RCM) Packet Discard Mask */
#define SPW_PKTRX1_PI_RCM_ACT_Pos             _U_(4)                                         /**< (SPW_PKTRX1_PI_RCM) Activated Position */
#define SPW_PKTRX1_PI_RCM_ACT_Msk             (_U_(0x1) << SPW_PKTRX1_PI_RCM_ACT_Pos)        /**< (SPW_PKTRX1_PI_RCM) Activated Mask */
#define SPW_PKTRX1_PI_RCM_Msk                 _U_(0x0000001F)                                /**< (SPW_PKTRX1_PI_RCM) Register Mask  */


/* -------- SPW_PKTRX1_PI_R : (SPW Offset: 0x808) ( R/ 32) PktRx Pending Read Interrupt -------- */
#define SPW_PKTRX1_PI_R_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTRX1_PI_R) Deactivated Position */
#define SPW_PKTRX1_PI_R_DEACT_Msk             (_U_(0x1) << SPW_PKTRX1_PI_R_DEACT_Pos)        /**< (SPW_PKTRX1_PI_R) Deactivated Mask */
#define SPW_PKTRX1_PI_R_EOP_Pos               _U_(1)                                         /**< (SPW_PKTRX1_PI_R) EOP seen Position */
#define SPW_PKTRX1_PI_R_EOP_Msk               (_U_(0x1) << SPW_PKTRX1_PI_R_EOP_Pos)          /**< (SPW_PKTRX1_PI_R) EOP seen Mask */
#define SPW_PKTRX1_PI_R_EEP_Pos               _U_(2)                                         /**< (SPW_PKTRX1_PI_R) EEP seen Position */
#define SPW_PKTRX1_PI_R_EEP_Msk               (_U_(0x1) << SPW_PKTRX1_PI_R_EEP_Pos)          /**< (SPW_PKTRX1_PI_R) EEP seen Mask */
#define SPW_PKTRX1_PI_R_DISCARD_Pos           _U_(3)                                         /**< (SPW_PKTRX1_PI_R) Packet Discard Position */
#define SPW_PKTRX1_PI_R_DISCARD_Msk           (_U_(0x1) << SPW_PKTRX1_PI_R_DISCARD_Pos)      /**< (SPW_PKTRX1_PI_R) Packet Discard Mask */
#define SPW_PKTRX1_PI_R_ACT_Pos               _U_(4)                                         /**< (SPW_PKTRX1_PI_R) Activated Position */
#define SPW_PKTRX1_PI_R_ACT_Msk               (_U_(0x1) << SPW_PKTRX1_PI_R_ACT_Pos)          /**< (SPW_PKTRX1_PI_R) Activated Mask */
#define SPW_PKTRX1_PI_R_Msk                   _U_(0x0000001F)                                /**< (SPW_PKTRX1_PI_R) Register Mask  */


/* -------- SPW_PKTRX1_PI_RCS : (SPW Offset: 0x80C) (R/W 32) PktRx Pending Read, Clear and Enabled Interrupt -------- */
#define SPW_PKTRX1_PI_RCS_DEACT_Pos           _U_(0)                                         /**< (SPW_PKTRX1_PI_RCS) Deactivated Position */
#define SPW_PKTRX1_PI_RCS_DEACT_Msk           (_U_(0x1) << SPW_PKTRX1_PI_RCS_DEACT_Pos)      /**< (SPW_PKTRX1_PI_RCS) Deactivated Mask */
#define SPW_PKTRX1_PI_RCS_EOP_Pos             _U_(1)                                         /**< (SPW_PKTRX1_PI_RCS) EOP seen Position */
#define SPW_PKTRX1_PI_RCS_EOP_Msk             (_U_(0x1) << SPW_PKTRX1_PI_RCS_EOP_Pos)        /**< (SPW_PKTRX1_PI_RCS) EOP seen Mask */
#define SPW_PKTRX1_PI_RCS_EEP_Pos             _U_(2)                                         /**< (SPW_PKTRX1_PI_RCS) EEP seen Position */
#define SPW_PKTRX1_PI_RCS_EEP_Msk             (_U_(0x1) << SPW_PKTRX1_PI_RCS_EEP_Pos)        /**< (SPW_PKTRX1_PI_RCS) EEP seen Mask */
#define SPW_PKTRX1_PI_RCS_DISCARD_Pos         _U_(3)                                         /**< (SPW_PKTRX1_PI_RCS) Packet Discard Position */
#define SPW_PKTRX1_PI_RCS_DISCARD_Msk         (_U_(0x1) << SPW_PKTRX1_PI_RCS_DISCARD_Pos)    /**< (SPW_PKTRX1_PI_RCS) Packet Discard Mask */
#define SPW_PKTRX1_PI_RCS_ACT_Pos             _U_(4)                                         /**< (SPW_PKTRX1_PI_RCS) Activated Position */
#define SPW_PKTRX1_PI_RCS_ACT_Msk             (_U_(0x1) << SPW_PKTRX1_PI_RCS_ACT_Pos)        /**< (SPW_PKTRX1_PI_RCS) Activated Mask */
#define SPW_PKTRX1_PI_RCS_Msk                 _U_(0x0000001F)                                /**< (SPW_PKTRX1_PI_RCS) Register Mask  */


/* -------- SPW_PKTRX1_IM : (SPW Offset: 0x810) (R/W 32) PktRx Interrupt Mask -------- */
#define SPW_PKTRX1_IM_DEACT_Pos               _U_(0)                                         /**< (SPW_PKTRX1_IM) Deactivated Position */
#define SPW_PKTRX1_IM_DEACT_Msk               (_U_(0x1) << SPW_PKTRX1_IM_DEACT_Pos)          /**< (SPW_PKTRX1_IM) Deactivated Mask */
#define SPW_PKTRX1_IM_EOP_Pos                 _U_(1)                                         /**< (SPW_PKTRX1_IM) EOP seen Position */
#define SPW_PKTRX1_IM_EOP_Msk                 (_U_(0x1) << SPW_PKTRX1_IM_EOP_Pos)            /**< (SPW_PKTRX1_IM) EOP seen Mask */
#define SPW_PKTRX1_IM_EEP_Pos                 _U_(2)                                         /**< (SPW_PKTRX1_IM) EEP seen Position */
#define SPW_PKTRX1_IM_EEP_Msk                 (_U_(0x1) << SPW_PKTRX1_IM_EEP_Pos)            /**< (SPW_PKTRX1_IM) EEP seen Mask */
#define SPW_PKTRX1_IM_DISCARD_Pos             _U_(3)                                         /**< (SPW_PKTRX1_IM) Packet Discard Position */
#define SPW_PKTRX1_IM_DISCARD_Msk             (_U_(0x1) << SPW_PKTRX1_IM_DISCARD_Pos)        /**< (SPW_PKTRX1_IM) Packet Discard Mask */
#define SPW_PKTRX1_IM_ACT_Pos                 _U_(4)                                         /**< (SPW_PKTRX1_IM) Activated Position */
#define SPW_PKTRX1_IM_ACT_Msk                 (_U_(0x1) << SPW_PKTRX1_IM_ACT_Pos)            /**< (SPW_PKTRX1_IM) Activated Mask */
#define SPW_PKTRX1_IM_Msk                     _U_(0x0000001F)                                /**< (SPW_PKTRX1_IM) Register Mask  */


/* -------- SPW_PKTRX1_PI_C : (SPW Offset: 0x814) ( /W 32) PktRx Clear Pending Interrupt -------- */
#define SPW_PKTRX1_PI_C_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTRX1_PI_C) Deactivated Position */
#define SPW_PKTRX1_PI_C_DEACT_Msk             (_U_(0x1) << SPW_PKTRX1_PI_C_DEACT_Pos)        /**< (SPW_PKTRX1_PI_C) Deactivated Mask */
#define SPW_PKTRX1_PI_C_EOP_Pos               _U_(1)                                         /**< (SPW_PKTRX1_PI_C) EOP seen Position */
#define SPW_PKTRX1_PI_C_EOP_Msk               (_U_(0x1) << SPW_PKTRX1_PI_C_EOP_Pos)          /**< (SPW_PKTRX1_PI_C) EOP seen Mask */
#define SPW_PKTRX1_PI_C_EEP_Pos               _U_(2)                                         /**< (SPW_PKTRX1_PI_C) EEP seen Position */
#define SPW_PKTRX1_PI_C_EEP_Msk               (_U_(0x1) << SPW_PKTRX1_PI_C_EEP_Pos)          /**< (SPW_PKTRX1_PI_C) EEP seen Mask */
#define SPW_PKTRX1_PI_C_DISCARD_Pos           _U_(3)                                         /**< (SPW_PKTRX1_PI_C) Packet Discard Position */
#define SPW_PKTRX1_PI_C_DISCARD_Msk           (_U_(0x1) << SPW_PKTRX1_PI_C_DISCARD_Pos)      /**< (SPW_PKTRX1_PI_C) Packet Discard Mask */
#define SPW_PKTRX1_PI_C_ACT_Pos               _U_(4)                                         /**< (SPW_PKTRX1_PI_C) Activated Position */
#define SPW_PKTRX1_PI_C_ACT_Msk               (_U_(0x1) << SPW_PKTRX1_PI_C_ACT_Pos)          /**< (SPW_PKTRX1_PI_C) Activated Mask */
#define SPW_PKTRX1_PI_C_Msk                   _U_(0x0000001F)                                /**< (SPW_PKTRX1_PI_C) Register Mask  */


/* -------- SPW_PKTRX1_IM_S : (SPW Offset: 0x818) ( /W 32) PktRx Interrupt Set Mask -------- */
#define SPW_PKTRX1_IM_S_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTRX1_IM_S) Deactivated Position */
#define SPW_PKTRX1_IM_S_DEACT_Msk             (_U_(0x1) << SPW_PKTRX1_IM_S_DEACT_Pos)        /**< (SPW_PKTRX1_IM_S) Deactivated Mask */
#define SPW_PKTRX1_IM_S_EOP_Pos               _U_(1)                                         /**< (SPW_PKTRX1_IM_S) EOP seen Position */
#define SPW_PKTRX1_IM_S_EOP_Msk               (_U_(0x1) << SPW_PKTRX1_IM_S_EOP_Pos)          /**< (SPW_PKTRX1_IM_S) EOP seen Mask */
#define SPW_PKTRX1_IM_S_EEP_Pos               _U_(2)                                         /**< (SPW_PKTRX1_IM_S) EEP seen Position */
#define SPW_PKTRX1_IM_S_EEP_Msk               (_U_(0x1) << SPW_PKTRX1_IM_S_EEP_Pos)          /**< (SPW_PKTRX1_IM_S) EEP seen Mask */
#define SPW_PKTRX1_IM_S_DISCARD_Pos           _U_(3)                                         /**< (SPW_PKTRX1_IM_S) Packet Discard Position */
#define SPW_PKTRX1_IM_S_DISCARD_Msk           (_U_(0x1) << SPW_PKTRX1_IM_S_DISCARD_Pos)      /**< (SPW_PKTRX1_IM_S) Packet Discard Mask */
#define SPW_PKTRX1_IM_S_ACT_Pos               _U_(4)                                         /**< (SPW_PKTRX1_IM_S) Activated Position */
#define SPW_PKTRX1_IM_S_ACT_Msk               (_U_(0x1) << SPW_PKTRX1_IM_S_ACT_Pos)          /**< (SPW_PKTRX1_IM_S) Activated Mask */
#define SPW_PKTRX1_IM_S_Msk                   _U_(0x0000001F)                                /**< (SPW_PKTRX1_IM_S) Register Mask  */


/* -------- SPW_PKTRX1_IM_C : (SPW Offset: 0x81C) ( /W 32) PktRx Interrupt Clear Mask -------- */
#define SPW_PKTRX1_IM_C_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTRX1_IM_C) Deactivated Position */
#define SPW_PKTRX1_IM_C_DEACT_Msk             (_U_(0x1) << SPW_PKTRX1_IM_C_DEACT_Pos)        /**< (SPW_PKTRX1_IM_C) Deactivated Mask */
#define SPW_PKTRX1_IM_C_EOP_Pos               _U_(1)                                         /**< (SPW_PKTRX1_IM_C) EOP seen Position */
#define SPW_PKTRX1_IM_C_EOP_Msk               (_U_(0x1) << SPW_PKTRX1_IM_C_EOP_Pos)          /**< (SPW_PKTRX1_IM_C) EOP seen Mask */
#define SPW_PKTRX1_IM_C_EEP_Pos               _U_(2)                                         /**< (SPW_PKTRX1_IM_C) EEP seen Position */
#define SPW_PKTRX1_IM_C_EEP_Msk               (_U_(0x1) << SPW_PKTRX1_IM_C_EEP_Pos)          /**< (SPW_PKTRX1_IM_C) EEP seen Mask */
#define SPW_PKTRX1_IM_C_DISCARD_Pos           _U_(3)                                         /**< (SPW_PKTRX1_IM_C) Packet Discard Position */
#define SPW_PKTRX1_IM_C_DISCARD_Msk           (_U_(0x1) << SPW_PKTRX1_IM_C_DISCARD_Pos)      /**< (SPW_PKTRX1_IM_C) Packet Discard Mask */
#define SPW_PKTRX1_IM_C_ACT_Pos               _U_(4)                                         /**< (SPW_PKTRX1_IM_C) Activated Position */
#define SPW_PKTRX1_IM_C_ACT_Msk               (_U_(0x1) << SPW_PKTRX1_IM_C_ACT_Pos)          /**< (SPW_PKTRX1_IM_C) Activated Mask */
#define SPW_PKTRX1_IM_C_Msk                   _U_(0x0000001F)                                /**< (SPW_PKTRX1_IM_C) Register Mask  */


/* -------- SPW_PKTRX1_CFG : (SPW Offset: 0x820) (R/W 32) PktRx Config -------- */
#define SPW_PKTRX1_CFG_DISCARD_Pos            _U_(0)                                         /**< (SPW_PKTRX1_CFG) Discard Position */
#define SPW_PKTRX1_CFG_DISCARD_Msk            (_U_(0x1) << SPW_PKTRX1_CFG_DISCARD_Pos)       /**< (SPW_PKTRX1_CFG) Discard Mask */
#define SPW_PKTRX1_CFG_Msk                    _U_(0x00000001)                                /**< (SPW_PKTRX1_CFG) Register Mask  */


/* -------- SPW_PKTRX1_STATUS : (SPW Offset: 0x824) ( R/ 32) PktRx Status -------- */
#define SPW_PKTRX1_STATUS_COUNT_Pos           _U_(0)                                         /**< (SPW_PKTRX1_STATUS) Packet Count Position */
#define SPW_PKTRX1_STATUS_COUNT_Msk           (_U_(0xFFFF) << SPW_PKTRX1_STATUS_COUNT_Pos)   /**< (SPW_PKTRX1_STATUS) Packet Count Mask */
#define SPW_PKTRX1_STATUS_COUNT(value)        (SPW_PKTRX1_STATUS_COUNT_Msk & ((value) << SPW_PKTRX1_STATUS_COUNT_Pos))
#define SPW_PKTRX1_STATUS_PACKET_Pos          _U_(16)                                        /**< (SPW_PKTRX1_STATUS) Packet Position */
#define SPW_PKTRX1_STATUS_PACKET_Msk          (_U_(0x1) << SPW_PKTRX1_STATUS_PACKET_Pos)     /**< (SPW_PKTRX1_STATUS) Packet Mask */
#define SPW_PKTRX1_STATUS_LOCKED_Pos          _U_(17)                                        /**< (SPW_PKTRX1_STATUS) Locked Position */
#define SPW_PKTRX1_STATUS_LOCKED_Msk          (_U_(0x1) << SPW_PKTRX1_STATUS_LOCKED_Pos)     /**< (SPW_PKTRX1_STATUS) Locked Mask */
#define SPW_PKTRX1_STATUS_ARM_Pos             _U_(18)                                        /**< (SPW_PKTRX1_STATUS) Armed Position */
#define SPW_PKTRX1_STATUS_ARM_Msk             (_U_(0x1) << SPW_PKTRX1_STATUS_ARM_Pos)        /**< (SPW_PKTRX1_STATUS) Armed Mask */
#define SPW_PKTRX1_STATUS_ACT_Pos             _U_(19)                                        /**< (SPW_PKTRX1_STATUS) Active Position */
#define SPW_PKTRX1_STATUS_ACT_Msk             (_U_(0x1) << SPW_PKTRX1_STATUS_ACT_Pos)        /**< (SPW_PKTRX1_STATUS) Active Mask */
#define SPW_PKTRX1_STATUS_PENDING_Pos         _U_(20)                                        /**< (SPW_PKTRX1_STATUS) Pending Position */
#define SPW_PKTRX1_STATUS_PENDING_Msk         (_U_(0x1) << SPW_PKTRX1_STATUS_PENDING_Pos)    /**< (SPW_PKTRX1_STATUS) Pending Mask */
#define SPW_PKTRX1_STATUS_DEACT_Pos           _U_(21)                                        /**< (SPW_PKTRX1_STATUS) Deactivating Position */
#define SPW_PKTRX1_STATUS_DEACT_Msk           (_U_(0x1) << SPW_PKTRX1_STATUS_DEACT_Pos)      /**< (SPW_PKTRX1_STATUS) Deactivating Mask */
#define SPW_PKTRX1_STATUS_Msk                 _U_(0x003FFFFF)                                /**< (SPW_PKTRX1_STATUS) Register Mask  */


/* -------- SPW_PKTRX1_NXTBUFDATAADDR : (SPW Offset: 0x830) (R/W 32) PktRx Next Buffer Data Address -------- */
#define SPW_PKTRX1_NXTBUFDATAADDR_ADDR_Pos    _U_(0)                                         /**< (SPW_PKTRX1_NXTBUFDATAADDR) Address Position */
#define SPW_PKTRX1_NXTBUFDATAADDR_ADDR_Msk    (_U_(0xFFFFFFFF) << SPW_PKTRX1_NXTBUFDATAADDR_ADDR_Pos) /**< (SPW_PKTRX1_NXTBUFDATAADDR) Address Mask */
#define SPW_PKTRX1_NXTBUFDATAADDR_ADDR(value) (SPW_PKTRX1_NXTBUFDATAADDR_ADDR_Msk & ((value) << SPW_PKTRX1_NXTBUFDATAADDR_ADDR_Pos))
#define SPW_PKTRX1_NXTBUFDATAADDR_Msk         _U_(0xFFFFFFFF)                                /**< (SPW_PKTRX1_NXTBUFDATAADDR) Register Mask  */


/* -------- SPW_PKTRX1_NXTBUFDATALEN : (SPW Offset: 0x834) (R/W 32) PktRx Next Buffer Data Length -------- */
#define SPW_PKTRX1_NXTBUFDATALEN_LEN_Pos      _U_(0)                                         /**< (SPW_PKTRX1_NXTBUFDATALEN) Length Position */
#define SPW_PKTRX1_NXTBUFDATALEN_LEN_Msk      (_U_(0xFFFFFF) << SPW_PKTRX1_NXTBUFDATALEN_LEN_Pos) /**< (SPW_PKTRX1_NXTBUFDATALEN) Length Mask */
#define SPW_PKTRX1_NXTBUFDATALEN_LEN(value)   (SPW_PKTRX1_NXTBUFDATALEN_LEN_Msk & ((value) << SPW_PKTRX1_NXTBUFDATALEN_LEN_Pos))
#define SPW_PKTRX1_NXTBUFDATALEN_Msk          _U_(0x00FFFFFF)                                /**< (SPW_PKTRX1_NXTBUFDATALEN) Register Mask  */


/* -------- SPW_PKTRX1_NXTBUFPKTADDR : (SPW Offset: 0x838) (R/W 32) PktRx Next Buffer Packet Address -------- */
#define SPW_PKTRX1_NXTBUFPKTADDR_ADDR_Pos     _U_(0)                                         /**< (SPW_PKTRX1_NXTBUFPKTADDR) Address Position */
#define SPW_PKTRX1_NXTBUFPKTADDR_ADDR_Msk     (_U_(0xFFFFFFFF) << SPW_PKTRX1_NXTBUFPKTADDR_ADDR_Pos) /**< (SPW_PKTRX1_NXTBUFPKTADDR) Address Mask */
#define SPW_PKTRX1_NXTBUFPKTADDR_ADDR(value)  (SPW_PKTRX1_NXTBUFPKTADDR_ADDR_Msk & ((value) << SPW_PKTRX1_NXTBUFPKTADDR_ADDR_Pos))
#define SPW_PKTRX1_NXTBUFPKTADDR_Msk          _U_(0xFFFFFFFF)                                /**< (SPW_PKTRX1_NXTBUFPKTADDR) Register Mask  */


/* -------- SPW_PKTRX1_NXTBUFCFG : (SPW Offset: 0x83C) (R/W 32) PktRx Next Buffer Config -------- */
#define SPW_PKTRX1_NXTBUFCFG_MAXCNT_Pos       _U_(0)                                         /**< (SPW_PKTRX1_NXTBUFCFG) Max Count Position */
#define SPW_PKTRX1_NXTBUFCFG_MAXCNT_Msk       (_U_(0xFFFF) << SPW_PKTRX1_NXTBUFCFG_MAXCNT_Pos) /**< (SPW_PKTRX1_NXTBUFCFG) Max Count Mask */
#define SPW_PKTRX1_NXTBUFCFG_MAXCNT(value)    (SPW_PKTRX1_NXTBUFCFG_MAXCNT_Msk & ((value) << SPW_PKTRX1_NXTBUFCFG_MAXCNT_Pos))
#define SPW_PKTRX1_NXTBUFCFG_VALUE_Pos        _U_(16)                                        /**< (SPW_PKTRX1_NXTBUFCFG) Start Value Position */
#define SPW_PKTRX1_NXTBUFCFG_VALUE_Msk        (_U_(0x3F) << SPW_PKTRX1_NXTBUFCFG_VALUE_Pos)  /**< (SPW_PKTRX1_NXTBUFCFG) Start Value Mask */
#define SPW_PKTRX1_NXTBUFCFG_VALUE(value)     (SPW_PKTRX1_NXTBUFCFG_VALUE_Msk & ((value) << SPW_PKTRX1_NXTBUFCFG_VALUE_Pos))
#define SPW_PKTRX1_NXTBUFCFG_START_Pos        _U_(22)                                        /**< (SPW_PKTRX1_NXTBUFCFG) Start Mode Position */
#define SPW_PKTRX1_NXTBUFCFG_START_Msk        (_U_(0x3) << SPW_PKTRX1_NXTBUFCFG_START_Pos)   /**< (SPW_PKTRX1_NXTBUFCFG) Start Mode Mask */
#define SPW_PKTRX1_NXTBUFCFG_START(value)     (SPW_PKTRX1_NXTBUFCFG_START_Msk & ((value) << SPW_PKTRX1_NXTBUFCFG_START_Pos))
#define   SPW_PKTRX1_NXTBUFCFG_START_STARTVALUE_Val _U_(0x0)                                       /**< (SPW_PKTRX1_NXTBUFCFG) Start if any bit in Start Value matches an incom-ing event  */
#define   SPW_PKTRX1_NXTBUFCFG_START_STARTNOW_Val _U_(0x1)                                       /**< (SPW_PKTRX1_NXTBUFCFG) Start immediately. Request a deactivation on next packet boundary.  */
#define   SPW_PKTRX1_NXTBUFCFG_START_STARTTCH1_Val _U_(0x2)                                       /**< (SPW_PKTRX1_NXTBUFCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 1  */
#define   SPW_PKTRX1_NXTBUFCFG_START_STARTTCH2_Val _U_(0x3)                                       /**< (SPW_PKTRX1_NXTBUFCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 2  */
#define SPW_PKTRX1_NXTBUFCFG_START_STARTVALUE (SPW_PKTRX1_NXTBUFCFG_START_STARTVALUE_Val << SPW_PKTRX1_NXTBUFCFG_START_Pos) /**< (SPW_PKTRX1_NXTBUFCFG) Start if any bit in Start Value matches an incom-ing event Position  */
#define SPW_PKTRX1_NXTBUFCFG_START_STARTNOW   (SPW_PKTRX1_NXTBUFCFG_START_STARTNOW_Val << SPW_PKTRX1_NXTBUFCFG_START_Pos) /**< (SPW_PKTRX1_NXTBUFCFG) Start immediately. Request a deactivation on next packet boundary. Position  */
#define SPW_PKTRX1_NXTBUFCFG_START_STARTTCH1  (SPW_PKTRX1_NXTBUFCFG_START_STARTTCH1_Val << SPW_PKTRX1_NXTBUFCFG_START_Pos) /**< (SPW_PKTRX1_NXTBUFCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 1 Position  */
#define SPW_PKTRX1_NXTBUFCFG_START_STARTTCH2  (SPW_PKTRX1_NXTBUFCFG_START_STARTTCH2_Val << SPW_PKTRX1_NXTBUFCFG_START_Pos) /**< (SPW_PKTRX1_NXTBUFCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 2 Position  */
#define SPW_PKTRX1_NXTBUFCFG_SPLIT_Pos        _U_(30)                                        /**< (SPW_PKTRX1_NXTBUFCFG) Split Pkt Position */
#define SPW_PKTRX1_NXTBUFCFG_SPLIT_Msk        (_U_(0x1) << SPW_PKTRX1_NXTBUFCFG_SPLIT_Pos)   /**< (SPW_PKTRX1_NXTBUFCFG) Split Pkt Mask */
#define SPW_PKTRX1_NXTBUFCFG_Msk              _U_(0x40FFFFFF)                                /**< (SPW_PKTRX1_NXTBUFCFG) Register Mask  */


/* -------- SPW_PKTRX1_CURBUFDATAADDR : (SPW Offset: 0x840) ( R/ 32) PktRx Current Buffer Data Address -------- */
#define SPW_PKTRX1_CURBUFDATAADDR_ADDR_Pos    _U_(0)                                         /**< (SPW_PKTRX1_CURBUFDATAADDR) Address Position */
#define SPW_PKTRX1_CURBUFDATAADDR_ADDR_Msk    (_U_(0xFFFFFFFF) << SPW_PKTRX1_CURBUFDATAADDR_ADDR_Pos) /**< (SPW_PKTRX1_CURBUFDATAADDR) Address Mask */
#define SPW_PKTRX1_CURBUFDATAADDR_ADDR(value) (SPW_PKTRX1_CURBUFDATAADDR_ADDR_Msk & ((value) << SPW_PKTRX1_CURBUFDATAADDR_ADDR_Pos))
#define SPW_PKTRX1_CURBUFDATAADDR_Msk         _U_(0xFFFFFFFF)                                /**< (SPW_PKTRX1_CURBUFDATAADDR) Register Mask  */


/* -------- SPW_PKTRX1_CURBUFDATALEN : (SPW Offset: 0x844) ( R/ 32) PktRx Current Buffer Data Length -------- */
#define SPW_PKTRX1_CURBUFDATALEN_LEN_Pos      _U_(0)                                         /**< (SPW_PKTRX1_CURBUFDATALEN) Length Position */
#define SPW_PKTRX1_CURBUFDATALEN_LEN_Msk      (_U_(0xFFFFFF) << SPW_PKTRX1_CURBUFDATALEN_LEN_Pos) /**< (SPW_PKTRX1_CURBUFDATALEN) Length Mask */
#define SPW_PKTRX1_CURBUFDATALEN_LEN(value)   (SPW_PKTRX1_CURBUFDATALEN_LEN_Msk & ((value) << SPW_PKTRX1_CURBUFDATALEN_LEN_Pos))
#define SPW_PKTRX1_CURBUFDATALEN_Msk          _U_(0x00FFFFFF)                                /**< (SPW_PKTRX1_CURBUFDATALEN) Register Mask  */


/* -------- SPW_PKTRX1_CURBUFPKTADDR : (SPW Offset: 0x848) ( R/ 32) PktRx Current Buffer Packet Address -------- */
#define SPW_PKTRX1_CURBUFPKTADDR_ADDR_Pos     _U_(0)                                         /**< (SPW_PKTRX1_CURBUFPKTADDR) Address Position */
#define SPW_PKTRX1_CURBUFPKTADDR_ADDR_Msk     (_U_(0xFFFFFFFF) << SPW_PKTRX1_CURBUFPKTADDR_ADDR_Pos) /**< (SPW_PKTRX1_CURBUFPKTADDR) Address Mask */
#define SPW_PKTRX1_CURBUFPKTADDR_ADDR(value)  (SPW_PKTRX1_CURBUFPKTADDR_ADDR_Msk & ((value) << SPW_PKTRX1_CURBUFPKTADDR_ADDR_Pos))
#define SPW_PKTRX1_CURBUFPKTADDR_Msk          _U_(0xFFFFFFFF)                                /**< (SPW_PKTRX1_CURBUFPKTADDR) Register Mask  */


/* -------- SPW_PKTRX1_CURBUFCFG : (SPW Offset: 0x84C) (R/W 32) PktRx Current Buffer Config -------- */
#define SPW_PKTRX1_CURBUFCFG_MAXCNT_Pos       _U_(0)                                         /**< (SPW_PKTRX1_CURBUFCFG) Max Count Position */
#define SPW_PKTRX1_CURBUFCFG_MAXCNT_Msk       (_U_(0xFFFF) << SPW_PKTRX1_CURBUFCFG_MAXCNT_Pos) /**< (SPW_PKTRX1_CURBUFCFG) Max Count Mask */
#define SPW_PKTRX1_CURBUFCFG_MAXCNT(value)    (SPW_PKTRX1_CURBUFCFG_MAXCNT_Msk & ((value) << SPW_PKTRX1_CURBUFCFG_MAXCNT_Pos))
#define SPW_PKTRX1_CURBUFCFG_SPLIT_Pos        _U_(30)                                        /**< (SPW_PKTRX1_CURBUFCFG) Split Position */
#define SPW_PKTRX1_CURBUFCFG_SPLIT_Msk        (_U_(0x1) << SPW_PKTRX1_CURBUFCFG_SPLIT_Pos)   /**< (SPW_PKTRX1_CURBUFCFG) Split Mask */
#define SPW_PKTRX1_CURBUFCFG_ABORT_Pos        _U_(31)                                        /**< (SPW_PKTRX1_CURBUFCFG) Abort Position */
#define SPW_PKTRX1_CURBUFCFG_ABORT_Msk        (_U_(0x1) << SPW_PKTRX1_CURBUFCFG_ABORT_Pos)   /**< (SPW_PKTRX1_CURBUFCFG) Abort Mask */
#define SPW_PKTRX1_CURBUFCFG_Msk              _U_(0xC000FFFF)                                /**< (SPW_PKTRX1_CURBUFCFG) Register Mask  */


/* -------- SPW_PKTRX1_PREVBUFDATALEN : (SPW Offset: 0x850) ( R/ 32) PktRx Previous Buffer Data Length -------- */
#define SPW_PKTRX1_PREVBUFDATALEN_LEN_Pos     _U_(0)                                         /**< (SPW_PKTRX1_PREVBUFDATALEN) Length Position */
#define SPW_PKTRX1_PREVBUFDATALEN_LEN_Msk     (_U_(0xFFFFFF) << SPW_PKTRX1_PREVBUFDATALEN_LEN_Pos) /**< (SPW_PKTRX1_PREVBUFDATALEN) Length Mask */
#define SPW_PKTRX1_PREVBUFDATALEN_LEN(value)  (SPW_PKTRX1_PREVBUFDATALEN_LEN_Msk & ((value) << SPW_PKTRX1_PREVBUFDATALEN_LEN_Pos))
#define SPW_PKTRX1_PREVBUFDATALEN_Msk         _U_(0x00FFFFFF)                                /**< (SPW_PKTRX1_PREVBUFDATALEN) Register Mask  */


/* -------- SPW_PKTRX1_PREVBUFSTS : (SPW Offset: 0x854) ( R/ 32) PktRx Previous Buffer Status -------- */
#define SPW_PKTRX1_PREVBUFSTS_CNT_Pos         _U_(0)                                         /**< (SPW_PKTRX1_PREVBUFSTS) Count Position */
#define SPW_PKTRX1_PREVBUFSTS_CNT_Msk         (_U_(0xFFFF) << SPW_PKTRX1_PREVBUFSTS_CNT_Pos) /**< (SPW_PKTRX1_PREVBUFSTS) Count Mask */
#define SPW_PKTRX1_PREVBUFSTS_CNT(value)      (SPW_PKTRX1_PREVBUFSTS_CNT_Msk & ((value) << SPW_PKTRX1_PREVBUFSTS_CNT_Pos))
#define SPW_PKTRX1_PREVBUFSTS_EEP_Pos         _U_(16)                                        /**< (SPW_PKTRX1_PREVBUFSTS) EEP seen Position */
#define SPW_PKTRX1_PREVBUFSTS_EEP_Msk         (_U_(0x1) << SPW_PKTRX1_PREVBUFSTS_EEP_Pos)    /**< (SPW_PKTRX1_PREVBUFSTS) EEP seen Mask */
#define SPW_PKTRX1_PREVBUFSTS_FULLI_Pos       _U_(17)                                        /**< (SPW_PKTRX1_PREVBUFSTS) Buffer Info Full Position */
#define SPW_PKTRX1_PREVBUFSTS_FULLI_Msk       (_U_(0x1) << SPW_PKTRX1_PREVBUFSTS_FULLI_Pos)  /**< (SPW_PKTRX1_PREVBUFSTS) Buffer Info Full Mask */
#define SPW_PKTRX1_PREVBUFSTS_FULLD_Pos       _U_(18)                                        /**< (SPW_PKTRX1_PREVBUFSTS) Buffer Data Full Position */
#define SPW_PKTRX1_PREVBUFSTS_FULLD_Msk       (_U_(0x1) << SPW_PKTRX1_PREVBUFSTS_FULLD_Pos)  /**< (SPW_PKTRX1_PREVBUFSTS) Buffer Data Full Mask */
#define SPW_PKTRX1_PREVBUFSTS_DMAERR_Pos      _U_(19)                                        /**< (SPW_PKTRX1_PREVBUFSTS) DMA Error Position */
#define SPW_PKTRX1_PREVBUFSTS_DMAERR_Msk      (_U_(0x1) << SPW_PKTRX1_PREVBUFSTS_DMAERR_Pos) /**< (SPW_PKTRX1_PREVBUFSTS) DMA Error Mask */
#define SPW_PKTRX1_PREVBUFSTS_LOCKED_Pos      _U_(31)                                        /**< (SPW_PKTRX1_PREVBUFSTS) Locked Position */
#define SPW_PKTRX1_PREVBUFSTS_LOCKED_Msk      (_U_(0x1) << SPW_PKTRX1_PREVBUFSTS_LOCKED_Pos) /**< (SPW_PKTRX1_PREVBUFSTS) Locked Mask */
#define SPW_PKTRX1_PREVBUFSTS_Msk             _U_(0x800FFFFF)                                /**< (SPW_PKTRX1_PREVBUFSTS) Register Mask  */


/* -------- SPW_PKTRX1_SWRESET : (SPW Offset: 0x87C) (R/W 32) PktRx Software Reset -------- */
#define SPW_PKTRX1_SWRESET_PATTERN_Pos        _U_(0)                                         /**< (SPW_PKTRX1_SWRESET) Pattern Position */
#define SPW_PKTRX1_SWRESET_PATTERN_Msk        (_U_(0xFFFFFFFF) << SPW_PKTRX1_SWRESET_PATTERN_Pos) /**< (SPW_PKTRX1_SWRESET) Pattern Mask */
#define SPW_PKTRX1_SWRESET_PATTERN(value)     (SPW_PKTRX1_SWRESET_PATTERN_Msk & ((value) << SPW_PKTRX1_SWRESET_PATTERN_Pos))
#define SPW_PKTRX1_SWRESET_Msk                _U_(0xFFFFFFFF)                                /**< (SPW_PKTRX1_SWRESET) Register Mask  */


/* -------- SPW_PKTTX1_PI_RM : (SPW Offset: 0xC00) ( R/ 32) PktTx Pending Read Masked Interrupt -------- */
#define SPW_PKTTX1_PI_RM_DEACT_Pos            _U_(0)                                         /**< (SPW_PKTTX1_PI_RM) Deactivated Position */
#define SPW_PKTTX1_PI_RM_DEACT_Msk            (_U_(0x1) << SPW_PKTTX1_PI_RM_DEACT_Pos)       /**< (SPW_PKTTX1_PI_RM) Deactivated Mask */
#define SPW_PKTTX1_PI_RM_ACT_Pos              _U_(1)                                         /**< (SPW_PKTTX1_PI_RM) Activated Position */
#define SPW_PKTTX1_PI_RM_ACT_Msk              (_U_(0x1) << SPW_PKTTX1_PI_RM_ACT_Pos)         /**< (SPW_PKTTX1_PI_RM) Activated Mask */
#define SPW_PKTTX1_PI_RM_EOP_Pos              _U_(2)                                         /**< (SPW_PKTTX1_PI_RM) EOP sent Position */
#define SPW_PKTTX1_PI_RM_EOP_Msk              (_U_(0x1) << SPW_PKTTX1_PI_RM_EOP_Pos)         /**< (SPW_PKTTX1_PI_RM) EOP sent Mask */
#define SPW_PKTTX1_PI_RM_EEP_Pos              _U_(3)                                         /**< (SPW_PKTTX1_PI_RM) EEP sent Position */
#define SPW_PKTTX1_PI_RM_EEP_Msk              (_U_(0x1) << SPW_PKTTX1_PI_RM_EEP_Pos)         /**< (SPW_PKTTX1_PI_RM) EEP sent Mask */
#define SPW_PKTTX1_PI_RM_Msk                  _U_(0x0000000F)                                /**< (SPW_PKTTX1_PI_RM) Register Mask  */


/* -------- SPW_PKTTX1_PI_RCM : (SPW Offset: 0xC04) ( R/ 32) PktTx Pending Read and Clear Masked Interrupt -------- */
#define SPW_PKTTX1_PI_RCM_DEACT_Pos           _U_(0)                                         /**< (SPW_PKTTX1_PI_RCM) Deactivated Position */
#define SPW_PKTTX1_PI_RCM_DEACT_Msk           (_U_(0x1) << SPW_PKTTX1_PI_RCM_DEACT_Pos)      /**< (SPW_PKTTX1_PI_RCM) Deactivated Mask */
#define SPW_PKTTX1_PI_RCM_ACT_Pos             _U_(1)                                         /**< (SPW_PKTTX1_PI_RCM) Activated Position */
#define SPW_PKTTX1_PI_RCM_ACT_Msk             (_U_(0x1) << SPW_PKTTX1_PI_RCM_ACT_Pos)        /**< (SPW_PKTTX1_PI_RCM) Activated Mask */
#define SPW_PKTTX1_PI_RCM_EOP_Pos             _U_(2)                                         /**< (SPW_PKTTX1_PI_RCM) EOP sent Position */
#define SPW_PKTTX1_PI_RCM_EOP_Msk             (_U_(0x1) << SPW_PKTTX1_PI_RCM_EOP_Pos)        /**< (SPW_PKTTX1_PI_RCM) EOP sent Mask */
#define SPW_PKTTX1_PI_RCM_EEP_Pos             _U_(3)                                         /**< (SPW_PKTTX1_PI_RCM) EEP sent Position */
#define SPW_PKTTX1_PI_RCM_EEP_Msk             (_U_(0x1) << SPW_PKTTX1_PI_RCM_EEP_Pos)        /**< (SPW_PKTTX1_PI_RCM) EEP sent Mask */
#define SPW_PKTTX1_PI_RCM_Msk                 _U_(0x0000000F)                                /**< (SPW_PKTTX1_PI_RCM) Register Mask  */


/* -------- SPW_PKTTX1_PI_R : (SPW Offset: 0xC08) ( R/ 32) PktTx Pending Read Interrupt -------- */
#define SPW_PKTTX1_PI_R_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTTX1_PI_R) Deactivated Position */
#define SPW_PKTTX1_PI_R_DEACT_Msk             (_U_(0x1) << SPW_PKTTX1_PI_R_DEACT_Pos)        /**< (SPW_PKTTX1_PI_R) Deactivated Mask */
#define SPW_PKTTX1_PI_R_ACT_Pos               _U_(1)                                         /**< (SPW_PKTTX1_PI_R) Activated Position */
#define SPW_PKTTX1_PI_R_ACT_Msk               (_U_(0x1) << SPW_PKTTX1_PI_R_ACT_Pos)          /**< (SPW_PKTTX1_PI_R) Activated Mask */
#define SPW_PKTTX1_PI_R_EOP_Pos               _U_(2)                                         /**< (SPW_PKTTX1_PI_R) EOP sent Position */
#define SPW_PKTTX1_PI_R_EOP_Msk               (_U_(0x1) << SPW_PKTTX1_PI_R_EOP_Pos)          /**< (SPW_PKTTX1_PI_R) EOP sent Mask */
#define SPW_PKTTX1_PI_R_EEP_Pos               _U_(3)                                         /**< (SPW_PKTTX1_PI_R) EEP sent Position */
#define SPW_PKTTX1_PI_R_EEP_Msk               (_U_(0x1) << SPW_PKTTX1_PI_R_EEP_Pos)          /**< (SPW_PKTTX1_PI_R) EEP sent Mask */
#define SPW_PKTTX1_PI_R_Msk                   _U_(0x0000000F)                                /**< (SPW_PKTTX1_PI_R) Register Mask  */


/* -------- SPW_PKTTX1_PI_RCS : (SPW Offset: 0xC0C) (R/W 32) PktTx Pending Read, Clear and Enabled Interrupt -------- */
#define SPW_PKTTX1_PI_RCS_DEACT_Pos           _U_(0)                                         /**< (SPW_PKTTX1_PI_RCS) Deactivated Position */
#define SPW_PKTTX1_PI_RCS_DEACT_Msk           (_U_(0x1) << SPW_PKTTX1_PI_RCS_DEACT_Pos)      /**< (SPW_PKTTX1_PI_RCS) Deactivated Mask */
#define SPW_PKTTX1_PI_RCS_ACT_Pos             _U_(1)                                         /**< (SPW_PKTTX1_PI_RCS) Activated Position */
#define SPW_PKTTX1_PI_RCS_ACT_Msk             (_U_(0x1) << SPW_PKTTX1_PI_RCS_ACT_Pos)        /**< (SPW_PKTTX1_PI_RCS) Activated Mask */
#define SPW_PKTTX1_PI_RCS_EOP_Pos             _U_(2)                                         /**< (SPW_PKTTX1_PI_RCS) EOP sent Position */
#define SPW_PKTTX1_PI_RCS_EOP_Msk             (_U_(0x1) << SPW_PKTTX1_PI_RCS_EOP_Pos)        /**< (SPW_PKTTX1_PI_RCS) EOP sent Mask */
#define SPW_PKTTX1_PI_RCS_EEP_Pos             _U_(3)                                         /**< (SPW_PKTTX1_PI_RCS) EEP sent Position */
#define SPW_PKTTX1_PI_RCS_EEP_Msk             (_U_(0x1) << SPW_PKTTX1_PI_RCS_EEP_Pos)        /**< (SPW_PKTTX1_PI_RCS) EEP sent Mask */
#define SPW_PKTTX1_PI_RCS_Msk                 _U_(0x0000000F)                                /**< (SPW_PKTTX1_PI_RCS) Register Mask  */


/* -------- SPW_PKTTX1_IM : (SPW Offset: 0xC10) (R/W 32) PktTx Interrupt Mask -------- */
#define SPW_PKTTX1_IM_DEACT_Pos               _U_(0)                                         /**< (SPW_PKTTX1_IM) Deactivated Position */
#define SPW_PKTTX1_IM_DEACT_Msk               (_U_(0x1) << SPW_PKTTX1_IM_DEACT_Pos)          /**< (SPW_PKTTX1_IM) Deactivated Mask */
#define SPW_PKTTX1_IM_ACT_Pos                 _U_(1)                                         /**< (SPW_PKTTX1_IM) Activated Position */
#define SPW_PKTTX1_IM_ACT_Msk                 (_U_(0x1) << SPW_PKTTX1_IM_ACT_Pos)            /**< (SPW_PKTTX1_IM) Activated Mask */
#define SPW_PKTTX1_IM_EOP_Pos                 _U_(2)                                         /**< (SPW_PKTTX1_IM) EOP sent Position */
#define SPW_PKTTX1_IM_EOP_Msk                 (_U_(0x1) << SPW_PKTTX1_IM_EOP_Pos)            /**< (SPW_PKTTX1_IM) EOP sent Mask */
#define SPW_PKTTX1_IM_EEP_Pos                 _U_(3)                                         /**< (SPW_PKTTX1_IM) EEP sent Position */
#define SPW_PKTTX1_IM_EEP_Msk                 (_U_(0x1) << SPW_PKTTX1_IM_EEP_Pos)            /**< (SPW_PKTTX1_IM) EEP sent Mask */
#define SPW_PKTTX1_IM_Msk                     _U_(0x0000000F)                                /**< (SPW_PKTTX1_IM) Register Mask  */


/* -------- SPW_PKTTX1_PI_C : (SPW Offset: 0xC14) ( /W 32) PktTx Clear Pending Interrupt -------- */
#define SPW_PKTTX1_PI_C_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTTX1_PI_C) Deactivated Position */
#define SPW_PKTTX1_PI_C_DEACT_Msk             (_U_(0x1) << SPW_PKTTX1_PI_C_DEACT_Pos)        /**< (SPW_PKTTX1_PI_C) Deactivated Mask */
#define SPW_PKTTX1_PI_C_ACT_Pos               _U_(1)                                         /**< (SPW_PKTTX1_PI_C) Activated Position */
#define SPW_PKTTX1_PI_C_ACT_Msk               (_U_(0x1) << SPW_PKTTX1_PI_C_ACT_Pos)          /**< (SPW_PKTTX1_PI_C) Activated Mask */
#define SPW_PKTTX1_PI_C_EOP_Pos               _U_(2)                                         /**< (SPW_PKTTX1_PI_C) EOP sent Position */
#define SPW_PKTTX1_PI_C_EOP_Msk               (_U_(0x1) << SPW_PKTTX1_PI_C_EOP_Pos)          /**< (SPW_PKTTX1_PI_C) EOP sent Mask */
#define SPW_PKTTX1_PI_C_EEP_Pos               _U_(3)                                         /**< (SPW_PKTTX1_PI_C) EEP sent Position */
#define SPW_PKTTX1_PI_C_EEP_Msk               (_U_(0x1) << SPW_PKTTX1_PI_C_EEP_Pos)          /**< (SPW_PKTTX1_PI_C) EEP sent Mask */
#define SPW_PKTTX1_PI_C_Msk                   _U_(0x0000000F)                                /**< (SPW_PKTTX1_PI_C) Register Mask  */


/* -------- SPW_PKTTX1_IM_S : (SPW Offset: 0xC18) ( /W 32) PktTx Interrupt Set Mask -------- */
#define SPW_PKTTX1_IM_S_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTTX1_IM_S) Deactivated Position */
#define SPW_PKTTX1_IM_S_DEACT_Msk             (_U_(0x1) << SPW_PKTTX1_IM_S_DEACT_Pos)        /**< (SPW_PKTTX1_IM_S) Deactivated Mask */
#define SPW_PKTTX1_IM_S_ACT_Pos               _U_(1)                                         /**< (SPW_PKTTX1_IM_S) Activated Position */
#define SPW_PKTTX1_IM_S_ACT_Msk               (_U_(0x1) << SPW_PKTTX1_IM_S_ACT_Pos)          /**< (SPW_PKTTX1_IM_S) Activated Mask */
#define SPW_PKTTX1_IM_S_EOP_Pos               _U_(2)                                         /**< (SPW_PKTTX1_IM_S) EOP sent Position */
#define SPW_PKTTX1_IM_S_EOP_Msk               (_U_(0x1) << SPW_PKTTX1_IM_S_EOP_Pos)          /**< (SPW_PKTTX1_IM_S) EOP sent Mask */
#define SPW_PKTTX1_IM_S_EEP_Pos               _U_(3)                                         /**< (SPW_PKTTX1_IM_S) EEP sent Position */
#define SPW_PKTTX1_IM_S_EEP_Msk               (_U_(0x1) << SPW_PKTTX1_IM_S_EEP_Pos)          /**< (SPW_PKTTX1_IM_S) EEP sent Mask */
#define SPW_PKTTX1_IM_S_Msk                   _U_(0x0000000F)                                /**< (SPW_PKTTX1_IM_S) Register Mask  */


/* -------- SPW_PKTTX1_IM_C : (SPW Offset: 0xC1C) ( /W 32) PktTx Interrupt Clear Mask -------- */
#define SPW_PKTTX1_IM_C_DEACT_Pos             _U_(0)                                         /**< (SPW_PKTTX1_IM_C) Deactivated Position */
#define SPW_PKTTX1_IM_C_DEACT_Msk             (_U_(0x1) << SPW_PKTTX1_IM_C_DEACT_Pos)        /**< (SPW_PKTTX1_IM_C) Deactivated Mask */
#define SPW_PKTTX1_IM_C_ACT_Pos               _U_(1)                                         /**< (SPW_PKTTX1_IM_C) Activated Position */
#define SPW_PKTTX1_IM_C_ACT_Msk               (_U_(0x1) << SPW_PKTTX1_IM_C_ACT_Pos)          /**< (SPW_PKTTX1_IM_C) Activated Mask */
#define SPW_PKTTX1_IM_C_EOP_Pos               _U_(2)                                         /**< (SPW_PKTTX1_IM_C) EOP sent Position */
#define SPW_PKTTX1_IM_C_EOP_Msk               (_U_(0x1) << SPW_PKTTX1_IM_C_EOP_Pos)          /**< (SPW_PKTTX1_IM_C) EOP sent Mask */
#define SPW_PKTTX1_IM_C_EEP_Pos               _U_(3)                                         /**< (SPW_PKTTX1_IM_C) EEP sent Position */
#define SPW_PKTTX1_IM_C_EEP_Msk               (_U_(0x1) << SPW_PKTTX1_IM_C_EEP_Pos)          /**< (SPW_PKTTX1_IM_C) EEP sent Mask */
#define SPW_PKTTX1_IM_C_Msk                   _U_(0x0000000F)                                /**< (SPW_PKTTX1_IM_C) Register Mask  */


/* -------- SPW_PKTTX1_STATUS : (SPW Offset: 0xC20) (R/W 32) PktTx Status -------- */
#define SPW_PKTTX1_STATUS_ARM_Pos             _U_(0)                                         /**< (SPW_PKTTX1_STATUS) Armed Position */
#define SPW_PKTTX1_STATUS_ARM_Msk             (_U_(0x1) << SPW_PKTTX1_STATUS_ARM_Pos)        /**< (SPW_PKTTX1_STATUS) Armed Mask */
#define SPW_PKTTX1_STATUS_ACT_Pos             _U_(1)                                         /**< (SPW_PKTTX1_STATUS) Active Position */
#define SPW_PKTTX1_STATUS_ACT_Msk             (_U_(0x1) << SPW_PKTTX1_STATUS_ACT_Pos)        /**< (SPW_PKTTX1_STATUS) Active Mask */
#define SPW_PKTTX1_STATUS_PENDING_Pos         _U_(2)                                         /**< (SPW_PKTTX1_STATUS) Pending Position */
#define SPW_PKTTX1_STATUS_PENDING_Msk         (_U_(0x1) << SPW_PKTTX1_STATUS_PENDING_Pos)    /**< (SPW_PKTTX1_STATUS) Pending Mask */
#define SPW_PKTTX1_STATUS_DEACT_Pos           _U_(3)                                         /**< (SPW_PKTTX1_STATUS) Deactivating Position */
#define SPW_PKTTX1_STATUS_DEACT_Msk           (_U_(0x1) << SPW_PKTTX1_STATUS_DEACT_Pos)      /**< (SPW_PKTTX1_STATUS) Deactivating Mask */
#define SPW_PKTTX1_STATUS_PREV_Pos            _U_(16)                                        /**< (SPW_PKTTX1_STATUS) Previous Position */
#define SPW_PKTTX1_STATUS_PREV_Msk            (_U_(0x7) << SPW_PKTTX1_STATUS_PREV_Pos)       /**< (SPW_PKTTX1_STATUS) Previous Mask */
#define SPW_PKTTX1_STATUS_PREV(value)         (SPW_PKTTX1_STATUS_PREV_Msk & ((value) << SPW_PKTTX1_STATUS_PREV_Pos))
#define   SPW_PKTTX1_STATUS_PREV_NOINFO_Val   _U_(0x0)                                       /**< (SPW_PKTTX1_STATUS) No information. Field not locked.  */
#define   SPW_PKTTX1_STATUS_PREV_LASTSENDLISTOK_Val _U_(0x1)                                       /**< (SPW_PKTTX1_STATUS) Last send list fully done  */
#define   SPW_PKTTX1_STATUS_PREV_ABORTEDMEMERR_Val _U_(0x2)                                       /**< (SPW_PKTTX1_STATUS) Aborted due to memory access error.  */
#define   SPW_PKTTX1_STATUS_PREV_ABORTEDNEWSD_Val _U_(0x3)                                       /**< (SPW_PKTTX1_STATUS) Aborted by new send list.  */
#define   SPW_PKTTX1_STATUS_PREV_ABORTEDUSERCMD_Val _U_(0x4)                                       /**< (SPW_PKTTX1_STATUS) Aborted by direct user command.  */
#define   SPW_PKTTX1_STATUS_PREV_ABORTEDTIMEOUT_Val _U_(0x5)                                       /**< (SPW_PKTTX1_STATUS) Aborted by timeout.  */
#define SPW_PKTTX1_STATUS_PREV_NOINFO         (SPW_PKTTX1_STATUS_PREV_NOINFO_Val << SPW_PKTTX1_STATUS_PREV_Pos) /**< (SPW_PKTTX1_STATUS) No information. Field not locked. Position  */
#define SPW_PKTTX1_STATUS_PREV_LASTSENDLISTOK (SPW_PKTTX1_STATUS_PREV_LASTSENDLISTOK_Val << SPW_PKTTX1_STATUS_PREV_Pos) /**< (SPW_PKTTX1_STATUS) Last send list fully done Position  */
#define SPW_PKTTX1_STATUS_PREV_ABORTEDMEMERR  (SPW_PKTTX1_STATUS_PREV_ABORTEDMEMERR_Val << SPW_PKTTX1_STATUS_PREV_Pos) /**< (SPW_PKTTX1_STATUS) Aborted due to memory access error. Position  */
#define SPW_PKTTX1_STATUS_PREV_ABORTEDNEWSD   (SPW_PKTTX1_STATUS_PREV_ABORTEDNEWSD_Val << SPW_PKTTX1_STATUS_PREV_Pos) /**< (SPW_PKTTX1_STATUS) Aborted by new send list. Position  */
#define SPW_PKTTX1_STATUS_PREV_ABORTEDUSERCMD (SPW_PKTTX1_STATUS_PREV_ABORTEDUSERCMD_Val << SPW_PKTTX1_STATUS_PREV_Pos) /**< (SPW_PKTTX1_STATUS) Aborted by direct user command. Position  */
#define SPW_PKTTX1_STATUS_PREV_ABORTEDTIMEOUT (SPW_PKTTX1_STATUS_PREV_ABORTEDTIMEOUT_Val << SPW_PKTTX1_STATUS_PREV_Pos) /**< (SPW_PKTTX1_STATUS) Aborted by timeout. Position  */
#define SPW_PKTTX1_STATUS_Msk                 _U_(0x0007000F)                                /**< (SPW_PKTTX1_STATUS) Register Mask  */


/* -------- SPW_PKTTX1_NXTSENDROUT : (SPW Offset: 0xC24) (R/W 32) PktTx Next Send List Router Bytes -------- */
#define SPW_PKTTX1_NXTSENDROUT_BYTE4_Pos      _U_(0)                                         /**< (SPW_PKTTX1_NXTSENDROUT) Byte4 Position */
#define SPW_PKTTX1_NXTSENDROUT_BYTE4_Msk      (_U_(0xFF) << SPW_PKTTX1_NXTSENDROUT_BYTE4_Pos) /**< (SPW_PKTTX1_NXTSENDROUT) Byte4 Mask */
#define SPW_PKTTX1_NXTSENDROUT_BYTE4(value)   (SPW_PKTTX1_NXTSENDROUT_BYTE4_Msk & ((value) << SPW_PKTTX1_NXTSENDROUT_BYTE4_Pos))
#define SPW_PKTTX1_NXTSENDROUT_BYTE3_Pos      _U_(8)                                         /**< (SPW_PKTTX1_NXTSENDROUT) Byte3 Position */
#define SPW_PKTTX1_NXTSENDROUT_BYTE3_Msk      (_U_(0xFF) << SPW_PKTTX1_NXTSENDROUT_BYTE3_Pos) /**< (SPW_PKTTX1_NXTSENDROUT) Byte3 Mask */
#define SPW_PKTTX1_NXTSENDROUT_BYTE3(value)   (SPW_PKTTX1_NXTSENDROUT_BYTE3_Msk & ((value) << SPW_PKTTX1_NXTSENDROUT_BYTE3_Pos))
#define SPW_PKTTX1_NXTSENDROUT_BYTE2_Pos      _U_(16)                                        /**< (SPW_PKTTX1_NXTSENDROUT) Byte2 Position */
#define SPW_PKTTX1_NXTSENDROUT_BYTE2_Msk      (_U_(0xFF) << SPW_PKTTX1_NXTSENDROUT_BYTE2_Pos) /**< (SPW_PKTTX1_NXTSENDROUT) Byte2 Mask */
#define SPW_PKTTX1_NXTSENDROUT_BYTE2(value)   (SPW_PKTTX1_NXTSENDROUT_BYTE2_Msk & ((value) << SPW_PKTTX1_NXTSENDROUT_BYTE2_Pos))
#define SPW_PKTTX1_NXTSENDROUT_BYTE1_Pos      _U_(24)                                        /**< (SPW_PKTTX1_NXTSENDROUT) Byte1 Position */
#define SPW_PKTTX1_NXTSENDROUT_BYTE1_Msk      (_U_(0xFF) << SPW_PKTTX1_NXTSENDROUT_BYTE1_Pos) /**< (SPW_PKTTX1_NXTSENDROUT) Byte1 Mask */
#define SPW_PKTTX1_NXTSENDROUT_BYTE1(value)   (SPW_PKTTX1_NXTSENDROUT_BYTE1_Msk & ((value) << SPW_PKTTX1_NXTSENDROUT_BYTE1_Pos))
#define SPW_PKTTX1_NXTSENDROUT_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_PKTTX1_NXTSENDROUT) Register Mask  */


/* -------- SPW_PKTTX1_NXTSENDADDR : (SPW Offset: 0xC28) (R/W 32) PktTx Next Send List Address -------- */
#define SPW_PKTTX1_NXTSENDADDR_ADDR_Pos       _U_(0)                                         /**< (SPW_PKTTX1_NXTSENDADDR) Address Position */
#define SPW_PKTTX1_NXTSENDADDR_ADDR_Msk       (_U_(0xFFFFFFFF) << SPW_PKTTX1_NXTSENDADDR_ADDR_Pos) /**< (SPW_PKTTX1_NXTSENDADDR) Address Mask */
#define SPW_PKTTX1_NXTSENDADDR_ADDR(value)    (SPW_PKTTX1_NXTSENDADDR_ADDR_Msk & ((value) << SPW_PKTTX1_NXTSENDADDR_ADDR_Pos))
#define SPW_PKTTX1_NXTSENDADDR_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_PKTTX1_NXTSENDADDR) Register Mask  */


/* -------- SPW_PKTTX1_NXTSENDCFG : (SPW Offset: 0xC2C) (R/W 32) PktTx Next Send List Config -------- */
#define SPW_PKTTX1_NXTSENDCFG_LEN_Pos         _U_(0)                                         /**< (SPW_PKTTX1_NXTSENDCFG) Length Position */
#define SPW_PKTTX1_NXTSENDCFG_LEN_Msk         (_U_(0xFFFF) << SPW_PKTTX1_NXTSENDCFG_LEN_Pos) /**< (SPW_PKTTX1_NXTSENDCFG) Length Mask */
#define SPW_PKTTX1_NXTSENDCFG_LEN(value)      (SPW_PKTTX1_NXTSENDCFG_LEN_Msk & ((value) << SPW_PKTTX1_NXTSENDCFG_LEN_Pos))
#define SPW_PKTTX1_NXTSENDCFG_VALUE_Pos       _U_(16)                                        /**< (SPW_PKTTX1_NXTSENDCFG) Start Value Position */
#define SPW_PKTTX1_NXTSENDCFG_VALUE_Msk       (_U_(0x1) << SPW_PKTTX1_NXTSENDCFG_VALUE_Pos)  /**< (SPW_PKTTX1_NXTSENDCFG) Start Value Mask */
#define SPW_PKTTX1_NXTSENDCFG_START_Pos       _U_(22)                                        /**< (SPW_PKTTX1_NXTSENDCFG) Start Mode Position */
#define SPW_PKTTX1_NXTSENDCFG_START_Msk       (_U_(0x3) << SPW_PKTTX1_NXTSENDCFG_START_Pos)  /**< (SPW_PKTTX1_NXTSENDCFG) Start Mode Mask */
#define SPW_PKTTX1_NXTSENDCFG_START(value)    (SPW_PKTTX1_NXTSENDCFG_START_Msk & ((value) << SPW_PKTTX1_NXTSENDCFG_START_Pos))
#define   SPW_PKTTX1_NXTSENDCFG_START_STARTVALUE_Val _U_(0x0)                                       /**< (SPW_PKTTX1_NXTSENDCFG) Start if any bit in Start Value matches an incom-ing event  */
#define   SPW_PKTTX1_NXTSENDCFG_START_STARTNOW_Val _U_(0x1)                                       /**< (SPW_PKTTX1_NXTSENDCFG) Start immediately, if possible  */
#define   SPW_PKTTX1_NXTSENDCFG_START_STARTTCH1_Val _U_(0x2)                                       /**< (SPW_PKTTX1_NXTSENDCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 1  */
#define   SPW_PKTTX1_NXTSENDCFG_START_STARTTCH2_Val _U_(0x3)                                       /**< (SPW_PKTTX1_NXTSENDCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 2  */
#define SPW_PKTTX1_NXTSENDCFG_START_STARTVALUE (SPW_PKTTX1_NXTSENDCFG_START_STARTVALUE_Val << SPW_PKTTX1_NXTSENDCFG_START_Pos) /**< (SPW_PKTTX1_NXTSENDCFG) Start if any bit in Start Value matches an incom-ing event Position  */
#define SPW_PKTTX1_NXTSENDCFG_START_STARTNOW  (SPW_PKTTX1_NXTSENDCFG_START_STARTNOW_Val << SPW_PKTTX1_NXTSENDCFG_START_Pos) /**< (SPW_PKTTX1_NXTSENDCFG) Start immediately, if possible Position  */
#define SPW_PKTTX1_NXTSENDCFG_START_STARTTCH1 (SPW_PKTTX1_NXTSENDCFG_START_STARTTCH1_Val << SPW_PKTTX1_NXTSENDCFG_START_Pos) /**< (SPW_PKTTX1_NXTSENDCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 1 Position  */
#define SPW_PKTTX1_NXTSENDCFG_START_STARTTCH2 (SPW_PKTTX1_NXTSENDCFG_START_STARTTCH2_Val << SPW_PKTTX1_NXTSENDCFG_START_Pos) /**< (SPW_PKTTX1_NXTSENDCFG) Start if Start Value matches an incoming Time Code from Time Code Handler 2 Position  */
#define SPW_PKTTX1_NXTSENDCFG_ABORT_Pos       _U_(29)                                        /**< (SPW_PKTTX1_NXTSENDCFG) Abort Position */
#define SPW_PKTTX1_NXTSENDCFG_ABORT_Msk       (_U_(0x1) << SPW_PKTTX1_NXTSENDCFG_ABORT_Pos)  /**< (SPW_PKTTX1_NXTSENDCFG) Abort Mask */
#define SPW_PKTTX1_NXTSENDCFG_Msk             _U_(0x20C1FFFF)                                /**< (SPW_PKTTX1_NXTSENDCFG) Register Mask  */


/* -------- SPW_PKTTX1_CURSENDROUT : (SPW Offset: 0xC30) ( R/ 32) PktTx Current Send List Router Bytes -------- */
#define SPW_PKTTX1_CURSENDROUT_BYTE4_Pos      _U_(0)                                         /**< (SPW_PKTTX1_CURSENDROUT) Byte4 Position */
#define SPW_PKTTX1_CURSENDROUT_BYTE4_Msk      (_U_(0xFF) << SPW_PKTTX1_CURSENDROUT_BYTE4_Pos) /**< (SPW_PKTTX1_CURSENDROUT) Byte4 Mask */
#define SPW_PKTTX1_CURSENDROUT_BYTE4(value)   (SPW_PKTTX1_CURSENDROUT_BYTE4_Msk & ((value) << SPW_PKTTX1_CURSENDROUT_BYTE4_Pos))
#define SPW_PKTTX1_CURSENDROUT_BYTE3_Pos      _U_(8)                                         /**< (SPW_PKTTX1_CURSENDROUT) Byte3 Position */
#define SPW_PKTTX1_CURSENDROUT_BYTE3_Msk      (_U_(0xFF) << SPW_PKTTX1_CURSENDROUT_BYTE3_Pos) /**< (SPW_PKTTX1_CURSENDROUT) Byte3 Mask */
#define SPW_PKTTX1_CURSENDROUT_BYTE3(value)   (SPW_PKTTX1_CURSENDROUT_BYTE3_Msk & ((value) << SPW_PKTTX1_CURSENDROUT_BYTE3_Pos))
#define SPW_PKTTX1_CURSENDROUT_BYTE2_Pos      _U_(16)                                        /**< (SPW_PKTTX1_CURSENDROUT) Byte2 Position */
#define SPW_PKTTX1_CURSENDROUT_BYTE2_Msk      (_U_(0xFF) << SPW_PKTTX1_CURSENDROUT_BYTE2_Pos) /**< (SPW_PKTTX1_CURSENDROUT) Byte2 Mask */
#define SPW_PKTTX1_CURSENDROUT_BYTE2(value)   (SPW_PKTTX1_CURSENDROUT_BYTE2_Msk & ((value) << SPW_PKTTX1_CURSENDROUT_BYTE2_Pos))
#define SPW_PKTTX1_CURSENDROUT_BYTE1_Pos      _U_(24)                                        /**< (SPW_PKTTX1_CURSENDROUT) Byte1 Position */
#define SPW_PKTTX1_CURSENDROUT_BYTE1_Msk      (_U_(0xFF) << SPW_PKTTX1_CURSENDROUT_BYTE1_Pos) /**< (SPW_PKTTX1_CURSENDROUT) Byte1 Mask */
#define SPW_PKTTX1_CURSENDROUT_BYTE1(value)   (SPW_PKTTX1_CURSENDROUT_BYTE1_Msk & ((value) << SPW_PKTTX1_CURSENDROUT_BYTE1_Pos))
#define SPW_PKTTX1_CURSENDROUT_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_PKTTX1_CURSENDROUT) Register Mask  */


/* -------- SPW_PKTTX1_CURSENDADDR : (SPW Offset: 0xC34) ( R/ 32) PktTx Current Send List Address -------- */
#define SPW_PKTTX1_CURSENDADDR_ADDR_Pos       _U_(0)                                         /**< (SPW_PKTTX1_CURSENDADDR) Address Position */
#define SPW_PKTTX1_CURSENDADDR_ADDR_Msk       (_U_(0xFFFFFFFF) << SPW_PKTTX1_CURSENDADDR_ADDR_Pos) /**< (SPW_PKTTX1_CURSENDADDR) Address Mask */
#define SPW_PKTTX1_CURSENDADDR_ADDR(value)    (SPW_PKTTX1_CURSENDADDR_ADDR_Msk & ((value) << SPW_PKTTX1_CURSENDADDR_ADDR_Pos))
#define SPW_PKTTX1_CURSENDADDR_Msk            _U_(0xFFFFFFFF)                                /**< (SPW_PKTTX1_CURSENDADDR) Register Mask  */


/* -------- SPW_PKTTX1_CURSENDCFG : (SPW Offset: 0xC38) (R/W 32) PktTx Current Send List Config -------- */
#define SPW_PKTTX1_CURSENDCFG_LEN_Pos         _U_(0)                                         /**< (SPW_PKTTX1_CURSENDCFG) Length Position */
#define SPW_PKTTX1_CURSENDCFG_LEN_Msk         (_U_(0xFFFF) << SPW_PKTTX1_CURSENDCFG_LEN_Pos) /**< (SPW_PKTTX1_CURSENDCFG) Length Mask */
#define SPW_PKTTX1_CURSENDCFG_LEN(value)      (SPW_PKTTX1_CURSENDCFG_LEN_Msk & ((value) << SPW_PKTTX1_CURSENDCFG_LEN_Pos))
#define SPW_PKTTX1_CURSENDCFG_ABORT_Pos       _U_(31)                                        /**< (SPW_PKTTX1_CURSENDCFG) Abort Position */
#define SPW_PKTTX1_CURSENDCFG_ABORT_Msk       (_U_(0x1) << SPW_PKTTX1_CURSENDCFG_ABORT_Pos)  /**< (SPW_PKTTX1_CURSENDCFG) Abort Mask */
#define SPW_PKTTX1_CURSENDCFG_Msk             _U_(0x8000FFFF)                                /**< (SPW_PKTTX1_CURSENDCFG) Register Mask  */


/* -------- SPW_PKTTX1_SWRESET : (SPW Offset: 0xC3C) (R/W 32) PktTx Software Reset -------- */
#define SPW_PKTTX1_SWRESET_PATTERN_Pos        _U_(0)                                         /**< (SPW_PKTTX1_SWRESET) Pattern Position */
#define SPW_PKTTX1_SWRESET_PATTERN_Msk        (_U_(0xFFFFFFFF) << SPW_PKTTX1_SWRESET_PATTERN_Pos) /**< (SPW_PKTTX1_SWRESET) Pattern Mask */
#define SPW_PKTTX1_SWRESET_PATTERN(value)     (SPW_PKTTX1_SWRESET_PATTERN_Msk & ((value) << SPW_PKTTX1_SWRESET_PATTERN_Pos))
#define SPW_PKTTX1_SWRESET_Msk                _U_(0xFFFFFFFF)                                /**< (SPW_PKTTX1_SWRESET) Register Mask  */


/* -------- SPW_RMAP1_CFG : (SPW Offset: 0xE00) (R/W 32) SpW RMAP 1 Config -------- */
#define SPW_RMAP1_CFG_DESTKEY_Pos             _U_(0)                                         /**< (SPW_RMAP1_CFG) DestKey Position */
#define SPW_RMAP1_CFG_DESTKEY_Msk             (_U_(0xFF) << SPW_RMAP1_CFG_DESTKEY_Pos)       /**< (SPW_RMAP1_CFG) DestKey Mask */
#define SPW_RMAP1_CFG_DESTKEY(value)          (SPW_RMAP1_CFG_DESTKEY_Msk & ((value) << SPW_RMAP1_CFG_DESTKEY_Pos))
#define SPW_RMAP1_CFG_TLA_Pos                 _U_(8)                                         /**< (SPW_RMAP1_CFG) Address Position */
#define SPW_RMAP1_CFG_TLA_Msk                 (_U_(0xFF) << SPW_RMAP1_CFG_TLA_Pos)           /**< (SPW_RMAP1_CFG) Address Mask */
#define SPW_RMAP1_CFG_TLA(value)              (SPW_RMAP1_CFG_TLA_Msk & ((value) << SPW_RMAP1_CFG_TLA_Pos))
#define SPW_RMAP1_CFG_RMAPENA_Pos             _U_(16)                                        /**< (SPW_RMAP1_CFG) RMAP Enable Position */
#define SPW_RMAP1_CFG_RMAPENA_Msk             (_U_(0x1) << SPW_RMAP1_CFG_RMAPENA_Pos)        /**< (SPW_RMAP1_CFG) RMAP Enable Mask */
#define SPW_RMAP1_CFG_Msk                     _U_(0x0001FFFF)                                /**< (SPW_RMAP1_CFG) Register Mask  */


/* -------- SPW_RMAP1_STS_RC : (SPW Offset: 0xE04) ( R/ 32) SpW RMAP 1 Read and Clear Status -------- */
#define SPW_RMAP1_STS_RC_ERRCODE_Pos          _U_(0)                                         /**< (SPW_RMAP1_STS_RC) Error Code Position */
#define SPW_RMAP1_STS_RC_ERRCODE_Msk          (_U_(0xFF) << SPW_RMAP1_STS_RC_ERRCODE_Pos)    /**< (SPW_RMAP1_STS_RC) Error Code Mask */
#define SPW_RMAP1_STS_RC_ERRCODE(value)       (SPW_RMAP1_STS_RC_ERRCODE_Msk & ((value) << SPW_RMAP1_STS_RC_ERRCODE_Pos))
#define   SPW_RMAP1_STS_RC_ERRCODE_NOERROR_Val _U_(0x0)                                       /**< (SPW_RMAP1_STS_RC) No error detected  */
#define   SPW_RMAP1_STS_RC_ERRCODE_DMAERROR_Val _U_(0x1)                                       /**< (SPW_RMAP1_STS_RC) Error while DMA accessing the internal bus, e.g. illegal address.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_RMAPERROR_Val _U_(0x2)                                       /**< (SPW_RMAP1_STS_RC) Unused RMAP command according to [RMAP]  */
#define   SPW_RMAP1_STS_RC_ERRCODE_DESTKEYERROR_Val _U_(0x3)                                       /**< (SPW_RMAP1_STS_RC) Destination key error  */
#define   SPW_RMAP1_STS_RC_ERRCODE_DATACRCERROR_Val _U_(0x4)                                       /**< (SPW_RMAP1_STS_RC) Data CRC error  */
#define   SPW_RMAP1_STS_RC_ERRCODE_EOPERROR_Val _U_(0x5)                                       /**< (SPW_RMAP1_STS_RC) Early EOP in header or data, i.e. EOP has been received with less data than expected from the RMAP command header.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_CARGOERROR_Val _U_(0x6)                                       /**< (SPW_RMAP1_STS_RC) Cargo too large. Late EOP or EEP in data, i.e. EOP/EEP has been received with more data than expected from the RMAP command header.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_EEPERROR_Val _U_(0x7)                                       /**< (SPW_RMAP1_STS_RC) Early EEP in data for RMAP commands. EEP has been received with less data or exactly as much as expected from the RMAP command header.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_CMDERROR_Val _U_(0xA)                                       /**< (SPW_RMAP1_STS_RC) Authorisation error:Invalid or unsupported command.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_TLAERROR_Val _U_(0xC)                                       /**< (SPW_RMAP1_STS_RC) Non-matching Target Logical Address.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_HEADERCRCERROR_Val _U_(0x10)                                      /**< (SPW_RMAP1_STS_RC) Incorrect header CRC.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_PROTOCOLIDERROR_Val _U_(0x11)                                      /**< (SPW_RMAP1_STS_RC) Protocol Identifier not supported.  */
#define   SPW_RMAP1_STS_RC_ERRCODE_REPLYADDERROR_Val _U_(0x12)                                      /**< (SPW_RMAP1_STS_RC) Unsupported reply address length  */
#define SPW_RMAP1_STS_RC_ERRCODE_NOERROR      (SPW_RMAP1_STS_RC_ERRCODE_NOERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) No error detected Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_DMAERROR     (SPW_RMAP1_STS_RC_ERRCODE_DMAERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Error while DMA accessing the internal bus, e.g. illegal address. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_RMAPERROR    (SPW_RMAP1_STS_RC_ERRCODE_RMAPERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Unused RMAP command according to [RMAP] Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_DESTKEYERROR (SPW_RMAP1_STS_RC_ERRCODE_DESTKEYERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Destination key error Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_DATACRCERROR (SPW_RMAP1_STS_RC_ERRCODE_DATACRCERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Data CRC error Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_EOPERROR     (SPW_RMAP1_STS_RC_ERRCODE_EOPERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Early EOP in header or data, i.e. EOP has been received with less data than expected from the RMAP command header. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_CARGOERROR   (SPW_RMAP1_STS_RC_ERRCODE_CARGOERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Cargo too large. Late EOP or EEP in data, i.e. EOP/EEP has been received with more data than expected from the RMAP command header. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_EEPERROR     (SPW_RMAP1_STS_RC_ERRCODE_EEPERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Early EEP in data for RMAP commands. EEP has been received with less data or exactly as much as expected from the RMAP command header. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_CMDERROR     (SPW_RMAP1_STS_RC_ERRCODE_CMDERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Authorisation error:Invalid or unsupported command. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_TLAERROR     (SPW_RMAP1_STS_RC_ERRCODE_TLAERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Non-matching Target Logical Address. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_HEADERCRCERROR (SPW_RMAP1_STS_RC_ERRCODE_HEADERCRCERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Incorrect header CRC. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_PROTOCOLIDERROR (SPW_RMAP1_STS_RC_ERRCODE_PROTOCOLIDERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Protocol Identifier not supported. Position  */
#define SPW_RMAP1_STS_RC_ERRCODE_REPLYADDERROR (SPW_RMAP1_STS_RC_ERRCODE_REPLYADDERROR_Val << SPW_RMAP1_STS_RC_ERRCODE_Pos) /**< (SPW_RMAP1_STS_RC) Unsupported reply address length Position  */
#define SPW_RMAP1_STS_RC_VALID_Pos            _U_(8)                                         /**< (SPW_RMAP1_STS_RC) Valid Position */
#define SPW_RMAP1_STS_RC_VALID_Msk            (_U_(0x1) << SPW_RMAP1_STS_RC_VALID_Pos)       /**< (SPW_RMAP1_STS_RC) Valid Mask */
#define SPW_RMAP1_STS_RC_Msk                  _U_(0x000001FF)                                /**< (SPW_RMAP1_STS_RC) Register Mask  */


/* -------- SPW_RMAP1_STS : (SPW Offset: 0xE08) ( R/ 32) SpW RMAP 1 Read Status -------- */
#define SPW_RMAP1_STS_ERRCODE_Pos             _U_(0)                                         /**< (SPW_RMAP1_STS) Error Code Position */
#define SPW_RMAP1_STS_ERRCODE_Msk             (_U_(0xFF) << SPW_RMAP1_STS_ERRCODE_Pos)       /**< (SPW_RMAP1_STS) Error Code Mask */
#define SPW_RMAP1_STS_ERRCODE(value)          (SPW_RMAP1_STS_ERRCODE_Msk & ((value) << SPW_RMAP1_STS_ERRCODE_Pos))
#define   SPW_RMAP1_STS_ERRCODE_NOERROR_Val   _U_(0x0)                                       /**< (SPW_RMAP1_STS) No error detected  */
#define   SPW_RMAP1_STS_ERRCODE_DMAERROR_Val  _U_(0x1)                                       /**< (SPW_RMAP1_STS) Error while DMA accessing the internal bus, e.g. illegal address.  */
#define   SPW_RMAP1_STS_ERRCODE_RMAPERROR_Val _U_(0x2)                                       /**< (SPW_RMAP1_STS) Unused RMAP command according to [RMAP]  */
#define   SPW_RMAP1_STS_ERRCODE_DESTKEYERROR_Val _U_(0x3)                                       /**< (SPW_RMAP1_STS) Destination key error  */
#define   SPW_RMAP1_STS_ERRCODE_DATACRCERROR_Val _U_(0x4)                                       /**< (SPW_RMAP1_STS) Data CRC error  */
#define   SPW_RMAP1_STS_ERRCODE_EOPERROR_Val  _U_(0x5)                                       /**< (SPW_RMAP1_STS) Early EOP in header or data, i.e. EOP has been received with less data than expected from the RMAP command header.  */
#define   SPW_RMAP1_STS_ERRCODE_CARGOERROR_Val _U_(0x6)                                       /**< (SPW_RMAP1_STS) Cargo too large. Late EOP or EEP in data, i.e. EOP/EEP has been received with more data than expected from the RMAP command header.  */
#define   SPW_RMAP1_STS_ERRCODE_EEPERROR_Val  _U_(0x7)                                       /**< (SPW_RMAP1_STS) Early EEP in data for RMAP commands. EEP has been received with less data or exactly as much as expected from the RMAP command header.  */
#define   SPW_RMAP1_STS_ERRCODE_CMDERROR_Val  _U_(0xA)                                       /**< (SPW_RMAP1_STS) Authorisation error:Invalid or unsupported command.  */
#define   SPW_RMAP1_STS_ERRCODE_TLAERROR_Val  _U_(0xC)                                       /**< (SPW_RMAP1_STS) Non-matching Target Logical Address.  */
#define   SPW_RMAP1_STS_ERRCODE_HEADERCRCERROR_Val _U_(0x10)                                      /**< (SPW_RMAP1_STS) Incorrect header CRC.  */
#define   SPW_RMAP1_STS_ERRCODE_PROTOCOLIDERROR_Val _U_(0x11)                                      /**< (SPW_RMAP1_STS) Protocol Identifier not supported.  */
#define   SPW_RMAP1_STS_ERRCODE_REPLYADDERROR_Val _U_(0x12)                                      /**< (SPW_RMAP1_STS) Unsupported reply address length  */
#define SPW_RMAP1_STS_ERRCODE_NOERROR         (SPW_RMAP1_STS_ERRCODE_NOERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) No error detected Position  */
#define SPW_RMAP1_STS_ERRCODE_DMAERROR        (SPW_RMAP1_STS_ERRCODE_DMAERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Error while DMA accessing the internal bus, e.g. illegal address. Position  */
#define SPW_RMAP1_STS_ERRCODE_RMAPERROR       (SPW_RMAP1_STS_ERRCODE_RMAPERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Unused RMAP command according to [RMAP] Position  */
#define SPW_RMAP1_STS_ERRCODE_DESTKEYERROR    (SPW_RMAP1_STS_ERRCODE_DESTKEYERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Destination key error Position  */
#define SPW_RMAP1_STS_ERRCODE_DATACRCERROR    (SPW_RMAP1_STS_ERRCODE_DATACRCERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Data CRC error Position  */
#define SPW_RMAP1_STS_ERRCODE_EOPERROR        (SPW_RMAP1_STS_ERRCODE_EOPERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Early EOP in header or data, i.e. EOP has been received with less data than expected from the RMAP command header. Position  */
#define SPW_RMAP1_STS_ERRCODE_CARGOERROR      (SPW_RMAP1_STS_ERRCODE_CARGOERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Cargo too large. Late EOP or EEP in data, i.e. EOP/EEP has been received with more data than expected from the RMAP command header. Position  */
#define SPW_RMAP1_STS_ERRCODE_EEPERROR        (SPW_RMAP1_STS_ERRCODE_EEPERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Early EEP in data for RMAP commands. EEP has been received with less data or exactly as much as expected from the RMAP command header. Position  */
#define SPW_RMAP1_STS_ERRCODE_CMDERROR        (SPW_RMAP1_STS_ERRCODE_CMDERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Authorisation error:Invalid or unsupported command. Position  */
#define SPW_RMAP1_STS_ERRCODE_TLAERROR        (SPW_RMAP1_STS_ERRCODE_TLAERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Non-matching Target Logical Address. Position  */
#define SPW_RMAP1_STS_ERRCODE_HEADERCRCERROR  (SPW_RMAP1_STS_ERRCODE_HEADERCRCERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Incorrect header CRC. Position  */
#define SPW_RMAP1_STS_ERRCODE_PROTOCOLIDERROR (SPW_RMAP1_STS_ERRCODE_PROTOCOLIDERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Protocol Identifier not supported. Position  */
#define SPW_RMAP1_STS_ERRCODE_REPLYADDERROR   (SPW_RMAP1_STS_ERRCODE_REPLYADDERROR_Val << SPW_RMAP1_STS_ERRCODE_Pos) /**< (SPW_RMAP1_STS) Unsupported reply address length Position  */
#define SPW_RMAP1_STS_VALID_Pos               _U_(8)                                         /**< (SPW_RMAP1_STS) Valid Position */
#define SPW_RMAP1_STS_VALID_Msk               (_U_(0x1) << SPW_RMAP1_STS_VALID_Pos)          /**< (SPW_RMAP1_STS) Valid Mask */
#define SPW_RMAP1_STS_Msk                     _U_(0x000001FF)                                /**< (SPW_RMAP1_STS) Register Mask  */


/* -------- SPW_TCH_PI_RM : (SPW Offset: 0xE80) ( R/ 32) SpW Tch Pending Read Masked Interrupt -------- */
#define SPW_TCH_PI_RM_TCEVENT_Pos             _U_(0)                                         /**< (SPW_TCH_PI_RM) TcEvent Position */
#define SPW_TCH_PI_RM_TCEVENT_Msk             (_U_(0x1) << SPW_TCH_PI_RM_TCEVENT_Pos)        /**< (SPW_TCH_PI_RM) TcEvent Mask */
#define SPW_TCH_PI_RM_TIMECODE_Pos            _U_(1)                                         /**< (SPW_TCH_PI_RM) Time Code Position */
#define SPW_TCH_PI_RM_TIMECODE_Msk            (_U_(0x1) << SPW_TCH_PI_RM_TIMECODE_Pos)       /**< (SPW_TCH_PI_RM) Time Code Mask */
#define SPW_TCH_PI_RM_ANYTIMECODE_Pos         _U_(2)                                         /**< (SPW_TCH_PI_RM) Any Time Code Position */
#define SPW_TCH_PI_RM_ANYTIMECODE_Msk         (_U_(0x1) << SPW_TCH_PI_RM_ANYTIMECODE_Pos)    /**< (SPW_TCH_PI_RM) Any Time Code Mask */
#define SPW_TCH_PI_RM_LATEWD_Pos              _U_(3)                                         /**< (SPW_TCH_PI_RM) Late Watchdog Position */
#define SPW_TCH_PI_RM_LATEWD_Msk              (_U_(0x1) << SPW_TCH_PI_RM_LATEWD_Pos)         /**< (SPW_TCH_PI_RM) Late Watchdog Mask */
#define SPW_TCH_PI_RM_EARLYWD_Pos             _U_(4)                                         /**< (SPW_TCH_PI_RM) Early Watchdog Position */
#define SPW_TCH_PI_RM_EARLYWD_Msk             (_U_(0x1) << SPW_TCH_PI_RM_EARLYWD_Pos)        /**< (SPW_TCH_PI_RM) Early Watchdog Mask */
#define SPW_TCH_PI_RM_Msk                     _U_(0x0000001F)                                /**< (SPW_TCH_PI_RM) Register Mask  */


/* -------- SPW_TCH_PI_RCM : (SPW Offset: 0xE84) ( R/ 32) SpW Tch Pending Read and Clear Masked Interrupt -------- */
#define SPW_TCH_PI_RCM_TCEVENT_Pos            _U_(0)                                         /**< (SPW_TCH_PI_RCM) TcEvent Position */
#define SPW_TCH_PI_RCM_TCEVENT_Msk            (_U_(0x1) << SPW_TCH_PI_RCM_TCEVENT_Pos)       /**< (SPW_TCH_PI_RCM) TcEvent Mask */
#define SPW_TCH_PI_RCM_TIMECODE_Pos           _U_(1)                                         /**< (SPW_TCH_PI_RCM) Time Code Position */
#define SPW_TCH_PI_RCM_TIMECODE_Msk           (_U_(0x1) << SPW_TCH_PI_RCM_TIMECODE_Pos)      /**< (SPW_TCH_PI_RCM) Time Code Mask */
#define SPW_TCH_PI_RCM_ANYTIMECODE_Pos        _U_(2)                                         /**< (SPW_TCH_PI_RCM) Any Time Code Position */
#define SPW_TCH_PI_RCM_ANYTIMECODE_Msk        (_U_(0x1) << SPW_TCH_PI_RCM_ANYTIMECODE_Pos)   /**< (SPW_TCH_PI_RCM) Any Time Code Mask */
#define SPW_TCH_PI_RCM_LATEWD_Pos             _U_(3)                                         /**< (SPW_TCH_PI_RCM) Late Watchdog Position */
#define SPW_TCH_PI_RCM_LATEWD_Msk             (_U_(0x1) << SPW_TCH_PI_RCM_LATEWD_Pos)        /**< (SPW_TCH_PI_RCM) Late Watchdog Mask */
#define SPW_TCH_PI_RCM_EARLYWD_Pos            _U_(4)                                         /**< (SPW_TCH_PI_RCM) Early Watchdog Position */
#define SPW_TCH_PI_RCM_EARLYWD_Msk            (_U_(0x1) << SPW_TCH_PI_RCM_EARLYWD_Pos)       /**< (SPW_TCH_PI_RCM) Early Watchdog Mask */
#define SPW_TCH_PI_RCM_Msk                    _U_(0x0000001F)                                /**< (SPW_TCH_PI_RCM) Register Mask  */


/* -------- SPW_TCH_PI_R : (SPW Offset: 0xE88) ( R/ 32) SpW Tch Pending Read Interrupt -------- */
#define SPW_TCH_PI_R_TCEVENT_Pos              _U_(0)                                         /**< (SPW_TCH_PI_R) TcEvent Position */
#define SPW_TCH_PI_R_TCEVENT_Msk              (_U_(0x1) << SPW_TCH_PI_R_TCEVENT_Pos)         /**< (SPW_TCH_PI_R) TcEvent Mask */
#define SPW_TCH_PI_R_TIMECODE_Pos             _U_(1)                                         /**< (SPW_TCH_PI_R) Time Code Position */
#define SPW_TCH_PI_R_TIMECODE_Msk             (_U_(0x1) << SPW_TCH_PI_R_TIMECODE_Pos)        /**< (SPW_TCH_PI_R) Time Code Mask */
#define SPW_TCH_PI_R_ANYTIMECODE_Pos          _U_(2)                                         /**< (SPW_TCH_PI_R) Any Time Code Position */
#define SPW_TCH_PI_R_ANYTIMECODE_Msk          (_U_(0x1) << SPW_TCH_PI_R_ANYTIMECODE_Pos)     /**< (SPW_TCH_PI_R) Any Time Code Mask */
#define SPW_TCH_PI_R_LATEWD_Pos               _U_(3)                                         /**< (SPW_TCH_PI_R) Late Watchdog Position */
#define SPW_TCH_PI_R_LATEWD_Msk               (_U_(0x1) << SPW_TCH_PI_R_LATEWD_Pos)          /**< (SPW_TCH_PI_R) Late Watchdog Mask */
#define SPW_TCH_PI_R_EARLYWD_Pos              _U_(4)                                         /**< (SPW_TCH_PI_R) Early Watchdog Position */
#define SPW_TCH_PI_R_EARLYWD_Msk              (_U_(0x1) << SPW_TCH_PI_R_EARLYWD_Pos)         /**< (SPW_TCH_PI_R) Early Watchdog Mask */
#define SPW_TCH_PI_R_Msk                      _U_(0x0000001F)                                /**< (SPW_TCH_PI_R) Register Mask  */


/* -------- SPW_TCH_PI_RCS : (SPW Offset: 0xE8C) (R/W 32) SpW Tch Pending Read, Clear and Enabled Interrupt -------- */
#define SPW_TCH_PI_RCS_TCEVENT_Pos            _U_(0)                                         /**< (SPW_TCH_PI_RCS) TcEvent Position */
#define SPW_TCH_PI_RCS_TCEVENT_Msk            (_U_(0x1) << SPW_TCH_PI_RCS_TCEVENT_Pos)       /**< (SPW_TCH_PI_RCS) TcEvent Mask */
#define SPW_TCH_PI_RCS_TIMECODE_Pos           _U_(1)                                         /**< (SPW_TCH_PI_RCS) Time Code Position */
#define SPW_TCH_PI_RCS_TIMECODE_Msk           (_U_(0x1) << SPW_TCH_PI_RCS_TIMECODE_Pos)      /**< (SPW_TCH_PI_RCS) Time Code Mask */
#define SPW_TCH_PI_RCS_ANYTIMECODE_Pos        _U_(2)                                         /**< (SPW_TCH_PI_RCS) Any Time Code Position */
#define SPW_TCH_PI_RCS_ANYTIMECODE_Msk        (_U_(0x1) << SPW_TCH_PI_RCS_ANYTIMECODE_Pos)   /**< (SPW_TCH_PI_RCS) Any Time Code Mask */
#define SPW_TCH_PI_RCS_LATEWD_Pos             _U_(3)                                         /**< (SPW_TCH_PI_RCS) Late Watchdog Position */
#define SPW_TCH_PI_RCS_LATEWD_Msk             (_U_(0x1) << SPW_TCH_PI_RCS_LATEWD_Pos)        /**< (SPW_TCH_PI_RCS) Late Watchdog Mask */
#define SPW_TCH_PI_RCS_EARLYWD_Pos            _U_(4)                                         /**< (SPW_TCH_PI_RCS) Early Watchdog Position */
#define SPW_TCH_PI_RCS_EARLYWD_Msk            (_U_(0x1) << SPW_TCH_PI_RCS_EARLYWD_Pos)       /**< (SPW_TCH_PI_RCS) Early Watchdog Mask */
#define SPW_TCH_PI_RCS_Msk                    _U_(0x0000001F)                                /**< (SPW_TCH_PI_RCS) Register Mask  */


/* -------- SPW_TCH_IM : (SPW Offset: 0xE90) (R/W 32) SpW Tch Interrupt Mask -------- */
#define SPW_TCH_IM_TCEVENT_Pos                _U_(0)                                         /**< (SPW_TCH_IM) TcEvent Position */
#define SPW_TCH_IM_TCEVENT_Msk                (_U_(0x1) << SPW_TCH_IM_TCEVENT_Pos)           /**< (SPW_TCH_IM) TcEvent Mask */
#define SPW_TCH_IM_TIMECODE_Pos               _U_(1)                                         /**< (SPW_TCH_IM) Time Code Position */
#define SPW_TCH_IM_TIMECODE_Msk               (_U_(0x1) << SPW_TCH_IM_TIMECODE_Pos)          /**< (SPW_TCH_IM) Time Code Mask */
#define SPW_TCH_IM_ANYTIMECODE_Pos            _U_(2)                                         /**< (SPW_TCH_IM) Any Time Code Position */
#define SPW_TCH_IM_ANYTIMECODE_Msk            (_U_(0x1) << SPW_TCH_IM_ANYTIMECODE_Pos)       /**< (SPW_TCH_IM) Any Time Code Mask */
#define SPW_TCH_IM_LATEWD_Pos                 _U_(3)                                         /**< (SPW_TCH_IM) Late Watchdog Position */
#define SPW_TCH_IM_LATEWD_Msk                 (_U_(0x1) << SPW_TCH_IM_LATEWD_Pos)            /**< (SPW_TCH_IM) Late Watchdog Mask */
#define SPW_TCH_IM_EARLYWD_Pos                _U_(4)                                         /**< (SPW_TCH_IM) Early Watchdog Position */
#define SPW_TCH_IM_EARLYWD_Msk                (_U_(0x1) << SPW_TCH_IM_EARLYWD_Pos)           /**< (SPW_TCH_IM) Early Watchdog Mask */
#define SPW_TCH_IM_Msk                        _U_(0x0000001F)                                /**< (SPW_TCH_IM) Register Mask  */


/* -------- SPW_TCH_PI_C : (SPW Offset: 0xE94) ( /W 32) SpW Tch Clear Pending Interrupt -------- */
#define SPW_TCH_PI_C_TCEVENT_Pos              _U_(0)                                         /**< (SPW_TCH_PI_C) TcEvent Position */
#define SPW_TCH_PI_C_TCEVENT_Msk              (_U_(0x1) << SPW_TCH_PI_C_TCEVENT_Pos)         /**< (SPW_TCH_PI_C) TcEvent Mask */
#define SPW_TCH_PI_C_TIMECODE_Pos             _U_(1)                                         /**< (SPW_TCH_PI_C) Time Code Position */
#define SPW_TCH_PI_C_TIMECODE_Msk             (_U_(0x1) << SPW_TCH_PI_C_TIMECODE_Pos)        /**< (SPW_TCH_PI_C) Time Code Mask */
#define SPW_TCH_PI_C_ANYTIMECODE_Pos          _U_(2)                                         /**< (SPW_TCH_PI_C) Any Time Code Position */
#define SPW_TCH_PI_C_ANYTIMECODE_Msk          (_U_(0x1) << SPW_TCH_PI_C_ANYTIMECODE_Pos)     /**< (SPW_TCH_PI_C) Any Time Code Mask */
#define SPW_TCH_PI_C_LATEWD_Pos               _U_(3)                                         /**< (SPW_TCH_PI_C) Late Watchdog Position */
#define SPW_TCH_PI_C_LATEWD_Msk               (_U_(0x1) << SPW_TCH_PI_C_LATEWD_Pos)          /**< (SPW_TCH_PI_C) Late Watchdog Mask */
#define SPW_TCH_PI_C_EARLYWD_Pos              _U_(4)                                         /**< (SPW_TCH_PI_C) Early Watchdog Position */
#define SPW_TCH_PI_C_EARLYWD_Msk              (_U_(0x1) << SPW_TCH_PI_C_EARLYWD_Pos)         /**< (SPW_TCH_PI_C) Early Watchdog Mask */
#define SPW_TCH_PI_C_Msk                      _U_(0x0000001F)                                /**< (SPW_TCH_PI_C) Register Mask  */


/* -------- SPW_TCH_IM_S : (SPW Offset: 0xE98) ( /W 32) SpW Tch Interrupt Set Mask -------- */
#define SPW_TCH_IM_S_TCEVENT_Pos              _U_(0)                                         /**< (SPW_TCH_IM_S) TcEvent Position */
#define SPW_TCH_IM_S_TCEVENT_Msk              (_U_(0x1) << SPW_TCH_IM_S_TCEVENT_Pos)         /**< (SPW_TCH_IM_S) TcEvent Mask */
#define SPW_TCH_IM_S_TIMECODE_Pos             _U_(1)                                         /**< (SPW_TCH_IM_S) Time Code Position */
#define SPW_TCH_IM_S_TIMECODE_Msk             (_U_(0x1) << SPW_TCH_IM_S_TIMECODE_Pos)        /**< (SPW_TCH_IM_S) Time Code Mask */
#define SPW_TCH_IM_S_ANYTIMECODE_Pos          _U_(2)                                         /**< (SPW_TCH_IM_S) Any Time Code Position */
#define SPW_TCH_IM_S_ANYTIMECODE_Msk          (_U_(0x1) << SPW_TCH_IM_S_ANYTIMECODE_Pos)     /**< (SPW_TCH_IM_S) Any Time Code Mask */
#define SPW_TCH_IM_S_LATEWD_Pos               _U_(3)                                         /**< (SPW_TCH_IM_S) Late Watchdog Position */
#define SPW_TCH_IM_S_LATEWD_Msk               (_U_(0x1) << SPW_TCH_IM_S_LATEWD_Pos)          /**< (SPW_TCH_IM_S) Late Watchdog Mask */
#define SPW_TCH_IM_S_EARLYWD_Pos              _U_(4)                                         /**< (SPW_TCH_IM_S) Early Watchdog Position */
#define SPW_TCH_IM_S_EARLYWD_Msk              (_U_(0x1) << SPW_TCH_IM_S_EARLYWD_Pos)         /**< (SPW_TCH_IM_S) Early Watchdog Mask */
#define SPW_TCH_IM_S_Msk                      _U_(0x0000001F)                                /**< (SPW_TCH_IM_S) Register Mask  */


/* -------- SPW_TCH_IM_C : (SPW Offset: 0xE9C) ( /W 32) SpW Tch Interrupt Clear Mask -------- */
#define SPW_TCH_IM_C_TCEVENT_Pos              _U_(0)                                         /**< (SPW_TCH_IM_C) TcEvent Position */
#define SPW_TCH_IM_C_TCEVENT_Msk              (_U_(0x1) << SPW_TCH_IM_C_TCEVENT_Pos)         /**< (SPW_TCH_IM_C) TcEvent Mask */
#define SPW_TCH_IM_C_TIMECODE_Pos             _U_(1)                                         /**< (SPW_TCH_IM_C) Time Code Position */
#define SPW_TCH_IM_C_TIMECODE_Msk             (_U_(0x1) << SPW_TCH_IM_C_TIMECODE_Pos)        /**< (SPW_TCH_IM_C) Time Code Mask */
#define SPW_TCH_IM_C_ANYTIMECODE_Pos          _U_(2)                                         /**< (SPW_TCH_IM_C) Any Time Code Position */
#define SPW_TCH_IM_C_ANYTIMECODE_Msk          (_U_(0x1) << SPW_TCH_IM_C_ANYTIMECODE_Pos)     /**< (SPW_TCH_IM_C) Any Time Code Mask */
#define SPW_TCH_IM_C_LATEWD_Pos               _U_(3)                                         /**< (SPW_TCH_IM_C) Late Watchdog Position */
#define SPW_TCH_IM_C_LATEWD_Msk               (_U_(0x1) << SPW_TCH_IM_C_LATEWD_Pos)          /**< (SPW_TCH_IM_C) Late Watchdog Mask */
#define SPW_TCH_IM_C_EARLYWD_Pos              _U_(4)                                         /**< (SPW_TCH_IM_C) Early Watchdog Position */
#define SPW_TCH_IM_C_EARLYWD_Msk              (_U_(0x1) << SPW_TCH_IM_C_EARLYWD_Pos)         /**< (SPW_TCH_IM_C) Early Watchdog Mask */
#define SPW_TCH_IM_C_Msk                      _U_(0x0000001F)                                /**< (SPW_TCH_IM_C) Register Mask  */


/* -------- SPW_TCH_CFGLISTEN : (SPW Offset: 0xEA0) (R/W 32) SpW Tch Config Listener -------- */
#define SPW_TCH_CFGLISTEN_L1_Pos              _U_(0)                                         /**< (SPW_TCH_CFGLISTEN) Listen  link 1 Position */
#define SPW_TCH_CFGLISTEN_L1_Msk              (_U_(0x1) << SPW_TCH_CFGLISTEN_L1_Pos)         /**< (SPW_TCH_CFGLISTEN) Listen  link 1 Mask */
#define SPW_TCH_CFGLISTEN_L2_Pos              _U_(1)                                         /**< (SPW_TCH_CFGLISTEN) Listen link 2 Position */
#define SPW_TCH_CFGLISTEN_L2_Msk              (_U_(0x1) << SPW_TCH_CFGLISTEN_L2_Pos)         /**< (SPW_TCH_CFGLISTEN) Listen link 2 Mask */
#define SPW_TCH_CFGLISTEN_Msk                 _U_(0x00000003)                                /**< (SPW_TCH_CFGLISTEN) Register Mask  */

#define SPW_TCH_CFGLISTEN_L_Pos               _U_(0)                                         /**< (SPW_TCH_CFGLISTEN Position) Listen link 2 */
#define SPW_TCH_CFGLISTEN_L_Msk               (_U_(0x3) << SPW_TCH_CFGLISTEN_L_Pos)          /**< (SPW_TCH_CFGLISTEN Mask) L */
#define SPW_TCH_CFGLISTEN_L(value)            (SPW_TCH_CFGLISTEN_L_Msk & ((value) << SPW_TCH_CFGLISTEN_L_Pos)) 

/* -------- SPW_TCH_CFGSEND : (SPW Offset: 0xEA4) (R/W 32) SpW Tch Config Sender -------- */
#define SPW_TCH_CFGSEND_S1_Pos                _U_(0)                                         /**< (SPW_TCH_CFGSEND) Send link 1 Position */
#define SPW_TCH_CFGSEND_S1_Msk                (_U_(0x1) << SPW_TCH_CFGSEND_S1_Pos)           /**< (SPW_TCH_CFGSEND) Send link 1 Mask */
#define SPW_TCH_CFGSEND_S2_Pos                _U_(1)                                         /**< (SPW_TCH_CFGSEND) Send link 2 Position */
#define SPW_TCH_CFGSEND_S2_Msk                (_U_(0x1) << SPW_TCH_CFGSEND_S2_Pos)           /**< (SPW_TCH_CFGSEND) Send link 2 Mask */
#define SPW_TCH_CFGSEND_Msk                   _U_(0x00000003)                                /**< (SPW_TCH_CFGSEND) Register Mask  */

#define SPW_TCH_CFGSEND_S_Pos                 _U_(0)                                         /**< (SPW_TCH_CFGSEND Position) Send link 2 */
#define SPW_TCH_CFGSEND_S_Msk                 (_U_(0x3) << SPW_TCH_CFGSEND_S_Pos)            /**< (SPW_TCH_CFGSEND Mask) S */
#define SPW_TCH_CFGSEND_S(value)              (SPW_TCH_CFGSEND_S_Msk & ((value) << SPW_TCH_CFGSEND_S_Pos)) 

/* -------- SPW_TCH_CFG : (SPW Offset: 0xEA8) (R/W 32) SpW Tch Config -------- */
#define SPW_TCH_CFG_EVENT_Pos                 _U_(0)                                         /**< (SPW_TCH_CFG) Event Position */
#define SPW_TCH_CFG_EVENT_Msk                 (_U_(0x3F) << SPW_TCH_CFG_EVENT_Pos)           /**< (SPW_TCH_CFG) Event Mask */
#define SPW_TCH_CFG_EVENT(value)              (SPW_TCH_CFG_EVENT_Msk & ((value) << SPW_TCH_CFG_EVENT_Pos))
#define SPW_TCH_CFG_Msk                       _U_(0x0000003F)                                /**< (SPW_TCH_CFG) Register Mask  */


/* -------- SPW_TCH_CFGRESTART : (SPW Offset: 0xEAC) (R/W 32) SpW Tch Config Restart -------- */
#define SPW_TCH_CFGRESTART_VALUE_Pos          _U_(0)                                         /**< (SPW_TCH_CFGRESTART) Value Position */
#define SPW_TCH_CFGRESTART_VALUE_Msk          (_U_(0x3F) << SPW_TCH_CFGRESTART_VALUE_Pos)    /**< (SPW_TCH_CFGRESTART) Value Mask */
#define SPW_TCH_CFGRESTART_VALUE(value)       (SPW_TCH_CFGRESTART_VALUE_Msk & ((value) << SPW_TCH_CFGRESTART_VALUE_Pos))
#define SPW_TCH_CFGRESTART_EVENT_Pos          _U_(8)                                         /**< (SPW_TCH_CFGRESTART) Event Position */
#define SPW_TCH_CFGRESTART_EVENT_Msk          (_U_(0x1) << SPW_TCH_CFGRESTART_EVENT_Pos)     /**< (SPW_TCH_CFGRESTART) Event Mask */
#define SPW_TCH_CFGRESTART_PPS_Pos            _U_(14)                                        /**< (SPW_TCH_CFGRESTART) Pps Position */
#define SPW_TCH_CFGRESTART_PPS_Msk            (_U_(0x1) << SPW_TCH_CFGRESTART_PPS_Pos)       /**< (SPW_TCH_CFGRESTART) Pps Mask */
#define SPW_TCH_CFGRESTART_ONESHOT_Pos        _U_(15)                                        /**< (SPW_TCH_CFGRESTART) One Shot Position */
#define SPW_TCH_CFGRESTART_ONESHOT_Msk        (_U_(0x1) << SPW_TCH_CFGRESTART_ONESHOT_Pos)   /**< (SPW_TCH_CFGRESTART) One Shot Mask */
#define SPW_TCH_CFGRESTART_Msk                _U_(0x0000C13F)                                /**< (SPW_TCH_CFGRESTART) Register Mask  */


/* -------- SPW_TCH_CFGTCEVENT : (SPW Offset: 0xEB0) (R/W 32) SpW Tch Config Tc Event -------- */
#define SPW_TCH_CFGTCEVENT_VALUE_Pos          _U_(0)                                         /**< (SPW_TCH_CFGTCEVENT) Value Position */
#define SPW_TCH_CFGTCEVENT_VALUE_Msk          (_U_(0x3F) << SPW_TCH_CFGTCEVENT_VALUE_Pos)    /**< (SPW_TCH_CFGTCEVENT) Value Mask */
#define SPW_TCH_CFGTCEVENT_VALUE(value)       (SPW_TCH_CFGTCEVENT_VALUE_Msk & ((value) << SPW_TCH_CFGTCEVENT_VALUE_Pos))
#define SPW_TCH_CFGTCEVENT_MASK_Pos           _U_(8)                                         /**< (SPW_TCH_CFGTCEVENT) Mask Position */
#define SPW_TCH_CFGTCEVENT_MASK_Msk           (_U_(0x3F) << SPW_TCH_CFGTCEVENT_MASK_Pos)     /**< (SPW_TCH_CFGTCEVENT) Mask Mask */
#define SPW_TCH_CFGTCEVENT_MASK(value)        (SPW_TCH_CFGTCEVENT_MASK_Msk & ((value) << SPW_TCH_CFGTCEVENT_MASK_Pos))
#define SPW_TCH_CFGTCEVENT_Msk                _U_(0x00003F3F)                                /**< (SPW_TCH_CFGTCEVENT) Register Mask  */


/* -------- SPW_TCH_CFGWD : (SPW Offset: 0xEB4) (R/W 32) SpW Tch Config Watchdog -------- */
#define SPW_TCH_CFGWD_LATE_Pos                _U_(0)                                         /**< (SPW_TCH_CFGWD) Late Position */
#define SPW_TCH_CFGWD_LATE_Msk                (_U_(0xFFFF) << SPW_TCH_CFGWD_LATE_Pos)        /**< (SPW_TCH_CFGWD) Late Mask */
#define SPW_TCH_CFGWD_LATE(value)             (SPW_TCH_CFGWD_LATE_Msk & ((value) << SPW_TCH_CFGWD_LATE_Pos))
#define SPW_TCH_CFGWD_EARLY_Pos               _U_(16)                                        /**< (SPW_TCH_CFGWD) Early Position */
#define SPW_TCH_CFGWD_EARLY_Msk               (_U_(0xFFFF) << SPW_TCH_CFGWD_EARLY_Pos)       /**< (SPW_TCH_CFGWD) Early Mask */
#define SPW_TCH_CFGWD_EARLY(value)            (SPW_TCH_CFGWD_EARLY_Msk & ((value) << SPW_TCH_CFGWD_EARLY_Pos))
#define SPW_TCH_CFGWD_Msk                     _U_(0xFFFFFFFF)                                /**< (SPW_TCH_CFGWD) Register Mask  */


/* -------- SPW_TCH_LASTTIMECODE : (SPW Offset: 0xEB8) (R/W 32) SpW Tch Last Time Code -------- */
#define SPW_TCH_LASTTIMECODE_VALUE_Pos        _U_(0)                                         /**< (SPW_TCH_LASTTIMECODE) Value Position */
#define SPW_TCH_LASTTIMECODE_VALUE_Msk        (_U_(0x3F) << SPW_TCH_LASTTIMECODE_VALUE_Pos)  /**< (SPW_TCH_LASTTIMECODE) Value Mask */
#define SPW_TCH_LASTTIMECODE_VALUE(value)     (SPW_TCH_LASTTIMECODE_VALUE_Msk & ((value) << SPW_TCH_LASTTIMECODE_VALUE_Pos))
#define SPW_TCH_LASTTIMECODE_SEND_Pos         _U_(8)                                         /**< (SPW_TCH_LASTTIMECODE) Send Now Position */
#define SPW_TCH_LASTTIMECODE_SEND_Msk         (_U_(0x1) << SPW_TCH_LASTTIMECODE_SEND_Pos)    /**< (SPW_TCH_LASTTIMECODE) Send Now Mask */
#define SPW_TCH_LASTTIMECODE_Msk              _U_(0x0000013F)                                /**< (SPW_TCH_LASTTIMECODE) Register Mask  */


/* -------- SPW_TCH_SWRESET : (SPW Offset: 0xEBC) (R/W 32) SpW Tch Software Reset -------- */
#define SPW_TCH_SWRESET_PATTERN_Pos           _U_(0)                                         /**< (SPW_TCH_SWRESET) Pattern Position */
#define SPW_TCH_SWRESET_PATTERN_Msk           (_U_(0xFFFFFFFF) << SPW_TCH_SWRESET_PATTERN_Pos) /**< (SPW_TCH_SWRESET) Pattern Mask */
#define SPW_TCH_SWRESET_PATTERN(value)        (SPW_TCH_SWRESET_PATTERN_Msk & ((value) << SPW_TCH_SWRESET_PATTERN_Pos))
#define SPW_TCH_SWRESET_Msk                   _U_(0xFFFFFFFF)                                /**< (SPW_TCH_SWRESET) Register Mask  */


/* -------- SPW_GROUP_IRQSTS1 : (SPW Offset: 0xF00) ( R/ 32) SpW Group Interrupt status 1 -------- */
#define SPW_GROUP_IRQSTS1_TX1_Pos             _U_(7)                                         /**< (SPW_GROUP_IRQSTS1) Tx 1 Position */
#define SPW_GROUP_IRQSTS1_TX1_Msk             (_U_(0x1) << SPW_GROUP_IRQSTS1_TX1_Pos)        /**< (SPW_GROUP_IRQSTS1) Tx 1 Mask */
#define SPW_GROUP_IRQSTS1_RX1_Pos             _U_(15)                                        /**< (SPW_GROUP_IRQSTS1) Rx 1 Position */
#define SPW_GROUP_IRQSTS1_RX1_Msk             (_U_(0x1) << SPW_GROUP_IRQSTS1_RX1_Pos)        /**< (SPW_GROUP_IRQSTS1) Rx 1 Mask */
#define SPW_GROUP_IRQSTS1_TCH_Pos             _U_(16)                                        /**< (SPW_GROUP_IRQSTS1) Time Code Handler Position */
#define SPW_GROUP_IRQSTS1_TCH_Msk             (_U_(0x1) << SPW_GROUP_IRQSTS1_TCH_Pos)        /**< (SPW_GROUP_IRQSTS1) Time Code Handler Mask */
#define SPW_GROUP_IRQSTS1_Msk                 _U_(0x00018080)                                /**< (SPW_GROUP_IRQSTS1) Register Mask  */

#define SPW_GROUP_IRQSTS1_TX_Pos              _U_(7)                                         /**< (SPW_GROUP_IRQSTS1 Position) Tx x */
#define SPW_GROUP_IRQSTS1_TX_Msk              (_U_(0x1) << SPW_GROUP_IRQSTS1_TX_Pos)         /**< (SPW_GROUP_IRQSTS1 Mask) TX */
#define SPW_GROUP_IRQSTS1_TX(value)           (SPW_GROUP_IRQSTS1_TX_Msk & ((value) << SPW_GROUP_IRQSTS1_TX_Pos)) 
#define SPW_GROUP_IRQSTS1_RX_Pos              _U_(15)                                        /**< (SPW_GROUP_IRQSTS1 Position) Rx x */
#define SPW_GROUP_IRQSTS1_RX_Msk              (_U_(0x1) << SPW_GROUP_IRQSTS1_RX_Pos)         /**< (SPW_GROUP_IRQSTS1 Mask) RX */
#define SPW_GROUP_IRQSTS1_RX(value)           (SPW_GROUP_IRQSTS1_RX_Msk & ((value) << SPW_GROUP_IRQSTS1_RX_Pos)) 

/* -------- SPW_GROUP_IRQSTS2 : (SPW Offset: 0xF04) ( R/ 32) SpW Group Interrupt status 2 -------- */
#define SPW_GROUP_IRQSTS2_Link2_Pos           _U_(18)                                        /**< (SPW_GROUP_IRQSTS2) Link 2 Position */
#define SPW_GROUP_IRQSTS2_Link2_Msk           (_U_(0x1) << SPW_GROUP_IRQSTS2_Link2_Pos)      /**< (SPW_GROUP_IRQSTS2) Link 2 Mask */
#define SPW_GROUP_IRQSTS2_Dia2_Pos            _U_(19)                                        /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt Acknowledge, Link 2 Position */
#define SPW_GROUP_IRQSTS2_Dia2_Msk            (_U_(0x1) << SPW_GROUP_IRQSTS2_Dia2_Pos)       /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt Acknowledge, Link 2 Mask */
#define SPW_GROUP_IRQSTS2_Di2_Pos             _U_(20)                                        /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt 2 Position */
#define SPW_GROUP_IRQSTS2_Di2_Msk             (_U_(0x1) << SPW_GROUP_IRQSTS2_Di2_Pos)        /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt 2 Mask */
#define SPW_GROUP_IRQSTS2_Link1_Pos           _U_(21)                                        /**< (SPW_GROUP_IRQSTS2) Link 1 Position */
#define SPW_GROUP_IRQSTS2_Link1_Msk           (_U_(0x1) << SPW_GROUP_IRQSTS2_Link1_Pos)      /**< (SPW_GROUP_IRQSTS2) Link 1 Mask */
#define SPW_GROUP_IRQSTS2_Dia1_Pos            _U_(22)                                        /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt Acknowledge, Link 1 Position */
#define SPW_GROUP_IRQSTS2_Dia1_Msk            (_U_(0x1) << SPW_GROUP_IRQSTS2_Dia1_Pos)       /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt Acknowledge, Link 1 Mask */
#define SPW_GROUP_IRQSTS2_Di1_Pos             _U_(23)                                        /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt 1 Position */
#define SPW_GROUP_IRQSTS2_Di1_Msk             (_U_(0x1) << SPW_GROUP_IRQSTS2_Di1_Pos)        /**< (SPW_GROUP_IRQSTS2) Distributed Interrupt 1 Mask */
#define SPW_GROUP_IRQSTS2_Msk                 _U_(0x00FC0000)                                /**< (SPW_GROUP_IRQSTS2) Register Mask  */


/* -------- SPW_GROUP_EDACSTS : (SPW Offset: 0xF08) ( R/ 32) SpW Group Interrupt status -------- */
#define SPW_GROUP_EDACSTS_CORR_Pos            _U_(0)                                         /**< (SPW_GROUP_EDACSTS) Correction Count Position */
#define SPW_GROUP_EDACSTS_CORR_Msk            (_U_(0xFF) << SPW_GROUP_EDACSTS_CORR_Pos)      /**< (SPW_GROUP_EDACSTS) Correction Count Mask */
#define SPW_GROUP_EDACSTS_CORR(value)         (SPW_GROUP_EDACSTS_CORR_Msk & ((value) << SPW_GROUP_EDACSTS_CORR_Pos))
#define SPW_GROUP_EDACSTS_UNCORR_Pos          _U_(8)                                         /**< (SPW_GROUP_EDACSTS) Uncorrectable Error Position */
#define SPW_GROUP_EDACSTS_UNCORR_Msk          (_U_(0xFF) << SPW_GROUP_EDACSTS_UNCORR_Pos)    /**< (SPW_GROUP_EDACSTS) Uncorrectable Error Mask */
#define SPW_GROUP_EDACSTS_UNCORR(value)       (SPW_GROUP_EDACSTS_UNCORR_Msk & ((value) << SPW_GROUP_EDACSTS_UNCORR_Pos))
#define SPW_GROUP_EDACSTS_Msk                 _U_(0x0000FFFF)                                /**< (SPW_GROUP_EDACSTS) Register Mask  */


/** \brief SPW register offsets definitions */
#define SPW_ROUTER_STS_REG_OFST        (0x00)         /**< (SPW_ROUTER_STS) SpW Router Status Offset */
#define SPW_ROUTER_CFG_REG_OFST        (0x04)         /**< (SPW_ROUTER_CFG) SpW Router Config Offset */
#define SPW_ROUTER_TIMEOUT_REG_OFST    (0x08)         /**< (SPW_ROUTER_TIMEOUT) SpW Router Timeout Offset */
#define SPW_ROUTER_TABLE0_REG_OFST     (0x80)         /**< (SPW_ROUTER_TABLE0) SpW Router Table (router_table_nb = 32) 0 Offset */
#define SPW_ROUTER_TABLE1_REG_OFST     (0x84)         /**< (SPW_ROUTER_TABLE1) SpW Router Table (router_table_nb = 32) 1 Offset */
#define SPW_ROUTER_TABLE2_REG_OFST     (0x88)         /**< (SPW_ROUTER_TABLE2) SpW Router Table (router_table_nb = 32) 2 Offset */
#define SPW_ROUTER_TABLE3_REG_OFST     (0x8C)         /**< (SPW_ROUTER_TABLE3) SpW Router Table (router_table_nb = 32) 3 Offset */
#define SPW_ROUTER_TABLE4_REG_OFST     (0x90)         /**< (SPW_ROUTER_TABLE4) SpW Router Table (router_table_nb = 32) 4 Offset */
#define SPW_ROUTER_TABLE5_REG_OFST     (0x94)         /**< (SPW_ROUTER_TABLE5) SpW Router Table (router_table_nb = 32) 5 Offset */
#define SPW_ROUTER_TABLE6_REG_OFST     (0x98)         /**< (SPW_ROUTER_TABLE6) SpW Router Table (router_table_nb = 32) 6 Offset */
#define SPW_ROUTER_TABLE7_REG_OFST     (0x9C)         /**< (SPW_ROUTER_TABLE7) SpW Router Table (router_table_nb = 32) 7 Offset */
#define SPW_ROUTER_TABLE8_REG_OFST     (0xA0)         /**< (SPW_ROUTER_TABLE8) SpW Router Table (router_table_nb = 32) 8 Offset */
#define SPW_ROUTER_TABLE9_REG_OFST     (0xA4)         /**< (SPW_ROUTER_TABLE9) SpW Router Table (router_table_nb = 32) 9 Offset */
#define SPW_ROUTER_TABLE10_REG_OFST    (0xA8)         /**< (SPW_ROUTER_TABLE10) SpW Router Table (router_table_nb = 32) 10 Offset */
#define SPW_ROUTER_TABLE11_REG_OFST    (0xAC)         /**< (SPW_ROUTER_TABLE11) SpW Router Table (router_table_nb = 32) 11 Offset */
#define SPW_ROUTER_TABLE12_REG_OFST    (0xB0)         /**< (SPW_ROUTER_TABLE12) SpW Router Table (router_table_nb = 32) 12 Offset */
#define SPW_ROUTER_TABLE13_REG_OFST    (0xB4)         /**< (SPW_ROUTER_TABLE13) SpW Router Table (router_table_nb = 32) 13 Offset */
#define SPW_ROUTER_TABLE14_REG_OFST    (0xB8)         /**< (SPW_ROUTER_TABLE14) SpW Router Table (router_table_nb = 32) 14 Offset */
#define SPW_ROUTER_TABLE15_REG_OFST    (0xBC)         /**< (SPW_ROUTER_TABLE15) SpW Router Table (router_table_nb = 32) 15 Offset */
#define SPW_ROUTER_TABLE16_REG_OFST    (0xC0)         /**< (SPW_ROUTER_TABLE16) SpW Router Table (router_table_nb = 32) 16 Offset */
#define SPW_ROUTER_TABLE17_REG_OFST    (0xC4)         /**< (SPW_ROUTER_TABLE17) SpW Router Table (router_table_nb = 32) 17 Offset */
#define SPW_ROUTER_TABLE18_REG_OFST    (0xC8)         /**< (SPW_ROUTER_TABLE18) SpW Router Table (router_table_nb = 32) 18 Offset */
#define SPW_ROUTER_TABLE19_REG_OFST    (0xCC)         /**< (SPW_ROUTER_TABLE19) SpW Router Table (router_table_nb = 32) 19 Offset */
#define SPW_ROUTER_TABLE20_REG_OFST    (0xD0)         /**< (SPW_ROUTER_TABLE20) SpW Router Table (router_table_nb = 32) 20 Offset */
#define SPW_ROUTER_TABLE21_REG_OFST    (0xD4)         /**< (SPW_ROUTER_TABLE21) SpW Router Table (router_table_nb = 32) 21 Offset */
#define SPW_ROUTER_TABLE22_REG_OFST    (0xD8)         /**< (SPW_ROUTER_TABLE22) SpW Router Table (router_table_nb = 32) 22 Offset */
#define SPW_ROUTER_TABLE23_REG_OFST    (0xDC)         /**< (SPW_ROUTER_TABLE23) SpW Router Table (router_table_nb = 32) 23 Offset */
#define SPW_ROUTER_TABLE24_REG_OFST    (0xE0)         /**< (SPW_ROUTER_TABLE24) SpW Router Table (router_table_nb = 32) 24 Offset */
#define SPW_ROUTER_TABLE25_REG_OFST    (0xE4)         /**< (SPW_ROUTER_TABLE25) SpW Router Table (router_table_nb = 32) 25 Offset */
#define SPW_ROUTER_TABLE26_REG_OFST    (0xE8)         /**< (SPW_ROUTER_TABLE26) SpW Router Table (router_table_nb = 32) 26 Offset */
#define SPW_ROUTER_TABLE27_REG_OFST    (0xEC)         /**< (SPW_ROUTER_TABLE27) SpW Router Table (router_table_nb = 32) 27 Offset */
#define SPW_ROUTER_TABLE28_REG_OFST    (0xF0)         /**< (SPW_ROUTER_TABLE28) SpW Router Table (router_table_nb = 32) 28 Offset */
#define SPW_ROUTER_TABLE29_REG_OFST    (0xF4)         /**< (SPW_ROUTER_TABLE29) SpW Router Table (router_table_nb = 32) 29 Offset */
#define SPW_ROUTER_TABLE30_REG_OFST    (0xF8)         /**< (SPW_ROUTER_TABLE30) SpW Router Table (router_table_nb = 32) 30 Offset */
#define SPW_ROUTER_TABLE31_REG_OFST    (0xFC)         /**< (SPW_ROUTER_TABLE31) SpW Router Table (router_table_nb = 32) 31 Offset */
#define SPW_ROUTER_TABLE32_REG_OFST    (0x100)        /**< (SPW_ROUTER_TABLE32) SpW Router Table (router_table_nb = 32) 32 Offset */
#define SPW_ROUTER_TABLE33_REG_OFST    (0x104)        /**< (SPW_ROUTER_TABLE33) SpW Router Table (router_table_nb = 32) 33 Offset */
#define SPW_ROUTER_TABLE34_REG_OFST    (0x108)        /**< (SPW_ROUTER_TABLE34) SpW Router Table (router_table_nb = 32) 34 Offset */
#define SPW_ROUTER_TABLE35_REG_OFST    (0x10C)        /**< (SPW_ROUTER_TABLE35) SpW Router Table (router_table_nb = 32) 35 Offset */
#define SPW_ROUTER_TABLE36_REG_OFST    (0x110)        /**< (SPW_ROUTER_TABLE36) SpW Router Table (router_table_nb = 32) 36 Offset */
#define SPW_ROUTER_TABLE37_REG_OFST    (0x114)        /**< (SPW_ROUTER_TABLE37) SpW Router Table (router_table_nb = 32) 37 Offset */
#define SPW_ROUTER_TABLE38_REG_OFST    (0x118)        /**< (SPW_ROUTER_TABLE38) SpW Router Table (router_table_nb = 32) 38 Offset */
#define SPW_ROUTER_TABLE39_REG_OFST    (0x11C)        /**< (SPW_ROUTER_TABLE39) SpW Router Table (router_table_nb = 32) 39 Offset */
#define SPW_ROUTER_TABLE40_REG_OFST    (0x120)        /**< (SPW_ROUTER_TABLE40) SpW Router Table (router_table_nb = 32) 40 Offset */
#define SPW_ROUTER_TABLE41_REG_OFST    (0x124)        /**< (SPW_ROUTER_TABLE41) SpW Router Table (router_table_nb = 32) 41 Offset */
#define SPW_ROUTER_TABLE42_REG_OFST    (0x128)        /**< (SPW_ROUTER_TABLE42) SpW Router Table (router_table_nb = 32) 42 Offset */
#define SPW_ROUTER_TABLE43_REG_OFST    (0x12C)        /**< (SPW_ROUTER_TABLE43) SpW Router Table (router_table_nb = 32) 43 Offset */
#define SPW_ROUTER_TABLE44_REG_OFST    (0x130)        /**< (SPW_ROUTER_TABLE44) SpW Router Table (router_table_nb = 32) 44 Offset */
#define SPW_ROUTER_TABLE45_REG_OFST    (0x134)        /**< (SPW_ROUTER_TABLE45) SpW Router Table (router_table_nb = 32) 45 Offset */
#define SPW_ROUTER_TABLE46_REG_OFST    (0x138)        /**< (SPW_ROUTER_TABLE46) SpW Router Table (router_table_nb = 32) 46 Offset */
#define SPW_ROUTER_TABLE47_REG_OFST    (0x13C)        /**< (SPW_ROUTER_TABLE47) SpW Router Table (router_table_nb = 32) 47 Offset */
#define SPW_ROUTER_TABLE48_REG_OFST    (0x140)        /**< (SPW_ROUTER_TABLE48) SpW Router Table (router_table_nb = 32) 48 Offset */
#define SPW_ROUTER_TABLE49_REG_OFST    (0x144)        /**< (SPW_ROUTER_TABLE49) SpW Router Table (router_table_nb = 32) 49 Offset */
#define SPW_ROUTER_TABLE50_REG_OFST    (0x148)        /**< (SPW_ROUTER_TABLE50) SpW Router Table (router_table_nb = 32) 50 Offset */
#define SPW_ROUTER_TABLE51_REG_OFST    (0x14C)        /**< (SPW_ROUTER_TABLE51) SpW Router Table (router_table_nb = 32) 51 Offset */
#define SPW_ROUTER_TABLE52_REG_OFST    (0x150)        /**< (SPW_ROUTER_TABLE52) SpW Router Table (router_table_nb = 32) 52 Offset */
#define SPW_ROUTER_TABLE53_REG_OFST    (0x154)        /**< (SPW_ROUTER_TABLE53) SpW Router Table (router_table_nb = 32) 53 Offset */
#define SPW_ROUTER_TABLE54_REG_OFST    (0x158)        /**< (SPW_ROUTER_TABLE54) SpW Router Table (router_table_nb = 32) 54 Offset */
#define SPW_ROUTER_TABLE55_REG_OFST    (0x15C)        /**< (SPW_ROUTER_TABLE55) SpW Router Table (router_table_nb = 32) 55 Offset */
#define SPW_ROUTER_TABLE56_REG_OFST    (0x160)        /**< (SPW_ROUTER_TABLE56) SpW Router Table (router_table_nb = 32) 56 Offset */
#define SPW_ROUTER_TABLE57_REG_OFST    (0x164)        /**< (SPW_ROUTER_TABLE57) SpW Router Table (router_table_nb = 32) 57 Offset */
#define SPW_ROUTER_TABLE58_REG_OFST    (0x168)        /**< (SPW_ROUTER_TABLE58) SpW Router Table (router_table_nb = 32) 58 Offset */
#define SPW_ROUTER_TABLE59_REG_OFST    (0x16C)        /**< (SPW_ROUTER_TABLE59) SpW Router Table (router_table_nb = 32) 59 Offset */
#define SPW_ROUTER_TABLE60_REG_OFST    (0x170)        /**< (SPW_ROUTER_TABLE60) SpW Router Table (router_table_nb = 32) 60 Offset */
#define SPW_ROUTER_TABLE61_REG_OFST    (0x174)        /**< (SPW_ROUTER_TABLE61) SpW Router Table (router_table_nb = 32) 61 Offset */
#define SPW_ROUTER_TABLE62_REG_OFST    (0x178)        /**< (SPW_ROUTER_TABLE62) SpW Router Table (router_table_nb = 32) 62 Offset */
#define SPW_ROUTER_TABLE63_REG_OFST    (0x17C)        /**< (SPW_ROUTER_TABLE63) SpW Router Table (router_table_nb = 32) 63 Offset */
#define SPW_ROUTER_TABLE64_REG_OFST    (0x180)        /**< (SPW_ROUTER_TABLE64) SpW Router Table (router_table_nb = 32) 64 Offset */
#define SPW_ROUTER_TABLE65_REG_OFST    (0x184)        /**< (SPW_ROUTER_TABLE65) SpW Router Table (router_table_nb = 32) 65 Offset */
#define SPW_ROUTER_TABLE66_REG_OFST    (0x188)        /**< (SPW_ROUTER_TABLE66) SpW Router Table (router_table_nb = 32) 66 Offset */
#define SPW_ROUTER_TABLE67_REG_OFST    (0x18C)        /**< (SPW_ROUTER_TABLE67) SpW Router Table (router_table_nb = 32) 67 Offset */
#define SPW_ROUTER_TABLE68_REG_OFST    (0x190)        /**< (SPW_ROUTER_TABLE68) SpW Router Table (router_table_nb = 32) 68 Offset */
#define SPW_ROUTER_TABLE69_REG_OFST    (0x194)        /**< (SPW_ROUTER_TABLE69) SpW Router Table (router_table_nb = 32) 69 Offset */
#define SPW_ROUTER_TABLE70_REG_OFST    (0x198)        /**< (SPW_ROUTER_TABLE70) SpW Router Table (router_table_nb = 32) 70 Offset */
#define SPW_ROUTER_TABLE71_REG_OFST    (0x19C)        /**< (SPW_ROUTER_TABLE71) SpW Router Table (router_table_nb = 32) 71 Offset */
#define SPW_ROUTER_TABLE72_REG_OFST    (0x1A0)        /**< (SPW_ROUTER_TABLE72) SpW Router Table (router_table_nb = 32) 72 Offset */
#define SPW_ROUTER_TABLE73_REG_OFST    (0x1A4)        /**< (SPW_ROUTER_TABLE73) SpW Router Table (router_table_nb = 32) 73 Offset */
#define SPW_ROUTER_TABLE74_REG_OFST    (0x1A8)        /**< (SPW_ROUTER_TABLE74) SpW Router Table (router_table_nb = 32) 74 Offset */
#define SPW_ROUTER_TABLE75_REG_OFST    (0x1AC)        /**< (SPW_ROUTER_TABLE75) SpW Router Table (router_table_nb = 32) 75 Offset */
#define SPW_ROUTER_TABLE76_REG_OFST    (0x1B0)        /**< (SPW_ROUTER_TABLE76) SpW Router Table (router_table_nb = 32) 76 Offset */
#define SPW_ROUTER_TABLE77_REG_OFST    (0x1B4)        /**< (SPW_ROUTER_TABLE77) SpW Router Table (router_table_nb = 32) 77 Offset */
#define SPW_ROUTER_TABLE78_REG_OFST    (0x1B8)        /**< (SPW_ROUTER_TABLE78) SpW Router Table (router_table_nb = 32) 78 Offset */
#define SPW_ROUTER_TABLE79_REG_OFST    (0x1BC)        /**< (SPW_ROUTER_TABLE79) SpW Router Table (router_table_nb = 32) 79 Offset */
#define SPW_ROUTER_TABLE80_REG_OFST    (0x1C0)        /**< (SPW_ROUTER_TABLE80) SpW Router Table (router_table_nb = 32) 80 Offset */
#define SPW_ROUTER_TABLE81_REG_OFST    (0x1C4)        /**< (SPW_ROUTER_TABLE81) SpW Router Table (router_table_nb = 32) 81 Offset */
#define SPW_ROUTER_TABLE82_REG_OFST    (0x1C8)        /**< (SPW_ROUTER_TABLE82) SpW Router Table (router_table_nb = 32) 82 Offset */
#define SPW_ROUTER_TABLE83_REG_OFST    (0x1CC)        /**< (SPW_ROUTER_TABLE83) SpW Router Table (router_table_nb = 32) 83 Offset */
#define SPW_ROUTER_TABLE84_REG_OFST    (0x1D0)        /**< (SPW_ROUTER_TABLE84) SpW Router Table (router_table_nb = 32) 84 Offset */
#define SPW_ROUTER_TABLE85_REG_OFST    (0x1D4)        /**< (SPW_ROUTER_TABLE85) SpW Router Table (router_table_nb = 32) 85 Offset */
#define SPW_ROUTER_TABLE86_REG_OFST    (0x1D8)        /**< (SPW_ROUTER_TABLE86) SpW Router Table (router_table_nb = 32) 86 Offset */
#define SPW_ROUTER_TABLE87_REG_OFST    (0x1DC)        /**< (SPW_ROUTER_TABLE87) SpW Router Table (router_table_nb = 32) 87 Offset */
#define SPW_ROUTER_TABLE88_REG_OFST    (0x1E0)        /**< (SPW_ROUTER_TABLE88) SpW Router Table (router_table_nb = 32) 88 Offset */
#define SPW_ROUTER_TABLE89_REG_OFST    (0x1E4)        /**< (SPW_ROUTER_TABLE89) SpW Router Table (router_table_nb = 32) 89 Offset */
#define SPW_ROUTER_TABLE90_REG_OFST    (0x1E8)        /**< (SPW_ROUTER_TABLE90) SpW Router Table (router_table_nb = 32) 90 Offset */
#define SPW_ROUTER_TABLE91_REG_OFST    (0x1EC)        /**< (SPW_ROUTER_TABLE91) SpW Router Table (router_table_nb = 32) 91 Offset */
#define SPW_ROUTER_TABLE92_REG_OFST    (0x1F0)        /**< (SPW_ROUTER_TABLE92) SpW Router Table (router_table_nb = 32) 92 Offset */
#define SPW_ROUTER_TABLE93_REG_OFST    (0x1F4)        /**< (SPW_ROUTER_TABLE93) SpW Router Table (router_table_nb = 32) 93 Offset */
#define SPW_ROUTER_TABLE94_REG_OFST    (0x1F8)        /**< (SPW_ROUTER_TABLE94) SpW Router Table (router_table_nb = 32) 94 Offset */
#define SPW_ROUTER_TABLE95_REG_OFST    (0x1FC)        /**< (SPW_ROUTER_TABLE95) SpW Router Table (router_table_nb = 32) 95 Offset */
#define SPW_ROUTER_TABLE96_REG_OFST    (0x200)        /**< (SPW_ROUTER_TABLE96) SpW Router Table (router_table_nb = 32) 96 Offset */
#define SPW_ROUTER_TABLE97_REG_OFST    (0x204)        /**< (SPW_ROUTER_TABLE97) SpW Router Table (router_table_nb = 32) 97 Offset */
#define SPW_ROUTER_TABLE98_REG_OFST    (0x208)        /**< (SPW_ROUTER_TABLE98) SpW Router Table (router_table_nb = 32) 98 Offset */
#define SPW_ROUTER_TABLE99_REG_OFST    (0x20C)        /**< (SPW_ROUTER_TABLE99) SpW Router Table (router_table_nb = 32) 99 Offset */
#define SPW_ROUTER_TABLE100_REG_OFST   (0x210)        /**< (SPW_ROUTER_TABLE100) SpW Router Table (router_table_nb = 32) 100 Offset */
#define SPW_ROUTER_TABLE101_REG_OFST   (0x214)        /**< (SPW_ROUTER_TABLE101) SpW Router Table (router_table_nb = 32) 101 Offset */
#define SPW_ROUTER_TABLE102_REG_OFST   (0x218)        /**< (SPW_ROUTER_TABLE102) SpW Router Table (router_table_nb = 32) 102 Offset */
#define SPW_ROUTER_TABLE103_REG_OFST   (0x21C)        /**< (SPW_ROUTER_TABLE103) SpW Router Table (router_table_nb = 32) 103 Offset */
#define SPW_ROUTER_TABLE104_REG_OFST   (0x220)        /**< (SPW_ROUTER_TABLE104) SpW Router Table (router_table_nb = 32) 104 Offset */
#define SPW_ROUTER_TABLE105_REG_OFST   (0x224)        /**< (SPW_ROUTER_TABLE105) SpW Router Table (router_table_nb = 32) 105 Offset */
#define SPW_ROUTER_TABLE106_REG_OFST   (0x228)        /**< (SPW_ROUTER_TABLE106) SpW Router Table (router_table_nb = 32) 106 Offset */
#define SPW_ROUTER_TABLE107_REG_OFST   (0x22C)        /**< (SPW_ROUTER_TABLE107) SpW Router Table (router_table_nb = 32) 107 Offset */
#define SPW_ROUTER_TABLE108_REG_OFST   (0x230)        /**< (SPW_ROUTER_TABLE108) SpW Router Table (router_table_nb = 32) 108 Offset */
#define SPW_ROUTER_TABLE109_REG_OFST   (0x234)        /**< (SPW_ROUTER_TABLE109) SpW Router Table (router_table_nb = 32) 109 Offset */
#define SPW_ROUTER_TABLE110_REG_OFST   (0x238)        /**< (SPW_ROUTER_TABLE110) SpW Router Table (router_table_nb = 32) 110 Offset */
#define SPW_ROUTER_TABLE111_REG_OFST   (0x23C)        /**< (SPW_ROUTER_TABLE111) SpW Router Table (router_table_nb = 32) 111 Offset */
#define SPW_ROUTER_TABLE112_REG_OFST   (0x240)        /**< (SPW_ROUTER_TABLE112) SpW Router Table (router_table_nb = 32) 112 Offset */
#define SPW_ROUTER_TABLE113_REG_OFST   (0x244)        /**< (SPW_ROUTER_TABLE113) SpW Router Table (router_table_nb = 32) 113 Offset */
#define SPW_ROUTER_TABLE114_REG_OFST   (0x248)        /**< (SPW_ROUTER_TABLE114) SpW Router Table (router_table_nb = 32) 114 Offset */
#define SPW_ROUTER_TABLE115_REG_OFST   (0x24C)        /**< (SPW_ROUTER_TABLE115) SpW Router Table (router_table_nb = 32) 115 Offset */
#define SPW_ROUTER_TABLE116_REG_OFST   (0x250)        /**< (SPW_ROUTER_TABLE116) SpW Router Table (router_table_nb = 32) 116 Offset */
#define SPW_ROUTER_TABLE117_REG_OFST   (0x254)        /**< (SPW_ROUTER_TABLE117) SpW Router Table (router_table_nb = 32) 117 Offset */
#define SPW_ROUTER_TABLE118_REG_OFST   (0x258)        /**< (SPW_ROUTER_TABLE118) SpW Router Table (router_table_nb = 32) 118 Offset */
#define SPW_ROUTER_TABLE119_REG_OFST   (0x25C)        /**< (SPW_ROUTER_TABLE119) SpW Router Table (router_table_nb = 32) 119 Offset */
#define SPW_ROUTER_TABLE120_REG_OFST   (0x260)        /**< (SPW_ROUTER_TABLE120) SpW Router Table (router_table_nb = 32) 120 Offset */
#define SPW_ROUTER_TABLE121_REG_OFST   (0x264)        /**< (SPW_ROUTER_TABLE121) SpW Router Table (router_table_nb = 32) 121 Offset */
#define SPW_ROUTER_TABLE122_REG_OFST   (0x268)        /**< (SPW_ROUTER_TABLE122) SpW Router Table (router_table_nb = 32) 122 Offset */
#define SPW_ROUTER_TABLE123_REG_OFST   (0x26C)        /**< (SPW_ROUTER_TABLE123) SpW Router Table (router_table_nb = 32) 123 Offset */
#define SPW_ROUTER_TABLE124_REG_OFST   (0x270)        /**< (SPW_ROUTER_TABLE124) SpW Router Table (router_table_nb = 32) 124 Offset */
#define SPW_ROUTER_TABLE125_REG_OFST   (0x274)        /**< (SPW_ROUTER_TABLE125) SpW Router Table (router_table_nb = 32) 125 Offset */
#define SPW_ROUTER_TABLE126_REG_OFST   (0x278)        /**< (SPW_ROUTER_TABLE126) SpW Router Table (router_table_nb = 32) 126 Offset */
#define SPW_ROUTER_TABLE127_REG_OFST   (0x27C)        /**< (SPW_ROUTER_TABLE127) SpW Router Table (router_table_nb = 32) 127 Offset */
#define SPW_ROUTER_TABLE128_REG_OFST   (0x280)        /**< (SPW_ROUTER_TABLE128) SpW Router Table (router_table_nb = 32) 128 Offset */
#define SPW_ROUTER_TABLE129_REG_OFST   (0x284)        /**< (SPW_ROUTER_TABLE129) SpW Router Table (router_table_nb = 32) 129 Offset */
#define SPW_ROUTER_TABLE130_REG_OFST   (0x288)        /**< (SPW_ROUTER_TABLE130) SpW Router Table (router_table_nb = 32) 130 Offset */
#define SPW_ROUTER_TABLE131_REG_OFST   (0x28C)        /**< (SPW_ROUTER_TABLE131) SpW Router Table (router_table_nb = 32) 131 Offset */
#define SPW_ROUTER_TABLE132_REG_OFST   (0x290)        /**< (SPW_ROUTER_TABLE132) SpW Router Table (router_table_nb = 32) 132 Offset */
#define SPW_ROUTER_TABLE133_REG_OFST   (0x294)        /**< (SPW_ROUTER_TABLE133) SpW Router Table (router_table_nb = 32) 133 Offset */
#define SPW_ROUTER_TABLE134_REG_OFST   (0x298)        /**< (SPW_ROUTER_TABLE134) SpW Router Table (router_table_nb = 32) 134 Offset */
#define SPW_ROUTER_TABLE135_REG_OFST   (0x29C)        /**< (SPW_ROUTER_TABLE135) SpW Router Table (router_table_nb = 32) 135 Offset */
#define SPW_ROUTER_TABLE136_REG_OFST   (0x2A0)        /**< (SPW_ROUTER_TABLE136) SpW Router Table (router_table_nb = 32) 136 Offset */
#define SPW_ROUTER_TABLE137_REG_OFST   (0x2A4)        /**< (SPW_ROUTER_TABLE137) SpW Router Table (router_table_nb = 32) 137 Offset */
#define SPW_ROUTER_TABLE138_REG_OFST   (0x2A8)        /**< (SPW_ROUTER_TABLE138) SpW Router Table (router_table_nb = 32) 138 Offset */
#define SPW_ROUTER_TABLE139_REG_OFST   (0x2AC)        /**< (SPW_ROUTER_TABLE139) SpW Router Table (router_table_nb = 32) 139 Offset */
#define SPW_ROUTER_TABLE140_REG_OFST   (0x2B0)        /**< (SPW_ROUTER_TABLE140) SpW Router Table (router_table_nb = 32) 140 Offset */
#define SPW_ROUTER_TABLE141_REG_OFST   (0x2B4)        /**< (SPW_ROUTER_TABLE141) SpW Router Table (router_table_nb = 32) 141 Offset */
#define SPW_ROUTER_TABLE142_REG_OFST   (0x2B8)        /**< (SPW_ROUTER_TABLE142) SpW Router Table (router_table_nb = 32) 142 Offset */
#define SPW_ROUTER_TABLE143_REG_OFST   (0x2BC)        /**< (SPW_ROUTER_TABLE143) SpW Router Table (router_table_nb = 32) 143 Offset */
#define SPW_ROUTER_TABLE144_REG_OFST   (0x2C0)        /**< (SPW_ROUTER_TABLE144) SpW Router Table (router_table_nb = 32) 144 Offset */
#define SPW_ROUTER_TABLE145_REG_OFST   (0x2C4)        /**< (SPW_ROUTER_TABLE145) SpW Router Table (router_table_nb = 32) 145 Offset */
#define SPW_ROUTER_TABLE146_REG_OFST   (0x2C8)        /**< (SPW_ROUTER_TABLE146) SpW Router Table (router_table_nb = 32) 146 Offset */
#define SPW_ROUTER_TABLE147_REG_OFST   (0x2CC)        /**< (SPW_ROUTER_TABLE147) SpW Router Table (router_table_nb = 32) 147 Offset */
#define SPW_ROUTER_TABLE148_REG_OFST   (0x2D0)        /**< (SPW_ROUTER_TABLE148) SpW Router Table (router_table_nb = 32) 148 Offset */
#define SPW_ROUTER_TABLE149_REG_OFST   (0x2D4)        /**< (SPW_ROUTER_TABLE149) SpW Router Table (router_table_nb = 32) 149 Offset */
#define SPW_ROUTER_TABLE150_REG_OFST   (0x2D8)        /**< (SPW_ROUTER_TABLE150) SpW Router Table (router_table_nb = 32) 150 Offset */
#define SPW_ROUTER_TABLE151_REG_OFST   (0x2DC)        /**< (SPW_ROUTER_TABLE151) SpW Router Table (router_table_nb = 32) 151 Offset */
#define SPW_ROUTER_TABLE152_REG_OFST   (0x2E0)        /**< (SPW_ROUTER_TABLE152) SpW Router Table (router_table_nb = 32) 152 Offset */
#define SPW_ROUTER_TABLE153_REG_OFST   (0x2E4)        /**< (SPW_ROUTER_TABLE153) SpW Router Table (router_table_nb = 32) 153 Offset */
#define SPW_ROUTER_TABLE154_REG_OFST   (0x2E8)        /**< (SPW_ROUTER_TABLE154) SpW Router Table (router_table_nb = 32) 154 Offset */
#define SPW_ROUTER_TABLE155_REG_OFST   (0x2EC)        /**< (SPW_ROUTER_TABLE155) SpW Router Table (router_table_nb = 32) 155 Offset */
#define SPW_ROUTER_TABLE156_REG_OFST   (0x2F0)        /**< (SPW_ROUTER_TABLE156) SpW Router Table (router_table_nb = 32) 156 Offset */
#define SPW_ROUTER_TABLE157_REG_OFST   (0x2F4)        /**< (SPW_ROUTER_TABLE157) SpW Router Table (router_table_nb = 32) 157 Offset */
#define SPW_ROUTER_TABLE158_REG_OFST   (0x2F8)        /**< (SPW_ROUTER_TABLE158) SpW Router Table (router_table_nb = 32) 158 Offset */
#define SPW_ROUTER_TABLE159_REG_OFST   (0x2FC)        /**< (SPW_ROUTER_TABLE159) SpW Router Table (router_table_nb = 32) 159 Offset */
#define SPW_ROUTER_TABLE160_REG_OFST   (0x300)        /**< (SPW_ROUTER_TABLE160) SpW Router Table (router_table_nb = 32) 160 Offset */
#define SPW_ROUTER_TABLE161_REG_OFST   (0x304)        /**< (SPW_ROUTER_TABLE161) SpW Router Table (router_table_nb = 32) 161 Offset */
#define SPW_ROUTER_TABLE162_REG_OFST   (0x308)        /**< (SPW_ROUTER_TABLE162) SpW Router Table (router_table_nb = 32) 162 Offset */
#define SPW_ROUTER_TABLE163_REG_OFST   (0x30C)        /**< (SPW_ROUTER_TABLE163) SpW Router Table (router_table_nb = 32) 163 Offset */
#define SPW_ROUTER_TABLE164_REG_OFST   (0x310)        /**< (SPW_ROUTER_TABLE164) SpW Router Table (router_table_nb = 32) 164 Offset */
#define SPW_ROUTER_TABLE165_REG_OFST   (0x314)        /**< (SPW_ROUTER_TABLE165) SpW Router Table (router_table_nb = 32) 165 Offset */
#define SPW_ROUTER_TABLE166_REG_OFST   (0x318)        /**< (SPW_ROUTER_TABLE166) SpW Router Table (router_table_nb = 32) 166 Offset */
#define SPW_ROUTER_TABLE167_REG_OFST   (0x31C)        /**< (SPW_ROUTER_TABLE167) SpW Router Table (router_table_nb = 32) 167 Offset */
#define SPW_ROUTER_TABLE168_REG_OFST   (0x320)        /**< (SPW_ROUTER_TABLE168) SpW Router Table (router_table_nb = 32) 168 Offset */
#define SPW_ROUTER_TABLE169_REG_OFST   (0x324)        /**< (SPW_ROUTER_TABLE169) SpW Router Table (router_table_nb = 32) 169 Offset */
#define SPW_ROUTER_TABLE170_REG_OFST   (0x328)        /**< (SPW_ROUTER_TABLE170) SpW Router Table (router_table_nb = 32) 170 Offset */
#define SPW_ROUTER_TABLE171_REG_OFST   (0x32C)        /**< (SPW_ROUTER_TABLE171) SpW Router Table (router_table_nb = 32) 171 Offset */
#define SPW_ROUTER_TABLE172_REG_OFST   (0x330)        /**< (SPW_ROUTER_TABLE172) SpW Router Table (router_table_nb = 32) 172 Offset */
#define SPW_ROUTER_TABLE173_REG_OFST   (0x334)        /**< (SPW_ROUTER_TABLE173) SpW Router Table (router_table_nb = 32) 173 Offset */
#define SPW_ROUTER_TABLE174_REG_OFST   (0x338)        /**< (SPW_ROUTER_TABLE174) SpW Router Table (router_table_nb = 32) 174 Offset */
#define SPW_ROUTER_TABLE175_REG_OFST   (0x33C)        /**< (SPW_ROUTER_TABLE175) SpW Router Table (router_table_nb = 32) 175 Offset */
#define SPW_ROUTER_TABLE176_REG_OFST   (0x340)        /**< (SPW_ROUTER_TABLE176) SpW Router Table (router_table_nb = 32) 176 Offset */
#define SPW_ROUTER_TABLE177_REG_OFST   (0x344)        /**< (SPW_ROUTER_TABLE177) SpW Router Table (router_table_nb = 32) 177 Offset */
#define SPW_ROUTER_TABLE178_REG_OFST   (0x348)        /**< (SPW_ROUTER_TABLE178) SpW Router Table (router_table_nb = 32) 178 Offset */
#define SPW_ROUTER_TABLE179_REG_OFST   (0x34C)        /**< (SPW_ROUTER_TABLE179) SpW Router Table (router_table_nb = 32) 179 Offset */
#define SPW_ROUTER_TABLE180_REG_OFST   (0x350)        /**< (SPW_ROUTER_TABLE180) SpW Router Table (router_table_nb = 32) 180 Offset */
#define SPW_ROUTER_TABLE181_REG_OFST   (0x354)        /**< (SPW_ROUTER_TABLE181) SpW Router Table (router_table_nb = 32) 181 Offset */
#define SPW_ROUTER_TABLE182_REG_OFST   (0x358)        /**< (SPW_ROUTER_TABLE182) SpW Router Table (router_table_nb = 32) 182 Offset */
#define SPW_ROUTER_TABLE183_REG_OFST   (0x35C)        /**< (SPW_ROUTER_TABLE183) SpW Router Table (router_table_nb = 32) 183 Offset */
#define SPW_ROUTER_TABLE184_REG_OFST   (0x360)        /**< (SPW_ROUTER_TABLE184) SpW Router Table (router_table_nb = 32) 184 Offset */
#define SPW_ROUTER_TABLE185_REG_OFST   (0x364)        /**< (SPW_ROUTER_TABLE185) SpW Router Table (router_table_nb = 32) 185 Offset */
#define SPW_ROUTER_TABLE186_REG_OFST   (0x368)        /**< (SPW_ROUTER_TABLE186) SpW Router Table (router_table_nb = 32) 186 Offset */
#define SPW_ROUTER_TABLE187_REG_OFST   (0x36C)        /**< (SPW_ROUTER_TABLE187) SpW Router Table (router_table_nb = 32) 187 Offset */
#define SPW_ROUTER_TABLE188_REG_OFST   (0x370)        /**< (SPW_ROUTER_TABLE188) SpW Router Table (router_table_nb = 32) 188 Offset */
#define SPW_ROUTER_TABLE189_REG_OFST   (0x374)        /**< (SPW_ROUTER_TABLE189) SpW Router Table (router_table_nb = 32) 189 Offset */
#define SPW_ROUTER_TABLE190_REG_OFST   (0x378)        /**< (SPW_ROUTER_TABLE190) SpW Router Table (router_table_nb = 32) 190 Offset */
#define SPW_ROUTER_TABLE191_REG_OFST   (0x37C)        /**< (SPW_ROUTER_TABLE191) SpW Router Table (router_table_nb = 32) 191 Offset */
#define SPW_ROUTER_TABLE192_REG_OFST   (0x380)        /**< (SPW_ROUTER_TABLE192) SpW Router Table (router_table_nb = 32) 192 Offset */
#define SPW_ROUTER_TABLE193_REG_OFST   (0x384)        /**< (SPW_ROUTER_TABLE193) SpW Router Table (router_table_nb = 32) 193 Offset */
#define SPW_ROUTER_TABLE194_REG_OFST   (0x388)        /**< (SPW_ROUTER_TABLE194) SpW Router Table (router_table_nb = 32) 194 Offset */
#define SPW_ROUTER_TABLE195_REG_OFST   (0x38C)        /**< (SPW_ROUTER_TABLE195) SpW Router Table (router_table_nb = 32) 195 Offset */
#define SPW_ROUTER_TABLE196_REG_OFST   (0x390)        /**< (SPW_ROUTER_TABLE196) SpW Router Table (router_table_nb = 32) 196 Offset */
#define SPW_ROUTER_TABLE197_REG_OFST   (0x394)        /**< (SPW_ROUTER_TABLE197) SpW Router Table (router_table_nb = 32) 197 Offset */
#define SPW_ROUTER_TABLE198_REG_OFST   (0x398)        /**< (SPW_ROUTER_TABLE198) SpW Router Table (router_table_nb = 32) 198 Offset */
#define SPW_ROUTER_TABLE199_REG_OFST   (0x39C)        /**< (SPW_ROUTER_TABLE199) SpW Router Table (router_table_nb = 32) 199 Offset */
#define SPW_ROUTER_TABLE200_REG_OFST   (0x3A0)        /**< (SPW_ROUTER_TABLE200) SpW Router Table (router_table_nb = 32) 200 Offset */
#define SPW_ROUTER_TABLE201_REG_OFST   (0x3A4)        /**< (SPW_ROUTER_TABLE201) SpW Router Table (router_table_nb = 32) 201 Offset */
#define SPW_ROUTER_TABLE202_REG_OFST   (0x3A8)        /**< (SPW_ROUTER_TABLE202) SpW Router Table (router_table_nb = 32) 202 Offset */
#define SPW_ROUTER_TABLE203_REG_OFST   (0x3AC)        /**< (SPW_ROUTER_TABLE203) SpW Router Table (router_table_nb = 32) 203 Offset */
#define SPW_ROUTER_TABLE204_REG_OFST   (0x3B0)        /**< (SPW_ROUTER_TABLE204) SpW Router Table (router_table_nb = 32) 204 Offset */
#define SPW_ROUTER_TABLE205_REG_OFST   (0x3B4)        /**< (SPW_ROUTER_TABLE205) SpW Router Table (router_table_nb = 32) 205 Offset */
#define SPW_ROUTER_TABLE206_REG_OFST   (0x3B8)        /**< (SPW_ROUTER_TABLE206) SpW Router Table (router_table_nb = 32) 206 Offset */
#define SPW_ROUTER_TABLE207_REG_OFST   (0x3BC)        /**< (SPW_ROUTER_TABLE207) SpW Router Table (router_table_nb = 32) 207 Offset */
#define SPW_ROUTER_TABLE208_REG_OFST   (0x3C0)        /**< (SPW_ROUTER_TABLE208) SpW Router Table (router_table_nb = 32) 208 Offset */
#define SPW_ROUTER_TABLE209_REG_OFST   (0x3C4)        /**< (SPW_ROUTER_TABLE209) SpW Router Table (router_table_nb = 32) 209 Offset */
#define SPW_ROUTER_TABLE210_REG_OFST   (0x3C8)        /**< (SPW_ROUTER_TABLE210) SpW Router Table (router_table_nb = 32) 210 Offset */
#define SPW_ROUTER_TABLE211_REG_OFST   (0x3CC)        /**< (SPW_ROUTER_TABLE211) SpW Router Table (router_table_nb = 32) 211 Offset */
#define SPW_ROUTER_TABLE212_REG_OFST   (0x3D0)        /**< (SPW_ROUTER_TABLE212) SpW Router Table (router_table_nb = 32) 212 Offset */
#define SPW_ROUTER_TABLE213_REG_OFST   (0x3D4)        /**< (SPW_ROUTER_TABLE213) SpW Router Table (router_table_nb = 32) 213 Offset */
#define SPW_ROUTER_TABLE214_REG_OFST   (0x3D8)        /**< (SPW_ROUTER_TABLE214) SpW Router Table (router_table_nb = 32) 214 Offset */
#define SPW_ROUTER_TABLE215_REG_OFST   (0x3DC)        /**< (SPW_ROUTER_TABLE215) SpW Router Table (router_table_nb = 32) 215 Offset */
#define SPW_ROUTER_TABLE216_REG_OFST   (0x3E0)        /**< (SPW_ROUTER_TABLE216) SpW Router Table (router_table_nb = 32) 216 Offset */
#define SPW_ROUTER_TABLE217_REG_OFST   (0x3E4)        /**< (SPW_ROUTER_TABLE217) SpW Router Table (router_table_nb = 32) 217 Offset */
#define SPW_ROUTER_TABLE218_REG_OFST   (0x3E8)        /**< (SPW_ROUTER_TABLE218) SpW Router Table (router_table_nb = 32) 218 Offset */
#define SPW_ROUTER_TABLE219_REG_OFST   (0x3EC)        /**< (SPW_ROUTER_TABLE219) SpW Router Table (router_table_nb = 32) 219 Offset */
#define SPW_ROUTER_TABLE220_REG_OFST   (0x3F0)        /**< (SPW_ROUTER_TABLE220) SpW Router Table (router_table_nb = 32) 220 Offset */
#define SPW_ROUTER_TABLE221_REG_OFST   (0x3F4)        /**< (SPW_ROUTER_TABLE221) SpW Router Table (router_table_nb = 32) 221 Offset */
#define SPW_ROUTER_TABLE222_REG_OFST   (0x3F8)        /**< (SPW_ROUTER_TABLE222) SpW Router Table (router_table_nb = 32) 222 Offset */
#define SPW_ROUTER_TABLE223_REG_OFST   (0x3FC)        /**< (SPW_ROUTER_TABLE223) SpW Router Table (router_table_nb = 32) 223 Offset */
#define SPW_LINK1_PI_RM_REG_OFST       (0x400)        /**< (SPW_LINK1_PI_RM) SpW Link 1 Pending Read Masked Interrupt Offset */
#define SPW_LINK1_PI_RCM_REG_OFST      (0x404)        /**< (SPW_LINK1_PI_RCM) SpW Link 1 Pending Read and Clear Masked Interrupt Offset */
#define SPW_LINK1_PI_R_REG_OFST        (0x408)        /**< (SPW_LINK1_PI_R) SpW Link 1 Pending Read Interrupt Offset */
#define SPW_LINK1_PI_RCS_REG_OFST      (0x40C)        /**< (SPW_LINK1_PI_RCS) SpW Link 1 Pending Read, Clear and Enabed Interrupt Offset */
#define SPW_LINK1_IM_REG_OFST          (0x410)        /**< (SPW_LINK1_IM) SpW Link 1 Interrupt Mask Offset */
#define SPW_LINK1_PI_C_REG_OFST        (0x414)        /**< (SPW_LINK1_PI_C) SpW Link 1 Clear Pending Interrupt Offset */
#define SPW_LINK1_IM_S_REG_OFST        (0x418)        /**< (SPW_LINK1_IM_S) SpW Link 1 Interrupt Set Mask Offset */
#define SPW_LINK1_IM_C_REG_OFST        (0x41C)        /**< (SPW_LINK1_IM_C) SpW Link 1 Interrupt Clear Mask Offset */
#define SPW_LINK1_CFG_REG_OFST         (0x420)        /**< (SPW_LINK1_CFG) SpW Link 1 Config Offset */
#define SPW_LINK1_CLKDIV_REG_OFST      (0x424)        /**< (SPW_LINK1_CLKDIV) SpW Link 1 Clock Division Offset */
#define SPW_LINK1_STATUS_REG_OFST      (0x428)        /**< (SPW_LINK1_STATUS) SpW Link 1 Status Offset */
#define SPW_LINK1_SWRESET_REG_OFST     (0x42C)        /**< (SPW_LINK1_SWRESET) SpW Link 1 Software Reset Offset */
#define SPW_LINK1_ESCCHAREVENT0_REG_OFST (0x430)        /**< (SPW_LINK1_ESCCHAREVENT0) SpW Link 1 Escape Character Event 0 Offset */
#define SPW_LINK1_ESCCHAREVENT1_REG_OFST (0x434)        /**< (SPW_LINK1_ESCCHAREVENT1) SpW Link 1 Escape Character Event 1 Offset */
#define SPW_LINK1_ESCCHARSTS_REG_OFST  (0x438)        /**< (SPW_LINK1_ESCCHARSTS) SpW Link 1 Escape Character Status Offset */
#define SPW_LINK1_TRANSESC_REG_OFST    (0x43C)        /**< (SPW_LINK1_TRANSESC) SpW Link 1 Transmit Escape Character Offset */
#define SPW_LINK1_DISTINTPI_RM_REG_OFST (0x440)        /**< (SPW_LINK1_DISTINTPI_RM) SpW Link 1 Distributed Interrupt Pending Read Masked Interrupt Offset */
#define SPW_LINK1_DISTINTPI_RCM_REG_OFST (0x444)        /**< (SPW_LINK1_DISTINTPI_RCM) SpW Link 1 Distributed Interrupt Pending Read and Clear Masked Interrupt Offset */
#define SPW_LINK1_DISTINTPI_R_REG_OFST (0x448)        /**< (SPW_LINK1_DISTINTPI_R) SpW Link 1 Distributed Interrupt Pending Read Interrupt Offset */
#define SPW_LINK1_DISTINTPI_RCS_REG_OFST (0x44C)        /**< (SPW_LINK1_DISTINTPI_RCS) SpW Link 1 Distributed Interrupt Pending Read and Clear Interrupt Offset */
#define SPW_LINK1_DISTINTIM_REG_OFST   (0x450)        /**< (SPW_LINK1_DISTINTIM) SpW Link 1 Distributed Interrupt Mask Offset */
#define SPW_LINK1_DISTINTPI_C_REG_OFST (0x454)        /**< (SPW_LINK1_DISTINTPI_C) SpW Link 1 Distributed Interrupt Clear Pending Interrupt Offset */
#define SPW_LINK1_DISTINTIM_S_REG_OFST (0x458)        /**< (SPW_LINK1_DISTINTIM_S) SpW Link 1 Distributed Interrupt Set Mask Offset */
#define SPW_LINK1_DISTINTIM_C_REG_OFST (0x45C)        /**< (SPW_LINK1_DISTINTIM_C) SpW Link 1 Distributed Interrupt Clear Mask Offset */
#define SPW_LINK1_DISTACKPI_RM_REG_OFST (0x460)        /**< (SPW_LINK1_DISTACKPI_RM) SpW Link 1 Distributed Interrupt Acknowledge Pending Read Masked Interrupt Offset */
#define SPW_LINK1_DISTACKPI_RCM_REG_OFST (0x464)        /**< (SPW_LINK1_DISTACKPI_RCM) SpW Link 1 Distributed Interrupt Acknowledge Pending Read and Clear Masked Interrupt Offset */
#define SPW_LINK1_DISTACKPI_R_REG_OFST (0x468)        /**< (SPW_LINK1_DISTACKPI_R) SpW Link 1 Distributed Interrupt Acknowledge Pending Read Interrupt Offset */
#define SPW_LINK1_DISTACKPI_RCS_REG_OFST (0x46C)        /**< (SPW_LINK1_DISTACKPI_RCS) SpW Link 1 Distributed Interrupt Acknowledge Pending Read and Clear Interrupt Offset */
#define SPW_LINK1_DISTACKIM_REG_OFST   (0x470)        /**< (SPW_LINK1_DISTACKIM) SpW Link 1 Distributed Interrupt Acknowledge Mask Offset */
#define SPW_LINK1_DISTACKPI_C_REG_OFST (0x474)        /**< (SPW_LINK1_DISTACKPI_C) SpW Link 1 Distributed Interrupt Acknowledge Clear Pending Interrupt Offset */
#define SPW_LINK1_DISTACKIM_S_REG_OFST (0x478)        /**< (SPW_LINK1_DISTACKIM_S) SpW Link 1 Distributed Interrupt Acknowledge Set Mask Offset */
#define SPW_LINK1_DISTACKIM_C_REG_OFST (0x47C)        /**< (SPW_LINK1_DISTACKIM_C) SpW Link 1 Distributed Interrupt Acknowledge Clear Mask Offset */
#define SPW_LINK2_PI_RM_REG_OFST       (0x480)        /**< (SPW_LINK2_PI_RM) SpW Link 2 Pending Read Masked Interrupt Offset */
#define SPW_LINK2_PI_RCM_REG_OFST      (0x484)        /**< (SPW_LINK2_PI_RCM) SpW Link 2 Pending Read and Clear Masked Interrupt Offset */
#define SPW_LINK2_PI_R_REG_OFST        (0x488)        /**< (SPW_LINK2_PI_R) SpW Link 2 Pending Read Interrupt Offset */
#define SPW_LINK2_PI_RCS_REG_OFST      (0x48C)        /**< (SPW_LINK2_PI_RCS) SpW Link 2 Pending Read, Clear and Enabled Interrupt Offset */
#define SPW_LINK2_IM_REG_OFST          (0x490)        /**< (SPW_LINK2_IM) SpW Link 2 Interrupt Mask Offset */
#define SPW_LINK2_PI_C_REG_OFST        (0x494)        /**< (SPW_LINK2_PI_C) SpW Link 2 Clear Pending Interrupt Offset */
#define SPW_LINK2_IM_S_REG_OFST        (0x498)        /**< (SPW_LINK2_IM_S) SpW Link 2 Interrupt Set Mask Offset */
#define SPW_LINK2_IM_C_REG_OFST        (0x49C)        /**< (SPW_LINK2_IM_C) SpW Link 2 Interrupt Clear Mask Offset */
#define SPW_LINK2_CFG_REG_OFST         (0x4A0)        /**< (SPW_LINK2_CFG) SpW Link 2 Config Offset */
#define SPW_LINK2_CLKDIV_REG_OFST      (0x4A4)        /**< (SPW_LINK2_CLKDIV) SpW Link 2 Clock Division Offset */
#define SPW_LINK2_STATUS_REG_OFST      (0x4A8)        /**< (SPW_LINK2_STATUS) SpW Link 2 Status Offset */
#define SPW_LINK2_SWRESET_REG_OFST     (0x4AC)        /**< (SPW_LINK2_SWRESET) SpW Link 2 Software Reset Offset */
#define SPW_LINK2_ESCCHAREVENT0_REG_OFST (0x4B0)        /**< (SPW_LINK2_ESCCHAREVENT0) SpW Link 2 Escape Character Event 0 Offset */
#define SPW_LINK2_ESCCHAREVENT1_REG_OFST (0x4B4)        /**< (SPW_LINK2_ESCCHAREVENT1) SpW Link 2 Escape Character Event 1 Offset */
#define SPW_LINK2_ESCCHARSTS_REG_OFST  (0x4B8)        /**< (SPW_LINK2_ESCCHARSTS) SpW Link 2 Escape Character Status Offset */
#define SPW_LINK2_TRANSESC_REG_OFST    (0x4BC)        /**< (SPW_LINK2_TRANSESC) SpW Link 2 Transmit Escape Character Offset */
#define SPW_LINK2_DISTINTPI_RM_REG_OFST (0x4C0)        /**< (SPW_LINK2_DISTINTPI_RM) SpW Link 2 Distributed Interrupt Pending Read Masked Interrupt Offset */
#define SPW_LINK2_DISTINTPI_RCM_REG_OFST (0x4C4)        /**< (SPW_LINK2_DISTINTPI_RCM) SpW Link 2 Distributed Interrupt Pending Read and Clear Masked Interrupt Offset */
#define SPW_LINK2_DISTINTPI_R_REG_OFST (0x4C8)        /**< (SPW_LINK2_DISTINTPI_R) SpW Link 2 Distributed Interrupt Pending Read Interrupt Offset */
#define SPW_LINK2_DISTINTPI_RCS_REG_OFST (0x4CC)        /**< (SPW_LINK2_DISTINTPI_RCS) SpW Link 2 Distributed Interrupt Pending Read and Clear Interrupt Offset */
#define SPW_LINK2_DISTINTIM_REG_OFST   (0x4D0)        /**< (SPW_LINK2_DISTINTIM) SpW Link 2 Distributed Interrupt Mask Offset */
#define SPW_LINK2_DISTINTPI_C_REG_OFST (0x4D4)        /**< (SPW_LINK2_DISTINTPI_C) SpW Link 2 Distributed Interrupt Clear Pending Interrupt Offset */
#define SPW_LINK2_DISTINTIM_S_REG_OFST (0x4D8)        /**< (SPW_LINK2_DISTINTIM_S) SpW Link 2 Distributed Interrupt Set Mask Offset */
#define SPW_LINK2_DISTINTIM_C_REG_OFST (0x4DC)        /**< (SPW_LINK2_DISTINTIM_C) SpW Link 2 Distributed Interrupt Clear Mask Offset */
#define SPW_LINK2_DISTACKPI_RM_REG_OFST (0x4E0)        /**< (SPW_LINK2_DISTACKPI_RM) SpW Link 2 Distributed Interrupt Acknowledge Pending Read Masked Interrupt Offset */
#define SPW_LINK2_DISTACKPI_RCM_REG_OFST (0x4E4)        /**< (SPW_LINK2_DISTACKPI_RCM) SpW Link 2 Distributed Interrupt Acknowledge Pending Read and Clear Masked Interrupt Offset */
#define SPW_LINK2_DISTACKPI_R_REG_OFST (0x4E8)        /**< (SPW_LINK2_DISTACKPI_R) SpW Link 2 Distributed Interrupt Acknowledge Pending Read Interrupt Offset */
#define SPW_LINK2_DISTACKPI_RCS_REG_OFST (0x4EC)        /**< (SPW_LINK2_DISTACKPI_RCS) SpW Link 2 Distributed Interrupt Acknowledge Pending Read and Clear Interrupt Offset */
#define SPW_LINK2_DISTACKIM_REG_OFST   (0x4F0)        /**< (SPW_LINK2_DISTACKIM) SpW Link 2 Distributed Interrupt Acknowledge Mask Offset */
#define SPW_LINK2_DISTACKPI_C_REG_OFST (0x4F4)        /**< (SPW_LINK2_DISTACKPI_C) SpW Link 2 Distributed Interrupt Acknowledge Clear Pending Interrupt Offset */
#define SPW_LINK2_DISTACKIM_S_REG_OFST (0x4F8)        /**< (SPW_LINK2_DISTACKIM_S) SpW Link 2 Distributed Interrupt Acknowledge Set Mask Offset */
#define SPW_LINK2_DISTACKIM_C_REG_OFST (0x4FC)        /**< (SPW_LINK2_DISTACKIM_C) SpW Link 2 Distributed Interrupt Acknowledge Clear Mask Offset */
#define SPW_PKTRX1_PI_RM_REG_OFST      (0x800)        /**< (SPW_PKTRX1_PI_RM) PktRx Pending Read Masked Interrupt Offset */
#define SPW_PKTRX1_PI_RCM_REG_OFST     (0x804)        /**< (SPW_PKTRX1_PI_RCM) PktRx Pending Read and Clear Masked Interrupt Offset */
#define SPW_PKTRX1_PI_R_REG_OFST       (0x808)        /**< (SPW_PKTRX1_PI_R) PktRx Pending Read Interrupt Offset */
#define SPW_PKTRX1_PI_RCS_REG_OFST     (0x80C)        /**< (SPW_PKTRX1_PI_RCS) PktRx Pending Read, Clear and Enabled Interrupt Offset */
#define SPW_PKTRX1_IM_REG_OFST         (0x810)        /**< (SPW_PKTRX1_IM) PktRx Interrupt Mask Offset */
#define SPW_PKTRX1_PI_C_REG_OFST       (0x814)        /**< (SPW_PKTRX1_PI_C) PktRx Clear Pending Interrupt Offset */
#define SPW_PKTRX1_IM_S_REG_OFST       (0x818)        /**< (SPW_PKTRX1_IM_S) PktRx Interrupt Set Mask Offset */
#define SPW_PKTRX1_IM_C_REG_OFST       (0x81C)        /**< (SPW_PKTRX1_IM_C) PktRx Interrupt Clear Mask Offset */
#define SPW_PKTRX1_CFG_REG_OFST        (0x820)        /**< (SPW_PKTRX1_CFG) PktRx Config Offset */
#define SPW_PKTRX1_STATUS_REG_OFST     (0x824)        /**< (SPW_PKTRX1_STATUS) PktRx Status Offset */
#define SPW_PKTRX1_NXTBUFDATAADDR_REG_OFST (0x830)        /**< (SPW_PKTRX1_NXTBUFDATAADDR) PktRx Next Buffer Data Address Offset */
#define SPW_PKTRX1_NXTBUFDATALEN_REG_OFST (0x834)        /**< (SPW_PKTRX1_NXTBUFDATALEN) PktRx Next Buffer Data Length Offset */
#define SPW_PKTRX1_NXTBUFPKTADDR_REG_OFST (0x838)        /**< (SPW_PKTRX1_NXTBUFPKTADDR) PktRx Next Buffer Packet Address Offset */
#define SPW_PKTRX1_NXTBUFCFG_REG_OFST  (0x83C)        /**< (SPW_PKTRX1_NXTBUFCFG) PktRx Next Buffer Config Offset */
#define SPW_PKTRX1_CURBUFDATAADDR_REG_OFST (0x840)        /**< (SPW_PKTRX1_CURBUFDATAADDR) PktRx Current Buffer Data Address Offset */
#define SPW_PKTRX1_CURBUFDATALEN_REG_OFST (0x844)        /**< (SPW_PKTRX1_CURBUFDATALEN) PktRx Current Buffer Data Length Offset */
#define SPW_PKTRX1_CURBUFPKTADDR_REG_OFST (0x848)        /**< (SPW_PKTRX1_CURBUFPKTADDR) PktRx Current Buffer Packet Address Offset */
#define SPW_PKTRX1_CURBUFCFG_REG_OFST  (0x84C)        /**< (SPW_PKTRX1_CURBUFCFG) PktRx Current Buffer Config Offset */
#define SPW_PKTRX1_PREVBUFDATALEN_REG_OFST (0x850)        /**< (SPW_PKTRX1_PREVBUFDATALEN) PktRx Previous Buffer Data Length Offset */
#define SPW_PKTRX1_PREVBUFSTS_REG_OFST (0x854)        /**< (SPW_PKTRX1_PREVBUFSTS) PktRx Previous Buffer Status Offset */
#define SPW_PKTRX1_SWRESET_REG_OFST    (0x87C)        /**< (SPW_PKTRX1_SWRESET) PktRx Software Reset Offset */
#define SPW_PKTTX1_PI_RM_REG_OFST      (0xC00)        /**< (SPW_PKTTX1_PI_RM) PktTx Pending Read Masked Interrupt Offset */
#define SPW_PKTTX1_PI_RCM_REG_OFST     (0xC04)        /**< (SPW_PKTTX1_PI_RCM) PktTx Pending Read and Clear Masked Interrupt Offset */
#define SPW_PKTTX1_PI_R_REG_OFST       (0xC08)        /**< (SPW_PKTTX1_PI_R) PktTx Pending Read Interrupt Offset */
#define SPW_PKTTX1_PI_RCS_REG_OFST     (0xC0C)        /**< (SPW_PKTTX1_PI_RCS) PktTx Pending Read, Clear and Enabled Interrupt Offset */
#define SPW_PKTTX1_IM_REG_OFST         (0xC10)        /**< (SPW_PKTTX1_IM) PktTx Interrupt Mask Offset */
#define SPW_PKTTX1_PI_C_REG_OFST       (0xC14)        /**< (SPW_PKTTX1_PI_C) PktTx Clear Pending Interrupt Offset */
#define SPW_PKTTX1_IM_S_REG_OFST       (0xC18)        /**< (SPW_PKTTX1_IM_S) PktTx Interrupt Set Mask Offset */
#define SPW_PKTTX1_IM_C_REG_OFST       (0xC1C)        /**< (SPW_PKTTX1_IM_C) PktTx Interrupt Clear Mask Offset */
#define SPW_PKTTX1_STATUS_REG_OFST     (0xC20)        /**< (SPW_PKTTX1_STATUS) PktTx Status Offset */
#define SPW_PKTTX1_NXTSENDROUT_REG_OFST (0xC24)        /**< (SPW_PKTTX1_NXTSENDROUT) PktTx Next Send List Router Bytes Offset */
#define SPW_PKTTX1_NXTSENDADDR_REG_OFST (0xC28)        /**< (SPW_PKTTX1_NXTSENDADDR) PktTx Next Send List Address Offset */
#define SPW_PKTTX1_NXTSENDCFG_REG_OFST (0xC2C)        /**< (SPW_PKTTX1_NXTSENDCFG) PktTx Next Send List Config Offset */
#define SPW_PKTTX1_CURSENDROUT_REG_OFST (0xC30)        /**< (SPW_PKTTX1_CURSENDROUT) PktTx Current Send List Router Bytes Offset */
#define SPW_PKTTX1_CURSENDADDR_REG_OFST (0xC34)        /**< (SPW_PKTTX1_CURSENDADDR) PktTx Current Send List Address Offset */
#define SPW_PKTTX1_CURSENDCFG_REG_OFST (0xC38)        /**< (SPW_PKTTX1_CURSENDCFG) PktTx Current Send List Config Offset */
#define SPW_PKTTX1_SWRESET_REG_OFST    (0xC3C)        /**< (SPW_PKTTX1_SWRESET) PktTx Software Reset Offset */
#define SPW_RMAP1_CFG_REG_OFST         (0xE00)        /**< (SPW_RMAP1_CFG) SpW RMAP 1 Config Offset */
#define SPW_RMAP1_STS_RC_REG_OFST      (0xE04)        /**< (SPW_RMAP1_STS_RC) SpW RMAP 1 Read and Clear Status Offset */
#define SPW_RMAP1_STS_REG_OFST         (0xE08)        /**< (SPW_RMAP1_STS) SpW RMAP 1 Read Status Offset */
#define SPW_TCH_PI_RM_REG_OFST         (0xE80)        /**< (SPW_TCH_PI_RM) SpW Tch Pending Read Masked Interrupt Offset */
#define SPW_TCH_PI_RCM_REG_OFST        (0xE84)        /**< (SPW_TCH_PI_RCM) SpW Tch Pending Read and Clear Masked Interrupt Offset */
#define SPW_TCH_PI_R_REG_OFST          (0xE88)        /**< (SPW_TCH_PI_R) SpW Tch Pending Read Interrupt Offset */
#define SPW_TCH_PI_RCS_REG_OFST        (0xE8C)        /**< (SPW_TCH_PI_RCS) SpW Tch Pending Read, Clear and Enabled Interrupt Offset */
#define SPW_TCH_IM_REG_OFST            (0xE90)        /**< (SPW_TCH_IM) SpW Tch Interrupt Mask Offset */
#define SPW_TCH_PI_C_REG_OFST          (0xE94)        /**< (SPW_TCH_PI_C) SpW Tch Clear Pending Interrupt Offset */
#define SPW_TCH_IM_S_REG_OFST          (0xE98)        /**< (SPW_TCH_IM_S) SpW Tch Interrupt Set Mask Offset */
#define SPW_TCH_IM_C_REG_OFST          (0xE9C)        /**< (SPW_TCH_IM_C) SpW Tch Interrupt Clear Mask Offset */
#define SPW_TCH_CFGLISTEN_REG_OFST     (0xEA0)        /**< (SPW_TCH_CFGLISTEN) SpW Tch Config Listener Offset */
#define SPW_TCH_CFGSEND_REG_OFST       (0xEA4)        /**< (SPW_TCH_CFGSEND) SpW Tch Config Sender Offset */
#define SPW_TCH_CFG_REG_OFST           (0xEA8)        /**< (SPW_TCH_CFG) SpW Tch Config Offset */
#define SPW_TCH_CFGRESTART_REG_OFST    (0xEAC)        /**< (SPW_TCH_CFGRESTART) SpW Tch Config Restart Offset */
#define SPW_TCH_CFGTCEVENT_REG_OFST    (0xEB0)        /**< (SPW_TCH_CFGTCEVENT) SpW Tch Config Tc Event Offset */
#define SPW_TCH_CFGWD_REG_OFST         (0xEB4)        /**< (SPW_TCH_CFGWD) SpW Tch Config Watchdog Offset */
#define SPW_TCH_LASTTIMECODE_REG_OFST  (0xEB8)        /**< (SPW_TCH_LASTTIMECODE) SpW Tch Last Time Code Offset */
#define SPW_TCH_SWRESET_REG_OFST       (0xEBC)        /**< (SPW_TCH_SWRESET) SpW Tch Software Reset Offset */
#define SPW_GROUP_IRQSTS1_REG_OFST     (0xF00)        /**< (SPW_GROUP_IRQSTS1) SpW Group Interrupt status 1 Offset */
#define SPW_GROUP_IRQSTS2_REG_OFST     (0xF04)        /**< (SPW_GROUP_IRQSTS2) SpW Group Interrupt status 2 Offset */
#define SPW_GROUP_EDACSTS_REG_OFST     (0xF08)        /**< (SPW_GROUP_EDACSTS) SpW Group Interrupt status Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief SPW register API structure */
typedef struct
{
  __I   uint32_t                       SPW_ROUTER_STS;  /**< Offset: 0x00 (R/   32) SpW Router Status */
  __I   uint32_t                       SPW_ROUTER_CFG;  /**< Offset: 0x04 (R/   32) SpW Router Config */
  __I   uint32_t                       SPW_ROUTER_TIMEOUT; /**< Offset: 0x08 (R/   32) SpW Router Timeout */
  __I   uint8_t                        Reserved1[0x74];
  __IO  uint32_t                       SPW_ROUTER_TABLE0; /**< Offset: 0x80 (R/W  32) SpW Router Table (router_table_nb = 32) 0 */
  __IO  uint32_t                       SPW_ROUTER_TABLE1; /**< Offset: 0x84 (R/W  32) SpW Router Table (router_table_nb = 32) 1 */
  __IO  uint32_t                       SPW_ROUTER_TABLE2; /**< Offset: 0x88 (R/W  32) SpW Router Table (router_table_nb = 32) 2 */
  __IO  uint32_t                       SPW_ROUTER_TABLE3; /**< Offset: 0x8C (R/W  32) SpW Router Table (router_table_nb = 32) 3 */
  __IO  uint32_t                       SPW_ROUTER_TABLE4; /**< Offset: 0x90 (R/W  32) SpW Router Table (router_table_nb = 32) 4 */
  __IO  uint32_t                       SPW_ROUTER_TABLE5; /**< Offset: 0x94 (R/W  32) SpW Router Table (router_table_nb = 32) 5 */
  __IO  uint32_t                       SPW_ROUTER_TABLE6; /**< Offset: 0x98 (R/W  32) SpW Router Table (router_table_nb = 32) 6 */
  __IO  uint32_t                       SPW_ROUTER_TABLE7; /**< Offset: 0x9C (R/W  32) SpW Router Table (router_table_nb = 32) 7 */
  __IO  uint32_t                       SPW_ROUTER_TABLE8; /**< Offset: 0xA0 (R/W  32) SpW Router Table (router_table_nb = 32) 8 */
  __IO  uint32_t                       SPW_ROUTER_TABLE9; /**< Offset: 0xA4 (R/W  32) SpW Router Table (router_table_nb = 32) 9 */
  __IO  uint32_t                       SPW_ROUTER_TABLE10; /**< Offset: 0xA8 (R/W  32) SpW Router Table (router_table_nb = 32) 10 */
  __IO  uint32_t                       SPW_ROUTER_TABLE11; /**< Offset: 0xAC (R/W  32) SpW Router Table (router_table_nb = 32) 11 */
  __IO  uint32_t                       SPW_ROUTER_TABLE12; /**< Offset: 0xB0 (R/W  32) SpW Router Table (router_table_nb = 32) 12 */
  __IO  uint32_t                       SPW_ROUTER_TABLE13; /**< Offset: 0xB4 (R/W  32) SpW Router Table (router_table_nb = 32) 13 */
  __IO  uint32_t                       SPW_ROUTER_TABLE14; /**< Offset: 0xB8 (R/W  32) SpW Router Table (router_table_nb = 32) 14 */
  __IO  uint32_t                       SPW_ROUTER_TABLE15; /**< Offset: 0xBC (R/W  32) SpW Router Table (router_table_nb = 32) 15 */
  __IO  uint32_t                       SPW_ROUTER_TABLE16; /**< Offset: 0xC0 (R/W  32) SpW Router Table (router_table_nb = 32) 16 */
  __IO  uint32_t                       SPW_ROUTER_TABLE17; /**< Offset: 0xC4 (R/W  32) SpW Router Table (router_table_nb = 32) 17 */
  __IO  uint32_t                       SPW_ROUTER_TABLE18; /**< Offset: 0xC8 (R/W  32) SpW Router Table (router_table_nb = 32) 18 */
  __IO  uint32_t                       SPW_ROUTER_TABLE19; /**< Offset: 0xCC (R/W  32) SpW Router Table (router_table_nb = 32) 19 */
  __IO  uint32_t                       SPW_ROUTER_TABLE20; /**< Offset: 0xD0 (R/W  32) SpW Router Table (router_table_nb = 32) 20 */
  __IO  uint32_t                       SPW_ROUTER_TABLE21; /**< Offset: 0xD4 (R/W  32) SpW Router Table (router_table_nb = 32) 21 */
  __IO  uint32_t                       SPW_ROUTER_TABLE22; /**< Offset: 0xD8 (R/W  32) SpW Router Table (router_table_nb = 32) 22 */
  __IO  uint32_t                       SPW_ROUTER_TABLE23; /**< Offset: 0xDC (R/W  32) SpW Router Table (router_table_nb = 32) 23 */
  __IO  uint32_t                       SPW_ROUTER_TABLE24; /**< Offset: 0xE0 (R/W  32) SpW Router Table (router_table_nb = 32) 24 */
  __IO  uint32_t                       SPW_ROUTER_TABLE25; /**< Offset: 0xE4 (R/W  32) SpW Router Table (router_table_nb = 32) 25 */
  __IO  uint32_t                       SPW_ROUTER_TABLE26; /**< Offset: 0xE8 (R/W  32) SpW Router Table (router_table_nb = 32) 26 */
  __IO  uint32_t                       SPW_ROUTER_TABLE27; /**< Offset: 0xEC (R/W  32) SpW Router Table (router_table_nb = 32) 27 */
  __IO  uint32_t                       SPW_ROUTER_TABLE28; /**< Offset: 0xF0 (R/W  32) SpW Router Table (router_table_nb = 32) 28 */
  __IO  uint32_t                       SPW_ROUTER_TABLE29; /**< Offset: 0xF4 (R/W  32) SpW Router Table (router_table_nb = 32) 29 */
  __IO  uint32_t                       SPW_ROUTER_TABLE30; /**< Offset: 0xF8 (R/W  32) SpW Router Table (router_table_nb = 32) 30 */
  __IO  uint32_t                       SPW_ROUTER_TABLE31; /**< Offset: 0xFC (R/W  32) SpW Router Table (router_table_nb = 32) 31 */
  __IO  uint32_t                       SPW_ROUTER_TABLE32; /**< Offset: 0x100 (R/W  32) SpW Router Table (router_table_nb = 32) 32 */
  __IO  uint32_t                       SPW_ROUTER_TABLE33; /**< Offset: 0x104 (R/W  32) SpW Router Table (router_table_nb = 32) 33 */
  __IO  uint32_t                       SPW_ROUTER_TABLE34; /**< Offset: 0x108 (R/W  32) SpW Router Table (router_table_nb = 32) 34 */
  __IO  uint32_t                       SPW_ROUTER_TABLE35; /**< Offset: 0x10C (R/W  32) SpW Router Table (router_table_nb = 32) 35 */
  __IO  uint32_t                       SPW_ROUTER_TABLE36; /**< Offset: 0x110 (R/W  32) SpW Router Table (router_table_nb = 32) 36 */
  __IO  uint32_t                       SPW_ROUTER_TABLE37; /**< Offset: 0x114 (R/W  32) SpW Router Table (router_table_nb = 32) 37 */
  __IO  uint32_t                       SPW_ROUTER_TABLE38; /**< Offset: 0x118 (R/W  32) SpW Router Table (router_table_nb = 32) 38 */
  __IO  uint32_t                       SPW_ROUTER_TABLE39; /**< Offset: 0x11C (R/W  32) SpW Router Table (router_table_nb = 32) 39 */
  __IO  uint32_t                       SPW_ROUTER_TABLE40; /**< Offset: 0x120 (R/W  32) SpW Router Table (router_table_nb = 32) 40 */
  __IO  uint32_t                       SPW_ROUTER_TABLE41; /**< Offset: 0x124 (R/W  32) SpW Router Table (router_table_nb = 32) 41 */
  __IO  uint32_t                       SPW_ROUTER_TABLE42; /**< Offset: 0x128 (R/W  32) SpW Router Table (router_table_nb = 32) 42 */
  __IO  uint32_t                       SPW_ROUTER_TABLE43; /**< Offset: 0x12C (R/W  32) SpW Router Table (router_table_nb = 32) 43 */
  __IO  uint32_t                       SPW_ROUTER_TABLE44; /**< Offset: 0x130 (R/W  32) SpW Router Table (router_table_nb = 32) 44 */
  __IO  uint32_t                       SPW_ROUTER_TABLE45; /**< Offset: 0x134 (R/W  32) SpW Router Table (router_table_nb = 32) 45 */
  __IO  uint32_t                       SPW_ROUTER_TABLE46; /**< Offset: 0x138 (R/W  32) SpW Router Table (router_table_nb = 32) 46 */
  __IO  uint32_t                       SPW_ROUTER_TABLE47; /**< Offset: 0x13C (R/W  32) SpW Router Table (router_table_nb = 32) 47 */
  __IO  uint32_t                       SPW_ROUTER_TABLE48; /**< Offset: 0x140 (R/W  32) SpW Router Table (router_table_nb = 32) 48 */
  __IO  uint32_t                       SPW_ROUTER_TABLE49; /**< Offset: 0x144 (R/W  32) SpW Router Table (router_table_nb = 32) 49 */
  __IO  uint32_t                       SPW_ROUTER_TABLE50; /**< Offset: 0x148 (R/W  32) SpW Router Table (router_table_nb = 32) 50 */
  __IO  uint32_t                       SPW_ROUTER_TABLE51; /**< Offset: 0x14C (R/W  32) SpW Router Table (router_table_nb = 32) 51 */
  __IO  uint32_t                       SPW_ROUTER_TABLE52; /**< Offset: 0x150 (R/W  32) SpW Router Table (router_table_nb = 32) 52 */
  __IO  uint32_t                       SPW_ROUTER_TABLE53; /**< Offset: 0x154 (R/W  32) SpW Router Table (router_table_nb = 32) 53 */
  __IO  uint32_t                       SPW_ROUTER_TABLE54; /**< Offset: 0x158 (R/W  32) SpW Router Table (router_table_nb = 32) 54 */
  __IO  uint32_t                       SPW_ROUTER_TABLE55; /**< Offset: 0x15C (R/W  32) SpW Router Table (router_table_nb = 32) 55 */
  __IO  uint32_t                       SPW_ROUTER_TABLE56; /**< Offset: 0x160 (R/W  32) SpW Router Table (router_table_nb = 32) 56 */
  __IO  uint32_t                       SPW_ROUTER_TABLE57; /**< Offset: 0x164 (R/W  32) SpW Router Table (router_table_nb = 32) 57 */
  __IO  uint32_t                       SPW_ROUTER_TABLE58; /**< Offset: 0x168 (R/W  32) SpW Router Table (router_table_nb = 32) 58 */
  __IO  uint32_t                       SPW_ROUTER_TABLE59; /**< Offset: 0x16C (R/W  32) SpW Router Table (router_table_nb = 32) 59 */
  __IO  uint32_t                       SPW_ROUTER_TABLE60; /**< Offset: 0x170 (R/W  32) SpW Router Table (router_table_nb = 32) 60 */
  __IO  uint32_t                       SPW_ROUTER_TABLE61; /**< Offset: 0x174 (R/W  32) SpW Router Table (router_table_nb = 32) 61 */
  __IO  uint32_t                       SPW_ROUTER_TABLE62; /**< Offset: 0x178 (R/W  32) SpW Router Table (router_table_nb = 32) 62 */
  __IO  uint32_t                       SPW_ROUTER_TABLE63; /**< Offset: 0x17C (R/W  32) SpW Router Table (router_table_nb = 32) 63 */
  __IO  uint32_t                       SPW_ROUTER_TABLE64; /**< Offset: 0x180 (R/W  32) SpW Router Table (router_table_nb = 32) 64 */
  __IO  uint32_t                       SPW_ROUTER_TABLE65; /**< Offset: 0x184 (R/W  32) SpW Router Table (router_table_nb = 32) 65 */
  __IO  uint32_t                       SPW_ROUTER_TABLE66; /**< Offset: 0x188 (R/W  32) SpW Router Table (router_table_nb = 32) 66 */
  __IO  uint32_t                       SPW_ROUTER_TABLE67; /**< Offset: 0x18C (R/W  32) SpW Router Table (router_table_nb = 32) 67 */
  __IO  uint32_t                       SPW_ROUTER_TABLE68; /**< Offset: 0x190 (R/W  32) SpW Router Table (router_table_nb = 32) 68 */
  __IO  uint32_t                       SPW_ROUTER_TABLE69; /**< Offset: 0x194 (R/W  32) SpW Router Table (router_table_nb = 32) 69 */
  __IO  uint32_t                       SPW_ROUTER_TABLE70; /**< Offset: 0x198 (R/W  32) SpW Router Table (router_table_nb = 32) 70 */
  __IO  uint32_t                       SPW_ROUTER_TABLE71; /**< Offset: 0x19C (R/W  32) SpW Router Table (router_table_nb = 32) 71 */
  __IO  uint32_t                       SPW_ROUTER_TABLE72; /**< Offset: 0x1A0 (R/W  32) SpW Router Table (router_table_nb = 32) 72 */
  __IO  uint32_t                       SPW_ROUTER_TABLE73; /**< Offset: 0x1A4 (R/W  32) SpW Router Table (router_table_nb = 32) 73 */
  __IO  uint32_t                       SPW_ROUTER_TABLE74; /**< Offset: 0x1A8 (R/W  32) SpW Router Table (router_table_nb = 32) 74 */
  __IO  uint32_t                       SPW_ROUTER_TABLE75; /**< Offset: 0x1AC (R/W  32) SpW Router Table (router_table_nb = 32) 75 */
  __IO  uint32_t                       SPW_ROUTER_TABLE76; /**< Offset: 0x1B0 (R/W  32) SpW Router Table (router_table_nb = 32) 76 */
  __IO  uint32_t                       SPW_ROUTER_TABLE77; /**< Offset: 0x1B4 (R/W  32) SpW Router Table (router_table_nb = 32) 77 */
  __IO  uint32_t                       SPW_ROUTER_TABLE78; /**< Offset: 0x1B8 (R/W  32) SpW Router Table (router_table_nb = 32) 78 */
  __IO  uint32_t                       SPW_ROUTER_TABLE79; /**< Offset: 0x1BC (R/W  32) SpW Router Table (router_table_nb = 32) 79 */
  __IO  uint32_t                       SPW_ROUTER_TABLE80; /**< Offset: 0x1C0 (R/W  32) SpW Router Table (router_table_nb = 32) 80 */
  __IO  uint32_t                       SPW_ROUTER_TABLE81; /**< Offset: 0x1C4 (R/W  32) SpW Router Table (router_table_nb = 32) 81 */
  __IO  uint32_t                       SPW_ROUTER_TABLE82; /**< Offset: 0x1C8 (R/W  32) SpW Router Table (router_table_nb = 32) 82 */
  __IO  uint32_t                       SPW_ROUTER_TABLE83; /**< Offset: 0x1CC (R/W  32) SpW Router Table (router_table_nb = 32) 83 */
  __IO  uint32_t                       SPW_ROUTER_TABLE84; /**< Offset: 0x1D0 (R/W  32) SpW Router Table (router_table_nb = 32) 84 */
  __IO  uint32_t                       SPW_ROUTER_TABLE85; /**< Offset: 0x1D4 (R/W  32) SpW Router Table (router_table_nb = 32) 85 */
  __IO  uint32_t                       SPW_ROUTER_TABLE86; /**< Offset: 0x1D8 (R/W  32) SpW Router Table (router_table_nb = 32) 86 */
  __IO  uint32_t                       SPW_ROUTER_TABLE87; /**< Offset: 0x1DC (R/W  32) SpW Router Table (router_table_nb = 32) 87 */
  __IO  uint32_t                       SPW_ROUTER_TABLE88; /**< Offset: 0x1E0 (R/W  32) SpW Router Table (router_table_nb = 32) 88 */
  __IO  uint32_t                       SPW_ROUTER_TABLE89; /**< Offset: 0x1E4 (R/W  32) SpW Router Table (router_table_nb = 32) 89 */
  __IO  uint32_t                       SPW_ROUTER_TABLE90; /**< Offset: 0x1E8 (R/W  32) SpW Router Table (router_table_nb = 32) 90 */
  __IO  uint32_t                       SPW_ROUTER_TABLE91; /**< Offset: 0x1EC (R/W  32) SpW Router Table (router_table_nb = 32) 91 */
  __IO  uint32_t                       SPW_ROUTER_TABLE92; /**< Offset: 0x1F0 (R/W  32) SpW Router Table (router_table_nb = 32) 92 */
  __IO  uint32_t                       SPW_ROUTER_TABLE93; /**< Offset: 0x1F4 (R/W  32) SpW Router Table (router_table_nb = 32) 93 */
  __IO  uint32_t                       SPW_ROUTER_TABLE94; /**< Offset: 0x1F8 (R/W  32) SpW Router Table (router_table_nb = 32) 94 */
  __IO  uint32_t                       SPW_ROUTER_TABLE95; /**< Offset: 0x1FC (R/W  32) SpW Router Table (router_table_nb = 32) 95 */
  __IO  uint32_t                       SPW_ROUTER_TABLE96; /**< Offset: 0x200 (R/W  32) SpW Router Table (router_table_nb = 32) 96 */
  __IO  uint32_t                       SPW_ROUTER_TABLE97; /**< Offset: 0x204 (R/W  32) SpW Router Table (router_table_nb = 32) 97 */
  __IO  uint32_t                       SPW_ROUTER_TABLE98; /**< Offset: 0x208 (R/W  32) SpW Router Table (router_table_nb = 32) 98 */
  __IO  uint32_t                       SPW_ROUTER_TABLE99; /**< Offset: 0x20C (R/W  32) SpW Router Table (router_table_nb = 32) 99 */
  __IO  uint32_t                       SPW_ROUTER_TABLE100; /**< Offset: 0x210 (R/W  32) SpW Router Table (router_table_nb = 32) 100 */
  __IO  uint32_t                       SPW_ROUTER_TABLE101; /**< Offset: 0x214 (R/W  32) SpW Router Table (router_table_nb = 32) 101 */
  __IO  uint32_t                       SPW_ROUTER_TABLE102; /**< Offset: 0x218 (R/W  32) SpW Router Table (router_table_nb = 32) 102 */
  __IO  uint32_t                       SPW_ROUTER_TABLE103; /**< Offset: 0x21C (R/W  32) SpW Router Table (router_table_nb = 32) 103 */
  __IO  uint32_t                       SPW_ROUTER_TABLE104; /**< Offset: 0x220 (R/W  32) SpW Router Table (router_table_nb = 32) 104 */
  __IO  uint32_t                       SPW_ROUTER_TABLE105; /**< Offset: 0x224 (R/W  32) SpW Router Table (router_table_nb = 32) 105 */
  __IO  uint32_t                       SPW_ROUTER_TABLE106; /**< Offset: 0x228 (R/W  32) SpW Router Table (router_table_nb = 32) 106 */
  __IO  uint32_t                       SPW_ROUTER_TABLE107; /**< Offset: 0x22C (R/W  32) SpW Router Table (router_table_nb = 32) 107 */
  __IO  uint32_t                       SPW_ROUTER_TABLE108; /**< Offset: 0x230 (R/W  32) SpW Router Table (router_table_nb = 32) 108 */
  __IO  uint32_t                       SPW_ROUTER_TABLE109; /**< Offset: 0x234 (R/W  32) SpW Router Table (router_table_nb = 32) 109 */
  __IO  uint32_t                       SPW_ROUTER_TABLE110; /**< Offset: 0x238 (R/W  32) SpW Router Table (router_table_nb = 32) 110 */
  __IO  uint32_t                       SPW_ROUTER_TABLE111; /**< Offset: 0x23C (R/W  32) SpW Router Table (router_table_nb = 32) 111 */
  __IO  uint32_t                       SPW_ROUTER_TABLE112; /**< Offset: 0x240 (R/W  32) SpW Router Table (router_table_nb = 32) 112 */
  __IO  uint32_t                       SPW_ROUTER_TABLE113; /**< Offset: 0x244 (R/W  32) SpW Router Table (router_table_nb = 32) 113 */
  __IO  uint32_t                       SPW_ROUTER_TABLE114; /**< Offset: 0x248 (R/W  32) SpW Router Table (router_table_nb = 32) 114 */
  __IO  uint32_t                       SPW_ROUTER_TABLE115; /**< Offset: 0x24C (R/W  32) SpW Router Table (router_table_nb = 32) 115 */
  __IO  uint32_t                       SPW_ROUTER_TABLE116; /**< Offset: 0x250 (R/W  32) SpW Router Table (router_table_nb = 32) 116 */
  __IO  uint32_t                       SPW_ROUTER_TABLE117; /**< Offset: 0x254 (R/W  32) SpW Router Table (router_table_nb = 32) 117 */
  __IO  uint32_t                       SPW_ROUTER_TABLE118; /**< Offset: 0x258 (R/W  32) SpW Router Table (router_table_nb = 32) 118 */
  __IO  uint32_t                       SPW_ROUTER_TABLE119; /**< Offset: 0x25C (R/W  32) SpW Router Table (router_table_nb = 32) 119 */
  __IO  uint32_t                       SPW_ROUTER_TABLE120; /**< Offset: 0x260 (R/W  32) SpW Router Table (router_table_nb = 32) 120 */
  __IO  uint32_t                       SPW_ROUTER_TABLE121; /**< Offset: 0x264 (R/W  32) SpW Router Table (router_table_nb = 32) 121 */
  __IO  uint32_t                       SPW_ROUTER_TABLE122; /**< Offset: 0x268 (R/W  32) SpW Router Table (router_table_nb = 32) 122 */
  __IO  uint32_t                       SPW_ROUTER_TABLE123; /**< Offset: 0x26C (R/W  32) SpW Router Table (router_table_nb = 32) 123 */
  __IO  uint32_t                       SPW_ROUTER_TABLE124; /**< Offset: 0x270 (R/W  32) SpW Router Table (router_table_nb = 32) 124 */
  __IO  uint32_t                       SPW_ROUTER_TABLE125; /**< Offset: 0x274 (R/W  32) SpW Router Table (router_table_nb = 32) 125 */
  __IO  uint32_t                       SPW_ROUTER_TABLE126; /**< Offset: 0x278 (R/W  32) SpW Router Table (router_table_nb = 32) 126 */
  __IO  uint32_t                       SPW_ROUTER_TABLE127; /**< Offset: 0x27C (R/W  32) SpW Router Table (router_table_nb = 32) 127 */
  __IO  uint32_t                       SPW_ROUTER_TABLE128; /**< Offset: 0x280 (R/W  32) SpW Router Table (router_table_nb = 32) 128 */
  __IO  uint32_t                       SPW_ROUTER_TABLE129; /**< Offset: 0x284 (R/W  32) SpW Router Table (router_table_nb = 32) 129 */
  __IO  uint32_t                       SPW_ROUTER_TABLE130; /**< Offset: 0x288 (R/W  32) SpW Router Table (router_table_nb = 32) 130 */
  __IO  uint32_t                       SPW_ROUTER_TABLE131; /**< Offset: 0x28C (R/W  32) SpW Router Table (router_table_nb = 32) 131 */
  __IO  uint32_t                       SPW_ROUTER_TABLE132; /**< Offset: 0x290 (R/W  32) SpW Router Table (router_table_nb = 32) 132 */
  __IO  uint32_t                       SPW_ROUTER_TABLE133; /**< Offset: 0x294 (R/W  32) SpW Router Table (router_table_nb = 32) 133 */
  __IO  uint32_t                       SPW_ROUTER_TABLE134; /**< Offset: 0x298 (R/W  32) SpW Router Table (router_table_nb = 32) 134 */
  __IO  uint32_t                       SPW_ROUTER_TABLE135; /**< Offset: 0x29C (R/W  32) SpW Router Table (router_table_nb = 32) 135 */
  __IO  uint32_t                       SPW_ROUTER_TABLE136; /**< Offset: 0x2A0 (R/W  32) SpW Router Table (router_table_nb = 32) 136 */
  __IO  uint32_t                       SPW_ROUTER_TABLE137; /**< Offset: 0x2A4 (R/W  32) SpW Router Table (router_table_nb = 32) 137 */
  __IO  uint32_t                       SPW_ROUTER_TABLE138; /**< Offset: 0x2A8 (R/W  32) SpW Router Table (router_table_nb = 32) 138 */
  __IO  uint32_t                       SPW_ROUTER_TABLE139; /**< Offset: 0x2AC (R/W  32) SpW Router Table (router_table_nb = 32) 139 */
  __IO  uint32_t                       SPW_ROUTER_TABLE140; /**< Offset: 0x2B0 (R/W  32) SpW Router Table (router_table_nb = 32) 140 */
  __IO  uint32_t                       SPW_ROUTER_TABLE141; /**< Offset: 0x2B4 (R/W  32) SpW Router Table (router_table_nb = 32) 141 */
  __IO  uint32_t                       SPW_ROUTER_TABLE142; /**< Offset: 0x2B8 (R/W  32) SpW Router Table (router_table_nb = 32) 142 */
  __IO  uint32_t                       SPW_ROUTER_TABLE143; /**< Offset: 0x2BC (R/W  32) SpW Router Table (router_table_nb = 32) 143 */
  __IO  uint32_t                       SPW_ROUTER_TABLE144; /**< Offset: 0x2C0 (R/W  32) SpW Router Table (router_table_nb = 32) 144 */
  __IO  uint32_t                       SPW_ROUTER_TABLE145; /**< Offset: 0x2C4 (R/W  32) SpW Router Table (router_table_nb = 32) 145 */
  __IO  uint32_t                       SPW_ROUTER_TABLE146; /**< Offset: 0x2C8 (R/W  32) SpW Router Table (router_table_nb = 32) 146 */
  __IO  uint32_t                       SPW_ROUTER_TABLE147; /**< Offset: 0x2CC (R/W  32) SpW Router Table (router_table_nb = 32) 147 */
  __IO  uint32_t                       SPW_ROUTER_TABLE148; /**< Offset: 0x2D0 (R/W  32) SpW Router Table (router_table_nb = 32) 148 */
  __IO  uint32_t                       SPW_ROUTER_TABLE149; /**< Offset: 0x2D4 (R/W  32) SpW Router Table (router_table_nb = 32) 149 */
  __IO  uint32_t                       SPW_ROUTER_TABLE150; /**< Offset: 0x2D8 (R/W  32) SpW Router Table (router_table_nb = 32) 150 */
  __IO  uint32_t                       SPW_ROUTER_TABLE151; /**< Offset: 0x2DC (R/W  32) SpW Router Table (router_table_nb = 32) 151 */
  __IO  uint32_t                       SPW_ROUTER_TABLE152; /**< Offset: 0x2E0 (R/W  32) SpW Router Table (router_table_nb = 32) 152 */
  __IO  uint32_t                       SPW_ROUTER_TABLE153; /**< Offset: 0x2E4 (R/W  32) SpW Router Table (router_table_nb = 32) 153 */
  __IO  uint32_t                       SPW_ROUTER_TABLE154; /**< Offset: 0x2E8 (R/W  32) SpW Router Table (router_table_nb = 32) 154 */
  __IO  uint32_t                       SPW_ROUTER_TABLE155; /**< Offset: 0x2EC (R/W  32) SpW Router Table (router_table_nb = 32) 155 */
  __IO  uint32_t                       SPW_ROUTER_TABLE156; /**< Offset: 0x2F0 (R/W  32) SpW Router Table (router_table_nb = 32) 156 */
  __IO  uint32_t                       SPW_ROUTER_TABLE157; /**< Offset: 0x2F4 (R/W  32) SpW Router Table (router_table_nb = 32) 157 */
  __IO  uint32_t                       SPW_ROUTER_TABLE158; /**< Offset: 0x2F8 (R/W  32) SpW Router Table (router_table_nb = 32) 158 */
  __IO  uint32_t                       SPW_ROUTER_TABLE159; /**< Offset: 0x2FC (R/W  32) SpW Router Table (router_table_nb = 32) 159 */
  __IO  uint32_t                       SPW_ROUTER_TABLE160; /**< Offset: 0x300 (R/W  32) SpW Router Table (router_table_nb = 32) 160 */
  __IO  uint32_t                       SPW_ROUTER_TABLE161; /**< Offset: 0x304 (R/W  32) SpW Router Table (router_table_nb = 32) 161 */
  __IO  uint32_t                       SPW_ROUTER_TABLE162; /**< Offset: 0x308 (R/W  32) SpW Router Table (router_table_nb = 32) 162 */
  __IO  uint32_t                       SPW_ROUTER_TABLE163; /**< Offset: 0x30C (R/W  32) SpW Router Table (router_table_nb = 32) 163 */
  __IO  uint32_t                       SPW_ROUTER_TABLE164; /**< Offset: 0x310 (R/W  32) SpW Router Table (router_table_nb = 32) 164 */
  __IO  uint32_t                       SPW_ROUTER_TABLE165; /**< Offset: 0x314 (R/W  32) SpW Router Table (router_table_nb = 32) 165 */
  __IO  uint32_t                       SPW_ROUTER_TABLE166; /**< Offset: 0x318 (R/W  32) SpW Router Table (router_table_nb = 32) 166 */
  __IO  uint32_t                       SPW_ROUTER_TABLE167; /**< Offset: 0x31C (R/W  32) SpW Router Table (router_table_nb = 32) 167 */
  __IO  uint32_t                       SPW_ROUTER_TABLE168; /**< Offset: 0x320 (R/W  32) SpW Router Table (router_table_nb = 32) 168 */
  __IO  uint32_t                       SPW_ROUTER_TABLE169; /**< Offset: 0x324 (R/W  32) SpW Router Table (router_table_nb = 32) 169 */
  __IO  uint32_t                       SPW_ROUTER_TABLE170; /**< Offset: 0x328 (R/W  32) SpW Router Table (router_table_nb = 32) 170 */
  __IO  uint32_t                       SPW_ROUTER_TABLE171; /**< Offset: 0x32C (R/W  32) SpW Router Table (router_table_nb = 32) 171 */
  __IO  uint32_t                       SPW_ROUTER_TABLE172; /**< Offset: 0x330 (R/W  32) SpW Router Table (router_table_nb = 32) 172 */
  __IO  uint32_t                       SPW_ROUTER_TABLE173; /**< Offset: 0x334 (R/W  32) SpW Router Table (router_table_nb = 32) 173 */
  __IO  uint32_t                       SPW_ROUTER_TABLE174; /**< Offset: 0x338 (R/W  32) SpW Router Table (router_table_nb = 32) 174 */
  __IO  uint32_t                       SPW_ROUTER_TABLE175; /**< Offset: 0x33C (R/W  32) SpW Router Table (router_table_nb = 32) 175 */
  __IO  uint32_t                       SPW_ROUTER_TABLE176; /**< Offset: 0x340 (R/W  32) SpW Router Table (router_table_nb = 32) 176 */
  __IO  uint32_t                       SPW_ROUTER_TABLE177; /**< Offset: 0x344 (R/W  32) SpW Router Table (router_table_nb = 32) 177 */
  __IO  uint32_t                       SPW_ROUTER_TABLE178; /**< Offset: 0x348 (R/W  32) SpW Router Table (router_table_nb = 32) 178 */
  __IO  uint32_t                       SPW_ROUTER_TABLE179; /**< Offset: 0x34C (R/W  32) SpW Router Table (router_table_nb = 32) 179 */
  __IO  uint32_t                       SPW_ROUTER_TABLE180; /**< Offset: 0x350 (R/W  32) SpW Router Table (router_table_nb = 32) 180 */
  __IO  uint32_t                       SPW_ROUTER_TABLE181; /**< Offset: 0x354 (R/W  32) SpW Router Table (router_table_nb = 32) 181 */
  __IO  uint32_t                       SPW_ROUTER_TABLE182; /**< Offset: 0x358 (R/W  32) SpW Router Table (router_table_nb = 32) 182 */
  __IO  uint32_t                       SPW_ROUTER_TABLE183; /**< Offset: 0x35C (R/W  32) SpW Router Table (router_table_nb = 32) 183 */
  __IO  uint32_t                       SPW_ROUTER_TABLE184; /**< Offset: 0x360 (R/W  32) SpW Router Table (router_table_nb = 32) 184 */
  __IO  uint32_t                       SPW_ROUTER_TABLE185; /**< Offset: 0x364 (R/W  32) SpW Router Table (router_table_nb = 32) 185 */
  __IO  uint32_t                       SPW_ROUTER_TABLE186; /**< Offset: 0x368 (R/W  32) SpW Router Table (router_table_nb = 32) 186 */
  __IO  uint32_t                       SPW_ROUTER_TABLE187; /**< Offset: 0x36C (R/W  32) SpW Router Table (router_table_nb = 32) 187 */
  __IO  uint32_t                       SPW_ROUTER_TABLE188; /**< Offset: 0x370 (R/W  32) SpW Router Table (router_table_nb = 32) 188 */
  __IO  uint32_t                       SPW_ROUTER_TABLE189; /**< Offset: 0x374 (R/W  32) SpW Router Table (router_table_nb = 32) 189 */
  __IO  uint32_t                       SPW_ROUTER_TABLE190; /**< Offset: 0x378 (R/W  32) SpW Router Table (router_table_nb = 32) 190 */
  __IO  uint32_t                       SPW_ROUTER_TABLE191; /**< Offset: 0x37C (R/W  32) SpW Router Table (router_table_nb = 32) 191 */
  __IO  uint32_t                       SPW_ROUTER_TABLE192; /**< Offset: 0x380 (R/W  32) SpW Router Table (router_table_nb = 32) 192 */
  __IO  uint32_t                       SPW_ROUTER_TABLE193; /**< Offset: 0x384 (R/W  32) SpW Router Table (router_table_nb = 32) 193 */
  __IO  uint32_t                       SPW_ROUTER_TABLE194; /**< Offset: 0x388 (R/W  32) SpW Router Table (router_table_nb = 32) 194 */
  __IO  uint32_t                       SPW_ROUTER_TABLE195; /**< Offset: 0x38C (R/W  32) SpW Router Table (router_table_nb = 32) 195 */
  __IO  uint32_t                       SPW_ROUTER_TABLE196; /**< Offset: 0x390 (R/W  32) SpW Router Table (router_table_nb = 32) 196 */
  __IO  uint32_t                       SPW_ROUTER_TABLE197; /**< Offset: 0x394 (R/W  32) SpW Router Table (router_table_nb = 32) 197 */
  __IO  uint32_t                       SPW_ROUTER_TABLE198; /**< Offset: 0x398 (R/W  32) SpW Router Table (router_table_nb = 32) 198 */
  __IO  uint32_t                       SPW_ROUTER_TABLE199; /**< Offset: 0x39C (R/W  32) SpW Router Table (router_table_nb = 32) 199 */
  __IO  uint32_t                       SPW_ROUTER_TABLE200; /**< Offset: 0x3A0 (R/W  32) SpW Router Table (router_table_nb = 32) 200 */
  __IO  uint32_t                       SPW_ROUTER_TABLE201; /**< Offset: 0x3A4 (R/W  32) SpW Router Table (router_table_nb = 32) 201 */
  __IO  uint32_t                       SPW_ROUTER_TABLE202; /**< Offset: 0x3A8 (R/W  32) SpW Router Table (router_table_nb = 32) 202 */
  __IO  uint32_t                       SPW_ROUTER_TABLE203; /**< Offset: 0x3AC (R/W  32) SpW Router Table (router_table_nb = 32) 203 */
  __IO  uint32_t                       SPW_ROUTER_TABLE204; /**< Offset: 0x3B0 (R/W  32) SpW Router Table (router_table_nb = 32) 204 */
  __IO  uint32_t                       SPW_ROUTER_TABLE205; /**< Offset: 0x3B4 (R/W  32) SpW Router Table (router_table_nb = 32) 205 */
  __IO  uint32_t                       SPW_ROUTER_TABLE206; /**< Offset: 0x3B8 (R/W  32) SpW Router Table (router_table_nb = 32) 206 */
  __IO  uint32_t                       SPW_ROUTER_TABLE207; /**< Offset: 0x3BC (R/W  32) SpW Router Table (router_table_nb = 32) 207 */
  __IO  uint32_t                       SPW_ROUTER_TABLE208; /**< Offset: 0x3C0 (R/W  32) SpW Router Table (router_table_nb = 32) 208 */
  __IO  uint32_t                       SPW_ROUTER_TABLE209; /**< Offset: 0x3C4 (R/W  32) SpW Router Table (router_table_nb = 32) 209 */
  __IO  uint32_t                       SPW_ROUTER_TABLE210; /**< Offset: 0x3C8 (R/W  32) SpW Router Table (router_table_nb = 32) 210 */
  __IO  uint32_t                       SPW_ROUTER_TABLE211; /**< Offset: 0x3CC (R/W  32) SpW Router Table (router_table_nb = 32) 211 */
  __IO  uint32_t                       SPW_ROUTER_TABLE212; /**< Offset: 0x3D0 (R/W  32) SpW Router Table (router_table_nb = 32) 212 */
  __IO  uint32_t                       SPW_ROUTER_TABLE213; /**< Offset: 0x3D4 (R/W  32) SpW Router Table (router_table_nb = 32) 213 */
  __IO  uint32_t                       SPW_ROUTER_TABLE214; /**< Offset: 0x3D8 (R/W  32) SpW Router Table (router_table_nb = 32) 214 */
  __IO  uint32_t                       SPW_ROUTER_TABLE215; /**< Offset: 0x3DC (R/W  32) SpW Router Table (router_table_nb = 32) 215 */
  __IO  uint32_t                       SPW_ROUTER_TABLE216; /**< Offset: 0x3E0 (R/W  32) SpW Router Table (router_table_nb = 32) 216 */
  __IO  uint32_t                       SPW_ROUTER_TABLE217; /**< Offset: 0x3E4 (R/W  32) SpW Router Table (router_table_nb = 32) 217 */
  __IO  uint32_t                       SPW_ROUTER_TABLE218; /**< Offset: 0x3E8 (R/W  32) SpW Router Table (router_table_nb = 32) 218 */
  __IO  uint32_t                       SPW_ROUTER_TABLE219; /**< Offset: 0x3EC (R/W  32) SpW Router Table (router_table_nb = 32) 219 */
  __IO  uint32_t                       SPW_ROUTER_TABLE220; /**< Offset: 0x3F0 (R/W  32) SpW Router Table (router_table_nb = 32) 220 */
  __IO  uint32_t                       SPW_ROUTER_TABLE221; /**< Offset: 0x3F4 (R/W  32) SpW Router Table (router_table_nb = 32) 221 */
  __IO  uint32_t                       SPW_ROUTER_TABLE222; /**< Offset: 0x3F8 (R/W  32) SpW Router Table (router_table_nb = 32) 222 */
  __IO  uint32_t                       SPW_ROUTER_TABLE223; /**< Offset: 0x3FC (R/W  32) SpW Router Table (router_table_nb = 32) 223 */
  __I   uint32_t                       SPW_LINK1_PI_RM; /**< Offset: 0x400 (R/   32) SpW Link 1 Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_LINK1_PI_RCM; /**< Offset: 0x404 (R/   32) SpW Link 1 Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_LINK1_PI_R;  /**< Offset: 0x408 (R/   32) SpW Link 1 Pending Read Interrupt */
  __IO  uint32_t                       SPW_LINK1_PI_RCS; /**< Offset: 0x40C (R/W  32) SpW Link 1 Pending Read, Clear and Enabed Interrupt */
  __IO  uint32_t                       SPW_LINK1_IM;    /**< Offset: 0x410 (R/W  32) SpW Link 1 Interrupt Mask */
  __O   uint32_t                       SPW_LINK1_PI_C;  /**< Offset: 0x414 ( /W  32) SpW Link 1 Clear Pending Interrupt */
  __O   uint32_t                       SPW_LINK1_IM_S;  /**< Offset: 0x418 ( /W  32) SpW Link 1 Interrupt Set Mask */
  __O   uint32_t                       SPW_LINK1_IM_C;  /**< Offset: 0x41C ( /W  32) SpW Link 1 Interrupt Clear Mask */
  __IO  uint32_t                       SPW_LINK1_CFG;   /**< Offset: 0x420 (R/W  32) SpW Link 1 Config */
  __IO  uint32_t                       SPW_LINK1_CLKDIV; /**< Offset: 0x424 (R/W  32) SpW Link 1 Clock Division */
  __I   uint32_t                       SPW_LINK1_STATUS; /**< Offset: 0x428 (R/   32) SpW Link 1 Status */
  __IO  uint32_t                       SPW_LINK1_SWRESET; /**< Offset: 0x42C (R/W  32) SpW Link 1 Software Reset */
  __IO  uint32_t                       SPW_LINK1_ESCCHAREVENT0; /**< Offset: 0x430 (R/W  32) SpW Link 1 Escape Character Event 0 */
  __IO  uint32_t                       SPW_LINK1_ESCCHAREVENT1; /**< Offset: 0x434 (R/W  32) SpW Link 1 Escape Character Event 1 */
  __I   uint32_t                       SPW_LINK1_ESCCHARSTS; /**< Offset: 0x438 (R/   32) SpW Link 1 Escape Character Status */
  __IO  uint32_t                       SPW_LINK1_TRANSESC; /**< Offset: 0x43C (R/W  32) SpW Link 1 Transmit Escape Character */
  __I   uint32_t                       SPW_LINK1_DISTINTPI_RM; /**< Offset: 0x440 (R/   32) SpW Link 1 Distributed Interrupt Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_LINK1_DISTINTPI_RCM; /**< Offset: 0x444 (R/   32) SpW Link 1 Distributed Interrupt Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_LINK1_DISTINTPI_R; /**< Offset: 0x448 (R/   32) SpW Link 1 Distributed Interrupt Pending Read Interrupt */
  __IO  uint32_t                       SPW_LINK1_DISTINTPI_RCS; /**< Offset: 0x44C (R/W  32) SpW Link 1 Distributed Interrupt Pending Read and Clear Interrupt */
  __IO  uint32_t                       SPW_LINK1_DISTINTIM; /**< Offset: 0x450 (R/W  32) SpW Link 1 Distributed Interrupt Mask */
  __O   uint32_t                       SPW_LINK1_DISTINTPI_C; /**< Offset: 0x454 ( /W  32) SpW Link 1 Distributed Interrupt Clear Pending Interrupt */
  __O   uint32_t                       SPW_LINK1_DISTINTIM_S; /**< Offset: 0x458 ( /W  32) SpW Link 1 Distributed Interrupt Set Mask */
  __O   uint32_t                       SPW_LINK1_DISTINTIM_C; /**< Offset: 0x45C ( /W  32) SpW Link 1 Distributed Interrupt Clear Mask */
  __I   uint32_t                       SPW_LINK1_DISTACKPI_RM; /**< Offset: 0x460 (R/   32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_LINK1_DISTACKPI_RCM; /**< Offset: 0x464 (R/   32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_LINK1_DISTACKPI_R; /**< Offset: 0x468 (R/   32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read Interrupt */
  __IO  uint32_t                       SPW_LINK1_DISTACKPI_RCS; /**< Offset: 0x46C (R/W  32) SpW Link 1 Distributed Interrupt Acknowledge Pending Read and Clear Interrupt */
  __IO  uint32_t                       SPW_LINK1_DISTACKIM; /**< Offset: 0x470 (R/W  32) SpW Link 1 Distributed Interrupt Acknowledge Mask */
  __O   uint32_t                       SPW_LINK1_DISTACKPI_C; /**< Offset: 0x474 ( /W  32) SpW Link 1 Distributed Interrupt Acknowledge Clear Pending Interrupt */
  __O   uint32_t                       SPW_LINK1_DISTACKIM_S; /**< Offset: 0x478 ( /W  32) SpW Link 1 Distributed Interrupt Acknowledge Set Mask */
  __O   uint32_t                       SPW_LINK1_DISTACKIM_C; /**< Offset: 0x47C ( /W  32) SpW Link 1 Distributed Interrupt Acknowledge Clear Mask */
  __I   uint32_t                       SPW_LINK2_PI_RM; /**< Offset: 0x480 (R/   32) SpW Link 2 Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_LINK2_PI_RCM; /**< Offset: 0x484 (R/   32) SpW Link 2 Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_LINK2_PI_R;  /**< Offset: 0x488 (R/   32) SpW Link 2 Pending Read Interrupt */
  __IO  uint32_t                       SPW_LINK2_PI_RCS; /**< Offset: 0x48C (R/W  32) SpW Link 2 Pending Read, Clear and Enabled Interrupt */
  __IO  uint32_t                       SPW_LINK2_IM;    /**< Offset: 0x490 (R/W  32) SpW Link 2 Interrupt Mask */
  __O   uint32_t                       SPW_LINK2_PI_C;  /**< Offset: 0x494 ( /W  32) SpW Link 2 Clear Pending Interrupt */
  __O   uint32_t                       SPW_LINK2_IM_S;  /**< Offset: 0x498 ( /W  32) SpW Link 2 Interrupt Set Mask */
  __O   uint32_t                       SPW_LINK2_IM_C;  /**< Offset: 0x49C ( /W  32) SpW Link 2 Interrupt Clear Mask */
  __IO  uint32_t                       SPW_LINK2_CFG;   /**< Offset: 0x4A0 (R/W  32) SpW Link 2 Config */
  __IO  uint32_t                       SPW_LINK2_CLKDIV; /**< Offset: 0x4A4 (R/W  32) SpW Link 2 Clock Division */
  __I   uint32_t                       SPW_LINK2_STATUS; /**< Offset: 0x4A8 (R/   32) SpW Link 2 Status */
  __IO  uint32_t                       SPW_LINK2_SWRESET; /**< Offset: 0x4AC (R/W  32) SpW Link 2 Software Reset */
  __IO  uint32_t                       SPW_LINK2_ESCCHAREVENT0; /**< Offset: 0x4B0 (R/W  32) SpW Link 2 Escape Character Event 0 */
  __IO  uint32_t                       SPW_LINK2_ESCCHAREVENT1; /**< Offset: 0x4B4 (R/W  32) SpW Link 2 Escape Character Event 1 */
  __I   uint32_t                       SPW_LINK2_ESCCHARSTS; /**< Offset: 0x4B8 (R/   32) SpW Link 2 Escape Character Status */
  __IO  uint32_t                       SPW_LINK2_TRANSESC; /**< Offset: 0x4BC (R/W  32) SpW Link 2 Transmit Escape Character */
  __I   uint32_t                       SPW_LINK2_DISTINTPI_RM; /**< Offset: 0x4C0 (R/   32) SpW Link 2 Distributed Interrupt Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_LINK2_DISTINTPI_RCM; /**< Offset: 0x4C4 (R/   32) SpW Link 2 Distributed Interrupt Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_LINK2_DISTINTPI_R; /**< Offset: 0x4C8 (R/   32) SpW Link 2 Distributed Interrupt Pending Read Interrupt */
  __IO  uint32_t                       SPW_LINK2_DISTINTPI_RCS; /**< Offset: 0x4CC (R/W  32) SpW Link 2 Distributed Interrupt Pending Read and Clear Interrupt */
  __IO  uint32_t                       SPW_LINK2_DISTINTIM; /**< Offset: 0x4D0 (R/W  32) SpW Link 2 Distributed Interrupt Mask */
  __O   uint32_t                       SPW_LINK2_DISTINTPI_C; /**< Offset: 0x4D4 ( /W  32) SpW Link 2 Distributed Interrupt Clear Pending Interrupt */
  __O   uint32_t                       SPW_LINK2_DISTINTIM_S; /**< Offset: 0x4D8 ( /W  32) SpW Link 2 Distributed Interrupt Set Mask */
  __O   uint32_t                       SPW_LINK2_DISTINTIM_C; /**< Offset: 0x4DC ( /W  32) SpW Link 2 Distributed Interrupt Clear Mask */
  __I   uint32_t                       SPW_LINK2_DISTACKPI_RM; /**< Offset: 0x4E0 (R/   32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_LINK2_DISTACKPI_RCM; /**< Offset: 0x4E4 (R/   32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_LINK2_DISTACKPI_R; /**< Offset: 0x4E8 (R/   32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read Interrupt */
  __IO  uint32_t                       SPW_LINK2_DISTACKPI_RCS; /**< Offset: 0x4EC (R/W  32) SpW Link 2 Distributed Interrupt Acknowledge Pending Read and Clear Interrupt */
  __IO  uint32_t                       SPW_LINK2_DISTACKIM; /**< Offset: 0x4F0 (R/W  32) SpW Link 2 Distributed Interrupt Acknowledge Mask */
  __O   uint32_t                       SPW_LINK2_DISTACKPI_C; /**< Offset: 0x4F4 ( /W  32) SpW Link 2 Distributed Interrupt Acknowledge Clear Pending Interrupt */
  __O   uint32_t                       SPW_LINK2_DISTACKIM_S; /**< Offset: 0x4F8 ( /W  32) SpW Link 2 Distributed Interrupt Acknowledge Set Mask */
  __O   uint32_t                       SPW_LINK2_DISTACKIM_C; /**< Offset: 0x4FC ( /W  32) SpW Link 2 Distributed Interrupt Acknowledge Clear Mask */
  __I   uint8_t                        Reserved2[0x300];
  __I   uint32_t                       SPW_PKTRX1_PI_RM; /**< Offset: 0x800 (R/   32) PktRx Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_PKTRX1_PI_RCM; /**< Offset: 0x804 (R/   32) PktRx Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_PKTRX1_PI_R; /**< Offset: 0x808 (R/   32) PktRx Pending Read Interrupt */
  __IO  uint32_t                       SPW_PKTRX1_PI_RCS; /**< Offset: 0x80C (R/W  32) PktRx Pending Read, Clear and Enabled Interrupt */
  __IO  uint32_t                       SPW_PKTRX1_IM;   /**< Offset: 0x810 (R/W  32) PktRx Interrupt Mask */
  __O   uint32_t                       SPW_PKTRX1_PI_C; /**< Offset: 0x814 ( /W  32) PktRx Clear Pending Interrupt */
  __O   uint32_t                       SPW_PKTRX1_IM_S; /**< Offset: 0x818 ( /W  32) PktRx Interrupt Set Mask */
  __O   uint32_t                       SPW_PKTRX1_IM_C; /**< Offset: 0x81C ( /W  32) PktRx Interrupt Clear Mask */
  __IO  uint32_t                       SPW_PKTRX1_CFG;  /**< Offset: 0x820 (R/W  32) PktRx Config */
  __I   uint32_t                       SPW_PKTRX1_STATUS; /**< Offset: 0x824 (R/   32) PktRx Status */
  __I   uint8_t                        Reserved3[0x08];
  __IO  uint32_t                       SPW_PKTRX1_NXTBUFDATAADDR; /**< Offset: 0x830 (R/W  32) PktRx Next Buffer Data Address */
  __IO  uint32_t                       SPW_PKTRX1_NXTBUFDATALEN; /**< Offset: 0x834 (R/W  32) PktRx Next Buffer Data Length */
  __IO  uint32_t                       SPW_PKTRX1_NXTBUFPKTADDR; /**< Offset: 0x838 (R/W  32) PktRx Next Buffer Packet Address */
  __IO  uint32_t                       SPW_PKTRX1_NXTBUFCFG; /**< Offset: 0x83C (R/W  32) PktRx Next Buffer Config */
  __I   uint32_t                       SPW_PKTRX1_CURBUFDATAADDR; /**< Offset: 0x840 (R/   32) PktRx Current Buffer Data Address */
  __I   uint32_t                       SPW_PKTRX1_CURBUFDATALEN; /**< Offset: 0x844 (R/   32) PktRx Current Buffer Data Length */
  __I   uint32_t                       SPW_PKTRX1_CURBUFPKTADDR; /**< Offset: 0x848 (R/   32) PktRx Current Buffer Packet Address */
  __IO  uint32_t                       SPW_PKTRX1_CURBUFCFG; /**< Offset: 0x84C (R/W  32) PktRx Current Buffer Config */
  __I   uint32_t                       SPW_PKTRX1_PREVBUFDATALEN; /**< Offset: 0x850 (R/   32) PktRx Previous Buffer Data Length */
  __I   uint32_t                       SPW_PKTRX1_PREVBUFSTS; /**< Offset: 0x854 (R/   32) PktRx Previous Buffer Status */
  __I   uint8_t                        Reserved4[0x24];
  __IO  uint32_t                       SPW_PKTRX1_SWRESET; /**< Offset: 0x87C (R/W  32) PktRx Software Reset */
  __I   uint8_t                        Reserved5[0x380];
  __I   uint32_t                       SPW_PKTTX1_PI_RM; /**< Offset: 0xC00 (R/   32) PktTx Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_PKTTX1_PI_RCM; /**< Offset: 0xC04 (R/   32) PktTx Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_PKTTX1_PI_R; /**< Offset: 0xC08 (R/   32) PktTx Pending Read Interrupt */
  __IO  uint32_t                       SPW_PKTTX1_PI_RCS; /**< Offset: 0xC0C (R/W  32) PktTx Pending Read, Clear and Enabled Interrupt */
  __IO  uint32_t                       SPW_PKTTX1_IM;   /**< Offset: 0xC10 (R/W  32) PktTx Interrupt Mask */
  __O   uint32_t                       SPW_PKTTX1_PI_C; /**< Offset: 0xC14 ( /W  32) PktTx Clear Pending Interrupt */
  __O   uint32_t                       SPW_PKTTX1_IM_S; /**< Offset: 0xC18 ( /W  32) PktTx Interrupt Set Mask */
  __O   uint32_t                       SPW_PKTTX1_IM_C; /**< Offset: 0xC1C ( /W  32) PktTx Interrupt Clear Mask */
  __IO  uint32_t                       SPW_PKTTX1_STATUS; /**< Offset: 0xC20 (R/W  32) PktTx Status */
  __IO  uint32_t                       SPW_PKTTX1_NXTSENDROUT; /**< Offset: 0xC24 (R/W  32) PktTx Next Send List Router Bytes */
  __IO  uint32_t                       SPW_PKTTX1_NXTSENDADDR; /**< Offset: 0xC28 (R/W  32) PktTx Next Send List Address */
  __IO  uint32_t                       SPW_PKTTX1_NXTSENDCFG; /**< Offset: 0xC2C (R/W  32) PktTx Next Send List Config */
  __I   uint32_t                       SPW_PKTTX1_CURSENDROUT; /**< Offset: 0xC30 (R/   32) PktTx Current Send List Router Bytes */
  __I   uint32_t                       SPW_PKTTX1_CURSENDADDR; /**< Offset: 0xC34 (R/   32) PktTx Current Send List Address */
  __IO  uint32_t                       SPW_PKTTX1_CURSENDCFG; /**< Offset: 0xC38 (R/W  32) PktTx Current Send List Config */
  __IO  uint32_t                       SPW_PKTTX1_SWRESET; /**< Offset: 0xC3C (R/W  32) PktTx Software Reset */
  __I   uint8_t                        Reserved6[0x1C0];
  __IO  uint32_t                       SPW_RMAP1_CFG;   /**< Offset: 0xE00 (R/W  32) SpW RMAP 1 Config */
  __I   uint32_t                       SPW_RMAP1_STS_RC; /**< Offset: 0xE04 (R/   32) SpW RMAP 1 Read and Clear Status */
  __I   uint32_t                       SPW_RMAP1_STS;   /**< Offset: 0xE08 (R/   32) SpW RMAP 1 Read Status */
  __I   uint8_t                        Reserved7[0x74];
  __I   uint32_t                       SPW_TCH_PI_RM;   /**< Offset: 0xE80 (R/   32) SpW Tch Pending Read Masked Interrupt */
  __I   uint32_t                       SPW_TCH_PI_RCM;  /**< Offset: 0xE84 (R/   32) SpW Tch Pending Read and Clear Masked Interrupt */
  __I   uint32_t                       SPW_TCH_PI_R;    /**< Offset: 0xE88 (R/   32) SpW Tch Pending Read Interrupt */
  __IO  uint32_t                       SPW_TCH_PI_RCS;  /**< Offset: 0xE8C (R/W  32) SpW Tch Pending Read, Clear and Enabled Interrupt */
  __IO  uint32_t                       SPW_TCH_IM;      /**< Offset: 0xE90 (R/W  32) SpW Tch Interrupt Mask */
  __O   uint32_t                       SPW_TCH_PI_C;    /**< Offset: 0xE94 ( /W  32) SpW Tch Clear Pending Interrupt */
  __O   uint32_t                       SPW_TCH_IM_S;    /**< Offset: 0xE98 ( /W  32) SpW Tch Interrupt Set Mask */
  __O   uint32_t                       SPW_TCH_IM_C;    /**< Offset: 0xE9C ( /W  32) SpW Tch Interrupt Clear Mask */
  __IO  uint32_t                       SPW_TCH_CFGLISTEN; /**< Offset: 0xEA0 (R/W  32) SpW Tch Config Listener */
  __IO  uint32_t                       SPW_TCH_CFGSEND; /**< Offset: 0xEA4 (R/W  32) SpW Tch Config Sender */
  __IO  uint32_t                       SPW_TCH_CFG;     /**< Offset: 0xEA8 (R/W  32) SpW Tch Config */
  __IO  uint32_t                       SPW_TCH_CFGRESTART; /**< Offset: 0xEAC (R/W  32) SpW Tch Config Restart */
  __IO  uint32_t                       SPW_TCH_CFGTCEVENT; /**< Offset: 0xEB0 (R/W  32) SpW Tch Config Tc Event */
  __IO  uint32_t                       SPW_TCH_CFGWD;   /**< Offset: 0xEB4 (R/W  32) SpW Tch Config Watchdog */
  __IO  uint32_t                       SPW_TCH_LASTTIMECODE; /**< Offset: 0xEB8 (R/W  32) SpW Tch Last Time Code */
  __IO  uint32_t                       SPW_TCH_SWRESET; /**< Offset: 0xEBC (R/W  32) SpW Tch Software Reset */
  __I   uint8_t                        Reserved8[0x40];
  __I   uint32_t                       SPW_GROUP_IRQSTS1; /**< Offset: 0xF00 (R/   32) SpW Group Interrupt status 1 */
  __I   uint32_t                       SPW_GROUP_IRQSTS2; /**< Offset: 0xF04 (R/   32) SpW Group Interrupt status 2 */
  __I   uint32_t                       SPW_GROUP_EDACSTS; /**< Offset: 0xF08 (R/   32) SpW Group Interrupt status */
} spw_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAMRH71_SPW_COMPONENT_H_ */
