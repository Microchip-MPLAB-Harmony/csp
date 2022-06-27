# Configurable Logic Cell \(CLC\)

The Configurable Logic Cell \(CLC\) module allows the user to specify combinations of signals as inputs to a logic function and to use the logic output to control other peripherals or I/O pins. CLC module can also be configured to generate and interrupt when the logic cell output changes.

**Using The Library**

CLC peripheral runs independent of the processor core. CLC peripheral is initialized using CLC\_Initialize\(\) API. This will be done by the auto-generated code as part of the system initialization \(that is, if CLC peripheral is added to the project graph\).

At any point during program execution, logic cell can be turned On or Off using CLC\_Enable API. Invoking CLC\_Enable\(\) with argument value of "true" will enable the logic cell and an argument value of "false" will disable it.

If CLC is configured to generate a processor Interrupt, a callback must be registered using the CLC\_CallbackRegister\(\) API. See code example below.

```c
/* Context is provided as part of callback */
void CLC_EventHandler(uintptr_t context)
{
    /* CLC interrupt occurred, do something */
}

int main(void)
{
    /* Register Callback */
    CLC1_CallbackRegister(CLC_EventHandler, (uintptr_t) NULL);

    /* Enable CLC */
    CLC1_Enable(true);
}
```

**Library Interface**

Peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|CLCx\_Initialize|Initializes CLC peripheral|
|CLCx\_Enable|Enable/Disable CLC module|
|CLCx\_CallbackRegister|Registers the function to be called from interrupt|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|CLC\_CALLBACK|Typedef|Defines the data type and function signature for the CLC peripheral callback function|

-   **[CLCx\_Initialize Function](GUID-9F4F745C-8546-4E77-996E-7FB80BF58208.md)**  

-   **[CLC\_Enable Function](GUID-92608FBF-862C-44DA-9B49-B2A4B54B8E26.md)**  

-   **[CLC\_CallbackRegister Function](GUID-0BC3003A-5EE0-44AC-B5AE-217D6FDED34F.md)**  

-   **[CLC\_CALLBACK Typedef](GUID-50522AA2-074D-4A9D-B3EE-11A6E2D7CFFB.md)**  


**Parent topic:**[PIC32MK GPG MCJ Peripheral Libraries](GUID-A0350A48-03F7-4370-A6C5-612386A4ABAC.md)

**Parent topic:**[PIC32MK MCA Peripheral Libraries](GUID-E11C5899-DD12-4B78-8076-8A415C20F144.md)

**Parent topic:**[PIC32MM GPL Peripheral Libraries](GUID-1AE2B428-AA57-43A7-A52E-C35ABF67EDC4.md)

**Parent topic:**[PIC32MM GPM Peripheral Libraries](GUID-CB22E113-2DFF-40FB-BA9B-BFA1C8003FEC.md)

