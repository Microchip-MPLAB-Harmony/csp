import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import {
  ComboBoxDefault,
  ConfigSymbol,
  PluginConfigContext,
  useComboSymbol,
  useIntegerSymbol,
  useStringSymbol,
  useSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import ComboRadio from '../ClientLib/ComboRadio';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';

let frcFreq = 8000000;
const PrimaryAndScondaryControllerBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const frcDiv = useComboSymbol({ componentId, symbolId: 'OSCCON_FRCDIV_VALUE' });

  const nosc = useComboSymbol({
    componentId,
    symbolId: 'OSCCON_NOSC_VALUE'
  });
  const vbkp32CSEL = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_VBKP_32KCSEL'
  });
  const rtcntm = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_RTCNTM_CSEL'
  });
  const wdtrmcs = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_WDTRMCS'
  });
  const vbkp1kCSEL = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_VBKP_1KCSEL'
  });
  const dswdtOSC = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_DSWDTOSC'
  });
  const lpclkDiv = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_LPCLK_MOD'
  });
  const vbkpDiv = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_VBKP_DIVSEL'
  });
  const poscFreqHook = useIntegerSymbol({
    componentId,
    symbolId: 'POSC_OUT_FREQ'
  });
  const poscMod = useComboSymbol({ componentId, symbolId: 'CONFIG_POSCMOD' });

  const productFamily = useStringSymbol({
    componentId,
    symbolId: 'PRODUCT_FAMILY'
  });
  let socenSymbolID = '';
  if (productFamily.value === 'PIC32CX_BZ2') {
    socenSymbolID = 'OSCCON_SOSCEN_VALUE';
  } else {
    socenSymbolID = 'CONFIG_LPOSCEN';
  }

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.controller));
  const [dynamicLabelSymbolsInfo] = useState(() => getDynamicLabelsFromJSON(props.controller));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolsInfo}
        cx={props.cx}
      />
      <ComboBoxDefault
        componentId={componentId}
        symbolId={'CONFIG_POSCMOD'}
        tooltip='When in HS mode, POSC input frequency needs to be between 4 Mhz and 32 Mhz.'
        className={props.cx('poscmod')}
      />
      <ComboRadio
        comboSymbolHook={nosc}
        classPrefix='noscSourceRadio'
        labelClassPrefix='noscSourceLabelName'
        classResolver={props.cx}
      />
      <ComboRadio
        comboSymbolHook={vbkp32CSEL}
        classPrefix='vbkp32kSourceRadio'
        classResolver={props.cx}
      />
      <ComboRadio
        comboSymbolHook={wdtrmcs}
        classPrefix='wdtrmcsSourceRadio'
        labelClassPrefix='wdtrmcsSourceRadioName'
        classResolver={props.cx}
      />
      <ComboRadio
        comboSymbolHook={rtcntm}
        classPrefix='rtcntmSourceRadio'
        labelClassPrefix='rtcntmSourceRadioName'
        classResolver={props.cx}
      />
      <ComboRadio
        comboSymbolHook={vbkp1kCSEL}
        classPrefix='vbkp1kSourceRadio'
        labelClassPrefix='vbkp1kSourceRadioName'
        classResolver={props.cx}
      />
      <ComboRadio
        comboSymbolHook={dswdtOSC}
        classPrefix='dsdwdtSourceRadio'
        classResolver={props.cx}
      />
      <ComboBoxDefault
        componentId={componentId}
        symbolId={socenSymbolID}
        className={props.cx('soscen')}
      />

      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'POSC_OUT_FREQ'}
        tooltip='When in HS mode, POSC input frequency needs to be between 4 Mhz and 32 Mhz.'
        // minMaxOutofRangeRedColorStatus={
        //   (poscFreqHook.value < 4000000 || poscFreqHook.value > 32000000) && poscMod.value === 'HS'
        // }
        className={props.cx('lbl_poscFreq')}
      />

      <PlainLabel
        disPlayText={lpclkDiv.value.replaceAll('DIV_', '').replaceAll('_', '.')}
        booldStatus={true}
        className={props.cx('jlabel_lpclkdiv')}
      />
      <PlainLabel
        disPlayText={vbkpDiv.value.replaceAll('DIV_', '').replaceAll('_', '.')}
        booldStatus={true}
        className={props.cx('jlabel_rtcdiv')}
      />
      <PlainLabel
        disPlayText={' Hz'}
        className={props.cx('lbl_Hz')}
      />
      <PlainLabel
        disPlayText={' Hz'}
        className={props.cx('lbl_Hz1')}
      />
      <PlainLabel
        disPlayText={'POSCMOD'}
        toolTip='This configures POSCMOD in DEVCFG1'
        booldStatus={true}
        className={props.cx('lbl_poscmod')}
      />

      <PlainLabel
        disPlayText={
          GetClockDisplayFreqValue(frcFreq / Number(frcDiv.value.replaceAll('DIV_', ''))) + ''
        }
        className={props.cx('lbl_frcdivFreq')}
      />

      <PlainLabel
        disPlayText={'CLKO'}
        booldStatus={true}
        toolTip='Can not use this pin for clock output if it is needed for oscillator input (HS mode).'
        className={props.cx('clko')}
      />
    </div>
  );
};

export default PrimaryAndScondaryControllerBox;
