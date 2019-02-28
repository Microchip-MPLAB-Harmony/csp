#ifndef PLIB_CLK_H
#define PLIB_CLK_H

void CLK_Initialize( void );
<#if CLK_UPLL_EN>
void CLK_UPLLInitStart(void);
void CLK_UPLLInitMiddle(void);
void CLK_UPLLInitEnd(void);
</#if>

#endif //PLIB_CLK_H
