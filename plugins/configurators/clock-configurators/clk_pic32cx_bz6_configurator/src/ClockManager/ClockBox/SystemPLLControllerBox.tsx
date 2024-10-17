import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
  PluginConfigContext,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getAllSymbolsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';

const SystemPLLControllerBox = (props: {
  systemPLLControllerData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const minSPLL2Freq = useIntegerSymbol({
    componentId,
    symbolId: 'SPLL2_FREQ_MIN'
  });
  const maxSPLL2Freq = useIntegerSymbol({
    componentId,
    symbolId: 'SPLL2_FREQ_MAX'
  });
  const spll2Freq = useIntegerSymbol({
    componentId,
    symbolId: 'SPLL2_FREQ'
  });
  const spllDiv2Value = useKeyValueSetSymbol({
    componentId,
    symbolId: 'SPLLCON_SPLLPOSTDIV2_VALUE'
  });
  const spllDiv1Value = useIntegerSymbol({
    componentId,
    symbolId: 'SPLLCON_SPLLPOSTDIV1_VALUE'
  });

  function replaceDivValue(text: any) {
    try {
      let divValue = text.replace('DIV_', '');
      return divValue;
    } catch (err) {}
  }

  const AddCustomLabels = () => {
    return (
      <div>
        <label
          className={props.cx('label_spll_div2Label')}
          style={{
            font: 'Calibri',
            fontSize: '14px',
            fontWeight: 'bold'
          }}>
          {replaceDivValue(spllDiv2Value.options[spllDiv2Value.value])}
        </label>
        <label
          style={{
            font: 'Calibri',
            fontSize: '14px',
            fontWeight: 'bold'
          }}
          className={props.cx('label_spll_div1Label')}>
          {spllDiv1Value.value}
        </label>
      </div>
    );
  };

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.systemPLLControllerData));

  const [dynamicSymbolInfo] = useState(() =>
    getDynamicSymbolsFromJSON(props.systemPLLControllerData)
  );

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'SPLL3_RFPLL_FREQ'}
        className={props.cx('label_spll3Freq1')}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'SPLL2_FREQ'}
        className={props.cx('label_spll2Freq')}
        // minMaxOutofRangeRedColorStatus={
        //   spll2Freq.value < minSPLL2Freq.value || spll2Freq.value > maxSPLL2Freq.value
        // }
        tooltip={
          'SPLL2 has to be between ' + minSPLL2Freq.value + ' Hz and ' + maxSPLL2Freq.value + ' Hz'
        }
      />
      <AddCustomLabels />
      <SettingsDialog
        tooltip='System PLL Configuration'
        componentId={componentId}
        className={props.cx('systemPll_settings')}
        symbolArray={allJsonSymbols}
        dialogWidth='50rem'
        dialogHeight='30rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset System PLL symbols to default value'
        className={props.cx('systemPll_reset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols}
      />
    </div>
  );
};

export default SystemPLLControllerBox;
