import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getAllSymbolsFromJSON,
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';

const SlowClockControllerBox = (props: {
  slowClockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmb_Slclk_oscsel = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_TD_OSCSEL'
  });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.slowClockController));
  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.slowClockController));
  const [dynamicLabelSymbolInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.slowClockController)
  );

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <PlainLabel
        disPlayText={'Use bootloader Clock tree'}
        className={props.cx('useBootloaderLabel')}
      />
      <PlainLabel
        disPlayText={'32 kHz'}
        className={props.cx('lbl_Slclk_SecMod')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmb_Slclk_oscsel}
        classPrefix='slowClockR'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Slow Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('slclk_settings')}
        symbolArray={['CLK_TD_OSCSEL']}
        dialogWidth='40rem'
        dialogHeight='20rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Slow Clock symbols to default value'
        className={props.cx('slclk_reset')}
        componentId={componentId}
        resetSymbolsArray={['CLK_TD_OSCSEL']}
      />
    </div>
  );
};

export default SlowClockControllerBox;
