    /* First thing, make sure the PS and Busy bit are set */
    uint32_t csmReport = CSM_REGS->CSM_CSMREPORT;
    csmReport &= ~CSM_CSMREPORT_PS_Msk;
    csmReport |=   CSM_CSMREPORT_PS(1)
                 | CSM_CSMREPORT_BUSY(1);
    CSM_REGS->CSM_CSMREPORT = csmReport;
