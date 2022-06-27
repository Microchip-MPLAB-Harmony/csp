# RTC\_PERIODIC\_INT\_MASK Enum

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-3578D06D-FEC5-4769-ADC7-0D46730CD973.md)

## C

```c
typedef enum
{
    /* Periodic Interrupt at 128 Hz (RTC Clock Frequency/8) - Prescaler Bit 0 */
    RTC_PER0_MASK,
    
    /* Periodic Interrupt at 64 Hz (RTC Clock Frequency/16) - Prescaler Bit 1 */
    RTC_PER1_MASK,
    
    /* Periodic Interrupt at 32 Hz (RTC Clock Frequency/32) - Prescaler Bit 2 */
    RTC_PER2_MASK,
    
    /* Periodic Interrupt at 16 Hz (RTC Clock Frequency/64) - Prescaler Bit 3 */
    RTC_PER3_MASK,
    
    /* Periodic Interrupt at 8 Hz (RTC Clock Frequency/128) - Prescaler Bit 4 */
    RTC_PER4_MASK,
    
    /* Periodic Interrupt at 4 Hz (RTC Clock Frequency/256) - Prescaler Bit 5 */
    RTC_PER5_MASK,
    
    /* Periodic Interrupt at 2 Hz (RTC Clock Frequency/512) - Prescaler Bit 6 */
    RTC_PER6_MASK,
    
    /* Periodic Interrupt at 1 Hz (RTC Clock Frequency/1024) - Prescaler Bit 7 */
    RTC_PER7_MASK
} RTC_PERIODIC_INT_MASK;

```

## Summary

Possible Periodic Interrupt Mask.

## Description

This enumeration defines the possible periodic interrupt mask.

## Remarks

None.

