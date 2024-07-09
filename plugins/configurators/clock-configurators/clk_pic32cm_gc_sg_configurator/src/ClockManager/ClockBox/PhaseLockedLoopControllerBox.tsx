import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import { useContext, useState } from 'react';
import {
  BooleanSymbol,
  IntegerSymbol,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
  useSymbols
} from '@mplab_harmony/harmony-plugin-client-lib';
import { getDynamicSymbolsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FrequencyLabelRangeComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelRangeComponent';

const tabTitle = 'PLL0';
const settingsArray = [
  'CONFIG_CLOCK_' + tabTitle + '_ENABLE',
  'CONFIG_CLOCK_' + tabTitle + '_ONDEMAND',
  'CONFIG_CLOCK_' + tabTitle + '_BWSEL',
  'CONFIG_CLOCK_' + tabTitle + '_REF_CLOCK',
  'CONFIG_CLOCK_' + tabTitle + '_PLLFBDIV_FBDIV',
  'CONFIG_CLOCK_' + tabTitle + '_PLLREFDIV_REFDIV',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_POSTDIV0',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_OUTEN0',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_POSTDIV1',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_OUTEN1',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_POSTDIV2',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_OUTEN2',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_POSTDIV3',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_OUTEN3',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_POSTDIV4',
  'CONFIG_CLOCK_' + tabTitle + '_PLLPOSTDIV_OUTEN4'
];

const getPLLSymbolIds = (symbolIdprefix: string) => {
  let a: string[] = [];
  for (let i = 0; i < 5; i++) {
    a.push(symbolIdprefix + i);
  }
  return a;
};
const pllFreqArray = getPLLSymbolIds('PLL0_CLOCK_FREQ');
const pllDivArray = getPLLSymbolIds('CONFIG_CLOCK_PLL0_PLLPOSTDIV_POSTDIV');
const pllOutEnable = getPLLSymbolIds('CONFIG_CLOCK_PLL0_PLLPOSTDIV_OUTEN');

let fckrFreqValue = 0;
let fpfdFreqValue = 0;
let fvcoFreqValue = 0;

const PhaseLockedLoopControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmb_refClk = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_' + tabTitle + '_REF_CLOCK'
  });
  const pllrefdiv = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_' + tabTitle + '_PLLREFDIV_REFDIV'
  });
  const pllfbdiv = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_PLL0_PLLFBDIV_FBDIV'
  });
  const pllDivSymbols = useSymbols({
    componentId: componentId,
    symbolIds: pllDivArray
  }) as IntegerSymbol[];

  const pllOutEnableSymbols = useSymbols({
    componentId: componentId,
    symbolIds: pllOutEnable
  }) as BooleanSymbol[];

  const gclkChannelEnable = useBooleanSymbol({
    componentId: componentId,
    symbolId: 'GCLK_ID_1_CHEN'
  });
  const gclkGenSel = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: 'GCLK_ID_1_GENSEL'
  });
  const gclkFreq = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'GCLK_' + gclkGenSel.value + '_FREQ'
  });
  const xOscFreq = useIntegerSymbol({ componentId: componentId, symbolId: 'XOSC_FREQ' });
  const dfllclockFreq = useIntegerSymbol({ componentId: componentId, symbolId: 'DFLL_CLOCK_FREQ' });

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));

  const updateFCKRPLLFreq = () => {
    let freq = 0;
    if (cmb_refClk.value === 0) {
      if (gclkChannelEnable.value === true) {
        freq = gclkFreq.value;
      }
    } else if (cmb_refClk.value === 1) {
      freq = xOscFreq.value;
    } else if (cmb_refClk.value === 2) {
      freq = dfllclockFreq.value;
    }
    fckrFreqValue = freq;
    return fckrFreqValue;
  };

  const updateFpfdPLLFreq = () => {
    fpfdFreqValue = fckrFreqValue / pllrefdiv.value;
    return fpfdFreqValue;
  };

  const updateFvcoPLLFreq = () => {
    fvcoFreqValue = (fckrFreqValue * pllfbdiv.value) / pllrefdiv.value;
    return fvcoFreqValue;
  };

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      {pllFreqArray.length !== 0 &&
        pllOutEnableSymbols.length !== 0 &&
        pllFreqArray.map(
          (id, index) =>
            pllOutEnableSymbols[index].value === true && (
              <FrequencyLabelRangeComponent
                key={id}
                componentId={componentId}
                symbolId={id}
                class={props.cx('pllFreq' + index)}
                minValue={12700000}
                maxValue={1600000000}
                labelTooltip={'Frequency Min Value: 12.7 MHz , Max Value : 1600 MHz'}
              />
            )
        )}
      {pllDivSymbols.length !== 0 &&
        pllDivSymbols.map((id, index) => (
          <PlainLabel
            key={id.symbolId}
            disPlayText={'' + id.value}
            className={props.cx('pllPostDivLabel' + index)}
          />
        ))}

      <PlainLabel
        disPlayText={'' + pllrefdiv.value}
        className={props.cx('pllrefdivLabel')}
      />
      <PlainLabel
        disPlayText={'' + pllfbdiv.value}
        className={props.cx('pllFBDivLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmb_refClk}
        classPrefix='pllRefClkRadio'
        classResolver={props.cx}
      />
      <PlainLabel
        disPlayText={updateFCKRPLLFreq() / 1000000 + ' MHz'}
        redColorStatus={fckrFreqValue === 0 ? true : false}
        className={props.cx('fckrFreqLabel')}
      />

      <PlainLabel
        disPlayText={updateFpfdPLLFreq() / 1000000 + ' MHz'}
        redColorStatus={fpfdFreqValue < 4000000 || fpfdFreqValue > 60000000 ? true : false}
        toolTip='Fpdf frequency Min value: 4 MHz && Max value: 60 MHz'
        className={props.cx('fpfdFreqLabel')}
      />

      <PlainLabel
        disPlayText={updateFvcoPLLFreq() / 1000000 + ' MHz'}
        redColorStatus={fvcoFreqValue < 800000000 || fvcoFreqValue > 1600000000 ? true : false}
        toolTip='Fvco frequency Min value:  800 MHz && Max value: 1600 MHz'
        className={props.cx('fvcoFreqLabel')}
      />

      <SettingsDialog
        tooltip='Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('pllSettings')}
        symbolArray={settingsArray}
        dialogWidth='50rem'
        dialogHeight='47rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('pllReset')}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />

      <label
        style={{
          font: 'Calibri',
          fontSize: '14px',
          alignContent: 'center'
        }}
        className={props.cx('phaseLockedLoopText')}>
        <span>4 MHz ≤ Fpfd ≤ 60 MHz</span>
        <br></br>
        <span>800 MHz ≤ Fvco ≤ 1600 MHz</span>
        <br></br>
        <span>12.7 MHz ≤ PLLx_y ≤ 1600 MHz</span>
      </label>
    </div>
  );
};

export default PhaseLockedLoopControllerBox;
