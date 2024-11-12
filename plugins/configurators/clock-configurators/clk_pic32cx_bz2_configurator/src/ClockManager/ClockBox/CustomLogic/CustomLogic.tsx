import { useContext, useEffect } from 'react';
import {
  BooleanSymbol,
  ComboSymbol,
  configSymbolApi,
  IntegerSymbol,
  PluginConfigContext,
  useComboSymbol,
  useIntegerSymbol,
  useStringSymbol,
  useSymbols
} from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';

let nPeripheralLength = 3;
let nReferenceClockLenght = 6;
const getClockIds = (startid: string, endId: string, total: number) => {
  let a: string[] = [];
  for (let i = 1; i <= total; i++) {
    a.push(startid + i + endId);
  }
  return a;
};
const pbClockDivSymbols = getClockIds('CONFIG_SYS_CLK_PBDIV', '', nPeripheralLength);
const pbClockEnableSymbols = getClockIds('CONFIG_SYS_CLK_PBCLK', '_ENABLE', nPeripheralLength);

const refRodivIds = getClockIds('CONFIG_SYS_CLK_RODIV', '', nReferenceClockLenght);
const refRoTrimIds = getClockIds('CONFIG_SYS_CLK_ROTRIM', '', nReferenceClockLenght);
const refClockSourceIds = getClockIds('CONFIG_SYS_CLK_REFCLK_SOURCE', '', nReferenceClockLenght);
const refClkEnableIds = getClockIds('CONFIG_SYS_CLK_REFCLK', '_ENABLE', nReferenceClockLenght);

export let refInputFreqs: number[] = [];
const CustomLogic = (props: { cx: (...classNames: string[]) => string }) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const poscFreqHook = useIntegerSymbol({ componentId, symbolId: 'POSC_OUT_FREQ' });
  const soscFreqHook = useIntegerSymbol({ componentId, symbolId: 'SOSC_OUT_FREQ' });
  const frcDiv = useComboSymbol({ componentId, symbolId: 'OSCCON_FRCDIV_VALUE' });
  const noscHook = useComboSymbol({ componentId, symbolId: 'OSCCON_NOSC_VALUE' });
  const spll1Freq = useIntegerSymbol({ componentId, symbolId: 'SPLL1_FREQ' });
  const spll3Freq = useIntegerSymbol({ componentId, symbolId: 'SPLL3_RFPLL_FREQ' });
  const poscMod = useComboSymbol({ componentId, symbolId: 'CONFIG_POSCMOD' });
  const sysClockFreq = useStringSymbol({ componentId, symbolId: 'SYS_CLK_FREQ' });
  const pbdiv1Hook = useIntegerSymbol({ componentId, symbolId: 'CONFIG_SYS_CLK_PBDIV1' });
  const refClockFreqHook = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_SYS_CLK_CONFIG_REFCLKI_PIN'
  });

  const pbclockDivSymbolHooks = useSymbols({
    componentId: componentId,
    symbolIds: pbClockDivSymbols
  }) as IntegerSymbol[];
  const pbclockEnableSymbolHooks = useSymbols({
    componentId: componentId,
    symbolIds: pbClockEnableSymbols
  }) as BooleanSymbol[];
  const refRodivSymbolHooks = useSymbols({
    componentId: componentId,
    symbolIds: refRodivIds
  }) as IntegerSymbol[];
  const refRoTrimSymbolHooks = useSymbols({
    componentId: componentId,
    symbolIds: refRoTrimIds
  }) as IntegerSymbol[];
  const refClockSourceHooks = useSymbols({
    componentId: componentId,
    symbolIds: refClockSourceIds
  }) as ComboSymbol[];
  const refClockEnableHooks = useSymbols({
    componentId: componentId,
    symbolIds: refClkEnableIds
  }) as BooleanSymbol[];

  useEffect(() => {
    const refreshPeripheralClockDisplay = (noscFreqValue: number) => {
      let pb1Freq = 0;
      let pb1div = 0;

      for (let index = 0; index < nPeripheralLength; index++) {
        pb1div = pbclockDivSymbolHooks[index].value;
        pb1Freq = noscFreqValue / pb1div;
        if (pbclockEnableSymbolHooks[index].value !== true) {
          pb1Freq = 0;
        }
        let id = index + 1;
        configSymbolApi.setValue(
          componentId,
          'CONFIG_SYS_CLK_PBCLK' + id + '_FREQ',
          pb1Freq.toString()
        );
      }
    };

    const refreshReferenceClockDisplay = (
      sysclkFreq: number,
      poscFreq: number,
      frcFreq: number,
      lprcFreq: number,
      soscFreq: number
    ) => {
      let pb1div = pbdiv1Hook.value;
      let pbclk1FreqVal = sysclkFreq / pb1div;

      let refclk1InputFreq = 0;

      let roselValue = '';

      for (let newIndex = 0; newIndex < nReferenceClockLenght; newIndex++) {
        roselValue = refClockSourceHooks[newIndex].value;
        if (roselValue === 'PBCLK1') {
          refclk1InputFreq = pbclk1FreqVal;
        } else if (roselValue === 'POSC') {
          refclk1InputFreq = poscFreq;
        } else if (roselValue === 'FRC') {
          refclk1InputFreq = frcFreq;
        } else if (roselValue === 'LPRC') {
          refclk1InputFreq = lprcFreq;
        } else if (roselValue === 'SOSC') {
          refclk1InputFreq = soscFreq;
        } else if (roselValue === 'SPLL1') {
          refclk1InputFreq = spll1Freq.value;
        } else if (roselValue === 'SPLL3') {
          refclk1InputFreq = spll3Freq.value;
        } else if (roselValue === 'SYSCLK') {
          refclk1InputFreq = sysclkFreq;
        } else if (roselValue === 'REFCLKI') {
          refclk1InputFreq = refClockFreqHook.value;
        }

        refInputFreqs[newIndex] = refclk1InputFreq;

        let ref1div = refRodivSymbolHooks[newIndex].value;
        let ref1trim = refRoTrimSymbolHooks[newIndex].value;

        let refclko1Freq: number = refclk1InputFreq / 2 / (ref1div + ref1trim / 512);

        if (ref1div <= 0) {
          refclko1Freq = refclk1InputFreq;
        }
        if (refClockEnableHooks[newIndex].value !== true) {
          refclko1Freq = 0;
        }
        let newId = newIndex + 1;
        configSymbolApi.setValue(
          componentId,
          'CONFIG_SYS_CLK_REFCLK' + newId + '_FREQ',
          refclko1Freq.toString()
        );
      }
    };

    if (
      pbclockDivSymbolHooks.length !== 0 &&
      pbclockEnableSymbolHooks.length !== 0 &&
      refRoTrimSymbolHooks.length !== 0 &&
      refRodivSymbolHooks.length !== 0 &&
      refClockEnableHooks.length !== 0 &&
      refClockSourceHooks.length !== 0
    ) {
      let poscFreq = poscFreqHook.value;
      let soscFreq = soscFreqHook.value;
      let frcFreq = 8000000;
      let lprcFreq = 32768;

      let frcdivVal = Number(frcDiv.value.replaceAll('DIV_', ''));
      let frcDivFreq = frcFreq / frcdivVal;

      let nosc = noscHook.value;
      let noscFreq = 0;

      if (nosc === 'SPLL') {
        noscFreq = spll1Freq.value;
      } else if (nosc === 'POSC') {
        noscFreq = poscFreq;
        if (poscMod.value === 'OFF') {
          noscFreq = 0;
        }
      } else if (nosc === 'SOSC') {
        noscFreq = soscFreq;
      } else if (nosc === 'FRCDIV') {
        noscFreq = frcDivFreq;
      } else if (nosc === 'LPRC') {
        noscFreq = lprcFreq;
      }
      configSymbolApi.setValue(componentId, sysClockFreq.symbolId, noscFreq.toString());
      refreshPeripheralClockDisplay(noscFreq);
      refreshReferenceClockDisplay(noscFreq, poscFreq, frcFreq, lprcFreq, soscFreq);
    }
  }, [
    componentId,
    frcDiv.value,
    noscHook.value,
    pbclockDivSymbolHooks,
    pbclockEnableSymbolHooks,
    pbdiv1Hook.value,
    poscFreqHook.value,
    poscMod.value,
    refClockEnableHooks,
    refClockFreqHook.value,
    refClockSourceHooks,
    refRoTrimSymbolHooks,
    refRodivSymbolHooks,
    soscFreqHook.value,
    spll1Freq.value,
    spll3Freq.value,
    sysClockFreq
  ]);

  return (
    <>
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(Number(sysClockFreq.value))}
        booldStatus={true}
        className={props.cx('sysclk_res')}
      />
    </>
  );
};
export default CustomLogic;
