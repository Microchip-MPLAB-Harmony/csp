#ifndef _DRV_CAN_LOCAL_INCLUDE_
#define _DRV_CAN_LOCAL_INCLUDE_


#ifdef __cplusplus
extern "C" {
#endif


typedef enum
{
    CAN_STD_FILTER_RANGE = 0,
    CAN_STD_FILTER_DUAL,
    CAN_STD_FILTER_CLASSIC
} CAN_STD_TYPE;


typedef enum
{
    CAN_FILTER_CONFIG_DISABLED = 0,
    CAN_FILTER_CONFIG_FIFO_0,
    CAN_FILTER_CONFIG_FIFO_1,
    CAN_FILTER_CONFIG_REJECT,
    CAN_FILTER_CONFIG_PRIORITY,
    CAN_FILTER_CONFIG_PRIORITY_FIFO_0,
    CAN_FILTER_CONFIG_PRIORITY_FIFO_1,
} CAN_CONFIG;


typedef enum
{
    CAN_EXT_FILTER_RANGE=0,
    CAN_EXT_FILTER_DUAL,
    CAN_EXT_FILTER_CLASSIC,
    CAN_EXT_FILTER_UNMASKED
} CAN_EXT_TYPE;


typedef enum {
    CAN_CHANNEL0 = 0x00,
    CAN_CHANNEL1 = 0x01,
    CAN_TOTAL_CHANNELS
} CAN_CHANNEL;



/**
 * \brief CAN receive FIFO element.
 */
struct _can_rx_fifo_entry {
	union {
		struct {
			uint32_t ID:29;    /*!< Identifier */
			uint32_t RTR:1;    /*!< Remote Transmission Request */
			uint32_t XTD:1;    /*!< Extended Identifier */
			uint32_t ESI:1;    /*!< Error State Indicator */
		} bit;
		uint32_t val;          /*!< Type used for register access */
	} R0;
	union {
		struct {
			uint32_t RXTS:16;  /*!< Rx Timestamp */
			uint32_t DLC:4;    /*!< Data Length Code */
			uint32_t BRS:1;    /*!< Bit Rate Switch */
			uint32_t EDL:1;    /*!< FD Format */
			uint32_t :2;       /*!< Reserved */
			uint32_t FIDX:7;   /*!< Filter Index */
			uint32_t ANMF:1;   /*!< Accepted Non-matching Frame */
		} bit;
		uint32_t val;            /*!< Type used for register access */
	} R1;
	uint8_t *data;
};

/**
 * \brief CAN transmit FIFO element.
 */
struct _can_tx_fifo_entry 
{
	uint32_t T0;
	uint32_t T1;
	uint8_t data[];
};

#define MCAN_TXFE_DLC_Pos     (16)
#define MCAN_TXFE_DLC_Msk     (0xF << MCAN_TXFE_DLC_Pos)
#define MCAN_TXFE_DLC(value)  (MCAN_TXFE_DLC_Msk & ((value) << MCAN_TXFE_DLC_Pos))

#define MCAN_TXFE_XTD_Pos     (30)
#define MCAN_TXFE_XTD_Msk     (0x1 << MCAN_TXFE_XTD_Pos)


/**
 * \brief CAN transmit Event element.
 */
struct _can_tx_event_entry {
	union {
		struct {
			uint32_t ID:29;    /*!< Identifier */
			uint32_t RTR:1;    /*!< Remote Transmission Request */
			uint32_t XTD:1;    /*!< Extended Identifier */
			uint32_t ESI:1;    /*!< Error State Indicator */
		} bit;
		uint32_t val;          /*!< Type used for register access */
	} E0;
	union {
		struct {
			uint32_t TXTS:16;  /*!< Tx Timestamp */
			uint32_t DLC:4;    /*!< Data Length Code */
			uint32_t BRS:1;    /*!< Bit Rate Switch */
			uint32_t EDL:1;    /*!< FD Format */
			uint32_t ET:2;     /*!< Event Type */
			uint32_t MM:8;     /*!< Message Marker */
		} bit;
		uint32_t val;            /*!< Type used for register access */
	} E1;
};

/**
 * \brief CAN standard message ID filter element structure.
 *
 *  Common element structure for standard message ID filter element.
 */
struct _can_standard_message_filter_element {
	union {
		struct {
			uint32_t SFID2:11;   /*!< Standard Filter ID 2 */
			uint32_t :5;         /*!< Reserved */
			uint32_t SFID1:11;   /*!< Standard Filter ID 1 */
			uint32_t SFEC:3;     /*!< Standard Filter Configuration */
			uint32_t SFT:2;      /*!< Standard Filter Type */
		} bit;
		uint32_t val;            /*!< Type used for register access */
	} S0;
};

#define MCAN_SMF_SFID2_Pos     (0)
#define MCAN_SMF_SFID2_Msk     (0x7FFU << MCAN_SMF_SFID2_Pos)
#define MCAN_SMF_SFID2(value)  (MCAN_SMF_SFID2_Msk & ((value) << MCAN_SMF_SFID2_Pos))
#define MCAN_SMF_SFID1_Pos     (16)
#define MCAN_SMF_SFID1_Msk     (0x7FFU << MCAN_SMF_SFID1_Pos)
#define MCAN_SMF_SFID1(value)  (MCAN_SMF_SFID1_Msk & ((value) << MCAN_SMF_SFID1_Pos))
#define MCAN_SMF_SFEC_Pos      (27)
#define MCAN_SMF_SFEC_Msk      (0x7U << MCAN_SMF_SFEC_Pos)
#define MCAN_SMF_SFEC(value)   (MCAN_SMF_SFEC_Msk & ((value) << MCAN_SMF_SFEC_Pos))
#define MCAN_SMF_SFT_Pos       (30)
#define MCAN_SMF_SFT_Msk       (0x3U << MCAN_SMF_SFT_Pos)
#define MCAN_SMF_SFT(value)    (MCAN_SMF_SFT_Msk & ((value) << MCAN_SMF_SFT_Pos))

#define _CAN_SFT_RANGE   0 /*!< Range filter from SFID1 to SFID2 */
#define _CAN_SFT_DUAL    1 /*!< Dual ID filter for SFID1 or SFID2 */
#define _CAN_SFT_CLASSIC 2 /*!< Classic filter: SFID1 = filter, SFID2 = mask */
#define _CAN_SFEC_DISABLE  0 /*!< Disable filter element */
#define _CAN_SFEC_STF0M    1 /*!< Store in Rx FIFO 0 if filter matches */
#define _CAN_SFEC_STF1M    2 /*!< Store in Rx FIFO 1 if filter matches */
#define _CAN_SFEC_REJECT   3 /*!< Reject ID if filter matches */
#define _CAN_SFEC_PRIORITY 4 /*!< Set priority if filter matches. */
#define _CAN_SFEC_PRIF0M   5 /*!< Set priority and store in FIFO 0 if filter matches */
#define _CAN_SFEC_PRIF1M   6 /*!< Set priority and store in FIFO 1 if filter matches. */
#define _CAN_SFEC_STRXBUF  7 /*!< Store into Rx Buffer or as debug message, configuration of SFT[1:0] ignored. */

#define _CAN_EFT_RANGE   0 /*!< Range filter from SFID1 to SFID2 */
#define _CAN_EFT_DUAL    1 /*!< Dual ID filter for SFID1 or SFID2 */
#define _CAN_EFT_CLASSIC 2 /*!< Classic filter: SFID1 = filter, SFID2 = mask */
#define _CAN_EFEC_DISABLE  0 /*!< Disable filter element */
#define _CAN_EFEC_STF0M    1 /*!< Store in Rx FIFO 0 if filter matches */
#define _CAN_EFEC_STF1M    2 /*!< Store in Rx FIFO 1 if filter matches */
#define _CAN_EFEC_REJECT   3 /*!< Reject ID if filter matches */
#define _CAN_EFEC_PRIORITY 4 /*!< Set priority if filter matches. */
#define _CAN_EFEC_PRIF0M   5 /*!< Set priority and store in FIFO 0 if filter matches */
#define _CAN_EFEC_PRIF1M   6 /*!< Set priority and store in FIFO 1 if filter matches. */
#define _CAN_EFEC_STRXBUF  7 /*!< Store into Rx Buffer or as debug message, configuration of SFT[1:0] ignored. */
/**
 * \brief CAN extended message ID filter element structure.
 *
 *  Common element structure for extended message ID filter element.
 */
struct _can_extended_message_filter_element {
	union {
		struct {
			uint32_t EFID1:29;  /*!< bit: Extended Filter ID 1 */
			uint32_t EFEC:3;    /*!< bit: Extended Filter Configuration */
		} bit;
		uint32_t val;           /*!< Type used for register access */
	} F0;
	union {
		struct {
			uint32_t EFID2:29;  /*!< bit: Extended Filter ID 2 */
			uint32_t :1;        /*!< bit: Reserved */
			uint32_t EFT:2;     /*!< bit: Extended Filter Type */
		} bit;
		uint32_t val;            /*!< Type used for register access */
	} F1;
};


#define MCAN_EFID2_Pos     (0)
#define MCAN_EFID2_Msk     (0x1FFFFFFFUL << MCAN_EFID2_Pos)
#define MCAN_EFID2(value)  (MCAN_EFID2_Msk & ((value) << MCAN_EFID2_Pos))
#define MCAN_EFID1_Pos     (0)
#define MCAN_EFID1_Msk     (0x1FFFFFFFUL << MCAN_EFID1_Pos)
#define MCAN_EFID1(value)  (MCAN_EFID1_Msk & ((value) << MCAN_EFID1_Pos))
#define MCAN_EFEC_Pos      (29)
#define MCAN_EFEC_Msk      (0x7UL << MCAN_EFEC_Pos)
#define MCAN_EFEC(value)   (MCAN_EFEC_Msk & ((value) << MCAN_EFEC_Pos))
#define MCAN_EFT_Pos       (30)
#define MCAN_EFT_Msk       (0x3UL << MCAN_EFT_Pos)
#define MCAN_EFT(value)    (MCAN_EFT_Msk & ((value) << MCAN_EFT_Pos))


struct _can_context {
	uint8_t                    *rx_fifo;   /*!< receive message fifo */
	uint8_t                    *tx_fifo;   /*!< transfer message fifo */
	struct _can_tx_event_entry *tx_event;  /*!< transfer event fifo */
	/* Standard filter List */
	struct _can_standard_message_filter_element *rx_std_filter;
	/* Extended filter List */
	struct _can_extended_message_filter_element *rx_ext_filter;
};

#ifdef __cplusplus
}
#endif

#endif
