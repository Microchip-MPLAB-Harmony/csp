#include "device.h"
#include "plib_clk.h"


//TODO: To handle the delay break this into different functions that SYS_Init can call
// and do the waitning in sys_init

static void initProgrammableClk(void)
{
    PMC_REGS->PMC_SCDR |= PMC_SCDR_PCK0_Msk | PMC_SCDR_PCK1_Msk;
}

static void initPeriphClk(void)
{
    struct {
        int id;
        int gclk;
        int css;
        int div;
    } periphList[] = {
        { ID_PIOA, 0, 0, 0},
        { ID_PIOB, 0, 0, 0},
        { ID_PIOC, 0, 0, 0},
        { ID_QSPI, 0, 0, 0},
        { ID_PIT64B, 0, 0, 0},
        { ID_PIOD, 0, 0, 0},
        { ID_PERIPH_MAX + 1, 0, 0, 0}//end of list marker
    };

    int i;
    int count;

    count = sizeof(periphList)/sizeof(periphList[0]);
    for (i=0; i<count; i++) {
        if (periphList[i].id == (ID_PERIPH_MAX + 1)) {
            break;
        }
        PMC_REGS->PMC_PCR = PMC_PCR_PID(periphList[i].id) |\
                            PMC_PCR_EN_Msk |\
                            PMC_PCR_CMD_Msk |\
                            PMC_PCR_GCLKEN(periphList[i].gclk) |\
                            PMC_PCR_GCLKCSS(periphList[i].css) |\
                            PMC_PCR_GCLKDIV(periphList[i].div);
    }

}

void initSysClks(void)
{

    PMC_REGS->PMC_SCER |= PMC_SCER_QSPICLK_Msk;
}

void CLK_Initialize( void )
{
initProgrammableClk();
initPeriphClk();
initSysClks();
}
