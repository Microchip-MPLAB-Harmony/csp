# Timer Counter \(TC\)

A Timer Counter \(TC\) module includes three identical TC channels. All channels of the Timer Counter are independent and identical in operation except when the quadrature encode mode is enabled. Timer counter module can be configured to operate in one of the following modes:

-   Timer mode used for periodic interrupt generation

-   Compare mode used for generating PWM signals

-   Capture mode used to perform measurements such as pulse timing, frequency, period, duty cycle and phase

-   Quadrature encoder mode used to measure the position and speed of the motor


**Timer mode**

The TC channel in timer mode is used for periodic interrupt generation.

**Using The Library**

When the timer is enabled, it increments by one on every rising edge of the input clock, and generates an interrupt on a period match \(Timer expiry period\). Timer mode is used for periodic interrupt generation.

It provides both polling and callback methods to indicate period match has occurred.

-   With polling, the application will need to continuously poll to check if the timer has expired.

-   With callback, the registered callback function will be called when the timer expires. This means the application do not have to poll continuously.


**Callback method**

This example demonstrates how to use TC channel in timer mode to<br />generate periodic callback.

```c
/* This function is called after period expires */
void TC0_CH0_TimerInterruptHandler(TC_TIMER_STATUS status, uintptr_t context)
{
    /* Toggle LED */
    LED_Toggle();
}

int main(void)
{

    /* Register callback function for CH0 period interrupt */
    TC0_CH0_TimerCallbackRegister(TC0_CH0_TimerInterruptHandler, (uintptr_t)NULL);

    /* Start the timer channel 0*/
    TC0_CH0_TimerStart();
}
```

**Library Interface**

Timer Counter peripheral library operating in timer mode provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|TCx\_CHy\_TimerInitialize|Initializes given instance of TC channel|
|TCx\_CHy\_TimerStart|Starts the given TC channel counter|
|TCx\_CHy\_TimerStop|Stops the given TC channel counter|
|TCx\_CHy\_TimerCompareSet|Sets the compare value of a given timer channel|
|TCx\_CHy\_TimerPeriodSet|Sets the period value of a given timer channel|
|TCx\_CHy\_TimerPeriodGet|Reads the period value of given timer channel|
|TCx\_CHy\_TimerCounterGet|Reads the timer channel counter value|
|TCx\_CHy\_TimerFrequencyGet|Provides the given timer's counter-increment frequency|
|TCx\_CHy\_TimerPeriodHasExpired|Checks whether timer period is elapsed|
|TCx\_CHy\_TimerCallbackRegister|Registers the function to be called from interrupt|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|TC\_TIMER\_STATUS|Enum|Identifies channel interrupt source mask|
|TC\_TIMER\_CALLBACK|Typedef|Defines the function pointer data type and function signature for the tc channel callback function|

**Compare mode**

The TC channel in compare mode generates one or two PWM signals with the same frequency and independently programmable duty cycles, or generates different types of one-shot or repetitive pulses.

**Using The Library**

In this mode, TIOAx is configured as an output. TIOBx is configured as an output, if it is not used as an external event.

**Functions**

|Name|Description|
|----|-----------|
|TCx\_CHy\_CompareInitialize|Initializes given TC channel in compare mode|
|TCx\_CHy\_CompareStart|Starts the given TC channel compare counter|
|TCx\_CHy\_CompareStop|Stops the given TC channel counter in compare mode|
|TCx\_CHy\_ComparePeriodSet|Sets the period value of a given TC channel in compare mode|
|TCx\_CHy\_ComparePeriodGet|Gets the period value of given timer channel in compare mode|
|TCx\_CHy\_CompareFrequencyGet|Provides the given timer's counter-increment frequency in compare mode|
|TCx\_CHy\_CompareCallbackRegister|Registers the function to be called from interrupt|
|TCx\_CHy\_CompareASet|Sets the Compare-A value of the given timer channel in compare mode|
|TCx\_CHy\_CompareBSet|Sets the Compare-B value of the given timer channel in compare mode|
|TCx\_CHy\_CompareStatusGet|Identifies status of the compare events|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|TC\_COMPARE\_STATUS|Enum|Identifies channel interrupt source mask|
|TC\_COMPARE\_CALLBACK|Typedef|Defines the function pointer data type and function signature for the tc channel callback function|

**Capture mode**

The TC channel in capture mode is used to measure pulse time, frequency, period and duty cycle.

**Using The Library**

In Capture mode, TIOAx and TIOBx are configured as inputs. The counter value is captured in the buffer on the selected input edge and it is used as a timestamp for the event. The user can select up to two input events and the respective timestamp is captured in Capture A and Capture B buffers, it can be used to measure pulse, period, frequency and duty cycle of the external input.

It provides both polling and callback methods to indicate capture event has occurred.

-   With polling, the application will need to continuously poll to check if the capture event has occurred

-   With callback, the registered callback function will be called when the capture event occurs. This means the application do not have to poll continuously


**Callback method**

This example demonstrates how to use the TC channel in capture mode to<br />measure off time and period. The rising edge is captured in Capture A<br />and Falling edge is captured in Capture B register, and then the timer<br />is reset.

```c
/* This function is called after Capture B */
void TC0_CH0_CaptureInterruptHandler(TC_CAPTURE_STATUS status, uintptr_t context)
{
    /* Read Captured values */
    off_time = TC0_CH0_CaptureAGet();
    period = TC0_CH0_CaptureBGet();
}

int main(void)
{

    /* Register callback function for CH0 period interrupt */
    TC0_CH0_CaptureCallbackRegister(TC0_CH0_CaptureInterruptHandler, (uintptr_t)NULL);

    /* Start the Capture channel 0*/
    TC0_CH0_CaptureStart();
}
```

**Functions**

|Name|Description|
|----|-----------|
|TCx\_CHy\_CaptureInitialize|Initializes given instance of TC channel to capture mode|
|TCx\_CHy\_CaptureStart|Starts the given TC channel capture counter|
|TCx\_CHy\_CaptureStop|Stops the given TC channel counter|
|TCx\_CHy\_CaptureCallbackRegister|Registers the function to be called from the capture-event|
|TCx\_CHy\_CaptureAGet|Returns the Capture-A value|
|TCx\_CHy\_CaptureBGet|Returns the Capture-B value|
|TCx\_CHy\_CaptureStatusGet|Identifies status of the capture events|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|TC\_CAPTURE\_STATUS|Enum|Identifies channel interrupt source mask|
|TC\_CAPTURE\_CALLBACK|Typedef|Defines the function pointer data type and function signature for the tc channel callback function|

**Quadrature decoder mode**

The quadrature decoder \(QDEC\) mode is used to measure the position and speed of the motor

**Using The Library**

The TC embeds a Quadrature Decoder \(QDEC\) connected in front of the timers and driven by TIOA0, TIOB0 and TIOB1 inputs. When enabled, the QDEC performs the input lines filtering, decoding of quadrature signals and connects to the timers and counters in order to read the position and speed of the motor through the user interface.

**Functions**

|Name|Description|
|----|-----------|
|TCx\_QuadratureInitialize|Initializes given instance of TC channel in quadrature mode|
|TCx\_QuadratureStart|Starts the given TC channel counter in quadrature mode|
|TCx\_QuadratureStop|Stops the given TC channel counter in quadrature mode|
|TCx\_QuadraturePositionGet|Reads the angular position from the quadrature encoder|
|TCx\_QuadratureRevolutionsGet|Reads the number of revolutions from the quadrature encoder|
|TCx\_QuadratureSpeedGet|Reads the quadrature index change speed|
|TCx\_CHy\_QuadratureStatusGet|Identifies status of the quadrature events|
|TCx\_QuadratureCallbackRegister|Registers the function to be called from interrupt|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|TC\_QUADRATURE\_STATUS|Enum|Identifies channel interrupt source mask|
|TC\_QUADRATURE\_CALLBACK|Typedef|Defines the function pointer data type and function signature for the tc channel callback function|

-   **[TCx\_CHy\_TimerInitialize Function](GUID-8D8F43BE-81AC-40DB-AE57-1377A7707E3E.md)**  

-   **[TCx\_CHy\_TimerCallbackRegister Function](GUID-9E44FC23-F202-4638-A993-470C8AC7569E.md)**  

-   **[TCx\_CHy\_TimerPeriodHasExpired Function](GUID-F08F7CBD-FC1A-4949-8602-3177E153361E.md)**  

-   **[TCx\_CHy\_TimerPeriodSet Function](GUID-6BAE3754-9FE0-4C42-9F5A-EB3F929EFA55.md)**  

-   **[TCx\_CHy\_TimerPeriodGet Function](GUID-DD9A128B-94D4-4046-B896-58D69C398971.md)**  

-   **[TCx\_CHy\_TimerCounterGet Function](GUID-BC4F762B-5660-4B0E-89E7-70A929C9BF3F.md)**  

-   **[TCx\_CHy\_TimerFrequencyGet Function](GUID-61A42F33-5C43-4DCF-B2F7-5EDFC504B9F6.md)**  

-   **[TCx\_CHy\_TimerCompareSet Function](GUID-6B1BFE7A-3BEE-4ACF-BB8B-1FD64D74B168.md)**  

-   **[TCx\_CHy\_TimerStop Function](GUID-2D254701-3B05-45F4-9389-7EE8561A8987.md)**  

-   **[TCx\_CHy\_TimerStart Function](GUID-77D8760B-0228-43F2-990F-9898678A49C6.md)**  

-   **[TCx\_CHy\_CompareInitialize Function](GUID-D9E21CCD-B7D8-4B54-96DF-3421A8C14C64.md)**  

-   **[TCx\_CHy\_ComparePeriodGet Function](GUID-AB55CA5A-6773-4F7A-914E-B4D1674C3728.md)**  

-   **[TCx\_CHy\_ComparePeriodSet Function](GUID-E2B4263C-8A83-471E-9FE6-FF4B2D888F24.md)**  

-   **[TCx\_CHy\_CompareStatusGet Function](GUID-542EEB56-E2AF-4881-9197-051234DD4885.md)**  

-   **[TCx\_CHy\_CompareStart Function](GUID-8FA48B50-32E7-4DC4-87FD-F8D50BA2116E.md)**  

-   **[TCx\_CHy\_CompareStop Function](GUID-F2EFD664-FBE0-4B72-8BDD-04229D1D14FB.md)**  

-   **[TCx\_CHy\_CompareASet Function](GUID-8E24A439-26C1-44F7-9CE3-1AADC4361516.md)**  

-   **[TCx\_CHy\_CompareBSet Function](GUID-D1604B2C-F534-462D-B246-90B5F792287D.md)**  

-   **[TCx\_CHy\_CompareCallbackRegister Function](GUID-89888121-4DF8-415C-ABAB-1798CB026895.md)**  

-   **[TCx\_CHy\_CompareFrequencyGet Function](GUID-BDB91E00-6AC2-4CCF-A99B-1442BA603A54.md)**  

-   **[TCx\_CHy\_CaptureAGet Function](GUID-F635EE1F-CD46-481B-B1ED-1D7987CB8840.md)**  

-   **[TCx\_CHy\_CaptureBGet Function](GUID-F46705DE-38B1-4284-AC1F-89A4634D7A01.md)**  

-   **[TCx\_CHy\_CaptureCallbackRegister Function](GUID-FDA85E34-B0D4-498C-8A11-0E9CF816189F.md)**  

-   **[TCx\_CHy\_CaptureInitialize Function](GUID-0303A17B-BA37-4D94-84F7-268A70867E84.md)**  

-   **[TCx\_CHy\_CaptureStart Function](GUID-6096D727-39AF-4D20-90D7-926CF3E789DD.md)**  

-   **[TCx\_CHy\_CaptureStatusGet Function](GUID-17B64F98-C8F8-4BEE-8196-1C245FE2DB0A.md)**  

-   **[TCx\_CHy\_CaptureStop Function](GUID-25EDB3AC-8514-430B-8448-CD828615899D.md)**  

-   **[TCx\_QuadratureInitialize Function](GUID-1100E841-4832-4359-9363-FF9FAB09C636.md)**  

-   **[TCx\_QuadratureCallbackRegister Function](GUID-DE6FEA22-AA50-45BD-B23A-1B7D8F045995.md)**  

-   **[TCx\_QuadraturePositionGet Function](GUID-265D45E1-9171-40F5-99E6-2AB4ECE356BA.md)**  

-   **[TCx\_QuadratureRevolutionsGet Function](GUID-A65FC8D5-2F03-4B44-9CD2-4307083F4941.md)**  

-   **[TCx\_QuadratureSpeedGet Function](GUID-B63D8BAB-57D1-41EA-815D-9EB35E6820C7.md)**  

-   **[TCx\_QuadratureStart Function](GUID-2158965D-F64E-463B-AA59-4FC6E72FAF7E.md)**  

-   **[TCx\_QuadratureStop Function](GUID-A20853C2-362C-4270-8AAF-07E82386276C.md)**  

-   **[TCx\_CHy\_QuadratureStatusGet Function](GUID-69DDB228-3FB4-435A-9BF9-2AD36EC6E039.md)**  

-   **[TC\_TIMER\_CALLBACK Typedef](GUID-728DB2A3-5AB5-4DE0-A517-22A17B31B31E.md)**  

-   **[TC\_TIMER\_STATUS Enum](GUID-8281F3F8-7070-42B2-A79E-344B2A69D786.md)**  

-   **[TC\_CAPTURE\_CALLBACK Typedef](GUID-E01AD9A5-A1FF-4891-A487-856A8D4A6B38.md)**  

-   **[TC\_CAPTURE\_STATUS Enum](GUID-A65209D9-3453-441F-9EF2-9A22F17216AB.md)**  

-   **[TC\_COMPARE\_CALLBACK Typedef](GUID-C6C2CC30-669D-4327-A433-6B11CFBBC90A.md)**  

-   **[TC\_COMPARE\_STATUS Enum](GUID-3AA5FE8A-4E92-4E19-8231-52CEE2F198C0.md)**  

-   **[TC\_QUADRATURE\_CALLBACK Typedef](GUID-57F988BA-D6EA-4D4D-B22A-2002EF718CB7.md)**  

-   **[TC\_QUADRATURE\_STATUS Enum](GUID-2787DA42-1D45-4564-BEC7-7AD7FF322914.md)**  


**Parent topic:**[PIC32CX MT Peripheral Libraries](GUID-EEA7836F-956F-4526-BF85-CD488C4CE708.md)

**Parent topic:**[SAM 9X60 Peripheral Libraries](GUID-CCAAC7F0-6BA8-4630-91AE-69718D188CBF.md)

**Parent topic:**[SAM 9X7 Peripheral Libraries](GUID-FB6741AA-355E-483F-9727-37728953D583.md)

**Parent topic:**[SAM A5D2 Peripheral Libraries](GUID-F6605EDC-FC71-4081-8560-0C1681C1FA8D.md)

**Parent topic:**[SAM A7G5 Peripheral Libraries](GUID-7EEB1AC5-4BFF-4259-97AD-8CF7367D7973.md)

**Parent topic:**[SAM E70 S70 V70 V71 Peripheral Libraries](GUID-6E45C146-6F6D-452A-A2E2-228C3CC905D7.md)

**Parent topic:**[SAM G51 G53 G54 Peripheral Libraries](GUID-E97B8116-033B-411A-925B-E8E6252A1E15.md)

**Parent topic:**[SAM G55 Peripheral Libraries](GUID-E3F1DCC4-CB31-4302-A60B-D2833C5CAD18.md)

**Parent topic:**[SAM RH707 Peripheral Libraries](GUID-C2AC236D-363B-4378-A381-B281F67C8647.md)

**Parent topic:**[SAM RH71 Peripheral Libraries](GUID-AC9BE324-E486-46EA-8D16-E04E15288053.md)

