# MPLAB® Harmony Peripheral Libraries

MPLAB® Harmony Chip Support Package \(CSP\) supports configuration of Microchip 32-bit microcontroller and microprocessor devices. This support can be used to initialize basic functionality necessary in order to use the device. When using the MCC to only generate minimal device configuration code, the application developer must create all additional logic. This includes any further peripheral control logic and potentially complex middleware

In addition to minimal device initialization, many developers prefer simple and direct control over peripherals with minimal overhead. To support this model, a developer can use the MCC to add additional peripheral libraries \(PLIBs\) to a project and the MCC will generate device-specific code to initialize and control the selected peripherals.

Peripheral Libraries are devices family specific. Below is the list of supported familes:

-   **[CEC173X Peripheral Libraries](GUID-73984A00-CB8F-4D95-BCB2-C21D89C44A89.md)**  

-   **[PIC32CM JH00 JH01 Peripheral Libraries](GUID-05924E45-D6B3-4F33-A5EA-9B080FC421D8.md)**  

-   **[PIC32CM LE00 LS00 LS60 Peripheral Libraries](GUID-F80F1B47-C3E4-4803-ACB6-D30AC5EB7B45.md)**  

-   **[PIC32CM MC00 Peripheral Libraries](GUID-ADF45DC0-B32C-4D1F-9332-59EC0DF5097E.md)**  

-   **[PIC32CX BZ2 WBZ45 Peripheral Libraries](GUID-3D519D00-FDEE-4A3E-9EF7-20F335E64CEE.md)**  

-   **[PIC32CX BZ3 WBZ3 Peripheral Libraries](GUID-5752DD6D-6E5D-484D-B564-DA87788492F3.md)**  

-   **[PIC32CX MT Peripheral Libraries](GUID-EEA7836F-956F-4526-BF85-CD488C4CE708.md)**  

-   **[PIC32CZ-CA Peripheral Libraries](GUID-7EAC3718-3D58-4007-AB2A-A0E3C167A2DF.md)**  

-   **[PIC32MK GPD GPE MCF Peripheral Libraries](GUID-A63F4C14-72E7-44D7-9C70-A48BBD41B583.md)**  

-   **[PIC32MK GPG MCJ Peripheral Libraries](GUID-A0350A48-03F7-4370-A6C5-612386A4ABAC.md)**  

-   **[PIC32MK GPK MCM Peripheral Libraries](GUID-801B9DE7-4616-4E38-BF86-C82B78A4F430.md)**  

-   **[PIC32MK MCA Peripheral Libraries](GUID-E11C5899-DD12-4B78-8076-8A415C20F144.md)**  

-   **[PIC32MM GPL Peripheral Libraries](GUID-1AE2B428-AA57-43A7-A52E-C35ABF67EDC4.md)**  

-   **[PIC32MM GPM Peripheral Libraries](GUID-CB22E113-2DFF-40FB-BA9B-BFA1C8003FEC.md)**  

-   **[PIC32MX 1XX 2XX Peripheral Libraries](GUID-DD9F92A3-1B1F-4068-A4CC-C71672A1BF54.md)**  

-   **[PIC32MX 1XX 2XX XLP Peripheral Libraries](GUID-8819552A-CB58-4DAC-BE25-EC305892232E.md)**  

-   **[PIC32MX 1XX 2XX 5XX Peripheral Libraries](GUID-232A3DC0-B096-45AA-9430-33A2C9BA694A.md)**  

-   **[PIC32MX 330 350 370 430 450 470 Peripheral Libraries](GUID-4F5C226F-136E-4C6B-8A7F-0DF12557C7F8.md)**  

-   **[PIC32MX 3XX 4XX Peripheral Libraries](GUID-2C79235F-A27F-4622-BBDA-943C35FD7940.md)**  

-   **[PIC32MX 5XX 6XX 7XX Peripheral Libraries](GUID-91DC3697-58A9-4E5B-95DE-F4B08BA9C8DD.md)**  

-   **[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)**  

-   **[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)**  

-   **[PIC32MZ W1 Peripheral Libraries](GUID-EBD28D67-7F6E-46D1-9ABE-2BDE1973D143.md)**  

-   **[SAM 9X60 Peripheral Libraries](GUID-CCAAC7F0-6BA8-4630-91AE-69718D188CBF.md)**  

-   **[SAM 9X7 Peripheral Libraries](GUID-FB6741AA-355E-483F-9727-37728953D583.md)**  

-   **[SAM A5D2 Peripheral Libraries](GUID-F6605EDC-FC71-4081-8560-0C1681C1FA8D.md)**  

-   **[SAM A7G5 Peripheral Libraries](GUID-7EEB1AC5-4BFF-4259-97AD-8CF7367D7973.md)**  

-   **[SAM C20 C21 Peripheral Libraries](GUID-49072E61-B7F2-4B32-952E-D6F5FB361AFB.md)**  

-   **[SAM D09 D10 D11 Peripheral Libraries](GUID-F4788319-C5F3-4EB3-8CC7-05770A2EBD32.md)**  

-   **[SAM D20 D21 Peripheral Libraries](GUID-86A69A90-EDAB-465F-A03A-57CD8BF54AE8.md)**  

-   **[SAM D51 E51 E53 E54 Peripheral Libraries](GUID-E33B93DD-6680-477E-AA96-966208DC9A50.md)**  

-   **[SAM DA1 Peripheral Libraries](GUID-0CDE5F35-9BE3-4484-8299-98161C496C00.md)**  

-   **[SAM E70 S70 V70 V71 Peripheral Libraries](GUID-6E45C146-6F6D-452A-A2E2-228C3CC905D7.md)**  

-   **[SAM G51 G53 G54 Peripheral Libraries](GUID-E97B8116-033B-411A-925B-E8E6252A1E15.md)**  

-   **[SAM G55 Peripheral Libraries](GUID-E3F1DCC4-CB31-4302-A60B-D2833C5CAD18.md)**  

-   **[SAM HA1 Peripheral Libraries](GUID-7E583BB3-CBFA-4862-8ED5-40D747167457.md)**  

-   **[SAM L1X Peripheral Libraries](GUID-D259BBBC-6BC2-4F69-849B-C06DF4DDD5F8.md)**  

-   **[SAM L21 Peripheral Libraries](GUID-230EF724-3CDA-4F88-8E42-0EF4C1CA112D.md)**  

-   **[SAM L22 Peripheral Libraries](GUID-C3997EBF-87A0-4DD9-BCB0-C8A58B62E44B.md)**  

-   **[SAM RH707 Peripheral Libraries](GUID-C2AC236D-363B-4378-A381-B281F67C8647.md)**  

-   **[SAM RH71 Peripheral Libraries](GUID-AC9BE324-E486-46EA-8D16-E04E15288053.md)**  


