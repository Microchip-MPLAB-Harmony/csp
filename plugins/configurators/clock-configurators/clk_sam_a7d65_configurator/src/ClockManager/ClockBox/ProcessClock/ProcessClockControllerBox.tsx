import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/LoadDynamicComponents';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getAllSymbolsFromJSON,
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FreqencyLabels from 'clock-common/lib/Components/LabelComponent/FreqencyLabels';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import { getFreqSymbolId } from '../../MainBlock';

const ProcessClockControllerBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const pclkCSS = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_CPU_CKR_CSS'
  });

  const cmb_Pclk_pres = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_CPU_CKR_PRES'
  });
  const cmb_Pclk_mdiv = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_CPU_CKR_MDIV'
  });
  const spn_pclk_ratio = useIntegerSymbol({
    componentId,
    symbolId: 'CLK_CPU_RATIO'
  });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.controller));
  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.controller));
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.controller));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        boxInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <FreqencyLabels
        componentId={componentId}
        boxInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={getFreqSymbolId(pclkCSS.selectedOptionPair?.key)}
        class={props.cx('lbl_Pclk_css_sel')}
        redColorForZeroFrequency={true}
      />
      <PlainLabel
        disPlayText={cmb_Pclk_pres.options[cmb_Pclk_pres.value]?.replaceAll('CLK_', '')}
        className={props.cx('lbl_Pclk_pres')}
      />
      <PlainLabel
        disPlayText={cmb_Pclk_mdiv.options[cmb_Pclk_mdiv.value]?.replaceAll('PCK_DIV', '')}
        className={props.cx('lbl_Pclk_mdiv')}
      />
      <PlainLabel
        disPlayText={'*((' + spn_pclk_ratio.value + '+1)/16)'}
        className={props.cx('lbl_Pclk_ratio')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={pclkCSS}
        classPrefix='processClkR'
        labelClassPrefix='processClkRName'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Main Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('pckClkSettings')}
        symbolArray={allJsonSymbols}
        dialogWidth='45rem'
        dialogHeight='25rem'
      />
      <ResetSymbolsIcon
        tooltip='Main Slow Clock symbols to default value'
        className={props.cx('pckclkReset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols}
      />
    </div>
  );
};

export default ProcessClockControllerBox;
